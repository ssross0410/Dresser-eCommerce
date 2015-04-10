from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
# Create your models here.
from carts.models import Cart


STATUS_CHOICES = (
		("Started", "Started"),
		("Shipped", "Shipped"),
		("Finished", "Finished"),
	)

#python tuples

User = get_user_model()

class Order(models.Model):
	user = models.ForeignKey(User, blank=True, null=True)
	order_id = models.CharField(max_length=50, default='ABC', unique=True)
	cart = models.ForeignKey(Cart)
	status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Started")
	# address **
	sub_total = models.DecimalField(default=10.99, max_digits=50, decimal_places=2)
	tax_total = models.DecimalField(default=0.00, max_digits=50, decimal_places=2)
	final_total = models.DecimalField(default=10.99, max_digits=50, decimal_places=2)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.order_id

	def get_final_amount(self):
		instance = Order.objects.get(id=self.id)
		instance.tax_total = 0.08 * float(self.sub_total)
		instance.final_total = float(self.sub_total) + float(instance.tax_total)
		instance.save()
		return instance.final_total