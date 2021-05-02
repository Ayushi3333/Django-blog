from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import BlogPost # relative import
from .forms import BlogPostForm
from .forms import BlogPostModelForm

def blog_post_list_view(request):
    queryset = BlogPost.objects.all()
    template_name = 'list.html'
    context = { 'object_list': queryset }
    return render(request, template_name, context)

@staff_member_required                  # decorator
@login_required(login_url='/login')
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    template_name = 'form.html'
    context = { 'form': form }
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

@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug) # lookup by slug field
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {'form': form, "title": f"Update {obj.title}" }
    return render(request, template_name, context)

@staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug) # lookup by slug field
    template_name = 'delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/blogs")
    context = {"object": obj}
    return render(request, template_name, context)

