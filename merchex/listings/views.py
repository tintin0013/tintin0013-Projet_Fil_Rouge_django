from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def contact(request):
    return HttpResponse('<h1>Pour nous contacter:</h1><p>Cliquez ICI</p>')
    # return render(request,
    #               'listings/contact.html')

def listings(request):
    # listings = Listing.objects.all()
    return HttpResponse('<h1>Voici la liste des Produits Disponibles</h1><p>choisir un produit</p>')
    # return render(request,
    #               'listings/listings.html',
    #               context={'listings': listings})
