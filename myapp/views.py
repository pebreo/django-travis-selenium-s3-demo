from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, render_to_response, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import CategoryForm
from .forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login

def index(request, template='myapp/hello.html'):
    #return HttpResponse('Hello World')
    return render(request, template)

def formview1(request, template='myapp/form1.html'):

    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            #form.save(commit=True)
            print "CATEGORY NAME %s" % form.cleaned_data['name']
            # Now call the index() view.
            # The user will be shown the homepage.
            #return index(request)
            return HttpResponseRedirect(reverse('myapp:formview1'))
        
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, template, locals())

def register(request, template='myapp/register.html'):
    # from django.contrib.auth import authenticate, login
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            print "USER FORM VALUES: " 
            for k,v in user_form.cleaned_data.items(): print k,v,"\n"
            print "PROFILE FORM VALUES: " 
            for k,v in profile_form.cleaned_data.items(): print k,v, "\n"
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, template, locals())

def user_login(request, template='myapp/login.html'):
    # from django.contrib.auth import authenticate, login
    if request.method == 'POST':
        # This information is obtained from the login form
        username = request.POST['username']
        password = request.POST['password']

        # Use Django 'authenticate' function to see if the username 
        # and password combo are valid

        user = authenticate(username=username,password=password)

        # If we have a User object and details are corrent
        if user is not None:
            if user.is_active:
                #If account is valid and active, we can log the user in
                # we'll send the user back to the homepage
                login(request, user)
                print "THE USER IS ACTIVE AND LOGGED IN"
                for k,v in user.__dict__.items(): print k,v, "\n"
                return HttpResponseRedirect(reverse('myapp:login'))
            else:
                # Not active
                return HttpResponse("Your account is not active.")
        else:
            #bad login details provided so we can't log in
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, template)
