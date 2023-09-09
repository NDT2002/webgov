from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .forms import PostForm
from .forms import TermForm
from .forms import UserForm
from . import forms
from . import models
from django.utils import timezone
# Create your views here.
def get_index(request):
    return render(request, 'manager/dashboard.html')
# news
def get_news_list(request):
    news= models.Post.objects.all()
    return render(request, 'manager/news/newslist.html',{'news':news})
def add_news(request):
    taxonomies=models.TermTaxonomy.objects.all()
    users = models.User.objects.all()  # Truy vấn tất cả user từ bảng User
    date_now = timezone.now().strftime("%Y-%m-%dT%H:%M")  # Định dạng ngày giờ theo ISO-8601
    return render(request, 'manager/news/addnews.html',{'users': users, 'date_now':date_now, 'taxonomies':taxonomies})
def create_news(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save()
            featured_image = request.FILES.get('featured_image')
            if featured_image:
                post.featured_image = featured_image
                post.save()
            post_id =post.id
            description = request.POST.get('description')
            tags = request.POST.get('tags')
            taxonomy=request.POST.get('taxonomies')
            term_taxonomy = models.TermTaxonomy.objects.get(pk=taxonomy)
            # Lưu mô tả vào bảng PostMeta
            models.TermRelationship.objects.create(object_id=post_id,term_taxonomy=term_taxonomy)
            models.PostMeta.objects.create(post_id=post_id, meta_key='description', meta_value=description)
            # models.PostMeta.objects.create(post_id=post_id, meta_key='image_post', meta_value=image_post)

            # Xử lý tags (chia chuỗi thành danh sách tags rồi lưu vào bảng PostMeta)
            tag_list = tags.split(',')
            for tag in tag_list:
                models.PostMeta.objects.create(post_id=post_id, meta_key='tag', meta_value=tag)

            return redirect('news_list')  # Điều hướng đến trang danh sách bài viết sau khi thêm
    else:
        form = PostForm()
    return render(request, 'add_news.html', {'form': form})

def edit_news(request,post_id):
    post = models.Post.objects.get(pk=post_id)
    users = models.User.objects.all()  # Truy vấn tất cả user từ bảng User
    return render(request,'manager/news/editnews.html', {"post":post,"users":users})

def update_news(request, post_id):
    try:
        post = models.Post.objects.get(pk=post_id)
    except models.Post.DoesNotExist:
        # Xử lý khi không tìm thấy bài viết với post_id cụ thể
        return HttpResponseNotFound("Bài viết không tồn tại")

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)  # Lưu form nhưng không commit vào database
            featured_image = request.FILES.get('featured_image')
            if featured_image:
                post.featured_image = featured_image
            description = request.POST.get('description')
            tags = request.POST.get('tags')
            taxonomy = request.POST.get('taxonomies')
            term_taxonomy = models.TermTaxonomy.objects.get(pk=taxonomy)
            post.save()  # Lưu bài viết sau khi cập nhật

            # Xóa tất cả các PostMeta liên quan đến bài viết cũ
            models.PostMeta.objects.filter(post_id=post_id).delete()

            # Lưu mô tả vào bảng PostMeta
            models.PostMeta.objects.create(post=post, meta_key='description', meta_value=description)

            # Xử lý tags (chia chuỗi thành danh sách tags rồi lưu vào bảng PostMeta)
            tag_list = tags.split(',')
            for tag in tag_list:
                models.PostMeta.objects.create(post=post, meta_key='tag', meta_value=tag)

            # Cập nhật term_taxonomy
            term_relationship = models.TermRelationship.objects.get(post_id=post.id)
            term_relationship.term_taxonomy = term_taxonomy
            term_relationship.save()

            return redirect('news_list')  # Điều hướng đến trang danh sách bài viết sau khi cập nhật
    else:
        form = PostForm(instance=post)

    return render(request, 'your_template.html', {'form': form, 'post': post})


def soft_delete_news(request, post_id):
    try:
        post = models.Post.objects.get(pk=post_id)
        post.is_deleted = True
        post.post_status="Ẩn"
        post.save()
        # Cập nhật giao diện hoặc chuyển hướng người dùng nếu cần
        return redirect('news_list')  # Điều hướng đến trang danh sách bài viết sau khi thêm

    except models.Post.DoesNotExist:
        # Xử lý trường hợp bài viết không tồn tại
        pass

#term
# def get_term_list(request):
#     term= models.Post.objects.all()
#     return render(request, 'manager/categories/category.html',{'term':term})
def new_term(request):
    terms = models.Term.objects.all()
    return render(request, 'manager/categories/newcategory.html',{'terms': terms})
def add_term(request):
    if request.method == 'POST':
        form = TermForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_categories')
    else:
        form = TermForm()
    return render(request, 'manager/categories/newcategory.html', {'form': form})

def taxonomy_manage(request):
    taxonomies=models.TermTaxonomy.objects.all()
    terms=models.Term.objects.all()
    return render(request, 'manager/categories/category.html',{'terms':terms, 'taxonomies':taxonomies})
def add_term_taxanomy(request):
    if request.method == 'POST':
        form = forms.TermTaxonomyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_list')
        else:
            form = forms.TermTaxonomyForm()
        return render(request, 'manager/categories/category.html', {'form': form})

def get_tags_list(request):
    return render(request, 'manager/categories/tags.html')

# auth
def get_authors_list(request):
    return render(request, 'manager/author/authlist.html')
def add_author(request):
    return render(request, 'manager/author/newauth.html')

def create_author(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_registered = timezone.now()
            user.save()
            return redirect('auth_list')
    else:
        form = UserForm()
    return render(request, 'manager/author/newauth.html', {'form': form})


# media
def get_images_list(request):
    return render(request, 'manager/media/image.html')
def get_gallery(request):
    return render(request, 'manager/media/gallery.html')
# setting 
# widget
def get_widget_manager(request):
    return render(request, 'manager/widget/widget.html')
def get_widget_area(request):
    return render(request, 'manager/widget/widgetlist.html')
def add_widget(request):
    return render(request, 'manager/widget/widgetnew.html')

def get_banner_manager(request):
    return render(request, 'manager/banner/banner.html')
def add_banner(request):
    return render(request, 'manager/banner/newbanner.html')

def get_menu_manager(request):
    return render(request, 'manager/menu/menusetting.html')
def add_menu(request):
    return render(request, 'manager/menu/newmenu.html')

def get_pageinfo(request):
    return render(request, 'manager/setting/pageinfo.html')
def login(request):
    return render(request,"manager/author/login.html")
def signup(request):
    return render(request,"manager/author/signup.html")