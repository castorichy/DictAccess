def view(dict):
    print("\nKey:\tValue")
    print("-------\t--------")
    for i in dict:
        print("{}:\t{}".format(i, dict[i]))
    print()


def signUp():
    usrName = input("Enter UsesName: ")
    return usrName


def home(name):
    print("Welcome {} Lets play\n". format(name))
    choice = input('''\
            Dictionary
        1. Add to Dictionary
        2. Delete by key
        3. View items
        4. replace dictionary
        5. Exit
        >>
    ''')
    return choice


def modify(dict, ModKey, key, Value):
    for ky in dict.keys():
        if ky == ModKey:
            dict.pop(ModKey)
            dict.update({key: Value})
        else:
            print(f"{ModKey} not Found")
