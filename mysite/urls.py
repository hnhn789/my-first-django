from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
from.views import SignupView, StoryListView, ShopListView, BuyItem, QRCode



urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/signup/$", SignupView.as_view(), name="account_signup"),
    url(r"^account/", include("account.urls")),
 #   url(r'^storypoints/(?P<uid>[0-9]+)/$', GetStoryPoints.as_view(), name='storypoints'),
#    url(r"^storyboard/", StoryListView.as_view(), name="storyboard"),
#    url(r"^shop/$", ShopListView.as_view(), name="shop"),
    url(r"^shop/(?P<uid>\d+)/(?P<item_id>\d+)/$", BuyItem.buy()),
    url(r"^QRcode/(?P<uid>\d+)/(?P<code>\d+)/$", QRCode.got_code()),  #TODO request not done
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
