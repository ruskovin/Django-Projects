from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView
from django.utils import timezone


# Create your views here.

class HomeView(ListView):
    model = Item
    paginate_by = 10
    template_name = 'home-page.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'item-detail.html'


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        user=request.user,
        item=item,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated")
            return redirect("e_commerce_app:item", slug=slug)
        else:
            messages.info(request, "This item was added to your cart")
            order.items.add(order_item)
            return redirect("e_commerce_app:item", slug=slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")
        return redirect("e_commerce_app:item", slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        print(order.items.filter(item__slug=slug))
        print(order.items.all())
        if order.items.filter(item__slug=slug).exists():
            print("inside the loop")
            order_item = OrderItem.objects.filter(
                user=request.user,
                item=item,
                ordered=False).first()
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your cart")
            order_item.delete()
            return redirect("e_commerce_app:item", slug=slug)
        else:
            # add a message saying the order doesn't contain the order we want to delete
            messages.info(request, "This item was not in your cart")
            return redirect("e_commerce_app:item", slug=slug)
    else:
        messages.info(request, "You don't have an active order")
        return redirect("e_commerce_app:item", slug=slug)
