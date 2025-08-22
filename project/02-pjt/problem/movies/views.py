# movies/views.py
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Genre, Movie, Review
from .serializers import GenreSerializer, MovieSerializer, ReviewSerializer, MovieDetailSerializer


# F02. api/v1/genres/
@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

# F03. api/v1/movies/
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

# F04. 단일 영화 상세 조회
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

# F05. 전체 리뷰 목록 조회
@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

# F06. 단일 리뷰 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
            
    elif request.method == 'DELETE':
        review.delete()
        return Response({'delete': f'{review_pk}번 째 리뷰가 정상적으로 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
    
# F07 POST api/v1/movies/<movie_pk>/reviews/
@api_view(['POST'])
def review_create(request, movie_pk):
    # 1. URL로부터 받은 movie_pk로 영화를 조회합니다.
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    # 2. 클라이언트로부터 받은 데이터로 Serializer를 초기화합니다.
    serializer = ReviewSerializer(data=request.data)
    
    # 3. 데이터 유효성 검사를 진행합니다.
    if serializer.is_valid(raise_exception=True):
        # 4. 유효성 검사를 통과하면, movie 객체를 추가하여 저장합니다.
        # .save() 메서드에 추가 인자를 전달하면, create() 메서드로 전달됩니다.
        serializer.save(movie=movie)
        
        # 5. 생성된 리뷰 데이터를 201 Created 상태 코드와 함께 반환합니다.
        return Response(serializer.data, status=status.HTTP_201_CREATED)