from django.shortcuts import render

# Create your views here.
def index(request):
    autor="Tobsad"
    context={'autor':autor}
    return render(request, 'index.html',context)

def contacto(request):
    autor="Tobsad"
    context={'autor':autor}
    return render(request, 'contacto.html',context)
def nosotros(request):
    autor="Tobsad"
    context={'autor':autor}
    return render(request, 'nosotros.html',context)
def asesoria(request):
    autor="Tobsad"
    context={'autor':autor}
    return render(request, 'asesoria.html',context)
def marketing(request):
    autor="Tobsad"
    context={'autor':autor}
    return render(request, 'marketing.html',context)