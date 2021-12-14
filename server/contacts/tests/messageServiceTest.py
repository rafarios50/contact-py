from django.http.response import JsonResponse
from django.test import TestCase
from django.test.client import RequestFactory
from contacts.services.messageService import MessageService
from unittest.mock import MagicMock
from contacts.data.repository.messageRepository import MessageRepository
from contacts.common.models.messageModel import MessageModel 

class MessageServiceTest(TestCase):
    def setUp(self):
        self.repositoryMock = self.createRepositoryMock()
        self.fakeRequest = RequestFactory().get('/messages')
        self.service = MessageService()
        self.service.messageRepository = self.repositoryMock

    def test_shouldListAllMessages(self):
        result = self.service.findAllMessages()

        self.assertEqual(len(result), 3)

    def test_shouldSaveNewMessage(self):
        message = MessageModel(1, 'content', None)
        self.service.saveMessage(message)

    def createRepositoryMock(self):
        thing = MessageRepository()
        thing.findAll = MagicMock(return_value=[0, 1, 2])
        thing.save = MagicMock(return_value=None)

        return thing

