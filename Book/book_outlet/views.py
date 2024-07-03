from django.http import Http404
from django.shortcuts import render,get_object_or_404
from . models import Booklist
from django.db.models import Avg,Max,Min

# Create your views here.
def index(request):
    data=Booklist.objects.all().order_by('-rating')
    num_books=data.count()
    avg_rating=data.aggregate(Avg("rating"),Max("rating"),Min("rating"))
    return render(request,'index.html',{
        'books':data,
        'total_number_of_books':num_books,
        'average_rating':avg_rating
    })


def book_details(request,slug): 
    book=get_object_or_404(Booklist,slug=slug)
    return render(request,'book_detail.html',{
          'book':book
    })