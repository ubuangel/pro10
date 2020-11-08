"""pro10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#esta es la rama 2
from django.contrib import admin
from django.urls import path
from pro10.views import saludo,despedida
#from pro10.views import despedida#importar funcion al archivo urls
from pro10.views import year_archive

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/',saludo),    
    path('nosveremos/',despedida),
    
    
    path('articles/<int:year>/', year_archive),
    #path('articles/<int:year>/<int:month>/', views.month_archive),
    #path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
    
]







