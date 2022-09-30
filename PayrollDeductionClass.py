
class PayrollDeduction:

    def __init__(self, description, date, amount, employeeID):
        self.__description = description
        self.__date = date
        self.__amount = amount
        self.__employeeID = employeeID

    def getDescription(self):
        return self.__description

    def getDate(self):
        return self.__date

    def getAmount(self):
        return self.__amount

    def getEmployeeID(self):
        return self.__employeeID