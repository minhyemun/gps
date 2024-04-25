from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash

# 강서소식
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def index(request):
    return render(request, 'accounts/index.html')

def login(request):
    if request.method == "POST":
        #pass
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            #contrib.auth 패키지의 login 함수를 사용하는데
            #현재 함수와 이름이 중복이므로 별명을 지어서 사용
            #login(request, form.get_user())

           auth_login(request, form.get_user())
           return redirect('accounts:home')
    else:
        form = AuthenticationForm()
    context={
        "form":form
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("accounts:login")


def signup(request):
    # 이미 로그인한 경우, 회원가입 로직 실행 막기
    if request.user.is_authenticated:
        return redirect("accounts:index")
    
    if request.method == "POST":
        #pass
        #form = UserCreationForm(request.POST)
        
        # 새로 생성한 customusercreationform을 활용하여 회원가입 #
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        #form = UserCreationForm()
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)


def delete(request):
    request.user.delete()
    return redirect('accounts:login')


def update(request):
    # 로그인 하지 않은 경우, 정보 수정 로직 수행 제한
    if not request.user.is_authenticated:
        return redirect("accounts:index")
    if request.method == "POST":
        #pass
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context={
        'form':form
    }
    return render(request, "accounts/update.html", context)


def change_password(request, user_id):
    if request.method == "POST":
        #pass
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form
    }
    return render(request, 'accounts/change_password.html', context)

# 로그인 하지 않은 경우, 정보수정 로직 수행 제한
#@login_required
#def update(request):
#    if request.method=="POST":

# 강서 소식
def list(request):
    account_list = Post.objects.all()
    context = {
        'account_list':account_list
    }
    return render(request, "accounts/list.html", context)
    #return render(request,'accounts/list.html')

def detail(request, pk):
    accountt = Post.objects.get(pk=pk)
    context = {
        'accountt':accountt
    }
    return render(request, 'accounts/detail.html', context)

#def write(request):
#    return render(request,'accounts/write.html')
from .forms import PostForm
from .forms import PostForm2

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('accounts:detail', post.pk)
        else:
            print(form.errors)
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/write.html', context)

# def edit(request, pk):
#      accountt = PostForm2.objects.get(pk=pk)
#      context = {
#          'accountt':accountt
#      }
#      return render(request, 'accounts/edit.html', context)


# def create(request):
#     if request.method == 'POST':
#         form = Post(request.POST)
#         if form.is_valid():
#             accountt=form.save()
#             return redirect('accounts:detail', accountt.pk)
#     else: form = Post()
#     context={
#             'form':form
#         }
#     return render(request,'accounts/write.html',context)

def save(request):
    if request.method == "POST":
        new_post = Post.objects.create(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            writer=request.POST.get('writer'),
            # days 필드는 auto_now_add=True로 설정되어 있으므로 지정할 필요 없음
        )
        return redirect('accounts:detail', pk=new_post.pk)
    return render(request, 'accounts/save.html')  # POST가 아닐 때 어떤 행동을 할지 명시

def edit(request,pk):
    if request.method == 'POST':
        form = PostForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail',pk)
    else:
        form = PostForm2()
    context={
        'form':form
    }
    return render(request,'accounts/edit.html',context)

def delete(request, pk):
    data = request.POST
    delete_post = Post.objects.filter(pk=pk).delete()
    return redirect('accounts:list')

# 조회수 증가
from django.shortcuts import get_object_or_404

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.count += 1 
    post.save()
    return render(request, 'accounts/post_detail.html', {'post': post})


# 분리배출 가이드
def guide(request):
    return render(request, 'accounts/guide.html')

# 우리동네 쓰레기 버리는 날
def trash(request):
    return render(request, 'accounts/trash.html')

# 마이페이지
def mypage(request):
    return render(request, 'accounts/mypage.html')



from .models import Post
print(Post.objects.values('writer', 'days', 'count'))