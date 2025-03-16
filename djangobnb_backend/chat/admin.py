from django.contrib import admin

from .models import Convsersation, ConversationMessage

admin.site.register(Convsersation)
admin.site.register(ConversationMessage)