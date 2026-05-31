from django.contrib import admin
from .models import Product, Category, Post, Banner, Visitor, ProductCategory, ContactMessage
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.html import format_html


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    search_fields = ('name',)
    #list_filter = ('category', 'product_category')

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date')
    search_fields = ('title',)

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display  = ('fname', 'email', 'subject', 'status_badge', 'created_at')
    list_filter   = ('status',)
    search_fields = ('fname', 'email', 'subject', 'message')
    readonly_fields = ('fname', 'email', 'phone', 'subject', 'message', 'created_at')

    fieldsets = (
        ('Thông tin khách hàng', {
            'fields': ('fname', 'email', 'phone', 'subject', 'message', 'created_at')
        }),
        ('Phản hồi', {
            'fields': ('status', 'reply_text')
        }),
    )

    # Badge màu theo trạng thái
    def status_badge(self, obj):
        colors = {'new': '#cc7a6f', 'replied': '#2e7d32', 'closed': '#888'}
        labels = {'new': 'Mới', 'replied': 'Đã phản hồi', 'closed': 'Đóng'}
        color = colors.get(obj.status, '#888')
        label = labels.get(obj.status, obj.status)
        return format_html(
            '<span style="background:{};color:#fff;padding:2px 10px;'
            'border-radius:12px;font-size:12px">{}</span>',
            color, label
        )
    status_badge.short_description = 'Trạng thái'

    # Nút gửi email phản hồi
    def save_model(self, request, obj, form, change):
        if obj.reply_text and obj.status != 'replied':
            send_mail(
                subject=f'NÓTE phản hồi: {obj.subject or "Tin nhắn của bạn"}',
                message=obj.reply_text,
                from_email='hello@note.vn',        # ← email gửi đi
                recipient_list=[obj.email],
                fail_silently=False,
            )
            obj.status     = 'replied'
            obj.replied_at = timezone.now()
        super().save_model(request, obj, form, change)

admin.site.register(Visitor) 

