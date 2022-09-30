class Employee:

    def __init__(self, name, ID_number, department, job_title, monthly_salary):
        self.__name = name
        self.__ID_number = ID_number
        self.__department = department
        self.__job_title = job_title
        self.__monthly_salary = monthly_salary

    def getName(self):
        return self.__name

    def getID_number(self):
        return self.__ID_number

    def getDepartment(self):
        return self.__department

    def getJobTitle(self):
        return self.__job_title

    def getSalary(self):
        return self.__monthly_salary