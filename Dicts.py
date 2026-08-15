dic = {}

print("1. Insert")
print("2. Get All Countries")
print("3. Get All Capitals")
print("4. Search Capital")
print("5. Delete")

while True:
    choice=input("Choose a number between 1-5: ")
    if choice == "1":
        country=input("What Country do you want to add to the list? ").upper()
        capital=input("What Capital do you want to add to the list? ").upper()
        dic[country]=capital
    elif choice == "2":
        for key in dic.keys():
            print(key)
    elif choice == "3":
        for val in dic.values():
            print(val)
    elif choice == "4":
        search_country=input("Enter your Country: ").upper()
        if search_country in dic.keys():
            print(dic[search_country])
        else:
            print("No Country found.")
    elif choice == "5":
        remove=input("What Country do you want to delete? ").upper()
        del dic[remove]
    else:
        print("Invalid Option.")