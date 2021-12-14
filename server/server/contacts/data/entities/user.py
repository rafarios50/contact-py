from django.db import models

from contacts.common.models import baseModel

class User(models.Model): 
    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, null=False, unique=True)
    temporalCode = models.CharField(max_length=255, null=True)

    def toModel(self) -> baseModel:
        from contacts.common.models.userModel import UserModel
        contact = UserModel(self.name, self.email, self.id, self.userId)

        return contact