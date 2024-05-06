def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "KeyError. No such name."
        except ValueError:
            return "ValueError. Enter the argument for the command."
        except IndexError:
            return "IndexError. Not enough arguments."

    return wrapper

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Contact not found."

@input_error
def print_contact(args, contacts):
    name = args[0]
    if name in contacts:
        phone_number = contacts[name]
        print(f'{name}:{phone_number}')
        return "Contact printed."
    else:
        return "Contact not found."

@input_error
def print_contacts(contacts):
    for key, value in contacts.items():
        print(f'{key}: {value}')
    return "All contacts printed."
    

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(print_contact(args, contacts))  
        elif command == "all":
            print(print_contacts(contacts))                       
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()