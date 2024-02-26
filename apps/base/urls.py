from django.urls import path
from .views import *

urlpatterns = [
    path('', index , name='index'),
    path('blog/', blog, name="blog"),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup')
]
