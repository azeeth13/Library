from django.contrib import admin
from django.urls import path,include
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage,name='home'),
    path('about/',AboutPage,name='about'),
    path('apis/',include('api.urls')),
    path('logout/', LogoutPage, name='logout'),
    # path('login/', LoginPage, name='login'),
    # path('signup/', SignupPage, name='signup'),
    path('',include('blog.urls')),
    path('search/', SearchPage, name='search'),
    path('', include('django.contrib.auth.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

