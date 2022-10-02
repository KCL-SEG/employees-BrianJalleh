"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contractType, salary, hoursWorked = None, commissionType = None, numberOfContracts = None, commission = None):
        self.name = name
        self.contractType = contractType
        self.salary = salary
        self.hoursWorked = hoursWorked
        self.commissionType = commissionType
        self.numberOfContracts = numberOfContracts
        self.commission = commission
        
    def calcContractPay(self):
        if(self.contractType == "monthly"):
            return self.salary
        else:
            return self.salary * self.hoursWorked
        
    
    def calcCommissionPay(self):
        if(self.commissionType == "bonus"):    
            return self.commission
        
        elif(self.commissionType == "contract"):
            return self.numberOfContracts * self.commission
        
        else:
            return 0
        

    def get_pay(self):
        return self.calcContractPay() + self.calcCommissionPay()

    def __str__(self):
        
        if(self.commissionType == None):
        
            if(self.contractType == "contract"):
    
                return f"{self.name} works on a {self.contractType} salary of {self.salary}. Their total pay is {self.get_pay()}."
            
            else:
                return f"{self.name} works on a contract of {self.hoursWorked} hours at {self.salary}/hour. Their total pay is {self.get_pay()}."


        elif(self.commissionType == "contract"):
            
            if(self.contractType == "monthly"):
                return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.numberOfContracts} contract(s) at {self.commission}/contract. Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a contract of {self.hoursWorked} hours at {self.salary}/hour and receives a commission for {self.numberOfContracts} contract(s) at {self.commission}/contract. Their total pay is {self.get_pay()}."
        
        else:
            if(self.contractType == "monthly"):
                return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.commission}. Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a contract of {self.hoursWorked} hours at {self.salary}/hour and receives a bonus commission of {self.commission}. Their total pay is {self.get_pay()}."
            
        


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', contractType = "monthly", salary = 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', contractType = "hourly", salary = 25, hoursWorked = 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', contractType = "monthly", salary = 3000, commissionType = "contract", numberOfContracts = 4, commission = 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', contractType = "hourly", salary = 25, hoursWorked = 150, commissionType = "contract", numberOfContracts = 3, commission = 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', contractType = "monthly", salary = 2000, commissionType= "bonus", commission = 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', contractType = "hourly", salary = 30, hoursWorked = 120, commissionType= "bonus", commission = 600)

print(str(billie))
print(str(charlie))
print(str(renee))
print(str(jan))
print(str(robbie))
print(str(ariel))

