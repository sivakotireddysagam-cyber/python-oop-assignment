
#Task 1: Class Design
#Question:
#ABC Company conducts training programs for employees to improve their skills. Employees can register for courses and provide feedback after attending the training.
Create the required Python classes based on the following information:
Employee
Employee ID
Employee Name
Salary
Course
Course ID
Course Name
Course Duration
Create the required classes and relationships. If you feel additional classes are needed, you may add them.

    class Employee:
    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary


class Course:
    def __init__(self, course_id, course_name, duration):
        self.course_id = course_id
        self.course_name = course_name
        self.duration = duration

 #Task 2: Inheritance
#Question:
#Employees belong to different categories:
Junior Engineer
Assessment Score
Feedback
Software Engineer
Project Name
Trainer
Skills
Certifications
Design the solution using appropriate OOP concepts. Continue using the classes created in Task 1.

class JuniorEngineer(Employee):
    def __init__(self, emp_id, emp_name, salary,
                 assessment_score, feedback):
        super().__init__(emp_id, emp_name, salary)
        self.assessment_score = assessment_score
        self.feedback = feedback


class SoftwareEngineer(Employee):
    def __init__(self, emp_id, emp_name, salary,
                 project_name):
        super().__init__(emp_id, emp_name, salary)
        self.project_name = project_name


class Trainer(Employee):
    def __init__(self, emp_id, emp_name, salary,
                 skills, certifications):
        super().__init__(emp_id, emp_name, salary)
        self.skills = skills
        self.certifications = certifications

          #Task 3: Composition / HAS-A Relationship
#Question:
#ABC Company introduces a new requirement:
Every Employee has an Address.
Address contains:
Floor Number
Street Name
City Name
State

class Address:
    def __init__(self, floor_no, street_name,
                 city_name, state, country):
        self.floor_no = floor_no
        self.street_name = street_name
        self.city_name = city_name
        self.state = state
        self.country = country


class Employee:
    def __init__(self, emp_id, emp_name,
                 salary, address):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary
        self.address = address


# Creating Address Object
addr = Address(
    101,
    "MG Road",
    "Hyderabad",
    "Telangana",
    "India"
)

# Employee HAS-A Address
emp = Employee(
    1,
    "Ravi",
    50000,
    addr
                   )
