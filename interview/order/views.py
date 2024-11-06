from django.shortcuts import render
from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class OrderRetrieveUpdateDeactivateView(APIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        order = self.get_queryset(id=kwargs["id"])
        serializer = self.serializer_class(order)

        return Response(serializer.data, status=200)

    def delete(self, request: Request, *args, **kwargs) -> Response:
        """Use DELETE to deactivate an order."""
        order = self.get_queryset(id=kwargs["id"])
        order.is_active = False
        order.save()
        return Response(status=204)

    def get_queryset(self, **kwargs):
        return self.queryset.get(**kwargs)
