from django.shortcuts import render
from django.views.generic import TemplateView


class MathFactsView(TemplateView):
    template_name = "math-facts.html"


class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"