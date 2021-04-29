import validate
import csv


class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}"


numOfUsers = int(input("How many users do you want to store? "))
with open("phone directory.txt", "a") as file:
    phone_list = validate.read_file("phone directory.txt")
    print(phone_list)

with open("phone directory.txt", "a", newline="") as file:
    fieldnames = ["Name", "Contact"]
    user_write = csv.DictWriter(file, fieldnames=fieldnames)
    if len(phone_list) == 0:
        user_write.writeheader()
    else:
        pass
    for x in range(numOfUsers):
        userName = validate.get_username()
        contact = validate.get_phone()
        user = Person(userName, contact)
        if user.phone in phone_list:
            pass
            # print(f"{user.phone} is in {phone_list}")
        else:
            user_write.writerow({"Name": user.name, "Contact": user.phone})























