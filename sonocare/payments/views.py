from django.conf import settings
from django.shortcuts import render
import stripe
import datetime

stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
    return render(request, 'index.html', locals())


def payments(request):

    publishKey = settings.STRIPE_PUBLISHABLE_KEY

    if request.method == 'POST':
        token = request.POST['stripeToken']
        # Create a charge: this will charge the user's card
        try:
            charge = stripe.Charge.create(
                amount=1000,  # Amount in cents
                currency="usd",
                source=token,
                description="Sonocare, LLC"
            )
            if charge:
                amount = str(charge['amount'])
                amount = amount[:2] + "." + amount[2:]
                charge['amount'] = amount
                date = datetime.datetime.now()
                return render(request, 'payments/success.html', locals())
        except stripe.error.CardError as e:
            # The card has been declined
            pass
    context = {'publishKey': publishKey}

    return render(request, 'payments/payments.html', locals())


def paymentsdev(request):

    publishKey = settings.STRIPE_PUBLISHABLE_KEY

    if request.method == 'POST':
        token = request.POST['stripeToken']
        # Create a charge: this will charge the user's card
        try:
            charge = stripe.Charge.create(
                amount=1000,  # Amount in cents
                currency="usd",
                source=token,
                description="Sonocare, LLC"
            )
            if charge:
                return render(request, 'payments/success.html', locals())
        except stripe.error.CardError as e:
            # The card has been declined
            pass
    context = {'publishKey': publishKey}

    return render(request, 'payments/payments-dev.html', locals())
