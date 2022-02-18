from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Horoscope, Photo, Profile
from django.contrib.auth.models import User
from django.db.models import Q

S3_BASE_URL = 'https://s3-ca-central-1.amazonaws.com/' 
BUCKET = 'astro-club-bucket'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/profile/new')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def profile(request):
    profile = Profile.objects.get(user__pk = request.user.id)
    sign_text = request.user.horoscope.horoscope
    if sign_text =='CP':
        request.user.horoscope.text = 'Capricorn'
    if sign_text =='CA':
        request.user.horoscope.text = 'Cancer' 
    if sign_text =='TA':
        request.user.horoscope.text = 'Taurus'
    if sign_text =='SC':
        request.user.horoscope.text = 'Scorpio'
    if sign_text =='GE':
        request.user.horoscope.text = 'Gemini'
    if sign_text =='LE':
        request.user.horoscope.text = 'Leo' 
    if sign_text =='SA':
        request.user.horoscope.text = 'Sagittarius'
    if sign_text =='AQ':
        request.user.horoscope.text = 'Aquarius'
    if sign_text =='LI':
        request.user.horoscope.text = 'Libra'
    if sign_text =='CA':
        request.user.horoscope.text = 'Cancer' 
    if sign_text =='PI':
        request.user.horoscope.text = 'Pisces'
    if sign_text =='VI':
        request.user.horoscope.text = 'Virgo'
    return render(request, 'accounts/profile.html', { 'profile': profile, 'user': request.user })

@login_required
def profile_view(request, pk):
    profile = Profile.objects.get(user__pk = pk)
    sign_text = request.user.horoscope.horoscope
    if sign_text =='CP':
        request.user.horoscope.text = 'Capricorn'
    if sign_text =='CA':
        request.user.horoscope.text = 'Cancer' 
    if sign_text =='TA':
        request.user.horoscope.text = 'Taurus'
    if sign_text =='SC':
        request.user.horoscope.text = 'Scorpio'
    if sign_text =='GE':
        request.user.horoscope.text = 'Gemini'
    if sign_text =='LE':
        request.user.horoscope.text = 'Leo' 
    if sign_text =='SA':
        request.user.horoscope.text = 'Sagittarius'
    if sign_text =='AQ':
        request.user.horoscope.text = 'Aquarius'
    if sign_text =='LI':
        request.user.horoscope.text = 'Libra'
    if sign_text =='CA':
        request.user.horoscope.text = 'Cancer' 
    if sign_text =='PI':
        request.user.horoscope.text = 'Pisces'
    if sign_text =='VI':
        request.user.horoscope.text = 'Virgo'
    return render(request, 'accounts/profile_view.html', { 'profile': profile, 'user': request.user })

