from django.shortcuts import render, redirect
import re
from django.http import HttpResponse
from django.views import View
from Content.models import Content
from Comments.models import Comments

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm


# from Blog.models import MyModelForm

# class ContentView(View):
#
#
#     def get(self, request):
#
#         all_notes = Content.objects.values_list(
#             'data',
#             'content',
#             'image',
#             'reaction_positive',
#             'reaction_negative',
#             'comments_amount',
#             )
#
#         data_list = []
#
#         additional_querry_set = Content.objects.all()
#         for each in additional_querry_set:
#             data = {}
#             data['data'] = each.data
#             data['content'] = each.content
#             data['image'] = each.image
#             data['reaction_positive'] = each.reaction_positive
#             data['reaction_negative'] = each.reaction_negative
#             data['comments_amount'] = each.comments_amount
#
#
#             data_list.append(data)
#
#         # my_ing = additional_querryset[1].image.url
#
#
#         return render(request,'index.html', {'notes': all_notes,  'data_list': data_list})
#         # form = MyModelForm()
#         # return render(request,'index.html', {'language': form})
#
#     def register(self, request):
#         if request.method == 'POST':
#             form = CustomUserCreationForm(request.POST)
#             if form.is_valid():
#                 user = form.save()
#                 login(request, user)
#                 return redirect('index')
#             else:
#                 form = CustomUserCreationForm()
#
#         return render(request, 'register.html', {'form': form})
#
#

def ContentView(request):
    if request.method == 'GET':
        data_list = []

        blog_queryset = Content.objects.all().order_by('id')
        for each in blog_queryset:
            data = {'data': each.data,
                    'content': each.content,
                    'image': each.image,
                    'reaction_positive': each.reaction_positive,
                    'reaction_negative': each.reaction_negative,
                    'comments_amount': each.comments_amount,
                    'id': each.id}

            data_list.append(data)

        return render(request, 'index.html', {'data_list': data_list})


    if request.method == 'POST':

        action = request.POST.get('action')
        if action != None:

            if action =='registration':
                form = CustomUserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('login/')
                else:
                    form = CustomUserCreationForm()
                return render(request, 'register.html', {'form': form})

            if action == 'login':
                return redirect('login/')

            # if action == 'home':
            #     data_list = []
            #     additional_queryset = Content.objects.all()
            #
            #     for each in additional_queryset:
            #         data = {'data': each.data,
            #                 'content': each.content,
            #                 'image': each.image,
            #                 'reaction_positive': each.reaction_positive,
            #                 'reaction_negative': each.reaction_negative,
            #                 'comments_amount': each.comments_amount,
            #                 'id':each.id}
            #
            #         data_list.append(data)
            #
            #     return render(request, 'index.html', {'data_list': data_list})

            if action[:3] == 'add':
                row = action[3:]
                split_obj = re.split(r'_',row)
                Content.objects.filter(id=split_obj[0]).update(reaction_positive=int(split_obj[1])+1)
                return redirect('/')

            if action[:3] == 'del':
                row = action[3:]
                split_obj = re.split(r'_', row)
                Content.objects.filter(id=split_obj[0]).update(reaction_negative=int(split_obj[1]) + 1)
                return redirect('/')