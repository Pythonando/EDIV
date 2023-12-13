from django.shortcuts import render
from services.models import Budgets
from rolepermissions.decorators import has_role_decorator, has_permission_decorator

@has_role_decorator('editor')
def list_budgets(request):
    budgets = Budgets.objects.all()
    return render(request, 'list_budget.html', {'budgets': budgets})
