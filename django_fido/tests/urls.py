"""URLs for django_fido application tests."""
from django.urls import re_path, include
from django.contrib import admin

from django_fido.views import AttestationConveyancePreference, Fido2RegistrationView

urlpatterns = [
    re_path('', include('django_fido.urls')),
    re_path('admin/', admin.site.urls),
    re_path('direct_registration/',
            Fido2RegistrationView.as_view(attestation=AttestationConveyancePreference.DIRECT),
            name='registration_direct'),
]
