from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedSoftDeleteModel


class Item(TimeStampedSoftDeleteModel):
    """
    Model for items in purchase order
    """

    item_code = models.PositiveIntegerField(verbose_name='Item Code', null=False, blank=False, default=00000)
    item_name = models.CharField(max_length=128)


class OrderCartItem(TimeStampedSoftDeleteModel):
    """
    Through Model for item in Order
    """

    item = models.ForeignKey('Item', related_name='cart_orders', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', related_name='cart_items', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(verbose_name=_('Item quantity'))
    price = models.DecimalField(verbose_name=_('Item price'), max_digits=8, decimal_places=3)


class Order(TimeStampedSoftDeleteModel):
    """
    Model for transaction order
    """

    SELL = 1
    PURCHASE = 2
    transaction_type = (
        (SELL, _('Sell')),
        (PURCHASE, _('Purchase'))
    )
    items = models.ManyToManyField('Item', through=OrderCartItem, related_name='orders')
    order_date = models.DateField()
    order_type = models.IntegerField(choices=transaction_type, default=SELL)
