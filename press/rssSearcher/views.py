from django.shortcuts import render
from django.http import HttpResponse
from rssSearcher.models import Feed,Item
import feedparser
# feed : http://www.theguardian.com/world/rss
def home(request):
	context_dict = {}
	source = feedparser.parse('http://www.theguardian.com/world/rss')
	subject = source['feed']['title']
	feed, _ = Feed.objects.get_or_create(subject=subject, link='http://www.theguardian.com/world/rss')
	for i in range(0,len(source['entries'])):
		print i
		print source.entries[i]['title']
		item, flag = Item.objects.get_or_create(feed=feed,title=source.entries[i]['title'], link=source.entries[i]['link'], description=source.entries[i]['description'])
	items = Item.objects.filter(feed = feed)
	context_dict['items'] = items
	return render(request, 'rssSearcher/home.html', context_dict)