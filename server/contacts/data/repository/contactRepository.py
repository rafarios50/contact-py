import typing
from collections import namedtuple
from contacts.common.serviceInjector import ServiceInjector
from contacts.data.entities.contact import Contact
from contacts.data.repository.baseRepository import BaseRepository
from contacts.common.models.contactModel import ContactModel

si = ServiceInjector()

@si.register(name='contactRepository')
class ContactRepository(BaseRepository):
    def __init__(self):
        super().__init__('Contact')

    def save(self, entityObject) -> None:
        super().save(entityObject)

    def findAll(self) -> typing.List[Contact]:
        return super().findAll()
         
    def findById(self, id: int) -> Contact:
        return super().findById(id)

    def findByEmail(self, email: str) -> typing.List[Contact]:
        return list(Contact.objects.filter(email=email).values())

    def findByName(self, name) -> typing.List[Contact]:
        raw = Contact.objects \
                     .filter(name=name) \
                     .values()
        return list(raw)
