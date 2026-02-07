from abc import ABC, abstractmethod

class Employee:
    def __init__(self, name: str, base_salary: float):
        self.name = name
        self.base_salary = base_salary

class SalaryCalculator(ABC):
    @abstractmethod
    def calculate_salary(self, employee: Employee) -> float:
        pass

class PermanentEmployeeSalaryCalculator(SalaryCalculator):
    def calculate_salary(self, employee: Employee) -> float:
        return employee.base_salary * 1.2

class ContractEmployeeSalaryCalculator(SalaryCalculator):
    def calculate_salary(self, employee: Employee) -> float:
        return employee.base_salary * 1.1

class InternSalaryCalculator(SalaryCalculator):
    def calculate_salary(self, employee: Employee) -> float:
        return employee.base_salary * 0.8

if __name__ == "__main__":
    employee = Employee("John", 1000)
    calculator = PermanentEmployeeSalaryCalculator()
    print(f"Salary: {calculator.calculate_salary(employee)}")
