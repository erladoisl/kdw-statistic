from django.urls import path
from statistic.views import RegistrationCountView
from statistic.views import TotalRegistrationCountView
from statistic.views import LocationCountView
from statistic.views import MonthsView

urlpatterns = [
	path(r'api/statistic/users/registrations/count/in-days/by-period', RegistrationCountView.as_view()),
	path(r'api/statistic/users/registrations/count/total/by-period', TotalRegistrationCountView.as_view()),
	path(r'api/statistic/users/registrations/locations/by-period', LocationCountView.as_view()),
	path(r'api/statistic/users/registrations/count/by-months', MonthsView.as_view()),
]