from django.urls import path, include, re_path

from django.contrib import admin

admin.autodiscover()

import hello.views

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("admin/", admin.site.urls),
    re_path(r'^ingredients/$', hello.views.IngredientList.as_view(), name='IngredientList'),
    re_path(r'^ingredient/(?P<ingredientid>[0-9]+)$', hello.views.ingredientdetail, name='ingredientdetail'),
    re_path(r'^ingredient/(?P<ingredientid>[0-9]+)/$', hello.views.ingredientdetail, name='ingredientdetail'),
    re_path(r'^ingredient/(?P<pk>[0-9]+)/edit', hello.views.IngredientUpdate.as_view(), name='update_ingredient'),
    re_path(r'^ingredient/(?P<pk>[0-9]+)/delete', hello.views.IngredientDelete.as_view(success_url="/"), name='delete_ingredient'),
    re_path(r'^ingredient/create', hello.views.IngredientCreate.as_view(), name='create_ingredient'),
    re_path(r'^formulas/$', hello.views.FormulaList.as_view(), name='FormulaList'),
    re_path(r'^formula/(?P<formulaid>[0-9]+)$', hello.views.formuladetail, name='formuladetail'),
    re_path(r'^formula/(?P<formulaid>[0-9]+)/$', hello.views.formuladetail, name='formuladetail'),
    re_path(r'^formula/(?P<pk>[0-9]+)/edit', hello.views.FormulaUpdate.as_view(), name='update_formula'),
    re_path(r'^formula/(?P<pk>[0-9]+)/delete', hello.views.FormulaDelete.as_view(success_url="/"), name='delete_formula'),
    re_path(r'^formula/create', hello.views.FormulaCreate.as_view(), name='create_formula'),
]
