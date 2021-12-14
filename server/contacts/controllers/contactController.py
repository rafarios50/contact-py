from rest_framework import viewsets
from rest_framework.decorators import action
from contacts.common.serviceInjector import ServiceInjector
from contacts.data.repository.contactRepository import ContactRepository
from contacts.common.exceptions import ContactNotFoundException, DuplicatedContactException, RequiredFieldException
from contacts.common.models.contactModel import ContactModel
from django.http import JsonResponse

class ContactController(viewsets.ViewSet):
    si = ServiceInjector()
    
    @si.inject('contactRepository')
    def __init__(self, contactRepository: ContactRepository) -> None:
        self.contactRepository: ContactRepository = contactRepository()

    @action(detail=True, methods=['get'])
    def retrieveAllContacts(self, request) -> JsonResponse:
        result = self.contactRepository.findAll()
        return JsonResponse(result, status=200, safe=False)

    @action(detail=True, methods=['get'])
    def retrieveContactsByName(self, request, name: str) -> JsonResponse:
        result = self.contactRepository.findByName(name)
        return JsonResponse(result, status=200, safe=False)

    @action(detail=True, methods=['get'])
    def retrieveContactById(self, request, id: int):
        contact = self.contactRepository.findById(id)
        if not contact:
            raise ContactNotFoundException("Unable to find contact with Id: " + id.__str__())

        return JsonResponse(contact, status=200, safe=False)

    @action(detail=True, methods=['post'])
    def saveContact(self, request):
        try:
            data = request.data
            contact = self.dictToContactModel(data)
            self.validateContactFields(contact)
            self.contactRepository.save(contact.toEntity())

            return JsonResponse('Contact created successfully', status=201, safe=False)
        except RequiredFieldException as e:
            return JsonResponse(e.__str__(), status=400, safe=False)

    def validateContactFields(self, contact: ContactModel) -> None:
        if not contact.email:
            raise RequiredFieldException("email")

        if not contact.name:
            raise RequiredFieldException("name")
        
        existingContact = self.contactRepository.findByEmail(contact.email)
        if len(existingContact):
            raise DuplicatedContactException("Unable to create contact due duplicated email: " + contact.email)

    def dictToContactModel(self, dictionary: dict) -> ContactModel:
        return ContactModel(dictionary.get('name', None), dictionary.get('email', None), dictionary.get('id', None), dictionary.get('userId', 1))
