from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from .forms import ContactForm
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template, render_to_string
from .models import Contact, Courses


class CourseDetailsViews(DetailView):
    model = Courses
    template_name = "detail.html"


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):

    form = ContactForm(request.POST or None)
    template = 'contact.html'

    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        phone = form.cleaned_data.get('phone')
        emailTo = [settings.EMAIL_HOST_USER]
        content = {
            'name': name,
            'email': email,
            'phone': phone,
            'message': message
        }

        contact = Contact(
            name=name,
            phone=phone,
            email=email,
            message=message
        )
        contact.save()
        content = template = render_to_string('contact_template.html', content)

        send_mail(
            'New email from contant form',
            content,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],

        )
        return redirect('../success/')
    return render(request, 'contact.html', {'form': form})


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


def success(request):
    return render(request, 'success.html')


def ieltsexam(request):
    return render(request, 'ielts-exam.html')
