"""Test URL configuration."""

from __future__ import unicode_literals

from django.conf.urls import include, patterns, url


urlpatterns = patterns('',
    (r'^', include('nutrition.urls')),
    (r'^', include('rapidsms.urls.login_logout')),
)
