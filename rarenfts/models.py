from django.db import models
from uuid import uuid4

from .helpers import get_media_paths


class Collection (models.Model):

    SOLANA = 'SOL'
    ETHEREUM = 'ETH'
    BINANCE_SMART_CHAIN = 'BSC'
    MATIC = 'MATIC'

    NETWORK = (
        ('Null', 'Null'),
        (SOLANA, 'SOLANA'),
        (ETHEREUM, 'ETHEREUM'),
        (BINANCE_SMART_CHAIN, 'BSC'),
        (MATIC, 'MATIC')
    )

    LISTING_TYPE = (('free', 'free'), ('paid', 'paid'))

    name = models.CharField(max_length=255)
    guid = models.UUIDField(default=uuid4, unique=True, editable=False)
    network = models.CharField(max_length=255, choices=NETWORK, default=ETHEREUM)
    floor_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, default=0)
    volume = models.PositiveIntegerField(default=0, null=True, blank=True)
    date = models.DateField()
    discord = models.URLField(max_length=550, null=True, blank=True)
    twitter = models.URLField(max_length=550, null=True, blank=True)
    website = models.URLField(max_length=550, null=True, blank=True)
    listing_type = models.CharField(
        max_length=10, choices=LISTING_TYPE, default='free')

    verification = models.BooleanField(default=False, verbose_name="approve",
                                       help_text="Only approved collections will be visible on the list page")

    featured = models.BooleanField(
        default=False, help_text='Toggle this option to make a collection display as featured')

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class NFT (models.Model):
    image = models.ImageField(upload_to=get_media_paths)
    collection = models.OneToOneField(
        Collection, on_delete=models.CASCADE, related_name='images')

    def __str__(self) -> str:
        return f'{self.collection.name} NFT'


class Transaction(models.Model):
    link = models.URLField(max_length=550)
    collection = models.OneToOneField(
        Collection, on_delete=models.CASCADE, related_name='transaction_link')

    def __str__(self) -> str:
        return f'{self.collection} Project'





