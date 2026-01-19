from django.urls import path
from . import views   # ← this imports views.py from the same app

urlpatterns = [
    path('',views.home,name='home'),
]
