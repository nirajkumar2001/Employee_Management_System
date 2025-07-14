from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
#from myapp.views import home, about, services

urlpatterns = [
    path("home/",emp_home),
    path("add-emp/",add_emp),
    path("delete-emp/<int:emp_id>",delete_emp),
    path("update-emp/<int:emp_id>",update_emp),
    path("do-update-emp/<int:emp_id>",do_update_emp),
    path("testimonials/",testimonials),
    # path("feedback/",feedback),
        
    
    
    
]
