from hashlib import sha256
class Individual:
    def __init__(self, name, dateOfBirth, SSN):

        self.name = name
        self.DOB = dateOfBirth
        self._ssn = SSN
        self._personalData = self.name + self.DOB + str(self._ssn)
        self._identity = sha256(str.encode(self._personalData))

    #Todo
    def getIndividualName(self):
        return self.name
    #def getIndividualDOB
    #def getAccountBalance
    #def getIncomeRate

    def __str__(self):
        
        return str(self._identity.hexdigest())



#Testing

if __name__ == "__main__":
    newIndividual = Individual("Sophia", "5/12/80",1234)
    print(newIndividual)