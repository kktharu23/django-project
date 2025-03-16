from django.urls import path
from .views import view1, view2

urlpatterns = [
    path('view1/', view1, name='viratkohli_view1'),
    path('view2/', view2, name='viratkohli_view2'),
]