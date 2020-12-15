from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Incomes
from .forms import IncomeForm


# def base_view(request):
#     return render(request, 'incomeApp/income_base_view.html', {})
#     # return render(request, 'incomeApp/incomes_list.html', {})

def incomes_list(request):
    incomes = Incomes.objects.all()
    return render(request, 'incomeApp/incomes_list.html', {'incomes': incomes})


def income_detail(request, pk):
    income = get_object_or_404(Incomes, pk=pk)
    return render(request, 'incomeApp/income_detail.html', {'income': income})


def income_new(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.save()
            return redirect('income_detail', pk=income.pk)
    else:
        form = IncomeForm()
    return render(request, 'incomeApp/income_edit.html', {'form': form})


def income_edit(request, pk):
    income = get_object_or_404(Incomes, pk=pk)
    if request.method == "POST":
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            income = form.save(commit=False)
            income.save()
            return redirect('income_detail', pk=income.pk)
    else:
        form = IncomeForm(instance=income)
    return render(request, 'incomeApp/income_edit.html', {'form': form})


# def incomes(request):
#     form = IncomesFormFilter(request.GET)
#     incomes_list = Incomes.objects.allfilters(CreateFilters(form))

#     return render(request, 'incomeApp/incomes_list.html', {'incomes_list': incomes_list})


# def testresults(request):
#     form = IncomesFormFilter(request.GET)

#     resultlist = Incomes.objects.allfilters(CreateFilters(form))

#     page = request.GET.get('page', 1)

#     paginator = Paginator(resultlist, 25)
#     try:
#         myresults = paginator.page(page)
#     except PageNotAnInteger:
#         myresults = paginator.page(1)
#     except EmptyPage:
#         myresults = paginator.page(paginator.num_pages)

#     PassFailRatiodict = PassFailRatio(resultlist)
#     TestedProductsdict = TestedProducts(resultlist)
#     FailureCausesdict = FailureCauses(resultlist)
#     resultdict = TestResultsbyFWVersion(resultlist)

#     data = {
#         'resultlist': myresults,
#         'filters': CreateFilters(form),
#         'testresultsnumber': TotalTestResultCount(resultlist),
#         'averageduration': AverageDuration(resultlist),
#         'passedfailedratiodata': json.dumps(list(PassFailRatiodict.values())),
#         'passedfailedratiolabel': json.dumps(list(PassFailRatiodict.keys())),
#         'testedproductsdata': json.dumps(list(TestedProductsdict.values())),
#         'testedproductslabel': json.dumps(list(TestedProductsdict.keys())),
#         'failureclassesdata': json.dumps(list(FailureCausesdict.values())),
#         'failureclasseslabel': json.dumps(list(FailureCausesdict.keys())),
#         'resultsbytestedfirmwaresdata': json.dumps(list(TestResultsbyFWVersionData(resultdict))),
#         'resultsbytestedfirmwareslabel': json.dumps(list(TestResultsbyFWVersionLabel(resultdict)))
#     }
#     return render(request, 'DashboardApp/testresults.html', {'data': data})
