from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51T7ddTRoe4mPZF9Nfx4vV6uKoPQNFyFBe3rbfrCQu6EdbXwochr0u6jcsMZ8qHRFzlcnlrdzM1Ziz7T3oJay7ZKC00pH9RloLE',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
