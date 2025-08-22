# movies/serializers.py
from rest_framework import serializers
from .models import Genre, Movie, Review, Cast

# Genre Serializer
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

# Movie 목록 조회를 위한 Serializer
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

# Review 기능(F05, F06)을 위한 Serializer
class ReviewSerializer(serializers.ModelSerializer):
    
    # 리뷰 조회 시 Movie의 id와 title만 포함시키기 위한 중첩 Serializer
    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title')

    # movie 필드를 위 Serializer로 설정 (읽기 전용)
    movie = MovieTitleSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

# 단일 영화 상세 정보에 포함될 Serializer들
class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = ('name', 'character', 'order')

# 영화 상세 정보에 포함될 Review 정보 (기존 ReviewSerializer와 별개)
class ReviewForMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('author', 'content', 'rating')

# 최종적으로 사용할 단일 영화 상세 정보 Serializer
class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # id를 제외한 모든 필드를 포함
        exclude = ('id',)
    # 중첩 Serializer 설정
    genres = GenreSerializer(many=True, read_only=True)
    cast_set = CastSerializer(many=True, read_only=True)
    review_set = ReviewForMovieSerializer(many=True, read_only=True)

# Review 기능을 위한 Serializer
class ReviewSerializer(serializers.ModelSerializer):
    
    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title')

    # movie 필드를 위 Serializer로 설정 (읽기 전용)
    movie = MovieTitleSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        # movie 필드는 URL을 통해 자동으로 할당되므로 읽기 전용으로 설정합니다.
        read_only_fields = ('movie',)