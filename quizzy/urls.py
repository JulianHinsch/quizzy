from django.contrib import admin, auth
from django.urls import include, path
from django.views.generic.base import TemplateView

from quizzes import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('quizzes/', include('quizzes.urls')),
    path('account/', views.account, name='account'),
]