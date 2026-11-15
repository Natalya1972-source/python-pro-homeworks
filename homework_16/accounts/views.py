from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm


def register(request):

    if request.user.is_authenticated:
        return redirect("books:home")

    if request.method == "POST":
        form = CustomUserCreationForm(
            request.POST
        )

        if form.is_valid():
            user = form.save()

            # Одразу авторизуємо нового користувача
            login(
                request,
                user,
            )

            return redirect(
                "books:home"
            )

    else:
        form = CustomUserCreationForm()

    return render(
        request,
        "registration/register.html",
        {
            "form": form,
        },
    )