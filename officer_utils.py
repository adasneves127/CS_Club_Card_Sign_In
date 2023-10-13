import db_conn
from print_func import draw_window
from input_utils import get_formatted_input_xy
from card_utils import hash_card_id

def appoint_officer(conn: db_conn.conn, data: list):
    # Appoint an officer
    menu_state = 4
    draw_window(data, menu_state)
    cardID = hash_card_id(''.join([x for x in get_formatted_input_xy("Please enter the card ID: ", 3, 9) if x.isdigit()]))
    role = get_formatted_input_xy("Please enter the role: ", 3, 10)
    conn.appoint_officer(cardID, role, data[0])

def get_all_officer_data(conn: db_conn.conn, data: list):
    # Get officer roster
    menu_state = 6
    results = conn.get_all_officer_data()
    officer_data = [["First Name", "Last Name", "Email ID", "Role"]]
    officer_data.extend(results)
    draw_window(data, menu_state, officer_data)
    get_formatted_input_xy("Press enter to continue...", 2, 7 + len(results) + 4)


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
            # case '3':
            #     remove_officer(conn, data)