# movies/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 1. 전체 영화 목록 조회
    path('movies/', views.movie_list),

    # 2. 단일 영화 조회 
    path('movies/<int:movie_pk>/', views.movie_detail),

    # 3. 전체 장르 목록 조회 
    path('genres/', views.genre_list),

    # 4. 전체 리뷰 목록 조회 (본인)
    path('reviews/', views.review_list),
    
    # 5. 단일 리뷰 조회 & 수정 & 삭제 
    path('reviews/<int:review_pk>/', views.review_detail),

    # 6. 특정 영화에 대한 리뷰 생성
    path('movies/<int:movie_pk>/reviews/', views.review_create),
]