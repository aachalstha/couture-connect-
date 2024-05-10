from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views import View
from django.db.models import Q
# from .forms import ProfileForm
from .models import ThreadModel, MessageModel


from .forms import OrderForm, CreateUserForm, ReviewForm, EditProfileForm, ThreadForm, MessageForm

def coutureconnect(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render({}, request))
# Create your views here.
@login_required(login_url='loginPage')
def home(request):
    print("Its working")
    # Get all users from the User model
    users = User.objects.all()
    # Create a context dictionary with the users
    context = {
      'users': users,
    }
    # Load the template
    template = loader.get_template('firstpage.html')
    # Render the template with the context
    return HttpResponse(template.render(context, request))

# @login_required(login_url='loginPage')
# def directmessage(request):
#     template = loader.get_template('directmessage.html')
#     return HttpResponse(template.render({}, request))

@login_required(login_url='loginPage')
def review(request):
    template = loader.get_template('review.html')
    return HttpResponse(template.render({}, request))

def signup(request):
  form = CreateUserForm()  # Correctly instantiate UserCreationForm
  if request.method == 'POST':
      form = CreateUserForm(request.POST)
      if form.is_valid():
          form.save()
          user = form.cleaned_data.get('username')
          messages.success(request, 'Account was created for ' + user)
          return redirect('loginPage')

  context = {'form': form}
  template = loader.get_template('signup.html')
  return HttpResponse(template.render(context, request))



def loginPage(request):

  if request.method == 'POST' :
    username = request.POST.get('username')
    password = request.POST.get('password')
    form = CreateUserForm() 

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('home')
    else :
      messages.info(request, 'Username Or password is incorrect')


  context = {}  # Add context variables if needed
  return render(request,'login.html') 

def logoutUser(request):
    logout(request)
    return redirect('loginPage')  

def review(request):

  if request.method == 'POST':
      form = ReviewForm(request.POST)
      if form.is_valid():
          review = form.save(commit=False)
          review.user = request.user
          review.save()
          return redirect('review')
  else:
      form = ReviewForm()
  return render(request, 'review.html', {'form': form})

@login_required
def review2(request):
 
    return render(request, 'review2.html', {})

class directmessage(View):
  def get(self, request, *args, **kwargs):
    form = ThreadForm()
    context = {
      'form': form
    }
    return render(request, 'directmessage.html', context)

  def post(self, request, *args, **kwargs):
    form = ThreadForm(request.POST)
    username = request.POST.get('username')
    
    try:
          receiver = User.objects.get(username=username)
          if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
              thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
              return redirect('thread', pk=thread.pk)
          elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
              thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
              return redirect('thread', pk=thread.pk)

          if form.is_valid():
              thread = ThreadModel(
                  user=request.user,
                  receiver=receiver
              )
              thread.save()

              return redirect('thread', pk=thread.pk)
    except:
        return redirect('directmessage')


class ListThreads(View):
  def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))
        context = {
            'threads': threads
        }
        return render(request, 'inbox.html', context)

class CreateMessage(View):
  def post(self, request, pk, *args, **kwargs):
    thread = ThreadModel.objects.get(pk=pk)
    if thread.receiver == request.user:
      receiver = thread.user
    else:
      receiver = thread.receiver
      message = MessageModel(
        thread=thread,
        sender_user=request.user,
        receiver_user=receiver,
        body=request.POST.get('message'),
      )
      message.save()
      return redirect('thread', pk=pk)

class ThreadView(View):
  def get(self, request, pk, *args, **kwargs):
    form = MessageForm()
    thread = ThreadModel.objects.get(pk=pk)
    message_list = MessageModel.objects.filter(thread__pk__contains=pk)
    context = {
      'thread': thread,
      'form': form,
      'message_list': message_list
    }
    return render(request, 'thread.html', context)  

def get_current_time(request):
    # Get the current time, with timezone awareness
    now = timezone.now()
    return HttpResponse(f"Current time: {now}")        
 
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to a new URL
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'editprofile.html', {'form': form})
    

@login_required
def view_profile(request):
    return render(request, 'profile.html', {'user': request.user})


def explore(request):
    # Create a range of numbers from 1 to 12
    image_range = range(1, 13)
    return render(request, 'explore.html', {'image_range': image_range})

@login_required
def report(request):
    template = loader.get_template('report.html')
    return HttpResponse(template.render({}, request))

def search_users(request):
    if 'username' in request.GET:
        username = request.GET['username']
        users = User.objects.filter(username__icontains=username)
        return render(request, 'inbox.html', {'users': users})
        


       
  

  

