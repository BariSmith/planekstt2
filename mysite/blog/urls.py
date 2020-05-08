from django_registration.forms import RegistrationFormUniqueEmail

from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from . import views, admin
from django.urls import path, include


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('accounts/', include('registration.urls')),
    # Uncomment the next line to enable the admin:
    path('admin/', include(admin.site.urls)),
    path('register/$', views.register, {'form': RegistrationFormUniqueEmail}, name='registration_register'),
    path('', include('registration')),
]

admin.site.unregister(User)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff','is_active',)
    list_filter = ('is_staff', 'is_superuser', 'is_active',)
admin.site.register(User, CustomUserAdmin)
