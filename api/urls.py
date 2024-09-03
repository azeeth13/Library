from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('books/', KitoblarViews.as_view(), name="kitoblar-api"),
    path('addbooks/',KitoblarCreate.as_view(),name='Kitoblar-add'),
    path('listaddbooks',KitoblarListCreateViews.as_view(),name='kitoblar-views'),
    path('deletebooks/<int:pk>/',KitoblarDeleteViews.as_view(),name='Kitoblar-delete'),
    path('updatebooks/<int:pk>/',KitoblarUpdateViews.as_view(),name="kitoblar-update"),
    path('booksapi/<int:pk>/',BooksApi.as_view()),
    path('categoryapi/',CategoryApi.as_view()),
    path('apibooks/',ApiBooks.as_view()),
    path("users",UserSignup.as_view()),
    # path("inputuser/",UserPage.as_view()),
    

]

