from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.disappear_maker.urls')),
]
