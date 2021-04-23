from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):

    # if request.method == "POST":
    #     return HttpResponse(request.POST['item_text'])
    # 第一个参数是请求，第二个参数要呈现的模板的名称。 
    # Django将在应用程序目录中自动搜索名为templates的文件夹。 
    # 然后，它会根据模板的内容为您构建一个HttpResponse。
    return render(request,'home.html',{
        'new_item_text': request.POST.get("item_text","")
    })
    # return HttpResponse("<html><title>To-Do lists</title></html>")