def edit_project(email):
    list = []
    id = input("please enter the id of project")
    key = input("please enter the key you want to update")
    new_value = input("please enter the new value you want to update")
    old_value = input("please enter the  old value you want to change")

    file = open(email + ".txt", "r")
    for line in file:
        Dict = eval(line)

        if id == Dict["id"]:
            if key in line:
                res = line.replace(old_value, new_value)

        file = open(email + ".txt", "w")
        file.writelines(res)
