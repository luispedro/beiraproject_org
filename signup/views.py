from django.shortcuts import render_to_response
from .models import SignupForm

def signup(request):
    if request.method != 'POST':
        return render_to_response('signup.html', { 'form' : SignupForm(), 'error' : False } )
    form = SignupForm(request.POST)
    if form.is_valid():
        form.save()
        return render_to_response('signedup.html')
    return render_to_response('signup.html', {
                                'form' : form,
                                'error' : 'Some error',
                            })

