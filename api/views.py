from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Orders
from .serializers import OrdersSerializer

class OrdersPagination(PageNumberPagination):
    page_size = 30  # Fixed number of orders per page
    max_page_size = 30  # Ensure the page size doesn't exceed this value

class OrdersListView(ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    pagination_class = OrdersPagination
    # permission_classes = [IsAuthenticated]  # Require authentication
    permission_classes = [AllowAny]  # Require authentication

    # Add filtering and ordering backends
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['part_number', 'client', 'status']  # Fields for exact match filtering
    ordering_fields = ['date_created', 'status']  # Allow ordering by date_created or status

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter by date range if both start_date and end_date are provided
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if start_date and end_date:
            queryset = queryset.filter(date_created__range=[start_date, end_date])
        return queryset

class OrdersCreateView(CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [IsAuthenticated]  # Require authentication

    def perform_create(self, serializer):
        # Ensure the logged-in user is associated with the order
        serializer.save(client=self.request.user)
