# from celery import shared_task
# from datetime import timedelta
# from django.conf import settings
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.utils import timezone
# from news.models import Post
#
# @shared_task
# def send_email_task(pk):
#     post = Post.objects.get(pk=pk)
#     categories = post.post_category.all()
#     title = post.post_title()
#     subscribers_emails = []
#     for category in categories:
#         subscribers_users = category.subscribers.all()
#         for sub_user in subscribers_users:
#             subscribers_emails.append(sub_user.email)
#     html_content = render_to_string(
#         'file.html'
#         (
#             'text': f'{post.post.title}',
#             'link': f'{settings.SITE_URL}/news/{pk}'
#         )
#     )
#
#     msg = EmailMultiAlternatives(
#         subject='title',
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers
#     )
#
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()
#
# @shared_task
# def weekly_newsletter():
#     last_week = timezone.now() - timedelta(days=7)
#     posts = Post.objects.filter(time_in__gte=last_week)
#     categories = set(posts.values_list('category__id', flat=True))
#     subscribers = set(Subscription.objects.filter(category__id__in=categories).values_list('user__email', flat=True))
#
#     html_content = render_to_string(
#         'weekly_posts.html',
#         {
#             'link': f'http://127.0.0.1:8000/',
#             'posts': posts
#         }
#     )
#
#     msg = EmailMultiAlternatives(
#         subject='Посты за неделю',
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers
#     )
#
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()
#
