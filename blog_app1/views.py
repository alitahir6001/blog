from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse


def root(request):
    return HttpResponse("This is the start of the blog!")

def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request, num):
    return HttpResponse(f"This is a placeholder to display the blog number: {num}")  # had to use an f-string to get it to display the number, otherwise it kept displaying {num} as a string.

def edit(request, num):
    return HttpResponse(f"placeholder to edit blog number {num}")

def destroy(request, num):
    return redirect('/blogs')

def json(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})  # I think i got this one right?  I emulated what I got from the examples in the tracks prior to the first assignment - it is returning the text of the code, as opposed to just the string itself.

# Create your views here.
