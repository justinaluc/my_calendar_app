from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]

admin.site.site_header = "My Calendar Admin Page"
admin.site.site_title = "My Calendar"
admin.site.index_title = "Welcome to The Admin Area...!"

