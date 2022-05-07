from djongo import models
from django.conf import settings

CATEGORY_CHOISES=(
    ('NS','Non subscriptive'),
    ('S','Subscription Needed'),
)

LABEL_CHOISES=(
    ('P','primary'),
    ('S','secondary'),
    ('D','danger'),
)

class Item(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    category=models.CharField(choices=CATEGORY_CHOISES,max_length=2)
    label=models.CharField(choices=LABEL_CHOISES,max_length=1)
    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item=Item
    def __str__(self):
        return self.title

class Order(models.Model):
    user=settings.AUTH_USER_MODEL
    items=models.ManyToManyField(OrderItem)
    start_date=models.DateTimeField(auto_now_add=True)
    ordered_date=models.DateTimeField()
    ordered=models.BooleanField(default=False)

    def __str__(self):
        return self.title