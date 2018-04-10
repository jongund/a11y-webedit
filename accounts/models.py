from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=160)

    class Meta:
        ordering = ['user']
        unique_together = ('user', 'slug')

    def __str__(self):
        return self.slug + ' (' + str(self.user) + ')'

    def save(self, **kwargs):
        self.slug = self.user.username.replace('@', '_at_').replace('.', '_dot_').replace('+', '_plus_')
        print('SLUG: ' + self.slug)
        super(Profile, self).save(**kwargs)  # Call real save

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
