from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="AirTickets",
        default_version='v1',
        description="Продажа и покупка авиабилетов",
        contact=openapi.Contact(url="https://www.vk.com/danonchibok"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns =[
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('auth/', include('src.oauth.urls'))
]