from django.urls import path
from .views import BlogView, BlogViewForm

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('blogform', BlogViewForm.as_view(), name='blogform')

]
