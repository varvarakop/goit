from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return f'{self.value}'


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phones=[]) -> None:
        self.name = name
        self.phone_list = phones

    def __str__(self) -> str:
        return f'User {self.name} - Phones: {", ".join([phone.value for phone in self.phone_list])}'

    def add_phone(self, phone: Phone) -> None:
        self.phone_list.append(phone)

    def del_phone(self, phone: Phone) -> None:
        self.phone_list.remove(phone)

    def edit_phone(self, phone: Phone, new_phone: Phone) -> None:
        self.phone_list.remove(phone)
        self.phone_list.append(new_phone)


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record


class InputError:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, contacts, *args):
        try:
            return self.func(contacts, *args)
        except IndexError:
            return 'Error! Give me name and phone please!'
        except KeyError:
            return 'Error! User not found!'
        except ValueError:
            return 'Error! Phone number is incorrect!'


def greeting(*args):
    return 'Hello! Can I help you?'


@InputError
def add(contacts, *args):
    name = Name(args[0])
    phone = Phone(args[1])
    if name.value in contacts:
        contacts[name.value].add_phone(phone)
        return f'Add phone {phone} to user {name}'
    else:
        contacts[name.value] = Record(name, [phone])
        return f'Add user {name} with phone number {phone}'


@InputError
def change(contacts, *args):
    name, old_phone, new_phone = args[0], args[1], args[2]
    contacts[name].edit_phone(Phone(old_phone), Phone(new_phone))
    return f'Change to user {name} phone number from {old_phone} to {new_phone}'


@InputError
def phone(contacts, *args):
    name = args[0]
    phone = contacts[name]
    return f'{phone}'


@InputError
def del_phone(contacts, *args):
    name, phone = args[0], args[1]
    contacts[name].del_phone(Phone(phone))
    return f'Delete phone {phone} from user {name}'


def show_all(contacts, *args):
    result = 'List of all users:'
    for key in contacts:
        result += f'\n{contacts[key]}'
    return result


def exiting(*args):
    return 'Good bye!'


def unknown_command(*args):
    return 'Unknown command! Enter again!'


def helping(*args):
    return """Command format:
    help or ? - this help;
    hello - greeting;
    add name phone - add user to directory;
    change name old_phone new_phone - change the user's phone number;
    del name phone - delete the user's phone number;
    phone name - show the user's phone number;
    show all - show data of all users;
    good bye or close or exit or . - exit the program"""


COMMANDS = {greeting: ['hello'], add: ['add '], change: ['change '], phone: ['phone '],
            helping: ['?', 'help'], show_all: ['show all'], exiting: ['good bye', 'close', 'exit', '.'],
            del_phone: ['del ']}


def command_parser(user_command: str) -> (str, list):
    for key, list_value in COMMANDS.items():
        for value in list_value:
            if user_command.lower().startswith(value):
                args = user_command[len(value):].split()
                return key, args
    else:
        return unknown_command, []


def main():
    contacts = AddressBook()
    while True:
        user_command = input('Enter command >>> ')
        command, data = command_parser(user_command)
        print(command(contacts, *data))
        if command is exiting:
            break


if __name__ == '__main__':
    main()