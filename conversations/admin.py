from django.contrib import admin
from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """Message Admin Model"""

    list_display = ("__str__", "created")


@admin.register(models.Conversation)
class Conversation(admin.ModelAdmin):

    """Conversation Admin Model"""

    list_display = ("__str__", "count_messages", "count_participants")