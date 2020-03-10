import json
import re
import project
import viewproject
import deleteproject
import edit


def menu2(email):
    print("1.CreateProject,\n 2.view Project \n 3.Delete Project \n 4.Edit Project \n")
    choose = input("Enter your choice \n")
    if choose == "1":
        project.projects(email)
    elif choose == "2":
        viewproject.list_project(email)
    elif choose == "3":
        deleteproject.delete_project(email)
    elif choose == "4":
        edit.edit_project(email)
    else:
        print("enter a vaild number")
    menu2(email)


def menu():
    print("Welcome,\n 1.Register \n 2.Login")
    choice = input("Enter your choice \n")
    if choice == "1":
        print("Register")
        fname = input("please enter your  first name \n")
        lname = input("please enter your  last name\n")
        email = input("please enter your  email\n")
        passwrd = input("please enter your password\n")
        repasswrd = input("please confirm your pass\n")
        while (passwrd != repasswrd):
            repasswrd = input("plaese rewrite your password\n")
        mobile = input("plaese rewrite your mobile\n")
        while (not re.match("^01[0125][0-9]{8}$", mobile)):
            input("please enter valid number ")
        data = {"Firstname": fname, "Lastname": lname, "email": email, "password": passwrd, "mobile": mobile}
        data_json = json.dumps(data)
        fregister = open("info.txt", "a")
        fregister.write(f"{data_json}\n")

        fregister.close()
        print("Successfully Registered")

        menu()
    elif choice == "2":
        print("Login")
        list = []
        lemail = input("please enter your mail")
        passwrd = input("please enetr yor password")
        file = open("info.txt", "r")
        # data=file.read()
        for line in file:
            Dict = eval(line)
            list.append(Dict)
            islogin = False
        for dict in list:
            if lemail == dict['email'] and passwrd == dict['password']:
                print("Login success")
                islogin = True
                break
            else:
                print("invalid data")
        if islogin:
            menu2(lemail)


menu()
