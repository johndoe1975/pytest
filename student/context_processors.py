from django.conf import settings
def insert_settings(request):
    return {"settings": settings}