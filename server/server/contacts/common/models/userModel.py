from .baseModel import BaseModel
from contacts.data.entities.user import User
from uuid import uuid4

class UserModel(BaseModel): 
    def __init__(self, fullName, password, username, temporalCode, id = None) -> None:
        self.id = id
        self.fullName = fullName
        self.password = password
        self.username = username
        self.temporalCode = temporalCode
    
    def __equals__(self, that: any):
        if self == that:
            return True
        if that == None or type(that) != type(self):
            return False
        
        return self.id == that.id and \
               self.fullName == that.fullName and \
               self.username == that.username and \
               self.password == that.password

    def toEntity(self) -> User:
        uuid = self.temporalCode if self.temporalCode != None else uuid4()
        user = User.objects.create(id = self.id ,username = self.username, fullName = self.fullName, password = self.password, temporalCode = uuid.__str__()[0:6])

        return user