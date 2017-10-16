# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
class ArticleView(view):
    def get(self, request):
        context = {name: 'haha'}
        return render(request, 'article/index.html', context)
