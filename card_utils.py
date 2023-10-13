import hashlib
import db_conn

def hash_card_id(cardID: int) -> str:
    """Hash the card ID"""
    return hashlib.sha512(str(cardID).encode()).hexdigest()


def create_card(conn: db_conn.conn, cardID: int):
    """Create a new card in the database"""
    first_name = input("First Name: ")
    lastName = input("Last Name: ")
    bannerID = input("Banner ID: ")
    emailID = input("Email ID: ")
    conn.create_card(cardID, first_name, lastName, bannerID, emailID)
    print("Card created successfully!")