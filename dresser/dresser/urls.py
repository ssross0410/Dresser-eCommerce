from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'products.views.home', name='home'),
    url(r'^s/$', 'products.views.search', name='search'),
    url(r'^products/$', 'products.views.all', name='products'),
    url(r'^products/(?P<slug>[\w-]+)/$', 'products.views.single', name='single_product'),

    url(r'^products/sales/sale$', 'products.views.sales_view', name='sales'),

    # the part of the urls will need to modified by passing the category id or brand id
    # to the corresponding view
    url(r'^products/categorys/shirts/$', 'products.views.shirts_category', name='shirts_category'),
    url(r'^products/categorys/jeans/$', 'products.views.jeans_category', name='jeans_category'),
    url(r'^products/categorys/tees/$', 'products.views.tees_category', name='tees_category'),
    url(r'^products/categorys/suits/$', 'products.views.suits_category', name='suits_category'),
    url(r'^products/categorys/hoodies/$', 'products.views.hoodies_category', name='hoodies_category'),
    url(r'^products/categorys/shoes/$', 'products.views.shoes_category', name='shoes_category'),
    url(r'^products/categorys/jackets/$', 'products.views.jackets_category', name='jackets_category'),

    url(r'^products/brands/zara/$', 'products.views.zara', name='zara'),
    url(r'^products/brands/northface/$', 'products.views.northface', name='northface'),
    url(r'^products/brands/jcrew/$', 'products.views.jcrew', name='jcrew'),
    url(r'^products/brands/nike/$', 'products.views.nike', name='nike'),
    url(r'^products/brands/topshop/$', 'products.views.topshop', name='topshop'),
    url(r'^products/brands/allsaints/$', 'products.views.allsaints', name='allsaints'),
    url(r'^products/brands/h_m/$', 'products.views.h_m', name='h_m'),
    

    url(r'^cart/(?P<id>\d+)/$', 'carts.views.remove_from_cart', name='remove_from_cart'),
    url(r'^cart/(?P<slug>[\w-]+)/$', 'carts.views.add_to_cart', name='add_to_cart'),
    url(r'^cart/$', 'carts.views.view', name='cart'),

    url(r'^checkout/$', 'orders.views.checkout', name='checkout'),
    url(r'^orders/(?P<id>\d+)/$', 'orders.views.order_detail', name='order_detail'),
    url(r'^orders/$', 'orders.views.orders', name='user_orders'),

    url(r'^ajax/add_user_address/$', 'accounts.views.add_user_address', name='ajax_add_user_address'),

    #(?P<all_items>.*)
    #(?P<id>\d+)
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/logout/$', 'accounts.views.logout_view', name='auth_logout'),
    url(r'^accounts/login/$', 'accounts.views.login_view', name='auth_login'),
    url(r'^accounts/register/$', 'accounts.views.registration_view', name='auth_register'),
    url(r'^accounts/activate/(?P<activation_key>\w+)/$', 'accounts.views.activation_view', name='activation_view'),
    url(r'^accounts/profile/$', 'accounts.views.profile_view', name='my_profile'),
) 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)