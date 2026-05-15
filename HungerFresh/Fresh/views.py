from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


def home(request):

    offers = Offer.objects.filter(
        is_active=True
    )[:6]

    latest_updates = LatestUpdate.objects.filter(
        is_active=True
    )[:6]

    context = {

        'offers': offers,

        'latest_updates': latest_updates,
    }

    return render(
        request,
        'home.html',
        context
    )

def about(request):
    return render(request, 'about.html')

def diet_plan(request):
    return render(request, 'diet_plan.html')


def terms_conditions(request):
    return render(request, 'terms_conditions.html')


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def refund_policy(request):
    return render(request, 'refund_policy.html')


def contact_create(request):

    form = ContactForm()

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Contact form submitted successfully.'
            )

            return redirect('contact_create')

    return render(
        request,
        'contact_create.html',
        {'form': form}
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        else:

            messages.error(
                request,
                'Invalid username or password'
            )

    return render(
        request,
        'login.html'
    )



@login_required
def logout_view(request):

    logout(request)

    return redirect('home')


@login_required
def dashboard(request):

    total_contacts = Contact.objects.count()

    new_contacts = Contact.objects.filter(
        status='new'
    ).count()

    read_contacts = Contact.objects.filter(
        status='read'
    ).count()

    context = {

        'total_contacts': total_contacts,

        'new_contacts': new_contacts,

        'read_contacts': read_contacts,
    }

    return render(
        request,
        'dashboard.html',
        context
    )


@login_required
def contact_list(request):

    contacts = Contact.objects.all()

    return render(
        request,
        'contact_list.html',
        {'contacts': contacts}
    )


@login_required
def contact_detail(request, pk):

    contact = get_object_or_404(
        Contact,
        pk=pk
    )

    if contact.status == 'new':

        contact.status = 'read'

        contact.save()

    return render(
        request,
        'contact_detail.html',
        {'contact': contact}
    )


@login_required
def contact_update(request, pk):

    contact = get_object_or_404(
        Contact,
        pk=pk
    )

    form = ContactUpdateForm(
        instance=contact
    )

    if request.method == 'POST':

        form = ContactUpdateForm(
            request.POST,
            instance=contact
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Contact updated successfully.'
            )

            return redirect('contact_list')

    return render(
        request,
        'contact_update.html',
        {
            'form': form,
            'contact': contact
        }
    )


@login_required
def contact_delete(request, pk):

    contact = get_object_or_404(
        Contact,
        pk=pk
    )

    if request.method == 'POST':

        contact.delete()

        messages.success(
            request,
            'Contact deleted successfully.'
        )

        return redirect('contact_list')

    return render(
        request,
        'contact_delete.html',
        {'contact': contact}
    )

def service_list(request):

    services = Service.objects.all()

    return render(
        request,
        'services/service_list.html',
        {'services': services}
    )


# =========================
# SERVICE CREATE
# =========================

@login_required
def service_create(request):

    form = ServiceForm()

    if request.method == 'POST':

        form = ServiceForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Service created successfully.'
            )

            return redirect('service_list')

    return render(
        request,
        'services/service_create.html',
        {'form': form}
    )


# =========================
# SERVICE DETAIL
# =========================


def service_detail(request, pk):

    service = get_object_or_404(
        Service,
        pk=pk
    )

    return render(
        request,
        'services/service_detail.html',
        {'service': service}
    )


# =========================
# SERVICE UPDATE
# =========================

@login_required
def service_update(request, pk):

    service = get_object_or_404(
        Service,
        pk=pk
    )

    form = ServiceForm(
        instance=service
    )

    if request.method == 'POST':

        form = ServiceForm(
            request.POST,
            request.FILES,
            instance=service
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Service updated successfully.'
            )

            return redirect('service_list')

    return render(
        request,
        'services/service_update.html',
        {
            'form': form,
            'service': service
        }
    )


# =========================
# SERVICE DELETE
# =========================

@login_required
def service_delete(request, pk):

    service = get_object_or_404(
        Service,
        pk=pk
    )

    if request.method == 'POST':

        service.delete()

        messages.success(
            request,
            'Service deleted successfully.'
        )

        return redirect('service_list')

    return render(
        request,
        'services/service_delete.html',
        {'service': service}
    )

def gallery_page(request):

    galleries = Gallery.objects.filter(
        is_active=True
    )

    category = request.GET.get('category')

    if category:

        galleries = galleries.filter(
            category=category
        )

    context = {
        'galleries': galleries
    }

    return render(
        request,
        'gallery/gallery_page.html',
        context
    )


