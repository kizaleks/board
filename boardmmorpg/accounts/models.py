from django.contrib.auth.models import User
from django.db import models

class AuthorUser(User):
    '''К модели User добавлено поле код активации '''
    activation_code=models.CharField(max_length=4)