from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,View
from django.shortcuts import redirect
from .models import Item, Order, OrderItem
from django.utils import timezone
from .forms import CheckoutForm

def product(request):
    context = {
        'items':Item.objects.all()
    }
    return render(request,"products.html",context)

class CheckoutView(View):
    def get(self,*args,**kwargs):
        form=CheckoutForm()
        context={
            'form':form
        }
        return render(self.request,"checkout.html",context)

    def post(self,*args,**kwargs):
        form=CheckoutForm(self.request.POST or None)
        if form.is_valid():
            print("form valid")
            return redirect('drugs:checkout')

class HomeView(ListView):
    model=Item
    paginate_by=10
    template_name="home.html"

class OrderSummaryView(View):
    def get(self,*args,**kwargs):
        try:
            order=Order.objects.get(user=self.request.user, ordered=False)
            context={
                'object': order
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "you don't have an active order")
            return redirect("/")

class ItemDetailView(DetailView):
    model=Item
    template_name="product.html"


def add_to_cart(request,slug):
    item=get_object_or_404(Item,slug=slug)
    order_item, created=OrderItem.objects.get_or_create(item=item,
                                               user=request.user,
                                               ordered=False)
    order_qs=Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity+=1
            order_item.save()
            messages.info(request,"This item quantity was updated.")
            return redirect("drugs:order-summary")
        else:
            order.items.add(order_item)
            messages.info(request,"This item was added to your cart.")
            return redirect("drugs:order-summary")

    else:
        ordered_date=timezone.now()
        order=Order.objects.create(
            user=request.user,
            ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("drugs:order-summary")



def remove_from_cart(request,slug):
    item=get_object_or_404(Item,slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item=OrderItem.objects.filter(item=item,
                                               user=request.user,
                                               ordered=False)[0]
            order_item.quantity -= 0
            order_item.save()
            order.items.remove(order_item)
            messages.info(request,"This item was removed from your cart.")
            return redirect("drugs:order-summary")
        else:
            messages.info(request,"This item wasn't in your cart.")
            return redirect("drugs:product", slug=slug)
    else:
        messages.info(request, "You don't have an active order")
        return redirect("drugs:product")


def remove_single_item_from_cart(request,slug):
    item=get_object_or_404(Item,slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item=OrderItem.objects.filter(item=item,
                                               user=request.user,
                                               ordered=False)[0]
            order_item.quantity -= 1
            if order_item.quantity==0:
                order.items.remove(order_item)
            order_item.save()
            messages.info(request,"This item quantity was updated.")
            return redirect("drugs:order-summary")
        else:
            messages.info(request,"This item wasn't in your cart.")
            return redirect("drugs:product", slug=slug)
    else:
        messages.info(request, "You don't have an active order")
        return redirect("drugs:product", slug=slug)
