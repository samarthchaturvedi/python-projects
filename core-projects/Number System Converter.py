# Number Converter

print("1.Decimal 2.Binary 3.Hex")
choice = input("Convert from: ")

num = input("Enter number: ")

if choice == '1':
    n = int(num)
    print("Binary:", bin(n))
    print("Hex:", hex(n))

elif choice == '2':
    print("Decimal:", int(num, 2))

elif choice == '3':
    print("Decimal:", int(num, 16))