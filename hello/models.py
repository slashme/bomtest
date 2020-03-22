from django.db import models, transaction
from django import forms
from django.forms import ModelForm
#from django.utils.encoding import python_2_unicode_compatible
#from django.utils.translation import ugettext_lazy as _
#from reversion import revisions as reversion
#from reversion.admin import VersionAdmin
#from reversion.models import Revision
#from django.contrib import admin
from django.contrib.auth.models import User
from django.shortcuts import redirect
#import allauth

# Create your models here.

class Ingredient(models.Model):
    #A raw material, not made up of other materials.
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]
    def get_absolute_url(self):
        return "/ingredient/%i/" % self.id
    name        = models.CharField('Ingredient name, not including supplier', max_length=100)
    description = models.TextField('Description of the ingredient')
    vendor      = models.CharField('Supplier of the ingredient', null=True, blank=True, max_length=100)
    moisture    = models.FloatField('Total moisture, g/100 g')
    fat         = models.FloatField('Total fat (lipids incl. phospholipids) in g/100 g of ingredient', null=True, blank=True)
    satfat      = models.FloatField('Saturated fat in g/100 g of ingredient', null=True, blank=True)
    monounsat   = models.FloatField('Cis mono-unsaturated fat in g/100 g of ingredient', null=True, blank=True)
    polyunsat   = models.FloatField('Cis polyunsaturated fat in g/100 g of ingredient', null=True, blank=True)
    carbs       = models.FloatField('Digestible carbohydrate including polyols in g/100 g of ingredient', null=True, blank=True)
    sugar       = models.FloatField('Mono and disaccharides in g/100 g of ingredient', null=True, blank=True)
    polyols     = models.FloatField('Polyols in g/100 g of ingredient', null=True, blank=True)
    starch      = models.FloatField('Total starch in g/100 g of ingredient', null=True, blank=True)
    fibre       = models.FloatField('Undigestible carbs DP>3 in g/100 g of ingredient', null=True, blank=True)
    protein     = models.FloatField('Protein (Kjeldahl N × 6.25) in g/100 g of ingredient', null=True, blank=True)
    salt        = models.FloatField('Salt equiv (Na × 2.5) in g/100 g of ingredient', null=True, blank=True)
    orgacid     = models.FloatField('Organic acids in g/100 g of ingredient', null=True, blank=True)
    energy      = models.FloatField('Energy value in kJ/100 g of ingredient', null=True, blank=True)

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = [ 'name', 'description', 'vendor', 'moisture', 'fat', 'satfat', 'monounsat', 'polyunsat', 'carbs', 'sugar', 'polyols', 'starch', 'fibre', 'protein', 'salt', 'orgacid', 'energy']

class Formula(models.Model):
    #A formula, can contain ingredients and other subformulas.
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]
    def get_absolute_url(self):
        return "/formula/%i/" % self.id
    name        = models.CharField('Formula name', max_length=100)
    description = models.TextField('Long description of the formula')

class FormulaForm(ModelForm):
    class Meta:
        model = Formula
        fields = [ 'name', 'description']

class FormulaIngredient(models.Model):
    #An item in a formula
    def __str__(self):
        return f'{self.ingredient.name}'
    formula = models.ForeignKey(Formula, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.FloatField('fraction of ingredient in recipe', null=False, blank=False)
