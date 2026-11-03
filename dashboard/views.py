from django.shortcuts import render


def home(request):

    context = {
        'page_title': "Christer's Financial Dashboard",
        'total_income': 15000,
        'total_expenses': 6500,
        'balance': 8500,
    }

    return render(request, 'dashboard/home.html', context)

def about(request):

    context = {
        'page_title': 'About Personal Expense Tracker'
    }
    
    return render(request, 'dashboard/about.html', context)