import hashlib


def hash_card_id(cardID) -> str:
    """Hash the card ID"""
    return hashlib.sha512(str(cardID).encode()).hexdigest()
