from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import NFT, Calendar, Transaction
# Register your models here.

class DropsNFTInline(admin.TabularInline):
    model = NFT
    readonly_fields = ['nft_art']

    def nft_art(self, instance):
        return format_html(f'<img src="{instance.image.url}" alt="{instance.collection.name}" class = "thumbnail" >')

@admin.register(Calendar)
class DropsCalendarAdmin(admin.ModelAdmin):
    list_display = ['name', 'network', 'floor_price',
                    'volume', 'verification', 'payment', 'featured']
    list_editable = ['verification']
    list_filter = ["date", "network"]
    list_per_page = 10
    inlines = [DropsNFTInline]
    search_fields = ['name__istartswith', 'network__istartswith']

    @admin.display(ordering='paid', description="Is Paid Listing?")
    def payment(self, collection):
        if collection.listing_type == 'paid':
            if collection.transaction_link:
                url = reverse("admin:drops_transaction_change",
                              args=(collection.transaction_link.id,))

                return format_html('<a href="{}">Yes</a>', url)
            else:
                return '-'
        return "No"

    class Media:
        css = {
            'all': ['thumbnail/image.css']
        }


@admin.register(NFT)
class DropsNFTAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    list_display = ['image', 'collection_volume', 'collection_link']
    list_select_related = ['collection']
    search_fields = ['collection__name__istartswith']

    def collection_volume(self, nft):
        return nft.collection.volume

    def collection_link(self, nft):
        url = reverse("admin:drops_calendar_change",
                      args=(nft.collection.id,))

        return format_html('<a href="{}">{}</a>', url, nft.collection)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass