from django.shortcuts import render

# Create your views here.
def Inicio(request):
    return render(request,'modelo/index.html')

def Cuenta(request):
    return render(request, 'modelo/crearcuenta.html')