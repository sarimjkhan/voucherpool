"""voucherpool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from voucherpool_api import urls as voucherpool_urls
from voucherpool_api.views import (
    AdminSpecificApiView,
    CustomerApiView,
    SpecialOfferApiView,
    VoucherApiView,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"customers", CustomerApiView)
router.register(r"specialoffers", SpecialOfferApiView)
router.register(r"vouchers", VoucherApiView)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    # Following paths are added for the custom routes
    path(
        "api/vouchers/validatecode/<str:code>/<str:email>",
        VoucherApiView.validateCode,
        name="validateCode",
    ),
    path(
        "api/vouchers/generate/<str:specialOfferId>",
        VoucherApiView.generate,
        name="generate",
    ),
    path(
        "api/vouchers/codes/<str:email>",
        VoucherApiView.getCodes,
        name="getCodes",
    ),
    path(
        "api/admin/vouchers/codes",
        AdminSpecificApiView.getCodesForAdmin,
        name="getCodesFroAdmin",
    ),
]
