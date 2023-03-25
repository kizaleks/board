import random
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import AuthorUser
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

@receiver(post_save, sender=AuthorUser)
def set_new_user_inactive(sender, instance, created, **kwargs):
    '''Отправка кода при регистрации'''
    if created:
        AuthorUser.objects.filter(email=instance.email).update(is_active=False)
        code=random.randint(1000,9999)
        AuthorUser.objects.filter(email=instance.email).update(activation_code = code)
        send_notifications(code, instance.email)


def send_notifications( code, email):
    html_content=render_to_string(
        'registration/activation_email.html',
        {
            'text':f'Для активации аккаунта передите по ссылке и введите код подтветждения {code}',
            'link': 'http://127.0.0.1:8000/accounts/activation'
        }
    )
    msg=EmailMultiAlternatives(
        subject='Код активации аккаунта',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email]
    )
    msg.attach_alternative(html_content,'text/html')
    msg.send()
