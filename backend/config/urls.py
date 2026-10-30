from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

def health_check(request):
    """Basic health check endpoint for container orchestrators and load balancers."""
    return JsonResponse({
        'status': 'healthy',
        'service': 'object_storage_api'
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check, name='health_check'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/auth/', include('apps.accounts.urls', namespace='accounts')),
    path('api/files/', include('apps.files.urls', namespace='files')),
]
