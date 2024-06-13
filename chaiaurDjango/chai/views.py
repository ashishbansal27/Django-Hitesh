from django.shortcuts import render
from .models import ChaiVariety, Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarityForm
# Create your views here.
def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'chais':chais})

def chai_details(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'chai/chai_details.html', {'chai':chai})

def chai_stores(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varities = chai_variety)
    else:
        form = ChaiVarityForm()


    return render(request, 'chai/chai_stores.html', {'stores': stores, 'form':form})
