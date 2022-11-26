memo

#routing project/urls

from django.contrib import admin
from djagno.urls import path, include 

urlpatterns= [
    path("admin/", admin.site.urls),#admin, 
    path("application/", include("application.urls"))#application--app/urls.py
]

#routing app/urls.py

from django.urls import path 
from . import views

app_name = "application"
urlpatterns = [
    path("", views.IndexView.as_view(), name= "index"),
    path("foo/", views.FooView.as_view(), name= "Foo")
    path("bar/<int:pk>/", views.BarView.as_view(), name = "Bar")
    #get int and pass it as pk to view


]

"""
str
path
int
slug
uuid
"""

#app/views.py

#function_style

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Bmi

@login_required #login
def index(request):
    context = {
        "bmi": Bmi.object.filter(user = request.user)
    }

    return render(request, "example.html", context)

#classbaseview

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Bmi

class IndexView(generic.ListView):
    model = Bmi
    template_name = "example.html"

    def get_queryset(self):
        return Bmi.object.filter(user = self.request.user)

#famous override class variables 
#
template_name: template_name = "foo.html"
model: modeL = Bmi
peginate_by : peginate_by = 5
queryset: queryset = Foo.objects.filter(foo = bar)
form_class : form_class=FooForm
success_url : success_url = reverse_lazy(app:inde)
fields: fields =["email", "name"]

#override method
get_context_data
    def get_context_data(self):
        context = super().get_context_data
        context["foo"] = FooModel.objects.get(user = self.request.user)
        return context

get_queryset
    def get_queryset(self):
        foo = FooModel.objects.filter(user = self.request.user)
        return foo
form_valid
    def form_valid(self, form):
        messages.success(self.request, "success")
        return super().form_valid(form)
form_invalid
    def form_invalid(self, form):
        message.error(self.request, "fail")
        return super().form_invalid(form)
get_success_url
    def get_success_urs(self):
        return reverse("app:detail", kwag = {"pk" :self.kwargs["pk"]})
delete
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "remove")
        return super().delete(request, *args, *kwargs)

get 
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello")
post 
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not form.is_vaild():
            return HttpResponseRedirect(reverse_lazy("app:index"))

        return render(request, self.template_name, {"form":form})

#form.py

#django,forms.Form or djangp.forms.ModelForm 
#前者はどのようなフォームでも、後者はモデルとにたフィールドだげど簡単


from django import forms

class InqueryForm(forms.Forms):
    name = forms.CharField(label= "name", max_length=30)
    email = forms.EmailField(label="email_address")
    message = forms.CharField(label = "message", widget=forms.Textarea)


from django import forms
from .model import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fiels = ("name", "email", "message")

#form field  and widget

option_form
required
label
widget
validators

#form validator

validator
clean_<br>
clean

#validators
#validation.py
from django.core.exceptions import ValidationError
def validate_admin(value):
    if "admin" in value:
        raise ValidationError("dame-")

forms.py
from django import forms
from .validation import validate_admin

class EmailForm(forms.Form):
    email = forms.EmailField(label="address", validators=[validate_admin])

#model.py

from django.db import models
from .validate import validate_admin

class Email(models.Model):
    email = models.EmailField(verbose_name = "address", validators=[validate_admin])

#use clean_<n>

from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(label="address")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if "admin" in email:
            reaise forms.ValidationError("inavailable")
        return email

#clean

from django import forms

class EmailForm(forms.Form):
    email_1  = forms.EmailField(label="1")
    email_2  = forms.EmailField(label="2")

    def clean(self):
        cleaned_data = super().clean()
        email_1 = cleaned_data.get("email_1")
        emial_2 = cleaned_data.get("email_2")

        if "admin" in email_1 and email_2:
            raise forms.ValidationError("inavalable")
view and form 

from django.views import generic
from .forms import InquryForm

class InquryView(generic.FormView):
    form_class: Optional[Type[BaseForm]] 

#model

from django.db improt models

class Bmi(models.Model):

    bmi = models.FloatField(verbose_name = "BMI", null = True, blanK = True)
    comment = models.CharField(verbose_name = "comment", max_length=100, null = True, True)
    created_at = models.DateTimeField(verbose_name = "date", auto_now_add=True)

    class Meta:
        verbose_name_plural = "Bmmi"

    def __str___(self):
        return self.created_at

#template kumikomi
user
object
object_list
messagaes
form

default
default_if_none
linebraksbr #</n>to</br>
safe
trancatechars "切り詰める"
urize #<a>

autoescape
Block
extend
for empty endfor 
load
url


#project/settiing

LANGUAGE_CODE = "ja"
TIME_ZONE = "Asia/Tokyo"

DATABASE={
    "default":{
        "ENGINE":"django.db.backends.splite3"#database
        ""
    }
}