from django.contrib import admin
from .models import *
from django.contrib import messages
from django.utils.safestring import mark_safe

def totalPrice(modeladmin, request, queryset):
	total = 0
	if queryset:
		for q in queryset:
			total += q.price
		messages.add_message(request, messages.INFO, "Total price : "+str(total))

totalPrice.short_description = "Calculate The Total Price"

class PurchaseLogAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'user')
	list_filter = ('user',)
	actions = [totalPrice]

admin.site.register(User)
admin.site.register(LoginLog)
admin.site.register(FoodList)
admin.site.register(PurchaseLog, PurchaseLogAdmin)