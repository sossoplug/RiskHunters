"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns


from django.conf.urls import ( handler400, handler403, handler404, handler500)


handler400              = 'core.views.custom_bad_request_view'
handler403              = 'core.views.custom_permission_denied_view'
handler404              = 'core.views.custom_page_not_found_view'
handler500              = 'core.views.custom_error_view'



urlpatterns             = [
    path('admin/',      admin.site.urls),
    path('rosetta/',    include('rosetta.urls')),
    path('',            include('home.urls')),                  # include the home app urls
    path('users/',      include('users.urls')),                 # include the users app urls
    path('strategy/',   include('strategies.urls')),                 # include the users app urls
    path('i18n/',       include('django.conf.urls.i18n')),

]

urlpatterns             += i18n_patterns(
    path('', include('home.urls')),

)


admin.site.index_title="SAT - Admin"
admin.site.site_header="SAT - Administration"
admin.site.site_title=" "
