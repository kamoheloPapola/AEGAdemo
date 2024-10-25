import stripe
from django.conf import settings
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

def process_payment(request):
    payment_intent = stripe.PaymentIntent.create(
        amount=1000,  # Replace with actual calculation logic
        currency='usd',
    )
    return JsonResponse({'client_secret': payment_intent['client_secret']})
