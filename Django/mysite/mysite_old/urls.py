"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views


# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('polls.urls')),
    url(r'^admin/', admin.site.urls),

    url(
        r'^admin/password_reset/$',
        auth_views.PasswordResetView.as_view(),
        name='admin_password_reset',
    ),
    url(
        r'^admin/password_reset/done/$',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    url(
        r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    url(
        r'^reset/done/$',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


