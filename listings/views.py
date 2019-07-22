from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing


# Create your views here.

def index(request):
    listings = Listing.objects.all()

    paginator = Paginator(listings, 6)
    page = request.Get.get('page')
    paged_listing = paginator.get_page(page)

    context = {
        'listings': paged_listing
    }
    return render(request, 'listings/listings.html', context)


def listing(request):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'search/search.html')
