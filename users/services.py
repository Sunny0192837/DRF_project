import stripe
from config.settings import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY

def create_stripe_price(amount):
    """
    Создает цену в страйпе.
    :param: amount-сумма, с которой создается цена
    :return: объект цены
    """

    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product_data={"name":"CoursePurchase"}
    )

def create_stripe_session(price):
    """
    Создает сессию для оплаты.
    :param: price-id объекта цены
    :return: id сессии, юрл сессии
    """

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )

    return session.get("id"), session.get("url")

