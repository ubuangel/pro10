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
    2. Add a UUURL to urlpatterns:  path('blog/', include('blog.urls'))
rama2 equivocacion
"""

# een las arams podemos tabajar y si estanseguros del codigo manda un pull request para que se agregue ala rama master
from django.contrib import admin
from django.urls import path
from pro10.views import saludo,despedida,dameFecha
#from pro10.views import despedida#importar funcion al archivo urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/',saludo),    
    path('nosveremos/',despedida),
    path('fechahora/',dameFecha),
]
