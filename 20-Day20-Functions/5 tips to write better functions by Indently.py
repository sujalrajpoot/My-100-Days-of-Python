# TIP-1:
def connect():
    pass
print(connect())

def connect():
    ...
print(connect())

def connect():
    raise NotImplementedError('connect() is missing code.')
print(connect())


# TIP-2:
def get_users():
    users: dict[int, str] = {1: 'Bob', 2: 'Jef', 3: 'Tom'}
    return users
print(get_users())

def get_users() -> dict[int, str]:
    users: dict[int, str] = {1: 'Bob', 2: 'Jef', 3: 'Tom'}
    return users
print(get_users())

def display_users(users) -> None:
    for k, v in users.items():
        print(k, v, sep=": ")

def display_users(users: dict[int, str]) -> None:
    for k, v in users.items():
        print(k, v, sep=": ")

def main() -> None:
    users: dict[int, str] = get_users()
    display_users(users)

if __name__=='__main__':
    main()


# TIP-3:
def get_users() -> dict[int, str]:
    """
    Retrieves the ids and usernames from a database as a dict.

    :return: dict[int, str]
    """
    users: dict[int, str] = {1: 'Bob', 2: 'Jef', 3: 'Tom'}
    return users
print(get_users())

def display_users(users: dict[int, str]) -> None:
    """
    Prints each user to the console in a nice format.
    :param users: The users to display
    :return: 
    Input: {1: 'Bob', 2: 'Jef', 3: 'Tom'}\n
    Output:
    1: Bob
    2: Jef
    3: Tom
    """
    for k, v in users.items():
        print(k, v, sep=": ")

display_users({1: 'Bob', 2: 'Jef', 3: 'Tom'})


# TIP-4:
from enum import Enum

class Quality(Enum):
    LOW:int = 480
    MEDIUM:int = 1080
    HIGH:int = 1440

class Privacy(Enum):
    PRIVATE:str = 'Private'
    UNLISTED:str = 'Unlisted'
    PUBLIC:str = 'Public'

def upload(file: str,quality: Quality, privacy: Privacy) -> None:
    print(f'Uploading: "{file}" in {quality.value}p ({privacy.value})')

def main() -> None:
    upload('cat.mp4', Quality.LOW, Privacy.PRIVATE)

def upload_1(file: str, *, quality: Quality, privacy: Privacy) -> None:
    """
    :parameters\nThis star symbol (*) represents after this star symbol in function's parameter the value of that parameter should be given by its and it also after this star symbol (*) in function's parameter those parameters will become required keywords\nFor Example:
    Without giving name of that parameter so it will raise an error like this.\n
    ==> upload_1('cat.mp4', Quality.LOW, Privacy.PRIVATE)
        TypeError: upload_1() takes 1 positional argument but 3 were given

    ==> So the best method is to use this kind of functions like this.
        upload_1('cat.mp4', quality=Quality.LOW, privacy=Privacy.PRIVATE)
    """
    print(f'Uploading: "{file}" in {quality.value}p ({privacy.value})')

def main_1() -> None:
    upload_1('cat.mp4', quality=Quality.LOW, privacy=Privacy.PRIVATE)

if __name__=='__main__':
    main()
    main_1()


# TIP-5:
def join_text_1(text_1:str,text_2:str, text_3:str, *, sep:str) -> str:
    """
    This function takes three string arguments (text_1, text_2, and text_3) and joins them together using the specified separator (sep). The separator sep is specified as a keyword-only argument, which means it must be provided by keyword when calling the function. This function is specifically designed to join exactly three strings together with a custom separator.

    Number of arguments: join_text_1 expects exactly three string arguments.
    join_text_1 uses fixed positional arguments for three strings. if you give more than three string arguments in this function it will raise TypeError: join_text_1() takes 3 positional arguments but 4 positional arguments (and 1 keyword-only argument) were given
    """
    return sep.join([text_1, text_2, text_3])

def join_text(*Strings, sep:str) -> str:
    """
    This function uses variable positional arguments (*Strings) to accept an arbitrary number of strings to join together. Similar to join_text_1, it also requires a separator (sep) to be provided as a keyword argument. This function is more flexible as it can join any number of strings together with a custom separator.

    Number of arguments: join_text can accept any number of string arguments. join_text can accept any number of string arguments.
    """
    return sep.join(Strings)

def main_1() -> None:
    print(join_text_1('A', 'B', 'C', sep='-'))

def main() -> None:
    print(join_text('A', 'B', 'C', 'D', 'E', sep='/'))

if __name__=='__main__':
    main_1()
    main()