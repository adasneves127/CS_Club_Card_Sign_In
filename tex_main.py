import textual.containers as cons
import textual.widgets as widgets
from textual.screen import Screen
from textual.app import App, ComposeResult
from card_utils import hash_card_id, get_sign_in_id
from db_conn import conn
import mysql.connector.errors as sqlErrors



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


class Input(widgets.Input):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = ""

    def on_input_changed(self, changed_input: widgets.Input):
        self.data = changed_input.value


# Make the main screen
class CS_Sign_In(App):
    CSS_PATH = "main.tcss"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = None
        self.cur = None

    def compose(self) -> ComposeResult:
        # Add a header
        yield widgets.Header(show_clock=True)
        with reactive()
        with widgets.TabbedContent(
                                "Log In" if self.db is None
                                else "Maintain Users"):
            if self.db is None:
                with widgets.TabPane("Log In"):
                    with cons.Container(classes="Heading"):
                        yield widgets.Static("Log Into Database")
                    # Add a username box
                    yield widgets.Label("Username: ")
                    yield Input(password=True, id="UBUN")
                    yield widgets.Label("Password: ")
                    yield Input(password=True, id="DBPW")
                    yield widgets.Button("Log In", id="logIn")

            with widgets.TabPane("Maintain Users"):
                yield widgets.Static("Test 1")
            with widgets.TabPane("Maintain Officers"):
                yield widgets.Static("Test2")
            with widgets.TabPane("Search"):
                yield widgets.Static("Test3")
            with widgets.TabPane("Sign In"):
                yield widgets.Static("Test4")

    def on_button_pressed(self, event: widgets.Button.Pressed):
        if event.button.id == 'logIn':
            username = self.get_widget_by_id('UBUN').value  # type: ignore
            password = self.get_widget_by_id("DBPW").value  # type: ignore
            username = get_sign_in_id(username)
            try:
                self.db = conn(
                                "csclub-bridgew.mysql.database.azure.com",
                                username,
                                password)
                self.cur = self.db.cursor
            except sqlErrors.ProgrammingError:
                self.push_screen(UserNotFound())
            self.app.refresh(layout=True)

if __name__ == "__main__":
    CS_Sign_In().run()
