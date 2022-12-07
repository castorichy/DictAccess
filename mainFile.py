from dictionary_game import add, delete
from dict2 import signUp, home, view, modify
if __name__ == "__main__":
    dict = {}
    print("""\
            A program to store, Edit and del a dictionary
                welcome and feel free to play
    """)
    name = signUp()
    while True:
        choice = home(name)
        match choice:
            case '1':
                i = 0
                num = int(input("How many items to add: "))
                while i < num:
                    key = input("key: ")
                    value = input("value: ")
                    add(dict, key, value)
                    i += 1
            case '2':
                key = input("Enter key to delete: ")
                delete(dict, key)

            case '3':
                view(dict)

            case '4':
                ModKey = input("Enter key to be replace: ")
                key = input("Key: ")
                Value = input("Value: ")
                modify(dict, ModKey, key, Value)
            case '5':
                exit(0)
            case other:
                print("Wrong Choice")
