from . import views


from django.urls import path


urlpatterns = [

    path("", views.PostList.as_view(), name="home"),
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login_request"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]

