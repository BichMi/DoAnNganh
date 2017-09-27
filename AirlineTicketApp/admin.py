from django.contrib import admin
from .models import *



admin.site.register(UserType)
admin.site.register(User)
admin.site.register(SeatType)
admin.site.register(TicketType)
admin.site.register(Airline)
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(FlightRoute)
admin.site.register(Plane)
admin.site.register(TicketBook)
admin.site.register(BookInfo)

