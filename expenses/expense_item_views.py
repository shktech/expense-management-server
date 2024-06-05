# expense_item_views.py
import logging
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import ExpenseItem, ExpenseReport
from .serializers import ExpenseItemSerializer

logger = logging.getLogger(__name__)

class ExpenseItemListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        report_id = self.kwargs['report_id']
        return ExpenseItem.objects.filter(report_id=report_id, report__user=self.request.user)

    def perform_create(self, serializer):
        report_id = self.kwargs['report_id']
        logger.debug(f'Creating ExpenseItem for report_id: {report_id} and user: {self.request.user}')
        try:
            report = ExpenseReport.objects.get(id=report_id, user=self.request.user)
            serializer.save(report=report)
        except ExpenseReport.DoesNotExist:
            logger.error(f'ExpenseReport with id {report_id} does not exist for user {self.request.user}')
            raise

class ExpenseItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        report_id = self.kwargs['report_id']
        return ExpenseItem.objects.filter(report_id=report_id, report__user=self.request.user)
