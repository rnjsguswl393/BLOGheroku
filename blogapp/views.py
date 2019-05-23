from django.shortcuts import render,get_object_or_404, redirect
from .models import Blog #붕어빵틀을 참고한다고 해줌
from django.core.paginator import Paginator
from django.utils import timezone

# Create your views here.
def home(request): 
    blogs=Blog.objects.all().order_by('-id') #식빵 #붕어빵틀안에 붕어빵들을 넣어라 뒤에 .all부터는 붕어빵의 순서를 배치
    blog_list = Blog.objects.all().order_by('-id')
    #블로그의 모든글을 대상으로 blog_list에 넣어준후 
    paginator = Paginator(blog_list, 3)
    #블로그 객체 들을 3개씩 한페이지로 자르고 
    page =request.GET.get('page')
    #요청된 페이지가 뭔지 알아내고 그걸 변수에 담는다
    posts=paginator.get_page(page)  #식빵조각들 
    #요청된 페이지를 얻은뒤 출력
    return render(request,'home.html',{'blogs':blogs,'posts':posts})#blogs를 home.html에서 불렀을때 blogs 안에있는 내용(위에꺼)를 풀어라
def detail(request, blog_id): 
    details=get_object_or_404(Blog, pk=blog_id) #pk(프라이머리키)는 고유값을 가져야함
    return render(request,'detail.html',{'details':details})
def new(request):
    return render(request, 'new.html')
def create(request): 
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_data=timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))