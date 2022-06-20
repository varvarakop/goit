def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            print("Repeat and enter correct user name and phone")
        else:
            return result
    return wrapper


def add():
    global contacts
    contacts = {}
    for i in range(3):
        contact = input('Your name (space) your phone: ')
        cont = contact.split(' ')
        name = cont[0]
        phone = cont[1]
        if len(name) > 0:
            contacts.update({name: phone})
        else:
            contacts = contacts
        ques = input('Do you want to add contact? ')
        if ques == "yes":
            i += 1
        else:
            break
    return contacts


add = input_error(add)


def change():

    contact_n = input('Your name (space) your new phone: ')
    cont_n = contact_n.split(' ')
    name = cont_n[0]
    phone_n = cont_n[1]
    global contacts
    for k in contacts.keys():
        if name == k:
            contacts[k] = phone_n
    return contacts


change = input_error(change)


def get_phone():
    name = input('Username: ')
    global contacts
    for k in contacts.keys():
        if name == k:
            user_phone = contacts.get(k)
    return user_phone


get_phone = input_error(get_phone)


def show_all():
    global contacts
    return contacts


show_all = input_error(show_all)


def main():
    gameloop = True
    while gameloop:
        request = input('You: ').lower()
        if request == 'hello':
            print('How can I help you?')

        elif request == 'add':
            print(add())
        elif request == 'change':
            print(change())
        elif request == 'phone':
            print(get_phone())
        elif request == 'show all':
            print(show_all())
        elif request == 'good bye' or request == 'close' or request == 'exit':
            print('Good bye!')
            gameloop = False
        else:
            print('I don\'t understand you')

    return gameloop


if __name__ == '__main__':
    main()