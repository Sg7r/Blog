from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
import re
from django.http import HttpResponse
from django.views import View
from Content.models import Content
from .models import Comments, M2MComentsTable

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

@login_required
def CommentView(request, data):
    if request.method == 'GET':
        data_list = []
        blog_id = ''
        queryset = Content.objects.filter(id=data)

        for each in queryset:
            data = {'data': each.data,
                    'content': each.content,
                    'image': each.image,
                    'reaction_positive': each.reaction_positive,
                    'reaction_negative': each.reaction_negative,
                    'id': each.id}
            blog_id = each.id
            data_list.append(data)

        comment_list = []
        queryset_comments = Comments.objects.all().filter(blog=blog_id).order_by('id')
        for each in queryset_comments:
            data = {'data': each.data,
                    'content_body': each.content_body,
                    'id':each.id}
            comment_list.append(data)

        form = CommentForm()
        return render(request,
                      'comments.html',
                      {'data_list': data_list, 'comment_list': comment_list, 'form': form}
                      )

    if request.method == 'POST':
        form = CommentForm(request.POST)
        id = request.POST.get('action')
        id_obj =Content.objects.get(id=id)
        if form.is_valid():
            comment = Comments.objects.create(
                data=form.cleaned_data['data'] ,
                content_body=form.cleaned_data['content_body'],
                blog=id_obj
            )
            comments_amount = Comments.objects.all().filter(blog=id).count()
            Content.objects.all().filter(id=id).update(comments_amount=comments_amount)

            # form.save()

            return redirect(f'../../comments/{id}')


# def add_comment(request):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = CommentForm()
#     return render(request, 'comments.html', {'form': form})

        # comment = Comments.objects.create(comment='That is my first comment')
        # queryset = Comments.objects.all().order_by('id')
        # return render(request, 'comments.html', {'data_list': queryset})
