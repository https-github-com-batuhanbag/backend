from django.contrib import admin

from .models import UserAccount, EditorAccount

# Register your models here.


@admin.register(UserAccount)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["email", "fullName", "gender", "date_joined"]

    list_display_links = ["email", "date_joined", ]

    search_fields = ["email"]

    list_filter = ["date_joined"]

    class Meta:
        model = UserAccount


@admin.register(EditorAccount)
class EditorAdmin(admin.ModelAdmin):

    list_display = ["email", "fullName", "gender", "date_joined"]

    list_display_links = ["email", "date_joined", ]

    search_fields = ["email"]

    list_filter = ["date_joined"]

    class Meta:
        model = EditorAccount
