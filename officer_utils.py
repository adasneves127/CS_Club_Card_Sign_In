import db_conn
from print_func import draw_window
from input_utils import get_formatted_input_xy
from card_utils import hash_card_id
import hashlib
import getpass


def appoint_officer(conn: db_conn.conn, data: list):
    # Appoint an officer
    menu_state = 4
    draw_window(data, menu_state)
    raw_card = get_formatted_input_xy(
                    "Please Swipe New Officer Card: ", 3, 9
                    )
    cardID = hash_card_id(
        ''.join(
            [
                x
                for x in raw_card
                if x.isdigit()]))
    role = get_formatted_input_xy("Please enter the role: ", 3, 10)
    conn.appoint_officer(cardID, role, data[0])
    # Create a login
    user_login = hashlib.sha256(
        "".join(
            [
                x
                for x in raw_card
                if x.isdigit()
            ]
        ).encode()
    ).hexdigest()[0:32]
    password = getpass.getpass("User Password: ")
    conn.create_acct(user_login, password)


def get_all_officer_data(conn: db_conn.conn, data: list):
    # Get officer roster
    menu_state = 6
    results = conn.get_all_officer_data()
    officer_data = [["First Name", "Last Name", "Email ID", "Role"]]
    officer_data.extend(results)
    draw_window(data, menu_state, officer_data)
    get_formatted_input_xy("Press enter to continue...", 2, 11 + len(results))


def remove_officer(conn: db_conn.conn, data: list):
    menu_state = 12
    draw_window(data, menu_state)
    # Get card ID
    raw_card = get_formatted_input_xy(
        "Please Swipe Officer Card: ", 3, 9)
    cardID = hash_card_id(raw_card)
    # Remove officer
    conn.remove_officer(cardID)

    # Remove Login
    username = hashlib.sha256(
        "".join([x for x in raw_card]).encode()
        ).hexdigest()[0:32]
    conn.remove_acct(username)


def maintain_officers(conn: db_conn.conn, data: list):
    choice = ""
    while choice != '0':

        menu_state = 3
        draw_window(data, menu_state)
        choice = get_formatted_input_xy("Please choose an option: ", 3, 9)
        match choice:
            case '1':
                appoint_officer(conn, data)
            case '2':
                get_all_officer_data(conn, data)
            case '3':
                remove_officer(conn, data)
            case '0':
                break
