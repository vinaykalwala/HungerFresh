from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def terms_conditions(request):
    return render(request, 'terms_conditions.html')


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def refund_policy(request):
    return render(request, 'refund_policy.html')