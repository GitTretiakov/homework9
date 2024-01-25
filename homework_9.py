import sys
from typing import Dict


contacts: Dict[str, str] = {}


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Invalid input"
        except IndexError:
            return "Missing input"
    return inner


@input_error
def add_contact(name: str, phone: str) -> str:
    contacts[name] = phone
    return "Contact added"


@input_error
def change_phone(name: str, phone: str) -> str:
    contacts[name] = phone
    return "Phone number updated"


@input_error
def get_phone(name: str) -> str:
    return contacts[name]


def show_all() -> str:
    if not contacts:
        return "No contacts found"
    output = ""
    for name, phone in contacts.items():
        output += f"{name}: {phone}\n"
    return output


def close_program() -> None:
    print("Good bye!")
    sys.exit()


def handle_command(command: str) -> str:
    parts = command.split()
    if parts[0].lower() == "hello":
        return "How can I help you?"
    elif parts[0].lower() == "add":
        if len(parts) < 3:
            return "Missing input"
        name = parts[1]
        phone = parts[2]
        return add_contact(name, phone)
    elif parts[0].lower() == "change":
        if len(parts) < 3:
            return "Missing input"
        name = parts[1]
        phone = parts[2]
        return change_phone(name, phone)
    elif parts[0].lower() == "phone":
        if len(parts) < 2:
            return "Missing input"
        name = parts[1]
        return get_phone(name)
    elif parts[0].lower() == "show" and parts[1].lower() == "all":
        return show_all()
    elif parts[0].lower() in ["good", "bye", "close", "exit"]:
        close_program()
    else:
        return "Invalid command"


def main() -> None:
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter command: ")
        response = handle_command(command)
        print(response)


if __name__ == '__main__':
    main()
