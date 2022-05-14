from.import views
from django.urls import path

app_name = 'address'
urlpatterns = [
    path('', views.AddressListView.as_view(), name='address_changelist'),
    path('add/', views.AddressCreateView.as_view(), name='address_add'),
    path('<int:pk>/', views.AddressUpdateView.as_view(), name='address_change'),
    path('ajax/load-sellers/', views.load_sellers, name='ajax_load_sellers'),

]