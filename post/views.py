from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import BlogPost # relative import

def blog_post_list_view(request):
    queryset = BlogPost.objects.all()
    template_name = 'list.html'
    context = { 'object_list': queryset }
    return render(request, template_name, context)

def blog_post_create_view(request):
    template_name = 'create.html'
    context = { 'form': None }
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    # obj = get_object_or_404(BlogPost, id=post_id) # with error handling and lookup by id
    # obj = BlogPost.objects.get(id=post_id) # without error handling
    obj = get_object_or_404(BlogPost, slug=slug) # lookup by slug field
    # print("HELLO DJANGO", request.method, request.path, request.user)

    # queryset = BlogPost.objects.filter(slug=slug) # returns a Query Set of all objects meeting that condition
    # if queryset.count() == 0:
    #     raise Http404
    # obj = queryset.first()

    template_name = 'detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

def blog_post_update_view(request):
    obj = get_object_or_404(BlogPost, slug=slug) # lookup by slug field
    template_name = 'update.html'
    context = {"object": obj, 'form': None}
    return render(request, template_name, context)

def blog_post_delete_view(request):
    obj = get_object_or_404(BlogPost, slug=slug) # lookup by slug field
    template_name = 'delete.html'
    context = {"object": obj}
    return render(request, template_name, context)

