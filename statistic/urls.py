from django.urls import path
import logging
from statistic.views import RegistrationCountView
from statistic.views import TotalRegistrationCountView
from statistic.views import LocationCountView
logging.basicConfig(filename='dtp.log', encoding='utf-8', level=logging.DEBUG)

urlpatterns = [
	path(r'api/user/registration', RegistrationCountView.as_view()),
	path(r'api/user/total/registration', TotalRegistrationCountView.as_view()),
	path(r'api/user/total/location', LocationCountView.as_view()),
]