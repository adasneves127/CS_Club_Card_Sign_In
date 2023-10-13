def get_formatted_input(prompt: str) -> str:
    print('\033[F\033[2C', end='')
    return input(prompt)

def get_formatted_input_xy(prompt: str, x: int, y: int) -> str:
    # Move the cursor to the specified location
    print(f'\033[{y};{x}H', end='')
    return input(prompt)
