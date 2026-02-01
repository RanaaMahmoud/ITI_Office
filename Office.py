class Office:
    employeesNum = 0   

    def __init__(self, name):
        self.name = name
        self.employees = {}  

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num

    def get_all_employees(self):
        return list(self.employees.values())

    def get_employee(self, emp_id):
        return self.employees.get(emp_id)

    def hire(self, employee):
        self.employees[employee.id] = employee
        Office.employeesNum += 1

    def fire(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            Office.employeesNum -= 1

    def deduct(self, emp_id, deduction):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary -= deduction

    def reward(self, emp_id, reward):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += reward

    def check_lateness(self, emp_id, moveHour):
        emp = self.get_employee(emp_id)
        if not emp:
            return

        late = Office.calculate_lateness(
            targetHour=9,
            moveHour=moveHour,
            distance=emp.distanceToWork,
            velocity=emp.car.velocity
        )

        if late:
            self.deduct(emp_id, 10)
        else:
            self.reward(emp_id, 10)

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        time_needed = distance / velocity
        arrival_time = moveHour + time_needed
        return arrival_time > targetHour
