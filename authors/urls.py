from django.urls import path

from authors.views import AuthorDetailView, AuthorListView


urlpatterns = [
    path('', AuthorListView.as_view(), name='showlist'),
    path('<int:pk>/', AuthorDetailView.as_view(), name='showdetail'),
]
