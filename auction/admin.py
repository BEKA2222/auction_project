from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Brand)
admin.site.register(CarModel)
admin.site.register(Car)
admin.site.register(Auction)
admin.site.register(Bid)
admin.site.register(Feedback)