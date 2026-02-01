print("Employee.py LOADED")

from Person import Person

class Employee(Person):
    moods = ("Happy", "Tired", "Lazy")

    def __init__(self, name, money, emp_id, car, email, salary, distanceToWork):
        super().__init__(name, money)
        self.id = emp_id              
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork



    def work(self, hours):
        if hours == 8:
            self.mood ="Happy"
        elif hours < 8:
            self.mood ="Tired"
        else:
            self.mood ="Lazy"


    def sendEmail(self, to, subject, email, receiver_name):
        mail = "email.txt"
        print(f"Preparing to send email to {to}...")
        with open(mail, 'w') as f:
            f.write(f"""From: {self.email}\nTo: {to}\n\nHi, {receiver_name}\nThis is an email template \nThanks""")
        print(f"Email sent to {to} with subject '{subject}' and message '{email}' for {receiver_name}")

    def drive(self, distance, velocity):
        time = distance / velocity
        return time

    def refuel(self, gasAmount=100):
        return gasAmount + self.car.fuelRate    

    