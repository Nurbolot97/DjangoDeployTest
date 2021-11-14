from django.shortcuts import render, redirect
from .forms import PageForm



def main(request):
    if request.method == "POST":
        form = PageForm(request.POST)
        form.save()
        return redirect('result')
    else:
        form = PageForm()
    return render(request, 'main.html', locals())


def result(request):
    return render(request, 'result.html', locals())


















