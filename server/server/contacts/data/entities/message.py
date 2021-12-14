from django.db import models

from contacts.common.models import baseModel
from .user import User

class Message(models.Model): 
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    contacts = models.ManyToManyField('Contact', related_name="messages")

    def toModel(self) -> baseModel:
        from contacts.common.models.messageModel import MessageModel
        contact = MessageModel(self.user, self.content, self.id, self.contacts)

        return contact