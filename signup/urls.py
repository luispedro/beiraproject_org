from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
    (r'^fr/signup', 'signup.views.signup'),
    )
