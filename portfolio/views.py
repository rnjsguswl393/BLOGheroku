from django.shortcuts import render
from .models import Portfolio

# Create your views here.
def portfolio(request):
    portfolios=Portfolio.objects
    return render(request,'portfolio.html',{'portfolios':portfolios}) 

def new(request):
    if request.method=='POST':
        form=Portfolio(request.POST)
        if form.is_valid():#폼에 다 입력되었는지 검사하는 함수
            post = form.save(commit=False) #아직 저장하지말아라
            post.pub_data=timezone.now() #폼에서 입력하지않은 시간을 등록해라
            form.save() #시간을 등록하였으면 저장을 하라
            return redirect('portfolio')
    else:
        form=Portfolio()
        return render(request,'new.html',{'form':form})