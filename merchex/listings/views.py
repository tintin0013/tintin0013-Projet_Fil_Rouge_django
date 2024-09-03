from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html',{'bands': bands})
    

def about(request):
    #return HttpResponse('<h1>À propos</h1> <p>Nous adorons Le soleil</p>')
    return render(request,
                  'listings/about.html')

def contact(request):
    #return HttpResponse('<h1>Pour nous contacter:</h1><p>Cliquez ICI</p>')
    return render(request,
                  'listings/contact.html')

def listings(request):
    listings = Listing.objects.all()
   # return HttpResponse('<h1>Voici la liste des Produits Disponibles</h1><p>choisir un produit</p>')
    return render(request,
                  'listings/listings.html',
                  context={'listings': listings})
