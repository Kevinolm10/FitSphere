from django.conf import settings


def social_links(request):
    return {
        'social_links': settings.SOCIAL_LINKS,
    }
