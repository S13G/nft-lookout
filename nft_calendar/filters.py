from .models import Calendar
from django.db.models import Q
class DropsFilter:

    def __init__(self, search_key) -> None:
        self.value = search_key

    def search(self):
        search_result = Calendar.objects.filter(
            Q(name__icontains=self.value) |
            # For more Accuracy, take just the first 3 characters of the network
            Q(network__icontains=self.value[:3])).\
            prefetch_related('images').filter(verification = True)

        #  This Step is necessary since there are multiple ways this object can be searched for.
        if self.value.lower() in ["binance", "smart", "chain", "bnb", "binance smart chain"]:
            search_result = Calendar.objects.filter(
                network='BSC', verification=True)

        return search_result.order_by('-featured')