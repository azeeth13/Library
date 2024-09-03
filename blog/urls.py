from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('',views.HomePage,name='home'),
    path('about/',AboutPage,name='about'),
    path('book/',BookPage,name='book'),
    path('search/', SearchPage, name='search'),
    path('book/<slug:slug>/', BookInfoPage),
    path('contact/', ContactPage, name='contact'),
    path('search/',SearchPage,name='search'),
    path('category/<slug:slug>/', views.category_books, name='category_books'),
    path('book/<slug:slug>/', views.book_detail, name='book_detail')
    # path('signup/', signup, name='signup'),
    # path('contact/',ContactPage.as_view(),name='contact'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
