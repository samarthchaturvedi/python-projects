# Contact Book

contacts = {}

while True:
    print("\n1.Add 2.View 3.Search 4.Delete 5.Exit")
    ch = input("Enter choice: ")

    if ch == '1':
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif ch == '2':
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif ch == '3':
        name = input("Search name: ")
        print(contacts.get(name, "Not found"))

    elif ch == '4':
        name = input("Delete name: ")
        contacts.pop(name, None)

    elif ch == '5':
        break