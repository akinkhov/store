from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from common.views import TitleMixin
from orders.forms import OrdersForm


class OrderCreateView(TitleMixin, CreateView):
    template_name = 'order-create.html'
    title = 'Оформление заказа'
    form_class = OrdersForm
    success_url = reverse_lazy('orders:order-create')

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)
