from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band


def hello(request):
    # return HttpResponse('<h1>Hello Django!</h1>')
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
""")
    

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
