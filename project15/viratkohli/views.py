from django.shortcuts import render

# Create your views here.
def view1(request):
    return render(request,'viratkohli/view1.html')

def view2(request):
    return render(request,'viratkohli/view2.html')