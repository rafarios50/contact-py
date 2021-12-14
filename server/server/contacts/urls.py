"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from contacts.controllers import ContactController, MessageController, UserController

urlpatterns = [
    path('contacts/', ContactController.as_view({
        'get': 'retrieveAllContacts', 'post': 'saveContact'
    })),
    path('contacts/<int:id>', ContactController.as_view({
        'get': 'retrieveContactById'
    })),
    path('contacts/<str:name>', ContactController.as_view({
        'get': 'retrieveContactsByName'
    })),
    path('messages/', MessageController.as_view({
        'get': 'retrieveAllMessages', 'post': 'saveMessage'
    })),
    path('users/', UserController.as_view({
        'get': 'retrieveAllUsers', 'post': 'saveUser', 'put': 'updateUser'
    })),
    path('users/<int:id>', UserController.as_view({
        'get': 'retrieveAllUsers', 'post': 'saveUser'
    })),
    path('users/<str:code>', UserController.as_view({
        'get': 'confirmUserCode'
    })),
    path('sign-in', UserController.as_view({
        'post': 'authenticateUser'
    })),
]
