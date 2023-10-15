import db_conn
import hashlib
from getpass import getpass
from print_func import draw_window
from input_utils import get_formatted_input_xy, get_formatted_input
from user_utils import maintain_users  # search, sign_in_menu
from officer_utils import maintain_officers
from card_utils import hash_card_id


def main():
    cardID = ' '
    while cardID != '':
        draw_window()
        # Move the cursor up one and to the right
        try:
            cardID = get_formatted_input_xy("Please swipe your card: ", 3, 7)
        except KeyboardInterrupt:
            print("Exiting...")
            exit(1)
        # Connect to the database
        # Get username and password
        password = getpass("| Please enter your password: ")
        user = hashlib.sha256(
            "".join(
                [
                    x
                    for x in cardID
                    if x.isdigit()
                ]
                ).encode()
            ).hexdigest()[0:32]

        conn = db_conn.conn(
            "csclub-bridgew.mysql.database.azure.com",
            user,
            password
        )
        # # get current user from database
        # Get the card ID from the user, remove extra chars from the string
        cardID = hash_card_id(''.join([x for x in cardID if x.isdigit()]))

        data = conn.get_officer_data(cardID)
        if len(data) == 0:
            print("User not found or user not an officer!")
            exit(1)
        draw_window(data[0], menu_state=1)
        ret_stat = 1
        while ret_stat:
            ret_stat = main_loop(conn, data[0])
    conn.close()


def main_loop(conn: db_conn.conn, data: list) -> int:
    try:
        while True:
            while True:
                draw_window(data, menu_state=1)
                match get_formatted_input("? "):
                    case '1':
                        maintain_users(conn, data)
                    case '2':
                        maintain_officers(conn, data)
                    # case '3':
                    #     search(conn, data)
                    # case '4':
                    #     sign_in_menu(conn, data)
                    case '0':
                        return 0

    except KeyboardInterrupt:
        return 1


if __name__ == "__main__":
    main()
