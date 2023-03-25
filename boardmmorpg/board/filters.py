from django.forms import DateInput
from django_filters import FilterSet, CharFilter, \
    ModelMultipleChoiceFilter, DateFilter, \
    ModelChoiceFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Advertisement, Comment


# создаём фильтр
class AdvertisementFilter(FilterSet):
    model = Advertisement
    # # В fields мы описываем по каким полям модели
    # # будет производиться фильтрация.
    # fields = {
    #     # поиск по названию
    #     'title': ['icontains'],
    #     'Category': ['icontains'],
    #     'dateCreation': ['icontains'],
    # }
    title = CharFilter('title',
                       label='Заголовок содержит:',
                       lookup_expr='icontains',
                       )

    Category = CharFilter('Category',
                       label='Категория:',
                       lookup_expr='icontains',
                       )


    datetime = DateFilter(
        field_name='dateCreation',
        widget=DateInput(attrs={'type': 'date'}),
        lookup_expr='gt',
        label='Даты позже'
    )

    class Meta:
        model = Advertisement
        fields = ['title','Category','dateCreation']

class CommentFilter(FilterSet):
    model = Advertisement
    # # В fields мы описываем по каким полям модели
    # # будет производиться фильтрация.
    # fields = {
    #     # поиск по названию
    #     'title': ['icontains'],
    #     'Category': ['icontains'],
    #     'dateCreation': ['icontains'],
    # }
    title = CharFilter('title',
                       label='Заголовок содержит:',
                       lookup_expr='icontains',
                       )

    Category = CharFilter('Category',
                       label='Категория:',
                       lookup_expr='icontains',
                       )


    datetime = DateFilter(
        field_name='dateCreation',
        widget=DateInput(attrs={'type': 'date'}),
        lookup_expr='gt',
        label='Даты позже'
    )

    class Meta:
        model = Advertisement
        fields = ['title','Category','dateCreation']