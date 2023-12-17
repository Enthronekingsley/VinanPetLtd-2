from django.urls import path
from .views import ReportView, ReportSubmissionRemarkView
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("logout/", views.logout_view, name="logout"),
    path('report/', ReportView.as_view(), name="report"),
    path('report-submitted/', ReportSubmissionRemarkView.as_view(), name="report_submitted"),

    # password change when for login user
    path('password_change/', views.password_change, name="password_change"),
    path("password_change/done/", views.password_change_done, name="password_change_done"),

    # password reset when user is not logged in (forgotten password)
    path('password_reset', views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name="password_reset_confirm")
]
