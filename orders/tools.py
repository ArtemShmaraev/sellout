import requests

import math

from django.db.models import Sum, F

from shipping.models import AddressInfo








def get_delivery_price(units, target_start, target, zip):
    sum = 0
    sum_weight = 0
    delivery_price = 0
    for unit in units:
        sum += unit.final_price
        sum_weight += unit.weight_kg
    delivery_info = get_delivery_costs(sum_weight, sum, target_start, target, zip)
    print(delivery_info, sum, sum_weight)
    if "price_base" in delivery_info:
        delivery_price += (delivery_info['price_base'] * 1.25) + delivery_info['price_service']
    return delivery_price


def get_delivery_costs(weight, ordersum, targetstart, target, zip):
    url = "http://api.boxberry.ru/json.php"
    params = {
        "method": "DeliveryCosts",
        "weight": weight * 1000,
        "target": target,
        "ordersum": ordersum,
        "targetstart": targetstart,
        "token": "f985be8eebb3a5ba0c954d598f176cda",
        "zip": zip
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(data)
        return data
    else:
        print(f"Ошибка {response.status_code}: {response.text}")
        return None


def round_to_nearest(value, step=50):
    return math.ceil(value / step) * step


def send_email_new_order(order, email):
    url = "https://sellout.su/mail/send_order_new_order_mail"
    params = {
        "recipient_email": email,
        "order": order
    }
    requests.post(url, json=params)
    return requests.status_codes


def send_email_confirmation_order(order, email):
    url = "https://sellout.su/mail/send_order_accepted_mail"
    params = {
        "recipient_email": email,
        "order": order
    }
    requests.post(url, json=params)
    return requests.status_codes


def send_email_start_order(order, email):
    url = "https://sellout.su/mail/send_order_on_way"
    params = {
        "recipient_email": email,
        "order": order
    }
    requests.post(url, json=params)
    return requests.status_codes


def send_email_full_order_shipped(order, email): # весь передан в боксбери
    url = "https://sellout.su/mail/send_order_shipped_mail"
    params = {
        "recipient_email": email,
        "order": order
    }
    requests.post(url, json=params)
    return requests.status_codes


def send_email_part_order_partly_shipped(order, email): # частично передан в боксбери
    url = "https://sellout.su/mail/send_order_partly_shipped_mail"
    params = {
        "recipient_email": email,
        "order": order
    }
    requests.post(url, json=params)
    return requests.status_codes






def get_delivery(order, data, cart):
    zip = "0"
    if "address_id" in data:
        zip = AddressInfo.objects.get(id=data['address_id']).post_index

    target = data.get("target", "0")

    if int(data['delivery_type']) == 0:
        order.delivery_price = 0
        order.delivery = "Курьером по Москве"
        order.groups_delivery.append([unit.id for unit in order.order_units.all()])
    else:
        if int(data['delivery_type']) == 1:
            zip = "0"
            name_delivery = "До ПВЗ Boxberry"
        else:
            target = "0"
            name_delivery = "Курьером"

        if data['consolidation']:
            order.groups_delivery.append([unit.id for unit in order.order_units.all()])
            order.delivery_price = int(cart.delivery_info['sum_all'])
            order.delivery = f"{name_delivery}"

        else:
            product_units = order.order_units.annotate(
                delivery_days=F('delivery_type__days_max')
            )
            sorted_product_units = product_units.order_by('delivery_days')
            tec = [sorted_product_units[0]]
            for unit in sorted_product_units[1:]:
                if abs(tec[0].delivery_days - unit.delivery_days) <= 3:
                    tec.append(unit)
                else:
                    order.groups_delivery.append([unit.id for unit in tec])
                    tec = [unit]
            order.groups_delivery.append([unit.id for unit in tec])

            order.delivery_price = int(cart.delivery_info['sum_part'])
            order.delivery = f"{name_delivery} по частям"

    # print(order.delivery_price)

    order.delivery_view_price = order.delivery_price
    order.save()
