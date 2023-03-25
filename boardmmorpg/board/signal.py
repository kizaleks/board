from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, m2m_changed
from django.contrib.auth.models import User
from .models import Comment, Advertisement
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail


@receiver(pre_save, sender=Comment)
def moderation(sender, instance, **kwargs):
    '''Отправка сообщения при успешной модерации'''
    if instance.commentStatus =='Accept':
        send_mail(
            'Успешная модерация',
            # f'Ваш коментарий {instance.commentUser} успешно прошел модерацию ',
            f'Ваш коментарий {instance.text} успешно прошел модерацию ',
            'kizaleks83@yandex.ru',
            # ["kizaleks83@yandex.ru"],
            [instance.commentUser.email],
            fail_silently=False,
        )


@receiver(post_save, sender=Comment)
def newcomment(sender, instance, created, **kwargs):
    '''Отправка сообщения при добавлении нового коментария'''
    if created:
        send_mail(
            'Новый коментарий',
            f'Пользователь  {instance.commentUser} оставил коментарий {instance.text} под обЪявлением  {instance.commentAdvertisement.title} ',
            'kizaleks83@yandex.ru',
            [instance.commentAdvertisement.author.email],
            fail_silently=False,
        )
@receiver(post_save,  sender=Advertisement)
def notfy_about_new_post(sender, instance, created, **kwargs):
    '''Отправка сообщения при добавлении нового объявления'''
    if  created:
        send_notifications(instance.pk, instance.title, instance.author.email)

def send_notifications(pk, title, email):
    html_content=render_to_string(
        'advertisement_created_email.html',
        {
            'text':title,
            'link': f'{settings.SITE_URL}/board/{pk}'
        }
    )
    msg=EmailMultiAlternatives(
        subject='Новое объявление',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email]
    )
    msg.attach_alternative(html_content,'text/html')
    msg.send()