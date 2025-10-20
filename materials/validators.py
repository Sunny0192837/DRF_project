from rest_framework.serializers import ValidationError


def validate_link(url):
    if not url.startswith("https://www.youtube.com") or url.startswith(
        "https://youtu.be"
    ):
        raise ValidationError("Допустимы только ссылки на YouTube")
