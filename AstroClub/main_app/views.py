from django.shortcuts import render, redirect
from .models import Photo, Profile
import uuid
import boto3

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

