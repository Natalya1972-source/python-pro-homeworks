from django.urls import path

from . import views


app_name = "books"


urlpatterns = [
    path(
        "",
        views.home,
        name="home",
    ),

    path(
        "catalog/",
        views.BookListView.as_view(),
        name="book_list",
    ),

    path(
        "books/add/",
        views.BookCreateView.as_view(),
        name="add_book",
    ),

    path(
        "books/<int:pk>/",
        views.BookDetailView.as_view(),
        name="book_detail",
    ),

    path(
        "books/<int:pk>/edit/",
        views.BookUpdateView.as_view(),
        name="book_edit",
    ),

    path(
        "books/<int:pk>/delete/",
        views.BookDeleteView.as_view(),
        name="book_delete",
    ),

    path(
        "stats/",
        views.BookStatsView.as_view(),
        name="book_stats",
    ),
]