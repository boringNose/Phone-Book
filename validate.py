import csv


def get_username():
    flag = True
    while flag:
        first_name = input("Enter first name: ").strip()
        last_name = input("Enter last Name: ").strip()
        if first_name.isalpha() and last_name.isalpha():
            flag = False
            return first_name + " " + last_name
        else:
            print("First and Last name can only contain Alphabets.")


def get_phone():
    flag = True
    while flag:
        number = input("Enter a 10 digit phone number: ").strip()
        if number.isnumeric():
            if len(number) == 10:
                flag = False
                return int(number)
            else:
                print("Number should be of exactly 10 digits.")
        else:
            print("Number can only contain digits")


def read_file(filename):
    user_phone = []
    with open(filename, "r") as file:
        line = file.readline()
        print(line)
        if line == "":
            print("line is empty")
        else:
            csv_reader = csv.reader(file, delimiter=",")
            line_count = 0
            for row in csv_reader:
                # print(row)
                user_phone.append(int(row[1]))
                line_count += 1

    print(user_phone)
    return user_phone
