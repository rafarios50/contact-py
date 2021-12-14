import typing
from contacts.common.models.messageModel import MessageModel
from contacts.data.repository.messageRepository import MessageRepository
from contacts.common.serviceInjector import ServiceInjector
from contacts.data.entities.message import Message

si = ServiceInjector()

@si.register(name='messageService')
class MessageService(object):
    @si.inject('messageRepository')
    def __init__(self, messageRepository: MessageRepository) -> None:
        self.messageRepository = messageRepository()

    def findAllMessages(self) -> typing.List[MessageModel]:
        return self.messageRepository.findAll()
    
    def saveMessage(self, message: MessageModel) -> None:
        self.messageRepository.save(message.toEntity())
