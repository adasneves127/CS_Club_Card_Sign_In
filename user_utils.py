import db_conn
from print_func import draw_window
from input_utils import get_formatted_input_xy
from card_utils import hash_card_id

color_preferences = {}


def get_all_user_data(conn: db_conn.conn, data: list):
    # Get all user data
    menu_state = 5
    results = conn.get_all_user_data()
    user_data = [["First Name", "Last Name", "Email ID", "Banner ID"]]
    user_data.extend(results)
    draw_window(data, menu_state, user_data)
    get_formatted_input_xy("Press enter to continue...", 2, 7 + len(results) + 4)


def sign_in(conn: db_conn.conn, data: list):
    """Sign in a user"""
    menu_state = 2
    draw_window(data[0], menu_state)
    raw_card = get_formatted_input_xy("Please enter the card ID: ", 3, 9)
    if raw_card == '':
        return 1
    cardID = hash_card_id(''.join([x for x in raw_card if x.isdigit()]))
    conn.sign_in(cardID)


def create_user(conn: db_conn.conn, data: list):
    # Create a user
    menu_state = 5
    draw_window(data, menu_state)
    cardID = hash_card_id(''.join([x for x in get_formatted_input_xy("Please enter the card ID: ", 3, 9) if x.isdigit()]))
    
    firstName = get_formatted_input_xy("Please enter the first name: ", 3, 10)
    lastName = get_formatted_input_xy("Please enter the last name: ", 3, 11)
    bannerID = get_formatted_input_xy("Please enter the banner ID: ", 3, 12)
    emailID = get_formatted_input_xy("Please enter the email ID: ", 3, 13)
    conn.create_card(cardID, firstName, lastName, bannerID, emailID, data[0])

def search_user(conn: db_conn.conn, data: list):
    menu_state = 6
    draw_window(data, menu_state)
    lastName = get_formatted_input_xy("Search by last name: ", 3, 10)
    results = conn.search_user_last_name(lastName)

    user_data = [["First Name", "Last Name", "Email ID", "Banner ID"]]
    user_data.extend(results)
    draw_window(data, menu_state, user_data)
    get_formatted_input_xy("Press enter to continue...", 3, len(user_data) + 11)

def deactivate_user(conn: db_conn.conn, data: list):
    menu_state = 7
    draw_window(data, menu_state)
    bannerID = get_formatted_input_xy("Member Banner ID: ", 3, 10)
    rowcount = conn.deactivate_member(bannerID)
    print(f"| {rowcount} row(s) updated")
    bannerID = get_formatted_input_xy("Press Enter to Continue...", 3, 12)
    
def reactivate_user(conn: db_conn.conn, data: list):
    menu_state = 8
    draw_window(data, menu_state)
    bannerID = get_formatted_input_xy("Member Banner ID: ", 3, 10)
    rowcount = conn.reactivate_member(bannerID)
    print(f"| {rowcount} row(s) updated")
    bannerID = get_formatted_input_xy("Press Enter to Continue...", 3, 12)

def update_user(conn: db_conn.conn, data: list):
    menu_state = 9
    draw_window(data, menu_state)
    cardID = hash_card_id(get_formatted_input_xy("Please swipe card: ", 3, 10))
    # Get the user data
    results = conn.get_card_data(cardID)
    if len(results) == 0:
        print("User not found!")
        return 1
    user_data = [['First Name', 'Last Name', 'Banner ID', 'Email ID']]
    user_data.extend([results[0][1:5]])
    print(user_data)
    input()
    # print the data
    draw_window(data, menu_state, user_data)
    # Ask the user what they want to update
    choice = get_formatted_input_xy("What column do you want to update? ", 3, 13)
    inputRow = 14
    if 'firstname' in choice.lower().replace(" ", '').split(","):
        conn.update_user(cardID, 'firstName', get_formatted_input_xy("New First Name: ", 3, inputRow))
        inputRow += 1
    if 'lastname' in choice.lower().replace(" ", '').split(","):
        conn.update_user(cardID, 'lastName', get_formatted_input_xy("New Last Name: ", 3, inputRow))
        inputRow += 1
    if 'emailid' in choice.lower().replace(" ", '').split(","):
        conn.update_user(cardID, 'emailID', get_formatted_input_xy("New Email ID: ", 3, inputRow))
        inputRow += 1
    if 'bannerid' in choice.lower().replace(" ", '').split(","):
        conn.update_user(cardID, 'bannerID', get_formatted_input_xy("New Banner ID: ", 3, inputRow))
        inputRow += 1
    print("User updated successfully!")
        

def maintain_users(conn: db_conn.conn, data: list):
    choice = ""
    while choice != '0':

        menu_state = 2
        draw_window(data, menu_state)
        choice = get_formatted_input_xy("Please choose an option: ", 3, 9)
        match choice:
            case '1':
                create_user(conn, data)
            case '2':
                search_user(conn, data)
            case '3':
                deactivate_user(conn, data)
            case '4':
                reactivate_user(conn, data)
            case '5':
                update_user(conn, data)