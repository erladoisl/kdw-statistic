from datetime import datetime
from rest_framework.views import APIView
from dateutil.relativedelta import relativedelta
from rest_framework.response import Response
from dbapi.users import getRegisterationCount, getTotalRegistrationCount, getLocationStatistic


class RegistrationCountView(APIView):
    def get(self, request):
        print('RegistrationCountView GET')
        start_date = request.GET.get('startDate', (datetime.now() - relativedelta(years=1)).strftime('%Y-%m-%d'))
        end_date = request.GET.get('endDate', datetime.now().strftime('%Y-%m-%d'))
        page = int(request.GET.get('page_num', 0))
        data = getRegisterationCount(start_date, end_date, page)
        
        print(f'start_date: {start_date} end_date: {end_date}')
        print(f'result: {data.to_json()}')
        return Response({'data': data.to_json()})


class TotalRegistrationCountView(APIView):
    def get(self, request):
        print('TotalRegistrationCountView GET')
        start_date = request.GET.get('startDate', (datetime.now() - relativedelta(years=1)).strftime('%Y-%m-%d'))
        end_date = request.GET.get('endDate', datetime.now().strftime('%Y-%m-%d'))

        data = getTotalRegistrationCount(start_date, end_date)

        return Response({'data': data.to_json()})


class LocationCountView(APIView):
    def get(self, request):
        print('LocationCountView GET')
        start_date = request.GET.get('startDate', (datetime.now() - relativedelta(years=1)).strftime('%Y-%m-%d'))
        end_date = request.GET.get('endDate', datetime.now().strftime('%Y-%m-%d'))

        data = getLocationStatistic(start_date, end_date)

        return Response({'data': data.to_json()})