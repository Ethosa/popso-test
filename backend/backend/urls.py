from django.contrib import admin
from django.urls import path
from authorization.views import auth, register, get_by_id, update_user

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", auth),
    path("register/", register),
    path("user/<int:user_id>", get_by_id),
    path("update-user/", update_user),
]
