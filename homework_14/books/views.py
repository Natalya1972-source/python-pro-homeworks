from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import BookForm
from .models import Book, Category


def home(request):
    categories = Category.objects.all()

    books = (
        Book.objects
        .select_related("category")
        .order_by("-id")[:6]
    )

    return render(
        request,
        "books/home.html",
        {
            "categories": categories,
            "books": books,
        },
    )


class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"
    paginate_by = 6

    def get_queryset(self):
        books = Book.objects.select_related("category").all()

        category_slug = self.request.GET.get("category")
        query = self.request.GET.get("q")

        if category_slug:
            books = books.filter(
                category__slug=category_slug
            )

        if query:
            query = query.strip()

            if query:
                books = books.filter(
                    Q(title__icontains=query)
                    | Q(author__icontains=query)
                    | Q(description__icontains=query)
                )

        return books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categories"] = Category.objects.all()

        context["query"] = self.request.GET.get(
            "q",
            "",
        )

        context["selected_category"] = (
            self.request.GET.get(
                "category",
                "",
            )
        )

        return context


class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"

    def get_queryset(self):
        return Book.objects.select_related("category")


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = "books/add_book.html"

    success_url = reverse_lazy(
        "books:book_list"
    )

    login_url = "/admin/login/"


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = "books/edit_book.html"

    success_url = reverse_lazy(
        "books:book_list"
    )

    login_url = "/admin/login/"


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "books/book_confirm_delete.html"

    success_url = reverse_lazy(
        "books:book_list"
    )

    login_url = "/admin/login/"


class BookStatsView(LoginRequiredMixin, View):
    login_url = "/admin/login/"

    def get(self, request):
        total_books = Book.objects.count()

        total_categories = (
            Category.objects.count()
        )

        total_stock = (
            Book.objects.aggregate(
                total=Sum("stock")
            )["total"]
            or 0
        )

        out_of_stock = (
            Book.objects.filter(
                stock=0
            ).count()
        )

        return render(
            request,
            "books/stats.html",
            {
                "total_books": total_books,
                "total_categories": total_categories,
                "total_stock": total_stock,
                "out_of_stock": out_of_stock,
            },
        )