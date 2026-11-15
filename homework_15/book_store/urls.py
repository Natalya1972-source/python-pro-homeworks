from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path


def custom_404(request, exception):
    return render(
        request,
        "errors/404.html",
        status=404,
    )


def custom_500(request):
    return render(
        request,
        "errors/500.html",
        status=500,
    )


urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),

    path(
        "",
        include("books.urls"),
    ),
]


handler404 = custom_404
handler500 = custom_500