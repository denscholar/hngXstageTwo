from django.urls import path
from . import views



urlpatterns = [
    path("", views.PersonListView.as_view(), name='add_list_persons'),
    path('<str:id_or_name>/', views.PersonRetrieveUpdateDelete.as_view(), name='add_list_persons'),

]
