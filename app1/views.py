from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    all_post=PostModel.objects.all().order_by('id')
    paginator = Paginator(all_post, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj,"********************************")
    return render(request, 'home.html',{'page_obj':page_obj})