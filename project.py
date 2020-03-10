import datetime
import json


def projects(email):
    try:
        id = input("Enter the id ")
        title = input("Please enter the title")
        details = input("Please enter your details")
        total_target = input("please enter your total target")

        start_date = input("enter  start date should be YYYY-MM-DD")
        end_date = input("enter end date should be YYYY-MM-DD")
        datetime.datetime.strptime(start_date, '%Y-%m-%d')
        datetime.datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        input("Incorrect data format, write it again  should be YYYY-MM-DD")
    project_data = {"id": id, "title": title,
                    "details": details, "total": total_target,
                    "satartDate": start_date,
                    "endDate": end_date}
    project_json = json.dumps(project_data)
    file = open(email + ".txt", "a")
    file.write(f"{project_json}\n")
    file.close()
