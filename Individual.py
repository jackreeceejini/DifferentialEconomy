class Individual:
    def __init__(self, name, dateOfBirth, SSN):

        self.name = name
        self.DOB = dateOfBirth
        self._ssn = SSN
        self._identity = hash(self.name + self.DOB + str(self._ssn))

    def __str__(self):
        
        return str(self._identity)



#Testing

if __name__ == "__main__":
    newIndividual = Individual("Sophia", "5/12/80",1234)
    print(newIndividual)