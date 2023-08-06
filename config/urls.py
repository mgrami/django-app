from django.contrib import admin
from django.urls import path

from django.http import HttpResponse, JsonResponse
def hello_json_view(request):
    return JsonResponse({"message": "Hello, world!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hello_json_view),
]
