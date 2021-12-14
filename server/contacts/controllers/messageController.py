import typing
from django.http.response import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from contacts.common.models.messageModel import MessageModel
from contacts.common.serviceInjector import ServiceInjector
from contacts.services.messageService import MessageService
from contacts.common.exceptions import requiredFieldException

class MessageController(viewsets.ViewSet):
    si = ServiceInjector()
    
    @si.inject('messageService')
    def __init__(self, messageService) -> None:
        self.messageService: MessageService = messageService()

    @action(detail=True, methods=['get'])
    def retrieveAllMessages(self, request) -> typing.List[MessageModel]:
        result = self.messageService.findAllMessages()
        
        return JsonResponse(result, status=200, safe=False)

    @action(detail=True, methods=['post'])
    def saveMessage(self, request):
        message = self.dictToMessageModel(request.data)
        self.validateMessageFields(message)
        self.messageService.saveMessage(message)

    def validateMessageFields(message) -> None:
        if not message.content:
            raise requiredFieldException("Content of the message is required.")

        if not message.contacts:
            raise requiredFieldException("At least one contact should be added to the message")
    
    def dictToMessageModel(self, dictionary: dict) -> MessageModel:
        return MessageModel(dictionary.get('userId', None), dictionary.get('content', None), dictionary.get('contacts', None))
