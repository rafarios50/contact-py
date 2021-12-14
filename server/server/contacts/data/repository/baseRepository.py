from abc import ABC, abstractmethod
from django.apps import apps 

class BaseRepository(ABC):
    def __init__(self, entity: str):
        self.__entity = entity

    def save(self, entityObject) -> None:
        apps.get_model('contacts', self.__entity).save(entityObject)

    def findAll(self) -> any:
        return list(apps.get_model('contacts', self.__entity).objects.all().values())
    
    def findById(self, id: int) -> any:
        return list(apps.get_model('contacts', self.__entity).objects.filter(id=id).values())

