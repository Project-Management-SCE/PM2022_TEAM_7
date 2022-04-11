from django.contrib import admin
from django.urls import path

from personal.views import (
    home_screen_view,
)
from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
)
#url list of pages
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name="home"),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('account/', account_view, name="account"),
]
