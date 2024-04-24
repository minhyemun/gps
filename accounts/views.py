from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash

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
           return redirect('accounts:index')
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
    #rslist = Post.objects.all()
    #return render(request, "accounts/list.html", {'rslist':rslist})
    return render(request,'accounts/list.html')

def view(request):
    return render(request, 'accounts/view.html')

def write(request):
    return render(request,'accounts/write.html')

def edit(request):
    return render(request,'accounts/edit.html')

# 분리배출 가이드
def guide(request):
    return render(request, 'accounts/guide.html')

# 우리동네 쓰레기 버리는 날
def trash(request):
    return render(request, 'accounts/trash.html')

# 마이페이지
def mypage(request):
    return render(request, 'accounts/mypage.html')