import typing
from django.http.response import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from contacts.common.models.userModel import UserModel
from contacts.common.exceptions import InvalidConfirmationCode, InvalidCredentialsException, RequiredFieldException
from contacts.data.repository.userRepository import UserRepository
from contacts.common.serviceInjector import ServiceInjector

class UserController(viewsets.ViewSet):
    si = ServiceInjector()
    
    @si.inject('userRepository')
    def __init__(self, userRepository) -> None:
        self.userRepository = userRepository()

    @action(detail=True, methods=['get'])
    def retrieveAllUsers(self, request) -> typing.List[UserModel]:
        users = self.userRepository.findAll()
        return JsonResponse(users, status=200, safe=False)
    
    @action(detail=True, methods=['get'])
    def confirmUserCode(self, request, code: str) -> UserModel:
        user = self.userRepository.findByCode(code) 
        if not user:
            raise InvalidConfirmationCode("Invalid code confirmation: " + code)

        return JsonResponse(user, status=201, safe=False)

    @action(detail=True, methods=['post'])
    def saveUser(self, request) -> UserModel:
        user = self.dictToUserModel(request.data)
        print(request.data['username'])
        self.validateUserFields(user)
        userData = user.toEntity()
        self.userRepository.save(userData)
        
        return JsonResponse(userData.temporalCode, status=201, safe=False)
    
    @action(detail=True, methods=['post'])
    def authenticateUser(self, request) -> UserModel:
        user = self.dictToUserModel(request.data)
        validUser = self.userRepository.findByUsernameAndPassword(user.username, user.password)

        if not validUser:
            raise InvalidCredentialsException("Invalid Username or password for user '" + user.getFullName() + "'")
        
        return JsonResponse(validUser, status=200, safe=False)
    
    @action(detail=True, methods=['put'])
    def updateUser(self, request):
        user = self.dictToUserModel(request.data)
        self.validateUserFields(user)
        self.userRepository.update(user.toEntity())

        return JsonResponse('Success', status=200, safe=False)

    def validateUserFields(self, user) -> None:
        if not user.username:
            raise RequiredFieldException("username")

    def dictToUserModel(self, dictionary: dict) -> UserModel:
        return UserModel(dictionary.get('fullName', ''), dictionary.get('password', ''), dictionary.get('username', ''), dictionary.get('temporalCode', None), dictionary.get('id', None))
