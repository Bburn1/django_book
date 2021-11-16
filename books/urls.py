from django.urls import path
from . import views

urlpatterns = [
    path("", views.BookView.as_view()),
    path("<slug:slug>/", views.BookDetailView.as_view(), name="book_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("avtor/<str:slug>/", views.AvtorView.as_view(), name="avtor_detail"),
    path("publishing/<str:slug>/", views.PublishingView.as_view(), name="publishing_detail")



]