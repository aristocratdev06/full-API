from django.urls import path
from .views import (
    home,
    krasovkaMakeApi,
    singleapi,
    PostJoylash,
    PostYangilash,
    PostDelete,
    postSearch,
    FilterPost,
    FilterBazm
)

app_name ="api"

urlpatterns = [
    path('', home, name="home"),
    path('new-api/', krasovkaMakeApi),
    path('new-api/<int:pk>/', singleapi),
    path("new-post/", PostJoylash, name="new_post"),
    path("update-post/<int:pk>",PostYangilash, name="new_post"),
    path("delete/<int:pk>/", PostDelete, name="delete"),
    path('search/', postSearch, name="post_search"),
    path("filter-sport/", FilterPost),
    path("filter-bazm/", FilterBazm)
]
