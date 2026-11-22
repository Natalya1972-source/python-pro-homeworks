from django.urls import include, path

from . import views


urlpatterns = [
    path(
        "register/",
        views.register,
        name="register",
    ),

    # Стандартні login/logout Django
    path(
        "",
        include(
            "django.contrib.auth.urls"
        ),
    ),
]