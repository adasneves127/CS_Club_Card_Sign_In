import hashlib


def hash_card_id(cardID: str) -> str:
    """Hash the card ID"""
    cardID = ''.join(
        [
            x
            for x
            in cardID
            if x.isdigit()
        ]
    )
    return hashlib.sha512(cardID.encode()).hexdigest()
