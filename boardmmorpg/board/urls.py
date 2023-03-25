from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import AdvertisementList, CommentList, AdvertisementCreate, AdvertisementSearch,\
AdvertisementDeleteView, AdvertisementUpdateView, HomeDetailView, CommentUpdateView

urlpatterns = [
    # path('personalArea/', personalArea.as_view(), name='personalArea'),
    # path('', 'advertisement.html', name='news1'),
    path('board', AdvertisementList.as_view(), name='AdvertisementList'),
    path('comment', CommentList.as_view(), name='comment'),
    path('board/create', AdvertisementCreate.as_view(), name='create'),
    path('board/<int:pk>', HomeDetailView.as_view(),name='AdvertisementDetail'),
    path('board/search', AdvertisementSearch.as_view(), name='AdvertisementSearch'),
    path('board/<int:pk>/edit', AdvertisementUpdateView.as_view(),name='AdvertisementUpdateView'),
    path('board/<int:pk>/delete', AdvertisementDeleteView.as_view(),name='AdvertisementDeleteView'),
    path('Comment/<int:pk>/edit', CommentUpdateView.as_view(),name='CommentUpdateView'),

    # path('register/', register, name="register"),
    # path('activation_code_form/', endreg, name="endreg"),
    # path('',views.activation, name='activation'),
]