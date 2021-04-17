from django.shortcuts import render, get_object_or_404
from django.http import Http404


# Create your views here.
from .models import BlogPost # relative import

# GET -> 1 object
# filter -> [] objects

def blog_post_detail_page(request, slug):
    # obj = get_object_or_404(BlogPost, id=post_id) # with error handling and lookup by id
    # obj = BlogPost.objects.get(id=post_id) # without error handling
    # obj = get_object_or_404(BlogPost, slug=slug) # lookup by slug field
    
    queryset = BlogPost.objects.filter(slug=slug) # returns a Query Set of all objects meeting that condition
    if queryset.count() == 0:
        raise Http404
    obj = queryset.first()

    template_name = 'blog_post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)
