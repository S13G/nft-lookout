from django.shortcuts import render

# Create your views here.

from core.models import Settings, Statistics
from django.contrib import messages
from django.db import transaction
from django.shortcuts import redirect, render
from decimal import Decimal
from .filters import DropsFilter
from .models import Calendar, NFT, Transaction
from rarenfts.signals import alert_admin_signal


def limited_drops(request):
    context = {}

    context['stats'], created = Statistics.objects.get_or_create(id=1)

    collections = Calendar.objects.filter(
        verification=True).order_by('-created_on')
    context['total'] = collections.count()

    days_list = collections.dates('date', 'day').distinct()

    context['days_list'] = days_list
    context['collections'] = collections

    context['settings'] = Settings.objects.first()
    return render(request, 'calendar.html', context)


def all_drops_by_days(request, day):
    context = {}

    context['stats'], created = Statistics.objects.get_or_create(id=1)

    collections = Calendar.objects.all().filter(date=day).filter(
        verification=True).order_by('-created_on')

    days_list = collections.dates('date', 'day').distinct()

    context['total'] = Calendar.objects.filter(verification=True).count()
    context['days_list'] = days_list
    context['collections'] = collections
    context['settings'] = Settings.objects.first()

    return render(request, 'all_drops_collection_by_date.html', context)


def search_drops_view(request):
    if request.method == 'POST':

        search_key = str(request.POST['search_key'])

        search_drops = DropsFilter(search_key)

        stats, created = Statistics.objects.get_or_create(id=1)

        context = {
            'collections': search_drops.search(),

            'search_key': search_key,
            'stats': stats,
            'total': Calendar.objects.filter(verification=True).count()

        }
        context['settings'] = Settings.objects.first()

    else:
        return redirect('index')
    return render(request, 'calendar_search.html', context)


def search_by_date(request):
    stats, created = Statistics.objects.get_or_create(id=1)

    if request.method == 'POST':
        date = request.POST['search_key']

    context = {
        'search_key': date,
        'collections': Calendar.objects.filter(date=date, verification=True).order_by('-created_on'),
        'stats': stats,
        'total': Calendar.objects.filter(verification=True).count()

    }
    context['settings'] = Settings.objects.first()

    return render(request, 'calendar_search.html', context)


def add_calendar(request):
    if request.method == 'POST':

        # Get all inputs

        name = request.POST['name']
        network = request.POST.get('network', '') # This is beacause there is a possibility that no network is selected
        floor_price = Decimal(request.POST['floor_price'])
        # volume = request.POST['volume']
        date = request.POST['date']
        discord = request.POST['discord']
        twitter = request.POST['twitter']
        website = request.POST['website']
        mint_time = request.POST['mint_time']
        mint_price = Decimal(request.POST['mint_price'])
        total_supply = request.POST['total_supply']

        listing_type = request.POST['listing_type']


    # create objects safely
        try:
            with transaction.atomic():

                collection = Calendar.objects.create(
                    name=name,
                    network=network,
                    floor_price=floor_price,
                    # volume=volume,
                    date=date,
                    discord=discord,
                    twitter=twitter,
                    website=website,
                    mint_price=mint_price,
                    mint_time=mint_time,
                    total_supply=total_supply


                )

                # we are using image2 because it is the secondary option
                image = request.FILES.get('image2', '')
                if image:
                    NFT.objects.create(image=image, collection=collection)

                if listing_type == 'paid':

                    link = request.POST['transaction_link']
                    if link:
                        Transaction.objects.create(
                            link=link, collection=collection)

                        collection.listing_type = 'paid'

                        collection.save()  # update database depending on wether the listing is paid for or not

                    else:
                        messages.warning(request, "No Link provided, defaults to free listing")
                            
                messages.success(request,"You have successfully added a collection to Drops Calendar")
                
                 # redirect home after success

        except:
            messages.error(request, "Invalid inputs")
            return redirect('calendar')

        alert_admin_signal.send_robust(Calendar, instance = collection , created = True)

        return redirect('calendar') 