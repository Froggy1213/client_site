from django.shortcuts import render
from .models import Book

def index(request):
    # Получаем книги (например, последние 3 для отображения на главной или все)
    books = Book.objects.filter(is_visible=True)
    return render(request, 'portfolio/index.html', {'books': books})

def books(request):
    # Отдельная страница для всех книг (если понадобится)
    books_list = Book.objects.filter(is_visible=True)
    return render(request, 'portfolio/books.html', {'books': books_list})