from django.urls import path
from .views import (
    FacebookLeadsView,
    AcresLeadsView,
    MagicBricksLeadsView,
    HousingLeadsView,
)

urlpatterns = [
    path("facebook/", FacebookLeadsView.as_view(), name="facebook_webhook"),
    path("99acres/", AcresLeadsView.as_view(), name="acres_webhook"),
    path("magicbricks/", MagicBricksLeadsView.as_view(), name="magicbricks_webhook"),
    path("housing/", HousingLeadsView.as_view(), name="housing_webhook"),
]
