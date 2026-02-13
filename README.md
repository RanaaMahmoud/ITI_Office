# 🚀 ITI Python OOP Project – Employee & Office Management System

This project is part of my **Python Object-Oriented Programming (OOP) Lab** at **ITI – Open Source Department**.

The goal of this project is to apply **OOP concepts**, **real-life modeling**, and **file handling** by simulating an employee working environment.

---

## 📌 Project Story

Samy is an employee who works at **ITI Smart Village**.  
He goes to work every day (except weekends) using his **Fiat 128 car**.

The system models:
- People and employees
- Cars and fuel consumption
- Offices and employee management
- Lateness calculation based on distance and velocity
- Saving office data to a JSON file

---

## 📁 Project Structure

```
project-name/
│
├── Person.py        # Base Person class
├── Employee.py      # Employee class (inherits Person)
├── Car.py           # Car class
├── Office.py        # Office class & employee management
├── main.py          # Entry point to run the project
├── office.json      # JSON file to save office data
└── README.md        # Project documentation
```




---

## 🧠 Concepts Applied

- Object-Oriented Programming (OOP)
  - Inheritance
  - Encapsulation
  - Class & Static methods
- Python Modules & Imports
- File Handling
  - Writing structured data to JSON
- Business Logic Simulation
- Debugging & Error Handling

---

## 🧑‍💻 Classes Overview

### 👤 Person
- Attributes: `name`, `money`, `mood`, `healthRate`
- Methods: `sleep()`, `eat()`, `buy()`

### 👨‍💼 Employee (inherits Person)
- Attributes: `id`, `car`, `email`, `salary`, `distanceToWork`
- Methods: `work()`, `drive()`, `refuel()`, `sendEmail()`

### 🚗 Car
- Attributes: `name`, `fuelRate`, `velocity`
- Methods: `run()`, `stop()`

### 🏢 Office
- Attributes: `name`, `employees`
- Methods:
  - `hire()`, 'fire()'
  - `get_employee()`, `get_all_employees()`
  - `deduct()`, `reward()`
  - `check_lateness()`
  - `calculate_lateness()` (static)

---

## 💾 JSON Output

Office data is saved into a JSON file:

```json
{
  "office_name": "ITI Smart Village",
  "employees": [
    {
      "id": 1,
      "name": "Samy",
      "email": "samy@gmail.com",
      "salary": 3000
    }
  ]
}
```

---
📬 Contact

If you’d like to reach out, you can connect with me through:

Email: ranammustafa@gmail.com

LinkedIn: http://linkedin.com/in/ranamahmoudmuhammed

