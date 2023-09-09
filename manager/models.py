from django.db import models

def upload_to(instance, filename):
    return f'post_images/{instance.id}/{filename}'

# Người dùng
class User(models.Model):
    user_login = models.CharField(max_length=60)
    user_pass = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=100)
    display_name = models.CharField(max_length=250)
    user_registered = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='created_users')
    updated_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='updated_users')
    is_deleted = models.BooleanField(default=False)

# Bài viết
class Post(models.Model):
    post_title = models.CharField(max_length=255)
    post_content = models.TextField()
    post_date = models.DateTimeField()
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_status = models.CharField(max_length=20)
    post_type = models.CharField(max_length=20)
    featured_image = models.ImageField(upload_to=upload_to, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_posts')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_posts')
    is_deleted = models.BooleanField(default=False)

# Danh mục
class Term(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    term_group = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_terms')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_terms')
    is_deleted = models.BooleanField(default=False)

# Phân loại danh mục
class TermTaxonomy(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    taxonomy = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_term_taxonomies')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_term_taxonomies')
    is_deleted = models.BooleanField(default=False)

# Mối quan hệ danh mục
class TermRelationship(models.Model):
    object_id = models.IntegerField()
    term_taxonomy = models.ForeignKey(TermTaxonomy, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_term_relationships')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_term_relationships')
    is_deleted = models.BooleanField(default=False)

# Tùy chọn
class Option(models.Model):
    option_name = models.CharField(max_length=64)
    option_value = models.TextField()
    autoload = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_options')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_options')
    is_deleted = models.BooleanField(default=False)

# Dữ liệu tùy chọn bài viết
class PostMeta(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    meta_key = models.CharField(max_length=255)
    meta_value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_post_metas')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_post_metas')
    is_deleted = models.BooleanField(default=False)

# Bình luận
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_comments')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_comments')
    is_deleted = models.BooleanField(default=False)

# Dữ liệu tùy chọn bình luận
class CommentMeta(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    meta_key = models.CharField(max_length=255)
    meta_value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_comment_metas')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_comment_metas')
    is_deleted = models.BooleanField(default=False)

# Liên kết
class Link(models.Model):
    link_url = models.URLField(max_length=200)
    link_name = models.CharField(max_length=255)
    link_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_links')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_links')
    is_deleted = models.BooleanField(default=False)

# Dữ liệu tùy chọn danh mục
class TermMeta(models.Model):
    term = models.ForeignKey('Term', on_delete=models.CASCADE)
    meta_key = models.CharField(max_length=255)
    meta_value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_term_metas')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_term_metas')
    is_deleted = models.BooleanField(default=False)

# Dữ liệu tùy chọn người dùng
class UserMeta(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    meta_key = models.CharField(max_length=255)
    meta_value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_user_metas')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_user_metas')
    is_deleted = models.BooleanField(default=False)

# Liên kết SEO của Yoast cho bài viết
class YoastSEOLink(models.Model):
    url = models.URLField(max_length=200)
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_yoast_seo_links')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_yoast_seo_links')
    is_deleted = models.BooleanField(default=False)

# Dữ liệu tùy chọn SEO của Yoast
class YoastSEOMeta(models.Model):
    object_id = models.IntegerField()
    meta_key = models.CharField(max_length=255)
    meta_value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_yoast_seo_metas')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_yoast_seo_metas')
    is_deleted = models.BooleanField(default=False)

# Lịch sử hoạt động (logs)
class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
