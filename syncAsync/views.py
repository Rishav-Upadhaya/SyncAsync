from django.http import HttpResponse
import time, asyncio
from movies.models import Movie
from stories.models import Story
from asgiref.sync import sync_to_async


def get_movies():
    print('Prepare to get the movies...')
    time.sleep(2)
    qs = Movie.objects.all()
    print(qs)
    print("Got the movies")
    return qs


def get_stories():
    print('Prepare to get the stories...')
    time.sleep(5)
    qs = Story.objects.all()
    print(qs)
    print("Got the stories")
    return qs

async def get_movies_async():
    print('Prepare to get the movies...')
    await asyncio.sleep(5)
    qs = await sync_to_async(list)(Movie.objects.all())
    print(qs)
    print("Got the movies")
    return qs

async def get_stories_async():
    print('Prepare to get the stories...')
    await asyncio.sleep(2)
    qs = await sync_to_async(list)(Story.objects.all())
    print(qs)
    print("Got the stories")
    return qs

def sync_view(request):
    starttime = time.time()
    get_movies()
    get_stories()
    print(f'Total Time: {time.time()-starttime}')
    return HttpResponse("Sync View")

async def async_view(request):
    starttime = time.time()
    await asyncio.gather(
        get_movies_async(),
        get_stories_async()
    )
    print(f'Total Time: {time.time()-starttime}')
    return HttpResponse('Async View')

def main_view(request):
    return HttpResponse("Main_View")