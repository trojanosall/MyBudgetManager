from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Costs
from .forms import CostForm


def costs_list(request):
    costs = Costs.objects.all()
    return render(request, 'costApp/costs_list.html', {'costs': costs})


def cost_detail(request, pk):
    cost = get_object_or_404(Costs, pk=pk)
    return render(request, 'costApp/cost_detail.html', {'cost': cost})


def cost_new(request):
    if request.method == "POST":
        form = CostForm(request.POST)
        if form.is_valid():
            cost = form.save(commit=False)
            cost.save()
            return redirect('cost_detail', pk=cost.pk)
    else:
        form = IncomeForm()
    return render(request, 'incomeApp/income_edit.html', {'form': form})


def cost_edit(request, pk):
    cost = get_object_or_404(Costs, pk=pk)
    if request.method == "POST":
        form = CostForm(request.POST, instance=cost)
        if form.is_valid():
            cost = form.save(commit=False)
            cost.save()
            return redirect('cost_detail', pk=cost.pk)
    else:
        form = CostForm(instance=cost)
    return render(request, 'costApp/cost_edit.html', {'form': form})
