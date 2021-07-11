from django.urls import path
from .views import UserList, UserDetail, PostList, PostDetail # new
from rest_framework.routers import SimpleRouter

router = SimpleRouter()


router.register('users', UserList, basename='users')
# router.register('users/<int:pk>/', UserDetail, basename='users') # new
# router.register('', PostList)
# router.register('<int:pk>/', PostDetail)

# urlpatterns = [
#     path('users/', UserList.as_view()),  # new
#     path('users/<int:pk>/', UserDetail.as_view()),  # new
#     path('', PostList.as_view()),
#     path('<int:pk>/', PostDetail.as_view()),
# ]


urlpatterns = router.urls
