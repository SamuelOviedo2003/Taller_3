from django.shortcuts import render
from .models import Telenovelas

# Create your views here.
def telenovelas(request):
    telenovelass= Telenovelas.objects.all()
    return render(request,'telenovelas.html',{'telenovelass':telenovelass})


