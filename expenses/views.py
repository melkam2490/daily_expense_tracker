
# Import tools to display pages and redirect users
from django.shortcuts import render, redirect, get_object_or_404

# Import Django's form for creating user accounts
from django.contrib.auth.forms import UserCreationForm

# Import our Expense model
from .models import Expense

# Import tools for accepting submitted forms
from django.views.decorators.http import require_POST, require_http_methods

# Import tool to require login
from django.contrib.auth.decorators import login_required

# Import today's date
from datetime import date


# Save a new expense to the database
@require_POST
def add_expense(request):
    # Make sure the user is logged in
    if not request.user.is_authenticated:
        return redirect('login')

    # Get information from the submitted form
    title = request.POST.get('title', '').strip()
    amount = request.POST.get('amount', '')
    category = request.POST.get('category', '')
    expense_date = request.POST.get('date', '')

    # Save the expense if all fields are provided
    if title and amount and category and expense_date:
        Expense.objects.create(
            user=request.user,
            title=title,
            amount=amount,
            category=category,
            date=expense_date,
        )

    # Return to the home page
    return redirect('home')


# Display the home page
def home(request):
    expenses = []
    total = 0
    monthly_total = 0
    monthly_count = 0

    # Get expenses belonging to the logged-in user
    if request.user.is_authenticated:
        expenses = Expense.objects.filter(user=request.user)

        # Calculate all expenses
        total = sum(expense.amount for expense in expenses)

        # Get this month and year
        today = date.today()

        # Find expenses from this month
        monthly_expenses = expenses.filter(
            date__year=today.year,
            date__month=today.month
        )

        # Calculate this month's total and count
        monthly_total = sum(
            expense.amount for expense in monthly_expenses
        )
        monthly_count = monthly_expenses.count()

    # Send information to the home page
    return render(request, 'expenses/home.html', {
        'expenses': expenses,
        'total': total,
        'monthly_total': monthly_total,
        'monthly_count': monthly_count,
    })


# Create a new user account
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {
        'form': form
    })


# Delete an expense
@login_required
@require_POST
def delete_expense(request, expense_id):
    # Find an expense belonging to this user
    expense = get_object_or_404(
        Expense,
        id=expense_id,
        user=request.user
    )

    expense.delete()
    return redirect('home')


# Edit an existing expense
@login_required
@require_http_methods(["GET", "POST"])
def edit_expense(request, expense_id):
    # Find an expense belonging to this user
    expense = get_object_or_404(
        Expense,
        id=expense_id,
        user=request.user
    )

    # Save changes when the form is submitted
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        amount = request.POST.get('amount', '')
        category = request.POST.get('category', '').strip()
        expense_date = request.POST.get('date', '')

        # Check that all fields have values
        if title and amount and category and expense_date:
            expense.title = title
            expense.amount = amount
            expense.category = category
            expense.date = expense_date
            expense.save()

            return redirect('home')

    # Display the edit page
    return render(request, 'expenses/edit_expense.html', {
        'expense': expense
    })
