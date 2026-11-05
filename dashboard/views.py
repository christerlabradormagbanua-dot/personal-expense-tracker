from django.shortcuts import render
from django.db.models import Sum
from transactions.models import Transaction

def home(request):
    transactions = Transaction.objects.none()

    if request.user.is_authenticated:
        transactions = Transaction.objects.filter(user=request.user)

    income = transactions.filter(
        transaction_type='INCOME'
    ).aggregate(total=Sum('amount'))['total'] or 0

    expenses = transactions.filter(
        transaction_type='EXPENSE'
    ).aggregate(total=Sum('amount'))['total'] or 0

    balance = income - expenses

    context = {
        'page_title': "Christer's Financial Dashboard",
        'total_income': income,
        'total_expenses': expenses,
        'balance': balance,
    }

    return render(request, 'dashboard/home.html', context)

def about(request):

    context = {
        'page_title': 'About Personal Expense Tracker'
    }
    
    return render(request, 'dashboard/about.html', context)