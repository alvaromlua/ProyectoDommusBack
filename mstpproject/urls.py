from django.urls import path, include

urlpatterns = [
    path('api/', include('locations.urls')),
    path('api/', include('accounts.urls'))
]