# =========================
# ADMIN GALLERY LIST
# =========================

@login_required
def gallery_list(request):

    galleries = Gallery.objects.all()

    return render(
        request,
        'gallery/gallery_list.html',
        {'galleries': galleries}
    )


# =========================
# CREATE GALLERY
# =========================

@login_required
def gallery_create(request):

    form = GalleryForm()

    if request.method == 'POST':

        form = GalleryForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Gallery item created successfully.'
            )

            return redirect('gallery_list')

    return render(
        request,
        'gallery/gallery_create.html',
        {'form': form}
    )


# =========================
# GALLERY DETAIL
# =========================

@login_required
def gallery_detail(request, pk):

    gallery = get_object_or_404(
        Gallery,
        pk=pk
    )

    return render(
        request,
        'gallery/gallery_detail.html',
        {'gallery': gallery}
    )


# =========================
# UPDATE GALLERY
# =========================

@login_required
def gallery_update(request, pk):

    gallery = get_object_or_404(
        Gallery,
        pk=pk
    )

    form = GalleryForm(
        instance=gallery
    )

    if request.method == 'POST':

        form = GalleryForm(
            request.POST,
            request.FILES,
            instance=gallery
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Gallery updated successfully.'
            )

            return redirect('gallery_list')

    return render(
        request,
        'gallery/gallery_update.html',
        {
            'form': form,
            'gallery': gallery
        }
    )


# =========================
# DELETE GALLERY
# =========================

@login_required
def gallery_delete(request, pk):

    gallery = get_object_or_404(
        Gallery,
        pk=pk
    )

    if request.method == 'POST':

        gallery.delete()

        messages.success(
            request,
            'Gallery deleted successfully.'
        )

        return redirect('gallery_list')

    return render(
        request,
        'gallery/gallery_delete.html',
        {'gallery': gallery}
    )

@login_required
def offer_list(request):

    offers = Offer.objects.all()

    return render(
        request,
        'offers/offer_list.html',
        {'offers': offers}
    )


@login_required
def offer_create(request):

    form = OfferForm()

    if request.method == 'POST':

        form = OfferForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Offer created successfully.'
            )

            return redirect('offer_list')

    return render(
        request,
        'offers/offer_create.html',
        {'form': form}
    )


@login_required
def offer_update(request, pk):

    offer = get_object_or_404(
        Offer,
        pk=pk
    )

    form = OfferForm(
        instance=offer
    )

    if request.method == 'POST':

        form = OfferForm(
            request.POST,
            request.FILES,
            instance=offer
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Offer updated successfully.'
            )

            return redirect('offer_list')

    return render(
        request,
        'offers/offer_update.html',
        {
            'form': form,
            'offer': offer
        }
    )


@login_required
def offer_delete(request, pk):

    offer = get_object_or_404(
        Offer,
        pk=pk
    )

    if request.method == 'POST':

        offer.delete()

        messages.success(
            request,
            'Offer deleted successfully.'
        )

        return redirect('offer_list')

    return render(
        request,
        'offers/offer_delete.html',
        {'offer': offer}
    )


# =========================
# LATEST UPDATE CRUD
# =========================

@login_required
def latest_update_list(request):

    updates = LatestUpdate.objects.all()

    return render(
        request,
        'updates/update_list.html',
        {'updates': updates}
    )


@login_required
def latest_update_create(request):

    form = LatestUpdateForm()

    if request.method == 'POST':

        form = LatestUpdateForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Update created successfully.'
            )

            return redirect('latest_update_list')

    return render(
        request,
        'updates/update_create.html',
        {'form': form}
    )


@login_required
def latest_update_update(request, pk):

    update = get_object_or_404(
        LatestUpdate,
        pk=pk
    )

    form = LatestUpdateForm(
        instance=update
    )

    if request.method == 'POST':

        form = LatestUpdateForm(
            request.POST,
            request.FILES,
            instance=update
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Update updated successfully.'
            )

            return redirect('latest_update_list')

    return render(
        request,
        'updates/update_update.html',
        {
            'form': form,
            'update': update
        }
    )


@login_required
def latest_update_delete(request, pk):

    update = get_object_or_404(
        LatestUpdate,
        pk=pk
    )

    if request.method == 'POST':

        update.delete()

        messages.success(
            request,
            'Update deleted successfully.'
        )

        return redirect('latest_update_list')

    return render(
        request,
        'updates/update_delete.html',
        {'update': update}
    )