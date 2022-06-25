import imp
from django.shortcuts import redirect, render
from django.db.models import Q
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm
# Create your views here.


def accueil(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    contacts = Contact.objects.filter(
        Q(nom__icontains=q) |
        Q(prenom__icontains=q)|
        Q(numero__icontains=q)
    )
    contact_count = contacts.count()
    context = {'contacts': contacts, 'contact_count':contact_count}
    return render(request, "Application/listes.html", context) 


def contact(request, pk):
    contact = Contact.objects.get(id=pk)
    context = {'contact':contact}   
    return render(request, 'Application/contacts.html', context)

def creer(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil')
    context = {'form':form}
    return render(request, 'Application/creer.html', context)

def modifier(request, pk):
    contact = Contact.objects.get(id=pk)
    form = ContactForm(instance=contact)
    if request.method=='POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('accueil')
    context = {'form':form}
    return render(request, 'Application/creer.html', context)

def supprimer(request,pk):
    contact = Contact.objects.get(id=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('accueil')
    return render(request, 'Application/supprimer.html')
