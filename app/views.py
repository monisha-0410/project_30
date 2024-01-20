from django.shortcuts import render

# Create your views here.
def filters(request):
    d={'data':'Django is a python based Framework','c':1,'y':6}
    return render(request,'filters.html',d)

