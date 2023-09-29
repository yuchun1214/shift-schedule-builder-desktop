# define user class here
# username: str, 
# password: str, 
# email: str, 
# shifts: []

class User(object):

    username=str
    password=str
    email=str
    shifts=[]

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getEmail(self):
        return self.email

    def getShifts(self):
        return self.shifts

    def setUsername(self, username):
        if(type(username) != str):
            raise Exception("TypeError")
        self.username = username

    def setPassword(self, password):
        if(type(password) != str):
            raise Exception("TypeError")
        self.password = password

    def setEmail(self, email):
        if(type(email) != str):
            raise Exception("TypeError")
        self.email = email

    def setShifts(self, shifts):
        if(type(shifts) != list):
            raise Exception("TypeError")
        self.shifts = shifts