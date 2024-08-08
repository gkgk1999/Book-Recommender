from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import BookRecommendation, Like, Comment
from .serializers import BookRecommendationSerializer, LikeSerializer, CommentSerializer
from django.shortcuts import render,redirect
import requests
from django.conf import settings
from django.http import JsonResponse
GOOGLE_BOOKS_API_URL = 'https://www.googleapis.com/books/v1/volumes'
class BookRecommendationViewSet(viewsets.ModelViewSet):
    queryset = BookRecommendation.objects.all()
    serializer_class = BookRecommendationSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['genre', 'rating', 'publication_date']
    ordering_fields = ['rating', 'publication_date']

    def create(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

@api_view(['POST'])
def like_recommendation(request, pk):
    try:
        recommendation = BookRecommendation.objects.get(pk=pk)
    except BookRecommendation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    like, created = Like.objects.get_or_create(user=request.user, recommendation=recommendation)
    if not created:
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
def add_comment(request, pk):
    try:
        recommendation = BookRecommendation.objects.get(pk=pk)
    except BookRecommendation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = request.data
    data['user'] = request.user.id
    data['recommendation'] = pk
    serializer = CommentSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

def search_books(request):
    query = request.GET.get('query', '')
    if not query:
        return JsonResponse({'error': 'Query parameter is required'}, status=400)
    
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={settings.GOOGLE_BOOKS_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return JsonResponse({'error': 'Failed to fetch data from Google Books API'}, status=response.status_code)

    return JsonResponse(data)


def index(request):
    return render(request, 'index.html')


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import BookRecommendation

@csrf_exempt
def recommendations(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            author = data.get('author')
            description = data.get('description')
            cover_image = data.get('cover_image')
            genre = data.get('genre')
            rating = data.get('rating')
            publication_date = data.get('publication_date')

            if not all([title, author, description, cover_image, genre, rating, publication_date]):
                return JsonResponse({'error': 'Missing fields'}, status=400)

            recommendation = Recommendation.objects.create(
                title=title,
                author=author,
                description=description,
                cover_image=cover_image,
                genre=genre,
                rating=rating,
                publication_date=publication_date
            )
            return JsonResponse({'status': 'success'}, status=201)
        except Exception as e:
            print(e)  # Log any errors
            return JsonResponse({'error': str(e)}, status=400)
