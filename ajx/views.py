from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, render_to_response, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login
import json

def mygetview(request):
    if request.method == 'GET':

        print "**get**"
        data = request.GET['mydata']
        astr = "<html><b> you sent a get request </b> <br> returned data: %s</html>" % data
        return HttpResponse(astr)
    return render(request)

def mypostview(request):
    if request.method == 'POST':

        print "**post**"
        data = request.POST['mydata']
        astr = "<html><b> you sent a post request </b> <br> returned data: %s</html>" % data
        return HttpResponse(astr)
    return render(request)

def myajaxview(request):
    if request.method == 'POST':
        if request.is_ajax():
            print "**ajax post**"
            data = request.POST['mydata']
            astr = "<html><b> you sent an ajax post request </b> <br> returned data: %s</html>" % data
            return HttpResponse(astr)
    return render(request)

def myajaxformview(request):
    if request.method == 'POST':
        if request.is_ajax():
            import json

            print "**ajax form post**"
            for k,v in request.POST.items(): 
                print k,v

            print "field1 data: %s" % request.POST['field1']
            print "field2 data: %s" % request.POST['field2']

            mydata = [{'foo':1, 'baz':2}]
            return HttpResponse(json.dumps(mydata), mimetype="application/json")
    
    return render(request)

def foo(request,template='ajx/foo.html'):
    return render(request,template)

# def foo2(request):
#     if request.method == 'POST': # If the form has been submitted...
#         form = ContactForm(request.POST) # A form bound to the POST data
#         if form.is_valid(): # All validation rules pass
#             # Process the data in form.cleaned_data
#             # ...
#             return HttpResponseRedirect('/thanks/') # Redirect after POST
#     else:
#         form = ContactForm() # An unbound form

#     return render(request, 'contact.html', {
#         'form': form,
#     })
