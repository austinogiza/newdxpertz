from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def programmes(request):
    return render(request, 'programmes.html')


def ielts(request):
    return render(request, 'ielts.html')


def php(request):
    return render(request, 'php.html')


def mcse(request):
    return render(request, 'mcse.html')


def oracle(request):
    return render(request, 'oracle.html')


def autocad(request):
    return render(request, 'autocad.html')


def webdesign(request):
    return render(request, 'webdesign.html')


def python(request):
    return render(request, 'python.html')


def java(request):
    return render(request, 'java.html')


def pmp(request):
    return render(request, 'pmp.html')


def ccna(request):
    return render(request, 'ccna.html')


def sql(request):
    return render(request, 'sql.html')


def primavera(request):
    return render(request, 'primavera.html')


def microsoft(request):
    return render(request, 'microsoft.html')
