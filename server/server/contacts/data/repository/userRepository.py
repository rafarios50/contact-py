import typing
from contacts.data.repository.baseRepository import BaseRepository
from contacts.data.entities.user import User
from contacts.common.serviceInjector import ServiceInjector

si = ServiceInjector()

@si.register(name='userRepository')
class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__('User')

    def save(self, entityObject) -> None:
        super().save(entityObject)

    def findAll(self) -> typing.List[User]:
        return super().findAll()
        
    def findByUsernameAndPassword(self, username, password) -> User:
        raw = User.objects \
                  .filter(username=username, password=password) \
                  .values()
        return list(raw)

    def findByCode(self, code) -> User:
        raw = User.objects \
                  .filter(temporalCode=code) \
                  .values()
        return list(raw)

    def update(self, user):
        user.save()