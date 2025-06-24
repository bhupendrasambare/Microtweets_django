from django.contrib import admin
from .models import Tweet
# Register your models here.

from django.contrib import admin
from .models import Tweet

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'short_text',
        'count_likes',
        'count_comment',
        'count_retweet',
        'created_at',
        'updated_at',
        'is_deleted'
    )
    list_filter = ('is_deleted', 'created_at', 'user__username')
    search_fields = ('text', 'user__username', 'user__email')
    ordering = ('-created_at',)

    def username(self, obj):
        return obj.user.username
    username.admin_order_field = 'user__username'
    username.short_description = 'Username'

    def short_text(self, obj):
        return (obj.text[:50] + '...') if len(obj.text) > 50 else obj.text
    short_text.short_description = 'Tweet'