from django.shortcuts import render

# Create your views here.
def htmlfile(request):
   # return render(request,'hai.html')
   return render(request,'app/ten.html')#sepecific templates
def hero(request):
    return render(request,'hai.html') #generic templates