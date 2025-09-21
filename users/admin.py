from django.contrib import admin

from users.models import Payment, User


@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone_number", "city")
    list_filter = ("email",)
    search_fields = (
        "email",
        "city",
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "date",
        "paid_course",
        "paid_lesson",
        "amount",
        "method",
    )
    list_filter = ("user", "method")
    search_fields = (
        "user",
        "paid_course",
        "paid_lesson",
    )
