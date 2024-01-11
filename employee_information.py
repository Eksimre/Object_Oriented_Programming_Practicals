import datetime
class Employee(object):
    
    def __init__(self,id,name,surname,salary):
        self.id = id
        self.name = name.title()
        self.surname = surname.title()
        self.salary = int(salary)
        self.em_list = []
    
    def e_mail(self):
        return f"{self.name}.{self.surname}@company.com"
       
    def salary_increase(self, n):
        self.salary = self.salary + (self.salary * int(n))/100

    def date_of_employment(self):
        return datetime.datetime.now().strftime('%d %B %Y')
    
    def __str__(self):
        return f"İd: {self.id} \nName: {self.name} \nSurname: {self.surname} \nTarih: {self.date_of_employment()} \nE-mail: {self.e_mail()} \nsalary: {self.salary} \ndepartment: {self.department}"
               
    def employee_list(self):
        self.em_list.append([self.id, self.name, self.surname, self.e_mail(), self.date_of_employment(), self.salary, self.department])       
        return self.em_list
        
class Developer(Employee):

    def __init__(self, id, name, surname, salary, language, department = "Developer"):
        super().__init__(id, name, surname, salary)
        self.department = department.title()
        self.language = language.title()
            
    def __str__(self):
        return f"{super().__str__()} \nLanguage: {self.language}"
    
    def employee_list(self):
        super_employee_list = super().employee_list()
        super_employee_list[0].append(self.language)
        return super_employee_list
        
class Manager(Employee):
    def __init__(self, id, name, surname, salary, department = "Manager"):
        super().__init__(id, name, surname, salary)
        self.department = department.title()