from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from Fresh import views

urlpatterns = [
    path('captcha/',include('captcha.urls')),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/',views.contact_create,name='contact_create'),
    path('terms-and-conditions/', views.terms_conditions, name='terms_conditions'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('refund-policy/', views.refund_policy, name='refund_policy'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard/contacts/',views.contact_list,name='contact_list'),
    path('dashboard/contacts/<int:pk>/',views.contact_detail,name='contact_detail'),
    path('dashboard/contacts/<int:pk>/update/',views.contact_update,name='contact_update'),
    path('dashboard/contacts/<int:pk>/delete/',views.contact_delete,name='contact_delete'),
    path(
        'services/',
        views.service_list,
        name='service_list'
    ),

    path(
        'dashboard/services/create/',
        views.service_create,
        name='service_create'
    ),

    path(
        'dashboard/services/<int:pk>/',
        views.service_detail,
        name='service_detail'
    ),

    path(
        'dashboard/services/<int:pk>/update/',
        views.service_update,
        name='service_update'
    ),

    path(
        'dashboard/services/<int:pk>/delete/',
        views.service_delete,
        name='service_delete'
    ),
    path(
        'gallery/',
        views.gallery_page,
        name='gallery_page'
    ),

   
    path(
        'dashboard/gallery/',
        views.gallery_list,
        name='gallery_list'
    ),

    path(
        'dashboard/gallery/create/',
        views.gallery_create,
        name='gallery_create'
    ),

    path(
        'dashboard/gallery/<int:pk>/',
        views.gallery_detail,
        name='gallery_detail'
    ),

    path(
        'dashboard/gallery/<int:pk>/update/',
        views.gallery_update,
        name='gallery_update'
    ),

    path(
        'dashboard/gallery/<int:pk>/delete/',
        views.gallery_delete,
        name='gallery_delete'
    ),
    path(
        'dashboard/offers/',
        views.offer_list,
        name='offer_list'
    ),

    path(
        'dashboard/offers/create/',
        views.offer_create,
        name='offer_create'
    ),

    path(
        'dashboard/offers/<int:pk>/update/',
        views.offer_update,
        name='offer_update'
    ),

    path(
        'dashboard/offers/<int:pk>/delete/',
        views.offer_delete,
        name='offer_delete'
    ),

    # =====================
    # LATEST UPDATES CRUD
    # =====================

    path(
        'dashboard/updates/',
        views.latest_update_list,
        name='latest_update_list'
    ),

    path(
        'dashboard/updates/create/',
        views.latest_update_create,
        name='latest_update_create'
    ),

    path(
        'dashboard/updates/<int:pk>/update/',
        views.latest_update_update,
        name='latest_update_update'
    ),

    path(
        'dashboard/updates/<int:pk>/delete/',
        views.latest_update_delete,
        name='latest_update_delete'
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)