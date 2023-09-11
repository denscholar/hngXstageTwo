from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from persons.views import PersonViewSet

router = DefaultRouter()
router.register(
    "",
    PersonViewSet,
    basename='persons'
)


schema_view = get_schema_view(
    openapi.Info(
        title="Person Resource API endpoint",
        default_version="v1",
        description="This endpoints provides acces to a peprson resource with all CRUD functionalities",
        contact=openapi.Contact(email="d.akagha20@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("", include("persons.urls")),
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
