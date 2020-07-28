from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Customer
from .forms import CustomerForm

# Create your views here.
class CustomerPostMixin:
    model = Customer
    # fields = '__all__'
    success_url = reverse_lazy('customers:list')
    form_class = CustomerForm


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view)

# customer_list = ListView.as_view(model=Customer)
# customer_detail = DetailView.as_view(model=Customer)

class CustomerList(LoginRequiredMixin, ListView):
    model = Customer


class CustomerDetail(LoginRequiredMixin, DetailView):
    model = Customer

class CustomerCreate(LoginRequiredMixin, CustomerPostMixin, CreateView):
    pass
    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(CustomerCreate, self).dispatch(request, *args, **kwargs)



class CustomerUpdate(LoginRequiredMixin ,CustomerPostMixin, UpdateView):
    pass
    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(CustomerUpdate, self).dispatch(request, *args, **kwargs)



class CustomerDelete(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return redirect(reverse_lazy('customers:list'))
