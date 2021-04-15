from django.urls import path, include
from .views import UserViewSet, ProblemViewSet, SolveStatusViewSet, TopicViewSet, ChallengeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register('roles',RoleViewSet,basename='roles')
router.register('users',UserViewSet,basename='users')
router.register('problems',ProblemViewSet,basename='problems')
router.register('solvestatus',SolveStatusViewSet,basename='solvestatus')
router.register('topics',TopicViewSet,basename='topics')
router.register('challenges',ChallengeViewSet,basename='challenges')


urlpatterns = [
    path('',include(router.urls)),
]
