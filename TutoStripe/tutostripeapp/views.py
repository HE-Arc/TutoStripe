from django.shortcuts import render
from django.http import JsonResponse
import stripe

stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

def index(request):
    return render(request, 'tutostripeapp/index.html')

def simple_buy(request):
    # Get the token of the request
    token = request.POST['stripeToken']

    amount = 999
    # Charge the user of the desired amount
    charge = stripe.Charge.create(
        amount=amount,
        currency='chf',
        description='Example charge',
        source=token,
    )

    context = {
        'amount' : amount / 100
    }

    return render(request, 'tutostripeapp/buy_response.html', context)

def different_buy(request):
    # Same as above but with a different response
    token = request.POST['stripeToken']

    charge = stripe.Charge.create(
        amount=999,
        currency='chf',
        description='Example charge',
        source=token,
    )

    return JsonResponse({ 'amount': 9.99 })
