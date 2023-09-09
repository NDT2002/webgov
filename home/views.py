from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from manager import models
# Create your views here.
def get_home(request):
    return render(request, 'home.html')
def new_detail(request, post_id):
    description = models.PostMeta.objects.filter(post_id=post_id, meta_key='description').first()
    if description:
        description_text = description.meta_value
    else:
        description_text = "Không có mô tả."
    # Lấy bài viết cụ thể hoặc trả về 404 nếu không tìm thấy
    post = get_object_or_404(models.Post, pk=post_id)
    return render(request, 'newspage/newsdetail.html', {'post': post, 'description_text':description_text})
def get_post_list(request):
     # Truy vấn tất cả bài viết
    all_posts = models.Post.objects.all()
    
    # Lặp qua danh sách bài viết và truy vấn thông tin mô tả từ PostMeta
    for post in all_posts:
        post.post_description = models.PostMeta.objects.filter(post=post, meta_key='description').first()

    # Phân trang
    posts_per_page = 5
    paginator = Paginator(all_posts, posts_per_page)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'newspage/postlist.html',{'posts':posts})