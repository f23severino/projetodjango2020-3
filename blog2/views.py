from django.shortcuts import render

def forumavisos(request):
    return render(request, 'blog2/forumavisos.html', {})
