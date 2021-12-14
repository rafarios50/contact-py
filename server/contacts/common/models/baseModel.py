from __future__ import annotations
from abc import ABC, abstractmethod

class BaseModel(ABC): 
    def __init__(self, id) -> None:
        self.id = id

    @abstractmethod
    def toEntity(self):
        pass