from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # '', include('blog.urls')) configurado em urls.py do blog
    path('', include('blog2.urls')),# '', include('blog.urls')) configurado em urls.py do blog2
    path('accounts/', include('django.contrib.auth.urls')),
    path('', LoginView.as_view(template_name='registration/login.html'), name="login"), #login.html do app blog
    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
]
