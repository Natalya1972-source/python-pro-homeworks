from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookForm
from .models import Book, Category


def home(request):
    categories = Category.objects.all()
    books = Book.objects.select_related("category").order_by("-id")[:6]

    return render(
        request,
        "books/home.html",
        {
            "categories": categories,
            "books": books,
        },
    )


def book_list(request):
    books = Book.objects.select_related("category").all()
    categories = Category.objects.all()

    category_slug = request.GET.get("category")
    query = request.GET.get("q")

    if category_slug:
        books = books.filter(category__slug=category_slug)

    if query:
        books = books.filter(
            Q(title__icontains=query)
            | Q(author__icontains=query)
            | Q(description__icontains=query)
        )

    return render(
        request,
        "books/book_list.html",
        {
            "books": books,
            "categories": categories,
            "query": query,
        },
    )


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    return render(
        request,
        "books/book_detail.html",
        {"book": book},
    )


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()

    return render(
        request,
        "books/add_book.html",
        {"form": form},
    )
