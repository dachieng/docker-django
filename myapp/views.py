from django.shortcuts import redirect, render
from .forms import PostForm


def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PostForm()
    return render(request, "myapp/index.html", {"form": form})
