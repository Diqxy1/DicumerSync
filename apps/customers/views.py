from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, View
from django.urls import reverse_lazy
from .models import Customer

# Create your views here.
class CustomerPostMixin:
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('customers:list')


customer_list = ListView.as_view(model=Customer)
customer_detail = DetailView.as_view(model=Customer)


class CustomerCreate(CustomerPostMixin, CreateView):
    pass


class CustomerUpdate(CustomerPostMixin, UpdateView):
    pass


class CustomerDelete(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return redirect(reverse_lazy('customers:list'))
