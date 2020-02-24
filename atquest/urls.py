from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customer import views
from atquest import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('add_house/', views.add_house, name='add_house'),
    path('product/<int:mid>', views.product, name='product'),
    # path('add_house_details/', views.add_house_details, name='add_house_details'),
    path('ticket/', views.ticket_generate, name='ticket'),
    path('see_ticket/', views.see_ticket, name='see_ticket'),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
