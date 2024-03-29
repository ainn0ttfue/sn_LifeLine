from django.urls import path

import communityapp.views as communityapp

app_name = 'communityapp'

urlpatterns = [
    path('', communityapp.CommunitiesListView.as_view(), name='main'),
    path('create/', communityapp.CreateCommunityView.as_view(), name='create'),
    path('update/<pk>/', communityapp.CommunityUpdateView.as_view(), name='update'),
    path('delete/<pk>/', communityapp.CommunityDeleteView.as_view(), name='delete'),
    path('subscribe/<pk>/', communityapp.subscribe_community, name='subscribe'),
    path('change_publisher/', communityapp.change_publisher, name='change_publisher'),
    path('<pk>/publishers/', communityapp.CommunityModeratorsView.as_view(), name='publishers'),
    path('<pk>/add_news/', communityapp.CreateCommunityNews.as_view(), name='add_news'),
    path('<pk>/', communityapp.CommunityDetailView.as_view(), name='detail'),
]
