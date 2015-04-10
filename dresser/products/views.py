from django.shortcuts import render, Http404

# Create your views here.

from .models import Product, ProductImage
from django.db.models import F

def search(request):
	try:
		q = request.GET.get('q')
	except:
		q = None
	
	if q:
		products = Product.objects.filter(title__icontains=q)
		context = {'query': q, 'products': products}
		template = 'products/results.html'	
	else:
		template = 'products/home.html'	
		context = {}
	return render(request, template, context)

def home(request):
	products = Product.objects.all()
	template = 'products/home.html'	
	context = {"products": products}
	return render(request, template, context)


def all(request):
	products = Product.objects.all()
	context = {'products': products}
	template = 'products/all.html'	
	return render(request, template, context)


def single(request, slug):
	try:
		product = Product.objects.get(slug=slug)
		#images = product.productimage_set.all()
		images = ProductImage.objects.filter(product=product)
		context = {'product': product, "images": images}
		template = 'products/single.html'	
		return render(request, template, context)
	except:
		raise Http404


####################################################################

def sales_view(request):
	products = Product.objects.filter(sale_price__lt=F('price')).order_by('sale_price')
	# products = Product.objects.filter(sale_price__lte=100.00)
	context = {"products": products}
	template = 'products/sales.html'
	return render(request, template, context)


####################################################################
# the category views
def shirts_category(request):
	products = Product.objects.filter(category__title="shirts").order_by('sale_price')
	context = {"products": products}
	template = 'products/category.html'
	return render(request, template, context)


def jeans_category(request):
	products = Product.objects.filter(category__title="Jeans").order_by('sale_price')
	context = {"products": products}
	template = 'products/category.html'
	return render(request, template, context)


def tees_category(request):
	products = Product.objects.filter(category__title="T-shirts").order_by('sale_price')
	context = {"products": products}
	template = 'products/category.html'
	return render(request, template, context)


def suits_category(request):
	products = Product.objects.filter(category__title="Suits").order_by('sale_price')
	context = {"products": products}
	template = 'products/category.html'
	return render(request, template, context)


def hoodies_category(request):
	products = Product.objects.filter(category__title="Sweaters & Hoodies").order_by('sale_price')
	context = {"products": products}
	template = 'products/category.html'
	return render(request, template, context)


def shoes_category(request):
	products = Product.objects.filter(category__title="Shoes").order_by('sale_price')
	context = {"products": products}
	template = 'products/category.html'
	return render(request, template, context)


def jackets_category(request):
	products = Product.objects.filter(category__title="Jackets").order_by('sale_price')
	context = {"products": products}
	template = 'products/category.html'
	return render(request, template, context)


####################################################################
# the brands views
def zara(request):
	products = Product.objects.filter(brand__title="Zara").order_by('sale_price')
	context = {"products": products}
	template = 'products/brand.html'
	return render(request, template, context)

def northface(request):
	products = Product.objects.filter(brand__title="North Face").order_by('sale_price')
	context = {"products": products}
	template = 'products/brand.html'
	return render(request, template, context)

def jcrew(request):
	products = Product.objects.filter(brand__title="J-Crew").order_by('sale_price')
	context = {"products": products}
	template = 'products/brand.html'
	return render(request, template, context)

def allsaints(request):
	products = Product.objects.filter(brand__title="All Saints").order_by('sale_price')
	context = {"products": products}
	template = 'products/brand.html'
	return render(request, template, context)

def h_m(request):
	products = Product.objects.filter(brand__title="H&M").order_by('sale_price')
	context = {"products": products}
	template = 'products/brand.html'
	return render(request, template, context)

def nike(request):
	products = Product.objects.filter(brand__title="Nike").order_by('sale_price')
	context = {"products": products}
	template = 'products/brand.html'
	return render(request, template, context)

def topshop(request):
	products = Product.objects.filter(brand__title="TopShop").order_by('sale_price')
	context = {"products": products}
	template = 'products/brand.html'
	return render(request, template, context)
