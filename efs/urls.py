from django.contrib import admin
from django.conf.urls import  include,url
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #url(r'^accounts/login/$', views.login, name='login'),
    #url( r'^login/$',auth_views.LoginView.as_view(template_name="useraccounts/login.html"), name="login"),
    #url( r'^logout/$',auth_views.LogoutView.as_view(template_name="useraccounts/logout.html"), name="logout"),
    #url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),

]
