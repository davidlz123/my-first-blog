#rom django.contrib import admin
#from django.urls import path

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', include('blog.urls')),
#]


from django.urls import path, include
from django.contrib import admin

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('blog.urls')),
]