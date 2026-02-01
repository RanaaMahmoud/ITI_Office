from Employee import Employee
from Car import Car
from Office import Office
from Person import Person
import json


def save_office_to_json(office):
    data = {
        "office_name": office.name,
        "employees": [
            {
                "id": emp.id,
                "name": emp.name,
                "email": emp.email,
                "salary": emp.salary
            } for emp in office.employees.values()
        ]
    }

    with open("office.json", "w") as f:
        json.dump(data, f, indent=4)



def main():
    car = Car("Fiat 128", 100, 60)
    samy = Employee("Samy", 500, 110, car, "samy@gmail.com", 3000, 20)
    iti = Office("ITI Smart Village")
    samy.sendEmail("Ahmed@gmail.com", "samy@gmail.com", "Samy", "Ahmed")

    iti.hire(samy)
    samy.drive(60, 30)
    iti.check_lateness(1, 8)
    save_office_to_json(iti)


if __name__ == "__main__":
    main()
