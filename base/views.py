from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .models import Profile, Home
from .forms import PostForm, ProfileUpdate
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin





class HomeView(TemplateView):
    template_name = 'base/home.html'

class SignUp(FormView):

    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignUp, self,).form_valid(form)

    def get(self, *args, **kwargs):
        
        if self.request.user.is_authenticated:
            return redirect('home_list', kwargs={'id': id})
        return super(SignUp, self).get(*args, **kwargs)


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = ["name", "profile_image", "bio"]
    redirect_authenticated_user = True
    success_url = reverse_lazy('home_list')


    def get_success_url(self):
        return reverse_lazy('home_list')

class customLogoutView(LogoutView):
    template_name='base/logout.html'


class TaskList(LoginRequiredMixin, ListView):
    model = Home
    context_object_name = 'home'
    
    def get_context_data(self, **kwargs):
        
        
        context = super().get_context_data(**kwargs)
        context['home'] = context['home'].exclude(username=self.request.user)  
        print(context) 
        return context



        

class ProfileView(DetailView):
    model = Profile
    form = ProfileUpdate
    template_name = 'base/profile.html'

    

    

    def get_context_data(self, **kwargs):
        
        id = self.kwargs["pk"]
        context = super(ProfileView, self).get_context_data(**kwargs)
        profile = Profile.objects.filter(pk=id)
        context['user'] = profile
        return context


class UploadPost(TemplateView):
    form = PostForm
    template_name = 'base/upload.html'
    redirect_authenticated_user = True
    

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('home_list'))
        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ProfileSetUp(FormView):
    model = Profile
    form = ProfileUpdate
    template_name = 'base/profilesetup.html'
    fields = ['profile_image', 'bio']
   
    success_url = reverse_lazy('home_list')

    # def form_valid(self, form):
    #     return super(ProfileSetUp, self).form_valid(form)
    # def get_context_data(self, **kwargs):
        
    #     id = self.kwargs["id"]
        
    #     context = super(ProfileUpdate, self).get_context_data(**kwargs)
    #     profile = Profile.objects.get(pk=id)

    #     context['user'] = profile
    #     context['profile_image'] = profile.profile_image
    #     context['bio'] = profile.bio
      
    #     return context


    

class TaskCreate(CreateView):

	model = Home
	fields = ['post_image', 'caption']
	success_url = reverse_lazy('tasks')

class ProfileUpdate(UpdateView):
    model = Profile
    form = ProfileUpdate
    template_name = 'base/update-profile.html'
    fields = ['profile_image', 'bio']
    success_url = reverse_lazy('home_list')

    # def get_context_data(self, **kwargs):
        
    #     id = self.kwargs["pk"]
        
    #     context = super(ProfileUpdate, self).get_context_data(**kwargs)
    #     profile = Profile.objects.get(pk=id)

    #     context['user'] = profile
    #     context['profile_image'] = profile.profile_image
    #     context['bio'] = profile.bio
      
    #     return context


class UserPosts(ListView):
    model = Profile
    template_name = "base/user_home_list.html"
    
    def get_context_data(self, **kwargs):
        
        username = self.kwargs["pk"]
        
        context = super(UserPosts, self).get_context_data(**kwargs)
        profile = Profile.objects.get(user=username)
        

        context['user'] = profile
        
      
        return context

class TaskDelete(DeleteView):
	model = Home
	context_object_name = 'task'
	success_url = reverse_lazy('tasks')
