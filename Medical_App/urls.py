from Medical_App.views import CompanyNameViewSet
from Medical_App import views
from django.urls import path,include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


router=routers.DefaultRouter()
router.register("company",views.CompanyViewSet,basename="company")
router.register("companybank",views.CompanyBankViewSet,basename="companybank")
router.register("medicine",views.MedicineViewSet,basename="medicine")




urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/',TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('api/token/refresh/',TokenRefreshView.as_view(),name="token_refresh"),
    path('api/companybyname/<str:name>',CompanyNameViewSet.as_view(),name="companybyname"),
]