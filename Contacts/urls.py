from django.urls import path
from .views import ContactList, ContactView

urlpatterns = [
    path('', ContactList.as_view(), name='contacts_list'),
    path('<int:pk>', ContactView.as_view(), name='contacts_view'),
]