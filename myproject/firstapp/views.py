from lib2to3.pgen2.pgen import DFAState
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')

    # return HttpResponse('<h2>hello first route</h2>')
# a function for for the path described in the urls


def vs(request):
    return render(request, 'vs.html')


# for the static respose, initial steps of learning
# def search(request):
#     return HttpResponse('<h2>search route</h2>')
