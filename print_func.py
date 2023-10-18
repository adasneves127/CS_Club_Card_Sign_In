import os
from datetime import datetime
from utils import get_col_widths


def print_title(width: int):

    # Print the centered text "CS Club Sign In"
    title_text = 'CS Club Sign In System'
    print_formatted_line(title_text, width)


def print_divide(width: int):
    print('+' + '-' * (width) + '+')


def print_header(width: int, user_data: list | None = None):
    width -= 2
    print_divide(width)
    print_title(width)
    print_divide(width)
    if user_data is not None:
        date = datetime.now().strftime('%I:%M:%S %p')
        print_formatted_line(f'Welcome, {user_data[1]} {user_data[2]}', width)
        print_formatted_line(f"{date}", width)
        print_formatted_line(f'Role: {user_data[4]}', width)
        print_divide(width)
    return 3 if user_data is None else 7


def print_mod_header(width: int,
                     user_data: list | None = None,
                     results: list | None = None):
    width -= 2
    print_divide(width)
    print_title(width)
    print_divide(width)
    if user_data is not None:
        date = datetime.now().strftime('%I:%M:%S %p')
        print_formatted_line(f'Welcome, {user_data[1]} {user_data[2]}', width)
        print_formatted_line(f"{date}", width - 2)
        print_formatted_line(f'Role: {user_data[4]}', width)
        print_divide(width)

    return 3 if user_data is None else 7


def menu_1(width: int):
    print(f'{"| Please choose an option:":<{width - 1}}' '|')
    print('|' + ' ' * (width - 2) + '|')
    print(f'{"| 1. Maintain Everyday Users":<{width - 1}}' + '|')
    print(f'{"| 2. Maintain Officers":<{width - 1}}' + '|')
    print(f'{"| 3. Search":<{width - 1}}' + '|')
    print(f'{"| 4. Sign In":<{width - 1}}' + '|')
    print(f'{"| 0. Log Out":<{width - 1}}' + '|')
    return 7


def menu_2(width: int):
    print_formatted_line("[Maintain Everyday Users]", width - 2)
    print(f'{"| Please choose an option:":<{width - 1}}' + '|')
    print('|' + ' ' * (width - 2) + '|')
    print(f'{"| 1. Create User":<{width - 1}}' + '|')
    print(f'{"| 2. Search User":<{width - 1}}' + '|')
    print(f'{"| 3. Deactivate User":<{width - 1}}' + '|')
    print(f'{"| 4. Reactivate User":<{width - 1}}' + '|')
    print(f'{"| 5. Update User":<{width - 1}}' + '|')
    print(f'{"| 0. Exit":<{width - 1}}' + '|')
    return 9


def menu_3(width: int):
    print_formatted_line("[Maintain Officers]", width - 2)
    print(f'{"| Please choose an option:":<{width - 1}}' + '|')
    print('|' + ' ' * (width - 2) + '|')
    print(f'{"| 1. Appoint Officer":<{width - 1}}' + '|')
    print(f'{"| 2. Get Officer Roster":<{width - 1}}' + '|')
    print(f'{"| 3. Remove Officer":<{width - 1}}' + '|')
    print(f'{"| 0. Exit":<{width - 1}}' + '|')
    return 7


def menu_4(width: int):
    print_formatted_line("[Appoint Officer]", width - 2)
    print(f'{"| Please Swipe New Officer Card:":<{width - 1}}' + '|')
    return 2


def menu_5(width: int):
    print_formatted_line("[Create User]", width - 2)
    return 1


def menu_6(width: int):
    print_formatted_line("[Search User]", width - 2)
    return 1


def menu_7(width: int):
    print_formatted_line("[Deactivate User]", width - 2)
    return 1


def menu_8(width: int):
    print_formatted_line("[Reactivate User]", width - 2)
    return 1


def menu_9(width: int):
    print_formatted_line("[Update User]", width - 2)
    return 1


def menu_10(width: int):
    print_formatted_line("[Sign In]", width - 2)
    print('|' + ' ' * (width - 2) + '|')
    print(f"| {'1. Single Sign In':{width - 3}}|")
    print(f"| {'2. Bulk Sign In':{width - 3}}|")
    print(f"| {'0. Exit':{width - 3}}|")
    return 5


def menu_11(width: int):
    print_formatted_line("[Single Sign In]", width - 2)
    return 1


def menu_12(width: int):
    print_formatted_line("[Bulk Sign In]", width - 2)
    return 1


def print_res_str(results: str, width: int):
    print(f"{results:<{width - 1}}")


def print_res_list(results: list, width: int):
    widths = get_col_widths(results)
    rows = ["|".join(
        [f'{x:<{widths[i]}}'
         for i, x in enumerate(y)]) for y in results]
    for row in rows:
        print(f"""|{f'{row}|':<{width - 2}}|""")
    border = '+' + '+'.join(['-' * x for x in widths]) + '+'
    print(f"{border:<{width - 1}}|")
    return len(results) + 2


def draw_window(user: list | None = None,
                menu_state: int = 0,
                results: list | str | None = None):
    size = tuple(os.get_terminal_size())
    row_count = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    row_count = print_header(size[0], user)
    if menu_state == 1:
        row_count += menu_1(size[0])
    if menu_state == 2:
        row_count += menu_2(size[0])
    if menu_state == 3:
        row_count += menu_3(size[0])
    if menu_state == 4:
        row_count += menu_4(size[0])
    if menu_state == 5:
        row_count += menu_5(size[0])
    if menu_state == 6:
        row_count += menu_6(size[0])
    if menu_state == 7:
        row_count += menu_7(size[0])
    if menu_state == 8:
        row_count += menu_8(size[0])
    if menu_state == 9:
        row_count += menu_9(size[0])
    if menu_state == 10:
        row_count += menu_10(size[0])
    if menu_state == 11:
        row_count += menu_11(size[0])
    if menu_state == 12:
        row_count += menu_12(size[0])

    if results is not None:
        if isinstance(results, str):
            print_res_str(results, size[0])
            row_count += 1
        if isinstance(results, (list, tuple)):
            border = '+' + '+'.join(
                ['-' * x for x in get_col_widths(results)]
                ) + '+'
            print(f"{border:<{size[0] - 1}}|")
            row_count += print_res_list(results, size[0])
            row_count += 1

    while row_count < size[1] - 1:
        print('|' + ' ' * (size[0] - 2) + '|')
        row_count += 1
    print('+' + '-' * (size[0] - 2) + '+', end='\r')


def print_formatted_line(text: str, size: int):
    """Print a line of text centered in a box"""
    print(f'|{text: ^{size}}|')
