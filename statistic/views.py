from datetime import datetime
from rest_framework.views import APIView
from dateutil.relativedelta import relativedelta
from rest_framework.response import Response
from dbapi.users import getRegisterationCount, getTotalRegistrationCount, getLocationStatistic, getYearStatistic, getLastAndCurrentYearStatistic


class RegistrationCountView(APIView):
    def get(self, request):
        start_date = request.GET.get('startDate', (datetime.now() - relativedelta(years=1)).strftime('%Y-%m-%d'))
        end_date = request.GET.get('endDate', datetime.now().strftime('%Y-%m-%d'))
        page = int(request.GET.get('page_num', 0))
        data = getRegisterationCount(start_date, end_date, page)
        
        return Response({'data': data.to_json()})


class TotalRegistrationCountView(APIView):
    def get(self, request):
        start_date = request.GET.get('startDate', (datetime.now() - relativedelta(years=1)).strftime('%Y-%m-%d'))
        end_date = request.GET.get('endDate', datetime.now().strftime('%Y-%m-%d'))

        data = getTotalRegistrationCount(start_date, end_date)

        return Response({'data': data.to_json()})


class LocationCountView(APIView):
    def get(self, request):
        start_date = request.GET.get('startDate', (datetime.now() - relativedelta(years=1)).strftime('%Y-%m-%d'))
        end_date = request.GET.get('endDate', datetime.now().strftime('%Y-%m-%d'))

        data = getLocationStatistic(start_date, end_date)

        return Response({'data': data.to_json()})


class MonthsView(APIView):
    def get(self, request):
        data = getYearStatistic()

        return Response({'data': {'months': data.keys(), '2022': [data[month][0] for month in data.keys()], '2021': [data[month][1] for month in data.keys()]}})


class LastAndCurrentYearStatisticView(APIView):
    def get(self, request):
        currentYear = datetime.now().year
        data = getLastAndCurrentYearStatistic(int(currentYear))
        dataInDict = {'Участники в прошлом году': data['last_year_users'][0], 'Спикеры прошлого года': data['last_year_speacers'][0], 
        'Участники текущего года': data['current_year_users'][0], 'Спикеры текущего года': data['current_year_speacers'][0]}

        return Response({'data': dataInDict})