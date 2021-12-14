from django.db import models
from contacts.common.models.baseModel import BaseModel
from .message import Message

class Contact(models.Model): 
    id = models.AutoField(primary_key=True)
    userId = models.BigIntegerField(null=True)
    name = models.CharField(max_length=255, null=False, unique=True)
    email = models.EmailField(null=False)
    
    def toModel(self) -> BaseModel:
        from contacts.common.models.contactModel import ContactModel
        contact = ContactModel(self.name, self.email, self.id, self.userId)

        return contact
