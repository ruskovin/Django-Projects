from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView, View
from django.utils import timezone


# Create your views here.

class HomeView(ListView):
    model = Item
    paginate_by = 10
    template_name = 'home-page.html'


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {"object": order}
            return render(self.request, "order_summary.html", context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect('/')


def checkout(request):
    return render(request, 'checkout-page.html')


class ItemDetailView(DetailView):
    model = Item
    template_name = 'item-detail.html'


@login_required
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
            return redirect("e_commerce_app:order-summary")
        else:
            messages.info(request, "This item was added to your cart")
            order.items.add(order_item)
            return redirect("e_commerce_app:order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")
        return redirect("e_commerce_app:order-summary")


@login_required
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
            return redirect("e_commerce_app:order-summary")
        else:
            # add a message saying the order doesn't contain the order we want to delete
            messages.info(request, "This item was not in your cart")
            return redirect("e_commerce_app:item", slug=slug)
    else:
        messages.info(request, "You don't have an active order")
        return redirect("e_commerce_app:item", slug=slug)


@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=slug).exists():
            order_item = OrderItem.objects.filter(
                user=request.user,
                item=item,
                ordered=False).first()
            if order_item.quantity == 1:
                order.items.remove(order_item)
                messages.info(request, "This item was removed from your cart")
                order_item.delete()
            order_item.quantity -= 1
            order_item.save()

            messages.info(request, "The quantity of this item decreased")
            return redirect("e_commerce_app:order-summary")
        else:
            # add a message saying the order doesn't contain the order we want to delete
            messages.info(request, "This item was not in your cart")
            return redirect("e_commerce_app:item", slug=slug)
    else:
        messages.info(request, "You don't have an active order")
        return redirect("e_commerce_app:item", slug=slug)
