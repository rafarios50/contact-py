from django.http.response import JsonResponse
from django.test import TestCase
from django.test.client import RequestFactory
from contacts.controllers.contactController import ContactController
from unittest.mock import MagicMock
from contacts.data.repository.contactRepository import ContactRepository 

class ContactControllerTest(TestCase):
    def setUp(self):
        self.repositoryMock = self.createRepositoryMock()
        self.fakeRequest = RequestFactory().get('/contacts')
        self.controller = ContactController()
        self.controller.contactRepository = self.repositoryMock

    def test_shouldReturnOkStatusWhenRetrievingAllContacts(self):
        result: JsonResponse = self.controller.retrieveAllContacts(self.fakeRequest)

        self.assertEqual(result.status_code, 200)

    def test_shouldReturnOkStatusWhenRetrievingContactById(self):
        result: JsonResponse = self.controller.retrieveContactById(self.fakeRequest, 5)

        self.assertEqual(result.status_code, 200)

    def test_shouldReturnBadRequestWhenEmailIsEmptyForNewContact(self):
        self.fakeRequest.data = {'email': '', 'name': 'testName'}
        result: JsonResponse = self.controller.saveContact(self.fakeRequest)

        self.assertEqual(result.status_code, 400)

    
    def test_shouldReturnOkWhenSavingContact(self):
        #TODO: Add this test
        pass


    def createRepositoryMock(self):
        thing = ContactRepository()
        thing.findAll = MagicMock(return_value=[])
        thing.findById = MagicMock(return_value=True)
        thing.findByEmail = MagicMock(return_value=[])
        thing.findByName = MagicMock(return_value=[])

        return thing
    

# shouldListAllMessages()
# shouldSaveNewMessage()

# shouldReturnOkStatusWhenRetrievingAllMessage()
# shouldReturnOkStatusWhenSavingMessage()
# shouldReturnBadRequestWhenMessageIsEmpty()