@login_required
def matches(request):
    user_sign = request.user.horoscope.horoscope
    print(user_sign)
    if user_sign == 'VI' or user_sign == 'PI':
        matches = User.objects.filter(
            Q(horoscope__horoscope = 'CP') | Q(horoscope__horoscope = 'CA') | Q(horoscope__horoscope = 'TA') | Q(horoscope__horoscope = 'SC'))[:3]
        print(matches)
        # sign_text = request.match.horoscope.horoscope
        # if sign_text =='CP':
        #     request.match.horoscope.text = 'Capricorn'
        # if sign_text =='CA':
        #     request.match.horoscope.text = 'Cancer' 
        # if sign_text =='TA':
        #     request.match.horoscope.text = 'Taurus'
        # if sign_text =='SC':
        #     request.match.horoscope.text = 'Scorpio'
        return render(request, 'matches.html', { 'matches': matches, 'user': request.user })
    if user_sign == 'AR' or user_sign == 'LI':
        matches = User.objects.filter(
            Q(horoscope__horoscope = 'GE') | Q(horoscope__horoscope = 'LE') | Q(horoscope__horoscope = 'SA') | Q(horoscope__horoscope = 'AQ'))[:3]
        print(matches)        
        # sign_text = request.match.horoscope.horoscope
        # if sign_text =='GE':
        #     request.match.horoscope.text = 'Gemini'
        # if sign_text =='LE':
        #     request.match.horoscope.text = 'Leo' 
        # if sign_text =='SA':
        #     request.match.horoscope.text = 'Sagittarius'
        # if sign_text =='AQ':
        #     request.match.horoscope.text = 'Aquarius'
        return render(request, 'matches.html', { 'matches': matches, 'user': request.user })
    if user_sign == 'TA' or user_sign == 'SC':
        matches = User.objects.filter(
            Q(horoscope__horoscope = 'CA') | Q(horoscope__horoscope = 'VI') | Q(horoscope__horoscope = 'CP') | Q(horoscope__horoscope = 'PI'))[:3]
        print(matches)         
        # sign_text = request.match.horoscope.horoscope
        # if sign_text =='CP':
        #     request.match.horoscope.text = 'Capricorn'
        # if sign_text =='CA':
        #     request.match.horoscope.text = 'Cancer' 
        # if sign_text =='PI':
        #     request.match.horoscope.text = 'Pisces'
        # if sign_text =='VI':
        #     request.match.horoscope.text = 'Virgo'
        return render(request, 'matches.html', { 'matches': matches, 'user': request.user })
    if user_sign == 'GE' or user_sign == 'SA':
        matches = User.objects.filter(
            Q(horoscope__horoscope = 'LI') | Q(horoscope__horoscope = 'AQ') | Q(horoscope__horoscope = 'AR') | Q(horoscope__horoscope = 'LE'))[:3]
        print(matches)     
        # sign_text = request.match.horoscope.horoscope
        # if sign_text =='LI':
        #     request.match.horoscope.text = 'Libra'
        # if sign_text =='AQ':
        #     request.match.horoscope.text = 'Aquarius' 
        # if sign_text =='AR':
        #     request.match.horoscope.text = 'Aries'
        # if sign_text =='LE':
        #     request.match.horoscope.text = 'Leo'
        return render(request, 'matches.html', { 'matches': matches, 'user': request.user })
    if user_sign == 'CA' or user_sign == 'CP':
        matches = User.objects.filter(
            Q(horoscope__horoscope = 'TA') | Q(horoscope__horoscope = 'VI') | Q(horoscope__horoscope = 'SC') | Q(horoscope__horoscope = 'PI'))[:3]
        print(matches)   
        # sign_text = request.match.horoscope.horoscope
        # if sign_text =='TA':
        #     request.match.horoscope.text = 'Taurus'
        # if sign_text =='VI':
        #     request.match.horoscope.text = 'Virgo' 
        # if sign_text =='PI':
        #     request.match.horoscope.text = 'Pisces'
        # if sign_text =='SC':
        #     request.match.horoscope.text = 'Scorpio'
        return render(request, 'matches.html', { 'matches': matches, 'user': request.user })
    if user_sign == 'LE' or user_sign == 'AQ':
        matches = User.objects.filter(
            Q(horoscope__horoscope = 'AR') | Q(horoscope__horoscope = 'GE') | Q(horoscope__horoscope = 'LI') | Q(horoscope__horoscope = 'SA'))[:3]
        print(matches)       
        # sign_text = request.match.horoscope.horoscope
        # if sign_text =='AR':
        #     request.match.horoscope.text = 'Aries'
        # if sign_text =='GE':
        #     request.match.horoscope.text = 'Gemini' 
        # if sign_text =='LI':
        #     request.match.horoscope.text = 'Libra'
        # if sign_text =='SA':
        #     request.match.horoscope.text = 'Sagittarius'
        return render(request, 'matches.html', { 'matches': matches, 'user': request.user })

class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['profile_pic', 'first_name', 'last_name', 'social_handles']
    success_url = '/horoscope/new'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class HoroscopeCreate(LoginRequiredMixin, CreateView):
    model = Horoscope
    fields = ['horoscope']
    success_url = '/profile/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class HoroscopeUpdate(LoginRequiredMixin, UpdateView):
    model = Horoscope
    fields = ['horoscope']
    success_url = '/profile/'

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['profile_pic', 'first_name', 'last_name', 'social_handles']
    success_url = '/profile/'

class ProfileDelete(DeleteView):
  model = Profile
  success_url = '/profile/new'

@login_required
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
    return redirect('/profile/')

@login_required
def horoscope(request):
    profile = Profile.objects.get(user = request.user)
    return render(request, 'accounts/horoscope.html', {
        "profile": profile
    })



#-----------------------------------------------------------------------------------------------------------------------------------



def home(request):
    return render(request, 'home.html')

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





