from django.contrib import sitemaps
from django.urls import reverse

from .models import Profile


class HomeSitemap(sitemaps.Sitemap):
    priority = 0.4
    changefreq = 'monthly'

    def items(self):
        return ['profiles:home']

    def location(self, item):
        return reverse(item)


class FaqSitemap(sitemaps.Sitemap):
    priority = 0.4
    changefreq = 'yearly'

    def items(self):
        return ['profiles:faq']

    def location(self, item):
        return reverse(item)


class AboutSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'yearly'

    def items(self):
        return ['profiles:about']

    def location(self, item):
        return reverse(item)


class ListSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return ['profiles:index']

    def location(self, item):
        return reverse(item)


class ProfilesSitemap(sitemaps.Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return Profile.objects.all()

    def lastmod(self, obj):
        return obj.last_updated
