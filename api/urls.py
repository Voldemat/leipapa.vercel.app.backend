from django.urls import path, include
from django.http import JsonResponse

urlpatterns = [
	path('healthcheck/', lambda request: JsonResponse(status = 200, data = {"ok": True}))
]