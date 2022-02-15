from django.shortcuts import render, redirect
from .models import Photo, Profile
import uuid
import boto3
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

S3_BASE_URL = 'https://s3-ca-central-1.amazonaws.com/' 
BUCKET = 'astro-club-bucket'


def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def matches(request):
    return render(request, 'matches.html')
    
def login(request):
    return render(request, 'registration/login.html')

def signup(request):
    return render(request, 'registration/signup.html')

def intro_one(request):
    return render(request, 'intro/intro_one.html')

def intro_two(request):
    return render(request, 'intro/intro_two.html')

def intro_three(request):
    return render(request, 'intro/intro_three.html')

def questions_one(request):
    return render(request, 'questions/questions_one.html')

def questions_two(request):
    return render(request, 'questions/questions_two.html')

def questions_three(request):
    return render(request, 'questions/questions_three.html')

def questions_matches(request):
    return render(request, 'questions/questions_matches.html')




def add_photo(request):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('profile/')


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      form.save() #change from user=form.save
      # This is how we log a user in via code
      login(request)
      return redirect('profile/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

