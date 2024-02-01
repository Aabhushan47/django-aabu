from django.shortcuts import redirect


# to check if user is logged in or not
def unauthenticated_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/")
        else:
            return view_function(request, *args, *kwargs)

    return wrapper_function


# access to admin if admin logs in else access to user
def admin_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff:
            return view_function(request, *args, **kwargs)
        else:
            return redirect("/")

    return wrapper_function
