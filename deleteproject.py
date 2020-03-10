def delete_project(email):
    list = []
    id = input("Please enter the id you want to delete")
    file = open(email + ".txt", "r")
    for line in file:
        Dict = eval(line)
        if id != Dict["id"]:
            # if "id" not in line:
            list.append(line)

    file.close()
    file = open(email + ".txt", "w")
    file.writelines(list)
