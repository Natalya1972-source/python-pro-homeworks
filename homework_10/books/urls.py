from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("catalog/", views.book_list, name="book_list"),
    path("books/add/", views.add_book, name="add_book"),
    path(
        "books/<int:book_id>/",
        views.book_detail,
        name="book_detail",
    ),
]