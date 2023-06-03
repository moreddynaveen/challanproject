from django.shortcuts import render
from app1.models import Challan
def index(request):
    return render(request,'app1/index.html')
def PasView(request):
    pas_list=Challan.objects.all()
    my_dict={'pas_list':pas_list}
    return render(request,'app1/pas.html',context=my_dict)
# Create your views here.
