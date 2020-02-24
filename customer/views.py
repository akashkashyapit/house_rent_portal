from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from houseowner.models import housedetail
from customer.models import TicketGenerate
from .forms import HouseDetailForm
from math import ceil


# Create your views here.

def home(request):
    product = housedetail.objects.all()
    return render(request, 'home.html', {'product': product})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


@login_required
def product(request, mid):
    product = housedetail.objects.filter(id=mid)
    print(product)

    return render(request, 'product.html', {'product': product[0]})


# @login_required
def add_house(request):
    if request.method == 'POST':
        form = HouseDetailForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            form = HouseDetailForm()
            return render(request, 'add_house.html', {'message': 'Your Data save successfully!!', 'form': form})
    else:
        form = HouseDetailForm()
    return render(request, 'add_house.html', {'form': form})


# def add_house_details(request):
#     bedrooms = request.POST.get('bedrooms')
#     bathrooms = request.POST.get('bathrooms')
#     area = request.POST.get('area')
#     expected_rent = request.POST.get('expected_rent')
#     expected_advance = request.POST.get('expected_advance')
#     images = request.POST.get('images')
#
#     details = housedetail(bedrooms=bedrooms,
#                           bathrooms=bathrooms,
#                           area=area,
#                           expected_rent=expected_rent,
#                           expected_advance=expected_advance,
#                           image=images
#                           )
#     details.save()
#     return render(request, 'add_house.html', {'message': "You have successfully submitted your details!!"})
#

def ticket_generate(request):
    uname = request.POST.get('uname')
    email = request.POST.get('email')
    message = request.POST.get('message')

    tc = TicketGenerate(uname=uname, email=email, message=message)
    tc.save()
    return render(request, 'secret_page.html')


def see_ticket(request):
    tickets = TicketGenerate.objects.all()
    return render(request, 'ticket_view.html', {'tickets': tickets})
