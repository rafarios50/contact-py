import typing
from contacts.common.models.contactModel import ContactModel
from contacts.data.entities.message import Message
from contacts.data.entities.user import User
from .baseModel import BaseModel

class MessageModel(BaseModel): 
    def __init__(self, userId: str, content: str, contacts: typing.List[ContactModel], id: int = 0) -> None:
        self.id = id 
        self.userId = userId
        self.content = content
        self.contacts = contacts

    def toEntity(self) -> Message:
        userData = User.objects.create()
        message = Message.objects.create(id = self.id, user = userData , content = self.content)
        return message
