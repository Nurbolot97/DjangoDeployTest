from django.shortcuts import render, redirect
from .forms import PageForm
from .models import Data



def main(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            datas = form.cleaned_data['login']
            existing_login = Data.objects.filter(login=datas).count()   
            if existing_login == 0:
                form.save()
                return redirect('result')
            else:
                form = PageForm()
    return render(request, 'main.html', locals())


def result(request):
    return render(request, 'result.html', locals())


















