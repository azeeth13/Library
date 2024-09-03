from django.shortcuts import render,get_object_or_404
from .models import Book,Category
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from .forms import RegistrationForm
from django.core.paginator import Paginator
from django.views.generic import *
from django.contrib.auth import login, logout, authenticate
import re
import time 
# def contact(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return redirect('registration_success')  # Redirect to a success page
#     else:
#         form = RegistrationForm()
#     return render(request, 'contact.html', {'form': form})


# def registration_success(request):
#     return render(request, 'registration_success.html')

# accounts/views.pyy
from .forms import SignUpForm




def HomePage(request):
    categories=Category.objects.all()
    return render(request, 'index.html',{'categories':categories})

def AboutPage(request):
    return render(request,'about.html')




def BookPage(request):
    kitoblar=Book.objects.all()
    paginator=Paginator(kitoblar,6)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)
    return render(request,'book.html',{'page_obj':page_obj})


# def Register(RegistrationForm):
    
def SearchPage(request):
    if request.method == "POST":
        text = request.POST.get("search")
        results = Book.objects.filter(name__icontains=text)
        print(results)

       
        return render(
            request,
            "search.html",
            {
                "results": results if results.exists() else False,
            },
        )
    else:
        return redirect("home")



def BookInfoPage(request, slug):
    book = Book.objects.filter(slug=slug)
    return render(request, "book-info.html", {"book": book if book.exists() else False})

def ContactPage(request):
    return render(request,'contact.html')

def LogoutPage(request):
    logout(request)
    return redirect("home")


def category_books(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = category.books.all()  # Retrieve all books in this category
    return render(request, 'category_books.html', {'category': category, 'books': books})

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_detail.html', {'book': book})