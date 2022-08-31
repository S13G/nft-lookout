import os
import statistics

from core.models import Settings,Statistics
from django.contrib.messages import success, warning, info, error
from django.db import transaction
from django.shortcuts import redirect, render
from decimal import Decimal
from .signals import alert_admin_signal
from .filters import CollectionFilter
from .models import NFT, Collection, Transaction
# Create your views here.


def index(request):
    featured_collections = Collection.objects.filter(
        featured=True, verification=True).prefetch_related('images').order_by('-created_on')

    verified_collections = Collection.objects.filter(
        verification=True, featured=False).prefetch_related('images').order_by('-created_on')[:19 - featured_collections.count()]

    # limiting the total number to 19
    stats, created = Statistics.objects.get_or_create(id=1)
    Settings.objects.get_or_create(id = 1)
    # Just passing the dummy stats to template
    
    context = {
        'collections': verified_collections,
        'stats': stats,
        'featured': featured_collections
    }
    context['settings'] = Settings.objects.first()

    if context['settings']:
        os.environ['web_name'] = context['settings'].title

    return render(request, 'index.html', context)


def all_collections(request):
    verified_collections = Collection.objects.filter(
        verification=True, featured=False).prefetch_related('images').order_by('-created_on')

    featured_collections = Collection.objects.filter(
        featured=True, verification=True).prefetch_related('images').order_by('-created_on')

    stats, created = Statistics.objects.get_or_create(id=1)

    context = {
        'collections': verified_collections,
        'stats': stats,
        'featured': featured_collections
    }
    context['settings'] = Settings.objects.first()

    return render(request, 'all_collections.html', context)


def search_view(request):
    if request.method == 'POST':

        search_key = str(request.POST['search_key'])

        search_collection = CollectionFilter(search_key)

        stats, created = Statistics.objects.get_or_create(id=1)

        context = {
            'collections': search_collection.search(),
            'featured': search_collection.featured(),
            'search_key': search_key,
            'stats': stats,

        }
        context['settings'] = Settings.objects.first()

    else:
        return redirect('index')
    return render(request, 'collection_search.html', context)


def add_collection(request):
    if request.method == 'POST':

        # Get all inputs

        name = request.POST.get('name')
        network = request.POST.get('network', '')
        floor_price = Decimal(request.POST.get('floor_price'))
        # volume = request.POST.get['volume']
        date = request.POST.get('date')
        discord = request.POST.get('discord')
        twitter = request.POST.get('twitter')
        website = request.POST.get('website')
        listing_type = request.POST.get('listing_type')


    # create objects safely
        try:
            with transaction.atomic():

                collection = Collection.objects.create(
                    name=name,
                    network=network,
                    floor_price=floor_price,
                    # volume=volume,
                    date=date,
                    discord=discord,
                    twitter=twitter,
                    website=website,

                )

                # we are using image2 because it is the secondary option

                image = request.FILES.get('image2', '')
                if image:
                    NFT.objects.create(image=image, collection=collection)

                if listing_type == 'paid':

                    link = request.POST.get('transaction_link', '')
                    if link:
                        Transaction.objects.create(
                            link=link, collection=collection)

                        collection.listing_type = 'paid'

                        collection.save()  # update database depending on wether the listing is paid for or not

                    else:
                        warning(
                            request, "No Link provided, defaults to free listing")

                success(request, "Collection added sucessfully, awaiting approval")
                

        except:
            error(request, "Invalid inputs")
            return redirect('index')

        alert_admin_signal.send_robust(sender=Collection, instance = collection, created = True)
        return redirect('index')
        
