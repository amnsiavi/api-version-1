from django.urls import path


from watch_list.api.views import (
    WatchListAV,
    WatchListDetailAV,
    StreamPlatformListAV,
    StreamPlatformDetailAV,
    ReviewListAV,
    ReviewDetail
)

urlpatterns = [
    
    # URL Patterns For WatchList
    path('list/',WatchListAV.as_view(),name='watch_list'),
    path('<int:pk>/',WatchListDetailAV.as_view(),name='watch_list_details'),
    
    # URL Patterns FOR StreamPlatform
    path('stream-platform/list', StreamPlatformListAV.as_view(),name='stream_platform_list'),
    path('stream-platform/<int:pk>',StreamPlatformDetailAV.as_view(),name='stream_platform_detail'),
    
    # URL Patterns FOR Reviews
    path('review/list',ReviewListAV.as_view(),name='review_list'),
    path('review/<int:pk>', ReviewDetail.as_view(),name='review_details')
    
    


]

