from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinValueValidator


class Transaction(models.Model):

    class TransactionType(models.TextChoices):
        INCOME = 'INCOME', 'Income'
        EXPENSE = 'EXPENSE', 'Expense'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='transactions'
    )

    title = models.CharField(max_length=100)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    transaction_type = models.CharField(
        max_length=10,
        choices=TransactionType.choices
    )

    date = models.DateField(default=timezone.localdate)

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.title} - {self.transaction_type} - ₱{self.amount}"