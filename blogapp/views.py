from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator
from .models import Blog
from django.utils import timezone
from .form import BlogPost


# Create your views here.

def home(request):
    blogs = Blog.objects
    #블로그 모든 글들을 대상으로
    blog_list=Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,3)
    #request된 페이지가 뭔지를 알아내고 ( request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)
    return render(request,'home.html',{'blogs':blogs,'posts':posts})
    
    #blogs = Blog.objects 
    #blog_list = Blog.objects.all()
    ##블로그 모든 글들을 다 가져와라
    #paginator = Paginator(blog_list,3)
    ##블로그 객체 세 개를 한 페이지로 자르기
    #page = request.GET.get('page')
    ##request된 페이지가 뭔지를 알아내고, request 페이지를 변수에 담는다
    #posts = Paginator.get_page(page)
    ##request된 페이지를 얻어온 뒤 return한다
    ##html에 띄우기 위해서는 사전형 객체로 만든다
    #return render(request, "home.html", {"blogs" : blogs}, {"posts" : posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, "detail.html", {"blog_detail" : blog_detail})

#def newone(request):
#    return render(request, "newone.html")

def submit(request): #데이터베이스에 내용을 입력해주는 함수
    new = Blog()
    new.title= request.GET['title']
    new.body = request.GET['body']
    new.date = request.GET['day']
    new.who = request.GET['who']
    new.save()
    return redirect("/blog/"+str(new.id))

def contributor(request):
    whos = Blog.objects
    return render(request, "contributor.html", {"whos" : whos})

def blogpost(request):
    #1.입력된 내용을 처리하는 기능 -> POST
    #2. 빈 페이지를 띄워주는 기능 -> GET
    if request.method == "POST":
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.now()
            post.save()
            return redirect('home')
    else :
        form = BlogPost()
        return render(request, "newone.html", {'form' : form})

    

