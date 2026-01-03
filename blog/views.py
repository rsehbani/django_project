from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
import datetime
from django.utils import timezone


from .models import Post
from .forms import PostForm

def count_visit(request):
    visit = request.session.get('visit',0) + 1
    request.session['visit'] = visit
    return HttpResponse(f"Visit count:{request.session['visit']}")


def about(request):
    return render(request, 'blog/about.html')

def home(request):
   
    #expires_date = timezone.now() + datetime.timedelta(days=0, seconds=60)
    
    posts = Post.objects.all()
    context = {'posts': posts}#,'expires_date': expires_date}
    return render(request, 'blog/home.html', context)
    





@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {'post': post}

    if request.method == 'GET':
        return render(request, 'blog/post_confirm_delete.html', context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('posts')


@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'GET':
        context = {'form': PostForm(instance=post), 'id': id}
        return render(request, 'blog/post_form.html', context)

    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'The post has been updated successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/post_form.html', {'form': form})


@login_required
def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'blog/post_form.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'The post has been created successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/post_form.html', {'form': form})


def set_language(request):
    # Set the user's preferred language in the session
    request.session['preferred_language'] = 'English'
    return HttpResponse("Language preference saved!")

def get_language(request):
    # Retrieve the user's preferred language from the session
    language = request.session.get('preferred_language')
    return HttpResponse(f"Preferred language is {language}")

def delete_language_preference(request):
    try:
        del request.session['preferred_language']
        return HttpResponse("Language preference deleted!")
    except KeyError:
        return HttpResponse("No language preference found.")
    
def logout_user(request):
    request.session.flush()  # Deletes all session data
    return HttpResponse("You have been logged out.")


def set_cookie_view(request):
    response = HttpResponse("Cookie Set")
    # Set a cookie named 'my_cookie' with a value 'cookie_value'
    response.set_cookie('my_cookie', 'cookie_value', max_age=300)  # max_age sets expiry in seconds (e.g., 1 hour)
    return response

def get_cookie_view(request):
    my_cookie_value = request.COOKIES.get('my_cookie', 'Cookie not found')  # Default value if cookie is not present
    return HttpResponse(f"Cookie value: {my_cookie_value}")

def delete_cookie_view(request):
    response = HttpResponse("Cookie Deleted")
    response.delete_cookie('my_cookie')
    return response

def accept_cookies(request):
    response = HttpResponse("Cookie consent accepted  <a href= '../' >Accept</a>")
    response.set_cookie('cookie_consent', 'accepted', max_age=31536000)  # 1 year
    return response  #redirect('posts')  # Redirect back to the homepage or another page

def get_cookie_view(request):
    # Access the 'name' cookie
    name = request.COOKIES.get('name') 
    
    if name:
        return HttpResponse(f"Welcome back, {name}!")
    else:
        return HttpResponse("Hello, new user!")


from django.shortcuts import render
from django.http import HttpResponse

def set_cookie(request):
    return render(request, 'set_cookie.html')

def process_cookie(request):
    if request.method == 'POST':
        cookie_value = request.POST.get('cookie_value')
        response = HttpResponse("Cookie has been set.")
        response.set_cookie('my_cookie', cookie_value)
        return response
    else:
        return HttpResponse("Invalid request")

def get_cookie(request):
    cookie_value = request.COOKIES.get('my_cookie')
    return render(request, 'get_cookie.html', {'cookie_value': cookie_value})