from django.contrib import admin
from .models import Advertisement, Comment
from django import forms
from ckeditor.widgets import CKEditorWidget

# class AdvertisementAdminForm(forms.ModelForm):
#     text = forms.CharField(widget=CKEditorWidget())
#     class Meta:
#         model = Advertisement
#         fields = '__all__'
# class AdvertisementAdmin(admin.ModelAdmin):
#     form = AdvertisementAdminForm

class CommentAdmin(admin.ModelAdmin):

    list_display = ('commentUser', 'commentAdvertisement', 'dateCreation','text','commentStatus')
    list_filter = ('commentUser', 'commentAdvertisement', 'dateCreation','commentStatus')
    search_fields = ('commentStatus', 'dateCreation', 'text')




admin.site.register(Advertisement,)
admin.site.register(Comment,CommentAdmin)

