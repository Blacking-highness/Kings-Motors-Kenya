# from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from allauth.account.signals import user_signed_up
# from django.dispatch import receiver

# from django.contrib.auth.models import User
# from store.models import Customer


# @receiver(post_save, sender=User)
# def create_or_save_user_profile(sender, created, instance, **kwargs):
# 	if created:
# 		#Customer.objects.create(user=instance)
# 		#customer = Customer.objects.create(name=sender.username, email=sender.email)
# 		Customer.objects.create(name=sender.username, email=sender.email)

# 	#instance.customer.save()