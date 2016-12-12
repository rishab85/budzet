from django.conf.urls import url
from budgetCat import views

urlpatterns = [
    url(r'^category/$', views.budgetC.as_view()),
    url(r'^category/(?P<pk>[0-9]+)/$', views.budgetCDetail.as_view()),
]