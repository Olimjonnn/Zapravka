import re
from unittest import removeResult
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication 
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView
from rest_framework.decorators import action, api_view, APIView, authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import status
from django.http import Http404
from main.models import *
from main.serializer import *


class InfoView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def get(self, request):
        info = Info.objects.last()
        inf = InfoSerializer(info)
        return Response(inf.data)

    def post(self, request):
        user = request.user
        if user.type == 2:
            info = InfoSerializer(data=request.data)
            if info.is_valid():
                info.save()
                return Response(info.data, status=status.HTTP_201_CREATED)
            return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"You are can not add informations"})

class InfoUpdate(UpdateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]


class ClientView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        if user.type == 2:
            client = Client.objects.all()
            serializer = ClientSerializer(client, many=True)
            return Response(serializer.data)
        else:
            return Response({"You are can not view informations"})

    def create(self, request):
        user = request.user
        if user.type == 3:
            client = ClientSerializer(data=request.data)
            if client.is_valid():
                client.save()
                return Response(client.data, status=status.HTTP_201_CREATED)
            return Response(client.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"You are can not register"})

class ClientUpdate(UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

            
class BenzinGet(ListAPIView):
    queryset = Benzin.objects.all()
    serializer_class = BenzinSerializer
    
    def list(self, request):
        benzin = Benzin.objects.all()
        benz = BenzinSerializer(benzin, many=True)
        return Response(benz.data)


class BenzinUpdate(UpdateAPIView):
    queryset = Benzin.objects.all()
    serializer_class = BenzinSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]


class BenzinProductionView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]


    def get(self, request):
        user = request.user
        if user.type == 2:
            prod = BenzinProduction.objects.all()
            pr = BenzinProductionSerializer(prod, many=True)
            return Response(pr.data)
        else:
            return Response({"You are can not view informations"})

    def post(self, request):
        user = request.user
        if user.type == 2:
            benzin = request.data['benzin']
            qunatity = request.data['quantity']
            allow = request.data['allow']
            force = BenzinProduction.objects.create(
                benzin_id=benzin,
                qunatity=qunatity,
                allow=allow,
            )
            addmission = BenzinProductionSerializer(force)
            return Response(addmission.data)
        else:
            return Response({"You are can not add informations"})


class BenzinProductionPost(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        if user.type == 2:
            production = request.data["production"]
            br = BenzinProduction.objects.get(id=production)
            benzin = br.benzin
            benzin.quantity += br.quantity
            benzin.save()
            br.allow = 2
            br.save()
            ar = BenzinProductionSerializer(br)
            return Response(ar.data)
        else:
            return Response({"You are can not add informations"})

class CashGet(ListAPIView):
    queryset = Cash.objects.all()
    serializer_class = CashSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        if user.type == 1:
            cash = Cash.objects.first()
            cas = CashSerializer(cash)
            return Response(cas.data)
        else:
            return Response({"You are can not view informations"})


class PayView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user 
        if user.type == 2 or user.type == 1:
            pay = Pay.objects.all()
            py = PaySerializer(pay, many=True)
            return Response(py.data)
        else:
            return Response({"You are can not view informations"})

    def post(self, request):
        try:
            user = request.user 
            if user.type == 3:
                client_id = request.data['client']
                benzin_id = request.data['benzin']
                quantity = request.data['quantity']
                Pay.objects.create(
                    client_id=client_id,
                    benzin_id=benzin_id,
                    quantity=quantity,
                )
                client = Client.objects.get(id=client_id)
                benzin = Benzin.objects.get(id=benzin_id)
                client.payed += int(quantity)*int(benzin.price)
                client.save()
                benzin.quantity -= int(quantity)
                benzin.save()
                cash = Cash.objects.filter()
                if cash.count()> 0:
                    cash = Cash.objects.first()
                else:
                    cash = Cash.objects.create(cash = int(quantity)*int(benzin.price))
                cash.cash += int(quantity)*int(benzin.price)
                cash.save()
                summa = 0
                summa += int(quantity)*int(benzin.price)
                return Response({f"Thank you for useing our oil, {benzin.name} oil, {quantity} liter successfully poured {summa} payed"})
        except Exception as ar:
            data = {
                'error':f"{ar}"
            }
            return Response(data)


class PayClientGet(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user
        if user.type == 2 or user.type == 3:
            client = request.GET.get("client")
            pay = Pay.objects.filter(client_id=client)
            py = PaySerializer(pay, many=True)
            return Response(py.data)

class PayTimeGet(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.type == 2 or user.type == 1:
            client = request.GET.get("client")
            st_time = request.GET.get("st_time")
            end_time = request.GET.get("end_time")
            pay = Pay.objects.filter(
                client_id=client, 
                date__gte=st_time,
                date__lte=end_time,
            )
            benefit = 0
            lis = []
            for i in pay:
                benefit += int(i.benzin.price)*int(i.quantity)
                dat = {
                    "Client name": i.client.name,
                    "Benzin Type": i.benzin.name,
                    "Summa": i.quantity*i.benzin.price
                }
                lis.append(dat)
            data = {
                "Payed": lis,
                "Total Benefit": benefit
            }            
            return Response(data)

class NewsView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk):
        news = News.objects.get(id=pk)
        new = NewsSerializer(news)
        return Response(new.data)


#  and {benzin.price*quantity} payed
# pay/time/get/?client=2&st_time=2022-05-22 19:18:45&end_time=2022-05-22 21:42:23