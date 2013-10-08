from django.contrib import admin

from polls.models import Poll
from polls.models import Choice


#admin.site.register(Poll)
admin.site.register(Choice)

#class PollAdmin(admin.ModelAdmin):
#    fields = ['pub_date','question']

#admin.site.register(Poll, PollAdmin)

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Panel de pregunta',{'fields':['question']}),
        ('Date information',{'fields':['pub_date']}),
    ]
    inlines = [ChoiceInline]




admin.site.register(Poll, PollAdmin)
#admin.site.register(Choice, ChoiceAdmin)
