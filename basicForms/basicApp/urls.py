from django.urls import path
from . import views

app_name = 'basicApp'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('form/', views.form_name_view, name = 'form_name'),
    # path('<int:question_id>/', views.detail, name = 'detail'),
    # path('<int:question_id>/results/', views.results, name = 'results'),
    # path('<int:question_id>/vote/', views.vote, name = 'vote'),

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]