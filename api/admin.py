from django.contrib import admin
from .models import Orders

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'part_number', 'quantity', 'client', 'plant', 'display_status', 'date_created')
    list_filter = ('status', 'plant')
    search_fields = ('part_number', 'client__username')

    # Custom method to display the status
    def display_status(self, obj):
        return obj.get_status_display()  # Returns the human-readable label
    display_status.short_description = 'Status'  # Column header in the admin

admin.site.register(Orders, OrdersAdmin)
