from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.get_index, name='dashboard'),
    path('news', views.get_news_list, name='news_list'),
    path('news/create', views.add_news, name='create_news'),
    path('news/add_news', views.create_news, name='add_news'),
    path('news/<int:post_id>/edit/', views.edit_news, name='edit_news'),
    path('news/update', views.update_news, name='update_news'),
    path('news/<int:post_id>/delete/', views.soft_delete_news, name='delete_news'),
    path('auth', views.get_authors_list, name='auth_list'),
    path('auth/create', views.add_author, name='create_auth'),
    path('auth/add_author', views.create_author, name='add_auth'),
    path('taxonomies', views.taxonomy_manage, name='categories_list'),
    path('add-taxonomy', views.add_term_taxanomy, name='add_term_taxanomy'),
    path('categories/create', views.new_term, name='create_categories'),
    path('add_term/', views.add_term, name='add_term'),
    path('tags', views.get_tags_list, name='tags_list'),
    path('media', views.get_images_list, name='media_list'),
    path('media/gallery', views.get_gallery, name='get_gallery'),
    path('widget', views.get_widget_manager, name='widget_manager'),
    path('widget/widget-area', views.get_widget_area, name='widget_list'),
    path('widget/create', views.add_widget, name='create_widget'),
    path('banner', views.get_banner_manager, name='banner_manager'),
    path('banner/create', views.add_banner, name='create_banner'),
    path('menu', views.get_menu_manager, name='menu_manager'),
    path('menu/create', views.add_banner, name='create_menu'),
    path('setting', views.get_pageinfo, name='get_pageinfo'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='sinup'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)