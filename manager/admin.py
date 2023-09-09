# manager/admin.py
from django.contrib import admin
from . import models

admin.site.register(models.Post)
admin.site.register(models.PostMeta)
admin.site.register(models.Comment)
admin.site.register(models.CommentMeta)
admin.site.register(models.Link)
admin.site.register(models.Log)
admin.site.register(models.User)
admin.site.register(models.UserMeta)
admin.site.register(models.Option)
admin.site.register(models.Term)
admin.site.register(models.TermTaxonomy)
admin.site.register(models.TermRelationship)
