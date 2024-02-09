from django.shortcuts import render
from webtestapp.form import EmployeeAdd, TestForm
from .models import Employee

def create(request):
    modelform_dict = {
        'title':'modelformテスト',
        'form': EmployeeAdd(),
    }
    return render(request, 'webtestapp/create.html', modelform_dict)

def info(request):
    infodata = Employee.objects.all()
    header = ['ID','名前','メール','性別','部署','社歴','作成日']
    my_dict2 = {
        'title': 'テスト',
        'employees': infodata,
        'header':header
    }
    return render(request, 'webtestapp/info.html',my_dict2)

def index(request):
    my_dict = {
        'insert_something':"views.pyのinsert_something部分です。",
        'name':'Bashi',
        'test_titles': ['title 1', 'title 2', 'title 3'],
        'form': TestForm(),
        'insert_forms': '初期値',
    }

    if (request.method == 'POST'):
        my_dict['insert_forms'] = '文字列:' + request.POST['text'] + '\n整数型:' + request.POST['num']
        my_dict['form'] = TestForm(request.POST)

    return render(request, 'webtestapp/index.html', my_dict)
