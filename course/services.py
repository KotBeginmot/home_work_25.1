import os

import stripe

def user_check(obj, instance):
    user = obj.context['request'].user
    return (instance.subscription_set.get(user=user).subscription if user in [i.user for i in
                                                                              instance.subscription_set.all()] else 'не студент курса')


def stripe_work(obj, instance):
    try:
        stripe.api_key = os.getenv("API_KEY")
        product = stripe.Product.create(name="Course payment")

        price = stripe.Price.create(
            unit_amount=1200,
            currency="usd",
            recurring={"interval": "month"},
            product=product["id"],
        )
        checkout = stripe.checkout.Session.create(
            success_url="https://example.com/success",
            line_items=[
                {
                    "price": price["id"],
                    "quantity": 2,
                },
            ],
            mode="subscription",
        )
        retrieve_session = stripe.checkout.Session.retrieve(
            checkout.id,
        )

        return checkout, retrieve_session, checkout.id

    except Exception as e:
        print(e)
        return [{"url": "some gonna wrong"}, 0]


