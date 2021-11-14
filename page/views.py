from django.shortcuts import render, redirect
from .forms import PageForm



def main(request):
    if request.method == "POST":
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('result')
    else:
        form = PageForm()
    return render(request, 'main.html', locals())


def result(request):
    return render(request, 'result.html', locals())


















