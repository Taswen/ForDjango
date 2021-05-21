from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item
# Create your views here.
def home_page(request):
    # if request.method == "POST":
    #     return HttpResponse(request.POST['item_text'])
    # 第一个参数是请求，第二个参数要呈现的模板的名称。 
    # Django将在应用程序目录中自动搜索名为templates的文件夹。 
    # 然后，它会根据模板的内容为您构建一个HttpResponse。
    # if request.method == 'POST':
    #     Item.objects.create(text=request.POST['item_text'])
    #     return redirect('/lists/the-only-list-in-the-world/')
    return render(request,'home.html')
    # return HttpResponse("<html><title>To-Do lists</title></html>")


def view_list(request):
    items = Item.objects.all()
    return render(request,'list.html',{'items':items})


def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')

