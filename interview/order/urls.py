from django.urls import path
from interview.order.views import (OrderListCreateView,
                                   OrderRetrieveUpdateDeactivateView,
                                   OrderTagListCreateView)

urlpatterns = [
    path("tags/", OrderTagListCreateView.as_view(), name="order-detail"),
    path(
        "<int:id>/",
        OrderRetrieveUpdateDeactivateView.as_view(),
        name="order-deactivate",
    ),
    path("", OrderListCreateView.as_view(), name="order-list"),
]
