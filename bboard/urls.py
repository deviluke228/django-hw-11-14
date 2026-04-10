from django.urls import path
from bboard.views import (
    index, by_rubric, BbCreateView,
    select_columns, exclude_values,
    bb_list, bb_detail, bb_delete,
    UserListView, UserDetailView,
    tags_demo,     IceCreamListView,
    IceCreamCreateView,
    IceCreamUpdateView,
    IceCreamDeleteView,
)

urlpatterns = [
    path('', index, name='index'),

    # объявления
    path('add/', BbCreateView.as_view(), name='add'),
    path('bb/<int:id>/', bb_detail, name='bb_detail'),
    path('bb/<int:id>/delete/', bb_delete, name='bb_delete'),

    # рубрики
    path('rubric/<int:rubric_id>/', by_rubric, name='by_rubric'),

    # выборки
    path('select/', select_columns, name='select_columns'),
    path('exclude/', exclude_values, name='exclude_values'),

    # пользователи
    path('users/', UserListView.as_view(), name='users_list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),

    path('tags/', tags_demo, name='tags_demo'),
    path('icecream/add/', IceCreamCreateView.as_view(), name='icecream_add'),
    path('icecream/<int:pk>/edit/', IceCreamUpdateView.as_view(), name='icecream_edit'),
    path('icecream/<int:pk>/delete/', IceCreamDeleteView.as_view(), name='icecream_delete'),
    path('icecream/', IceCreamListView.as_view(), name='icecream_list'),


]