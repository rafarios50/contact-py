from __future__ import annotations
from django.apps import apps
from contacts.data.entities.contact import Contact
from .baseModel import BaseModel

class ContactModel(BaseModel): 
    def __init__(self, name: str, email: str, id: int = 0, userId: int = 0) -> None:
        self.name = name
        self.email = email
        self.id = id
        self.userId = userId

    def __equals__(self, that: any):
        if self == that:
            return True
        if that == None or type(that) != type(self):
            return False
        
        return self.name == that.name and \
               self.email == that.email
               
    def __str__(self):
        return "Contact{" + "id=" + self.id + ", name='" + self.name + '\'' + ", email='" + self.email + '\'' + '}'

    def toEntity(self) -> Contact :
        contact = Contact.objects.create(name = self.name, email = self.email, id = self.id, userId = self.userId)
        return contact