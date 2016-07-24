from django.shortcuts import render
from django.db import models
from .models import TopicModel, SubTopicModel
from sympy import *
from random import randint
# Create your views here.

def init(request):
    return render(request, 'index.html')

# def init(request):
#     #ax*2+bx+c
#     x = Symbol('x')
#     questions = []
#     solutions = []
#     for i in range(15):
#         origin = (x + randint(1,6))*(x + randint(1,6))
#         question = expand(origin)
#         solution = factor(question)
#         question = latex(question)
#         questions.append(question)
#         solution = latex(solution)
#         solutions.append(solution)
#     # for item in questions:
#     #     print item
#     # eqn2 = expand((4 + x)**2)
#     # eqn2 = latex(eqn2)
#     # Next to do....
#     # equations in a list
#     # generate using random numbers
#     return render(request, 'quadratics.html', {'questions': questions, 'solutions': solutions})

def topics(request):
    topicModel = TopicModel.objects.all()
    return render(request, 'topics.html', {'topicModel': topicModel})

def subtopics(request, id):
    topicModel = TopicModel.objects.all()
    subtopicModel = SubTopicModel.objects.all().filter(topic = id)
    print "yolo!"
    return render(request, 'topics.html', {'subtopicModel': subtopicModel, 'topicModel': topicModel})
