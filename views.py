from django.shortcuts import render
from django.http import HttpResponse
from .models import categories


def category(request):

    categ = categories.objects.all()

    return render(request,'index.html',{'categ' : categ})

