from django.shortcuts import redirect, render
from .models import Listings
from .form import ListingForm
# Create your views here.
def listing_list(request):
    listings=Listings.objects.all()
    context={
        "listings":listings
    }
    return render(request,"list.html",context=context)

def listing_retrieve(request,id):
    listing=Listings.objects.get(id=id)
    context={
        "listing":listing
    }
    return render(request,"retrieve.html",context=context)

def listing_create(request):
    if request.method== "POST":
        form=ListingForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            redirect("listing_list")
    form =ListingForm()
    context={"form":form}
    return render (request,"create.html",context)

def listing_update(request,id):
    listing=Listings.objects.get(id=id)
    form=ListingForm(instance=listing)
    if request.method== "POST":
        form=ListingForm(request.POST,instance=listing)
        if form.is_valid():
            form.save()
            redirect("listing_list")
    context={"form":form}
    return render (request,"update.html",context)

def listing_delete(request,id):
    listing=Listings.objects.get(id=id)
    listing.delete()
    return redirect ("listing_list")
    

