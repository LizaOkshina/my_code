from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'auction', 'created_at', 'created_date', 'update_date', 'user', 'image','small_image']
    list_filter = ['auction', 'created_at']
    actions = ['make_action_false','make_action_true']


    @admin.action(description='Перевести auction в False')
    def make_action_false(self,request, query):
        query.update(action=False)

    @admin.action(description='Перевести auction в True')
    def make_action_true(self, request, query):
        query.update(action=True)



    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'user', 'image', 'small_image'),
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )


admin.site.register(Advertisement, AdvertisementAdmin)