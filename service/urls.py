from django.urls import path

from .views import (
    SpareListCreateView,
    SpareDetailView,
    ServiceListCreateView,
    ServiceDetailView,
    OrderListCreateView,
    OrderDetailView,
    OrderItemCreateView,
    OrderItemDetailView,
    RepairRequestListCreateView,
    RepairRequestDetailView, order_status_graph,
)

urlpatterns = [
    path('spares/', SpareListCreateView.as_view(), name='spare-list-create'),
    path('spares/<int:pk>/', SpareDetailView.as_view(), name='spare-detail'),

    path('services/', ServiceListCreateView.as_view(), name='service-list-create'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),

    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),

    path('order-items/', OrderItemCreateView.as_view(), name='orderitem-create'),
    path('order-items/<int:pk>/', OrderItemDetailView.as_view(), name='orderitem-detail'),

    path('repair-requests/', RepairRequestListCreateView.as_view(), name='repair-request-list'),
    path('repair-requests/<int:pk>/', RepairRequestDetailView.as_view(), name='repair-request-detail'),

    path('order_status_graph/', order_status_graph, name='order_status_graph'),

    # path('admin/order-status-graph/', admin_site.admin_view(admin_site.order_status_graph), name='order_status_graph'),
]
