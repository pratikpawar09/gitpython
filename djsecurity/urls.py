from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
#from appone.views import get_token
from rest_framework.authtoken import views      # app --> drf-->security --> method called
schema_view = get_swagger_view(title='Secure API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),#http://localhost:8000/api-auth/
    url(r'swagger/', schema_view), #http://localhost:8000/swagger
    path('emp/',include('appone.urls')),
    path('token/',views.obtain_auth_token)
]
