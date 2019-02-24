from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import DetailView
#from django.core.urlresolvers import reverse_lazy
#from reversion import revisions as reversion
from django.db import models, transaction
#from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from django.http import HttpResponse

from .models import Ingredient, IngredientForm

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


class IngredientList(ListView):
    model = Ingredient
    form_class = IngredientForm

def ingredientdetail(request, ingredientid):
    ingredient = Ingredient.objects.filter(id=ingredientid)
    return render(request, 'ingredientdetail.html', {'ingredient': ingredient[0]})

class IngredientCreate(CreateView):
    model = Ingredient
    form_class = IngredientForm

class IngredientUpdate(UpdateView):
    model = Ingredient
    form_class = IngredientForm

class IngredientDelete(DeleteView):
    model = Ingredient
    form_class = IngredientForm

