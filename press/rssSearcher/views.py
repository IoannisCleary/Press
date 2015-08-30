from django.shortcuts import render
from django.http import HttpResponse
from rssSearcher.models import Feed,Item
import feedparser
import time
# feed : http://www.theguardian.com/world/rss
def home(request):
	context_dict = {}
	source = feedparser.parse('http://www.theguardian.com/world/rss')
	subject = source['feed']['title']
	feed, _ = Feed.objects.get_or_create(subject=subject, link='http://www.theguardian.com/world/rss')
	for i in range(0,len(source['entries'])):
		try:
			item = Item.objects.get(feed=feed,title=source.entries[i]['title'])
		except Item.DoesNotExist:
			item, flag = Item.objects.get_or_create(feed=feed,title=source.entries[i]['title'], link=source.entries[i]['link'], description=source.entries[i]['description'], dateTime=time.strftime("%H:%M %d/%m/%Y", source.entries[i].date_parsed))

	items = Item.objects.filter(feed = feed)
	context_dict['items'] = items
	context_dict['subject'] = subject
	if request.method == 'GET': # If the form is submitted
		search_query = request.GET.get('search_box', None)
		print "User searched"
		print search_query
		if search_query != None:
			return results(request, search_query)
	return render(request, 'rssSearcher/home.html', context_dict)
def results(request,query_search):
	context_dict = {}
	source = feedparser.parse('http://www.theguardian.com/world/rss')
	subject = source['feed']['title']
	feed, _ = Feed.objects.get_or_create(subject=subject, link='http://www.theguardian.com/world/rss')
	items = Item.objects.filter(feed = feed, title__contains=query_search)
	context_dict['items'] = items
	context_dict['subject'] = subject
	context_dict['term'] = query_search
	return render(request, 'rssSearcher/list.html', context_dict)