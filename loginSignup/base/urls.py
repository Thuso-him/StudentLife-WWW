from django.urls import path, include
from .views import authView, home, create_reminder, edit_reminder, delete_reminder

urlpatterns = [
 path("accounts/", include("django.contrib.auth.urls")),
 path("signup/", authView, name="authView"),
 path("", home, name="home"),
 path('edit/<int:reminder_id>/', edit_reminder, name='edit_reminder'),
 path("delete/<int:reminder_id>/", delete_reminder, name="delete_reminder"),
 path('create_reminder/', create_reminder, name='create_reminder'),

]
