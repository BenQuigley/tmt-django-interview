from datetime import datetime

from django.shortcuts import render
from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer
from rest_framework import generics
from rest_framework.response import Response


# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self, **kwargs):
        # Example requests:
        # - /orders/?embargoRangeStart=2020-12-01&embargoRangeStop=2024-12-25
        # - /orders/?embargoRangeStart=2025-12-01
        embargo_range_start_str = self.request.GET.get("embargoRangeStart")
        if embargo_range_start_str:
            try:
                kwargs["embargo_date__gte"] = datetime.strptime(
                    embargo_range_start_str, "%Y-%m-%d"
                ).date()
            except Exception:
                return Response(
                    "Invalid embargo start date parameter received.", status=400
                )
        embargo_range_stop_str = self.request.GET.get("embargoRangeStop")
        if embargo_range_stop_str:  # TODO Deduplicate me
            try:
                kwargs["embargo_date__lt"] = datetime.strptime(
                    embargo_range_stop_str, "%Y-%m-%d"
                ).date()
            except Exception:
                return Response(
                    "Invalid embargo stop date parameter received.", status=400
                )
        return self.queryset.filter(**kwargs)


class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer
