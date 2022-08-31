from django.db.models import Q
from .models import Collection


class CollectionFilter:

    def __init__(self, search_key) -> None:
        self.value = search_key

    def search(self):
        search_result = Collection.objects.filter(
            Q(name__icontains=self.value) |
            # For more Accuracy, take just the first 3 characters of the network
            Q(network__icontains=self.value[:3]),
            verification=True, featured=False).\
            prefetch_related('images')

        #  This Step is necessary since there are multiple ways this object can be searched for.
        if self.value.lower() in ["binance", "smart", "chain", "bnb", "binance smart chain"]:
            search_result = Collection.objects.filter(
                network='BSC', verification=True)

        return search_result

    def featured(self):
        search_featured = Collection.objects.filter(
            Q(name__icontains=self.value) |
            # For more Accuracy, take just the first 3 characters of the network
            Q(network__icontains=self.value[:3]),
            verification=True, featured=True).\
            prefetch_related('images')

        #  This Step is necessary since there are multiple ways this object can be searched for.
        if self.value.lower() in ["binance", "smart", "chain", "bnb", "binance smart chain"]:
            search_featured = Collection.objects.filter(
                network='BSC', verification=True, featured=True)

        return search_featured



