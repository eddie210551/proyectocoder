from django.http import HttpResponse
def saludo(request):
    return HttpResponse("Hola Django - Coder")
def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :)")
