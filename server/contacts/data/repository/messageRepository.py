import typing
from contacts.data.repository.baseRepository import BaseRepository
from contacts.data.entities.message import Message
from contacts.common.serviceInjector import ServiceInjector

si = ServiceInjector()

@si.register(name='messageRepository')
class MessageRepository(BaseRepository):
    def __init__(self):
        super().__init__('message')

    def Save(self, entityObject) -> None:
        super().save(entityObject)

    def FindAll(self) -> typing.List[Message]:
        return super().findAll()
