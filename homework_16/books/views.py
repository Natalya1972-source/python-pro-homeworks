import logging

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
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


logger = logging.getLogger(__name__)


def home(request):
    logger.info(
        "Користувач відкрив головну сторінку"
    )

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
        logger.info(
            "Користувач відкрив каталог книг"
        )

        books = (
            Book.objects
            .select_related("category")
            .all()
        )

        category_slug = self.request.GET.get(
            "category"
        )

        query = self.request.GET.get(
            "q"
        )

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

    def get_context_data(
        self,
        **kwargs,
    ):
        context = super().get_context_data(
            **kwargs
        )

        context["categories"] = (
            Category.objects.all()
        )

        context["query"] = (
            self.request.GET.get(
                "q",
                "",
            )
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
        return (
            Book.objects
            .select_related("category")
        )


class BookCreateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    CreateView,
):
    model = Book
    form_class = BookForm
    template_name = "books/add_book.html"

    success_url = reverse_lazy(
        "books:book_list"
    )

    permission_required = (
        "books.add_book"
    )

    raise_exception = True

    def form_valid(self, form):
        logger.info(
            "Користувач %s додав книгу: %s",
            self.request.user.username,
            form.instance.title,
        )

        return super().form_valid(form)


class BookUpdateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UpdateView,
):
    model = Book
    form_class = BookForm
    template_name = "books/edit_book.html"

    success_url = reverse_lazy(
        "books:book_list"
    )

    permission_required = (
        "books.change_book"
    )

    raise_exception = True

    def form_valid(self, form):
        logger.info(
            "Користувач %s відредагував книгу: %s",
            self.request.user.username,
            form.instance.title,
        )

        return super().form_valid(form)


class BookDeleteView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DeleteView,
):
    model = Book

    template_name = (
        "books/book_confirm_delete.html"
    )

    success_url = reverse_lazy(
        "books:book_list"
    )

    permission_required = (
        "books.delete_book"
    )

    raise_exception = True

    def form_valid(self, form):
        logger.info(
            "Користувач %s видалив книгу: %s",
            self.request.user.username,
            self.object.title,
        )

        return super().form_valid(form)


class BookStatsView(
    LoginRequiredMixin,
    View,
):
    def get(
        self,
        request,
    ):
        logger.info(
            "Користувач %s відкрив статистику",
            request.user.username,
        )

        total_books = (
            Book.objects.count()
        )

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
                "total_books": (
                    total_books
                ),
                "total_categories": (
                    total_categories
                ),
                "total_stock": (
                    total_stock
                ),
                "out_of_stock": (
                    out_of_stock
                ),
            },
        )