import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza, Topping

pizzas = Pizza.objects.all()

for p in pizzas:
    print(p.id)
    print(p.text)
    print(p.date_added)

p = Pizza.objects.get(id=2)
print(p)

toppings = p.topping_set.all()

for t in toppings:
    print(t)