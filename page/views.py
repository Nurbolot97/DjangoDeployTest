from django.shortcuts import render, redirect
from .forms import PageForm



def main(request):
    if request.method == "POST":
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('result')
    else:
        form = PageForm()
    return render(request, 'main.html', locals())


def result(request):
    return render(request, 'result.html', locals())


















