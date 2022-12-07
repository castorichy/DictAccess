def add(dict, Key, Value):
    myDict = dict.update({Key: Value})
    print("Item Added Successfully")
    return myDict


def delete(dict, Key):
    try:
        myDict = dict.pop(Key)
        if len(myDict) != 0:
            print("Item Added Successfully")
            return myDict
        else:
            print("Item Deletion failed")
    except KeyError:
        print("Key '{}' not found.")
