from django.urls import path
from django.views.generic import TemplateView, RedirectView
from django.contrib import admin

from cards import views

urlpatterns = [
    path("admin", admin.site.urls),
    path("", TemplateView.as_view(template_name="user/index.html"), name="home"),
    path("cards", views.CardListView.as_view(), name="card-list"),
    path("new", views.CardCreateView.as_view(), name="card-create"),
    path("edit/<int:pk>", views.CardUpdateView.as_view(), name="card-update"),
    path("box/<int:box_num>", views.BoxView.as_view(), name="box"),
    path("register", views.RegisterNewUserView.as_view(), name="register-new-user"),
    path("login", views.UserLoginView.as_view(), name="user-login"),
    path("logout", views.UserLogoutView.as_view(), name="user-logout"),
    path("profile", views.UserProfileView.as_view(), name="user-profile"),
    path("favicon.ico", RedirectView.as_view(url="/static/favicon.ico")),

    # path("register/", views.register, name="register-new-user"),  # <-- added
]
