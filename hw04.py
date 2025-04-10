from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone number please."
        except KeyError:
            return "Contact not exist."
        except IndexError:
            return "Enter the argument for the command."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
  if len(args) < 2:
    raise IndexError
  name, phone = args
  contacts[name] = phone
  return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise IndexError  
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact phone number update."

@input_error
def show_contact(args, contacts):
  if len(args) < 1:
    raise IndexError
  name = args[0]
  if name not in contacts:
    raise KeyError 
  return f"{name}: {contacts[name]}"

@input_error
def show_all_contacts(contacts):
    if not contacts:
        return "There are no contacts in phone book."
    
    result = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return result


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
      user_input = input("Enter a command: ").strip().lower()
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
        print(show_contact(args, contacts))
      elif command == "all":
        print(show_all_contacts(contacts))
      else:
        print("Invalid command.")


if __name__ == "__main__":
  main()