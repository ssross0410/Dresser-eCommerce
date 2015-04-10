from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=120, unique=True)
	description = models.TextField(null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.title


class Brand(models.Model):
	title = models.CharField(max_length=120, unique=True)
	description = models.TextField(null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.title


class Product(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=50, default=29.99)
	sale_price = models.DecimalField(decimal_places=2, max_digits=50,\
												null=True, blank=True)
	slug = models.SlugField(unique=True)
	category = models.ForeignKey(Category, null=True, blank=True)
	brand = models.ForeignKey(Brand, null=True, blank=True)

	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	update_defaults = models.BooleanField(default=False)

	def __unicode__(self):
		return self.title

	class Meta:
		unique_together = ('title', 'slug')

	def get_price(self):
		return self.price

	def get_absolute_url(self):
		return reverse("single_product", kwargs={"slug": self.slug})


class ProductImage(models.Model):
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to='products/images/')
	featured = models.BooleanField(default=False)
	thumbnail = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.product.title


class VariationManager(models.Manager):
	def all(self):
		return super(VariationManager, self).filter(active=True)

	def sizes(self):
		return self.all().filter(category='size')

	def colors(self):
		return self.all().filter(category='color')


VAR_CATEGORIES = (
	('size', 'size'),
	('color', 'color'),
	('package', 'package'),
	)


class Variation(models.Model):
	product = models.ForeignKey(Product)
	category = models.CharField(max_length=50, choices=VAR_CATEGORIES, default='size')
	title = models.CharField(max_length=50)
	image = models.ForeignKey(ProductImage, null=True, blank=True)
	price = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	objects = VariationManager()

	def __unicode__(self):
		return self.title

class Rating(models.Model):
	product = models.ForeignKey(Product)
	rates = models.DecimalField(max_digits=50, decimal_places=2)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return str(self.rates)

# def product_defaults(sender, instance, created, *args, **kwargs):
# 	if instance.update_defaults:
# 		categories = instance.category.all()
# 		print categories
# 		for cat in categories:
# 			print cat.id
# 			if cat.title == "Shirts":
# 				small_size = Variation.objects.get_or_create(product=instance, 
# 											category='size', 
# 											title='Small')
# 				medium_size = Variation.objects.get_or_create(product=instance, 
# 											category='size', 
# 											title='Medium')
# 				large_size = Variation.objects.get_or_create(product=instance, 
# 											category='size', 
# 											title='Large')
# 		instance.update_defaults = False
# 		instance.save()
# 	#print args, kwargs

# post_save.connect(product_defaults, sender=Product)
