from textual import events
import textual.containers as cons
import textual.widgets as widgets
from textual.screen import Screen
from textual.app import App, ComposeResult
from card_utils import get_sign_in_id, hash_card_id
from db_conn import conn
import mysql.connector.errors as sqlErrors
from textual.reactive import reactive
from textual.widget import Widget


class Name(Widget):
    """Generates a greeting."""

    who = reactive("Log In To Databases")

    def render(self) -> str:
        return f"{self.who}"


class UserNotFound(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen"),
                ("enter", "app.pop_screen", "Pop Screen")]

    def compose(self) -> ComposeResult:
        yield widgets.Static(" ERROR ", id="title")
        yield widgets.Static(
            "User not Found as an authorized user in SQL Database!"
            )
        yield widgets.Static("Press enter to continue [blink]_[/]",
                             id="any-key")


class LogInScreen(Screen):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.who = Name()
    
    def compose(self) -> ComposeResult:
        # Add a header
        yield widgets.Header(show_clock=True)
        with widgets.TabbedContent("Log In"):
            with widgets.TabPane("Log In"):
                with cons.Container(classes="Heading"):
                    yield self.who

                # Add a username box
                yield widgets.Label("Username: ")
                yield widgets.Input(password=True, id="UBUN")
                yield widgets.Label("Password: ")
                yield widgets.Input(password=True, id="DBPW")
                yield widgets.Button("Log In", id="logIn")
        yield widgets.Footer()

    def on_button_pressed(self, event: widgets.Button.Pressed):
        print("TEST")
        if event.button.id == 'logIn':
            raw_username = self.get_widget_by_id('UBUN').value  # type: ignore
            password = self.get_widget_by_id("DBPW").value  # type: ignore

            username = get_sign_in_id(raw_username)
            try:
                app.db = conn(
                                "csclub-bridgew.mysql.database.azure.com",
                                username,
                                password)
                app.current_user = hash_card_id(raw_username)
                user = app.db.get_officer_data(app.current_user)
                self.who.who = f"""Welcome {user[0][1]} {user[0][2]}
Role: {user[0][4]}"""
                app.switch_mode("maintainUsers")
            except sqlErrors.ProgrammingError:
                app.push_screen(UserNotFound())

    def _on_screen_resume(self) -> None:
        for item in self.children:
            item.refresh(layout=True)
        super()._on_screen_resume()


class MaintainUsers(Screen):
    def compose(self) -> ComposeResult:
        yield widgets.Footer()

    def _on_focus(self):
        pass

    def focus(self, scroll_visible: bool = True):
        for item in self.children:
            item.refresh(layout=True)


class HelpScreen(Screen):
    def compose(self) -> ComposeResult:
        yield widgets.Footer()


class ModesApp(App):
    BINDINGS = [
        ("l", "switch_mode('logIn')", "Log-In Screen"),
        ("s", "switch_mode('maintainUsers')", "Maintain Users"),
        ("h", "switch_mode('help')", "Help"),
    ]
    MODES = {
        "logIn": LogInScreen,
        "maintainUsers": MaintainUsers,
        "help": HelpScreen,
    }

    def __init__(self):
        super().__init__()
        self.db: conn | None = None
        self.current_user = ""

    def on_mount(self) -> None:
        self.switch_mode("logIn")


if __name__ == "__main__":
    app = ModesApp()
    app.run()
