from django.contrib import admin

# Register your models here.
from select_learn.models import UserSentence, UserWord

admin.site.register(UserSentence)
admin.site.register(UserWord)
