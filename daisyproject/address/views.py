# from django.shortcuts import render, redirect, get_object_or_404
# from . models import District, Seller, Customer
# from .forms import AddAddressForm
# # Create your views here.
# def address_list_view(request):
#     form = AddAddressForm
#     return render(request, 'delivery.html', {'form': form})
#
# def address_create_view(request):
#     form = AddAddressForm()
#     if request.method == 'POST':
#         form = AddAddressForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('address_add')
#     return render(request, 'address.html', {'form': form})
#
#
# def address_update_view(request, pk):
#     customer = get_object_or_404(Customer, pk=pk)
#     form = AddAddressForm(instance=customer)
#     if request.method == 'POST':
#         form = AddAddressForm(request.POST, instance=customer)
#         if form.is_valid():
#             form.save()
#             return redirect('address_change', pk=pk)
#     return render(request, 'address.html', {'form': form})
#
# # AJAX
# def load_sellers(request):
#     district_id = request.GET.get('district_id')
#     sellers = Seller.objects.filter(district_id=district_id).all()
#     return render(request, 'add.html', {'sellers': sellers})
#
#-----------------------------------------------------------------------------------------------------------

from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from . forms import AddAddressForm
from .models import Customer, Seller


class AddressListView(ListView):
    model = Customer
    context_object_name = 'address'


class AddressCreateView(CreateView):
    model = Customer
    form_class = AddAddressForm
    success_url = reverse_lazy('address_changelist')


class AddressUpdateView(UpdateView):
    model = Customer
    form_class = AddAddressForm
    success_url = reverse_lazy('address_changelist')


def load_sellers(request):
    district_id = request.GET.get('district_id')
    sellers = Seller.objects.filter(district_id=district_id).all()
    return render(request, 'address/add.html', {'sellers': sellers})