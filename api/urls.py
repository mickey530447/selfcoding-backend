from django.urls import path, include
from .views import UserViewSet, ProblemViewSet, SolveStatusViewSet, TopicViewSet, ChallengeViewSet, EnrolmentViewSet, ClassViewSet, LoginViewSet, ParticipantViewSet
from rest_framework.routers import DefaultRouter
from . import views
from django.conf.urls import url

router = DefaultRouter()

# router.register('roles',RoleViewSet,basename='roles')
router.register('users',UserViewSet,basename='users')
router.register('problems',ProblemViewSet,basename='problems')
router.register('solvestatus',SolveStatusViewSet,basename='solvestatus')
router.register('topics',TopicViewSet,basename='topics')
router.register('challenges',ChallengeViewSet,basename='challenges')
router.register('classes',ClassViewSet,basename='classes')
router.register('enrollments',EnrolmentViewSet,basename='enrollments')
router.register('login',LoginViewSet, basename='login')
router.register('participant',ParticipantViewSet, basename='participant')


urlpatterns = [
    path('',include(router.urls)),
    url(r'^getuserbyemail$', views.get_user_by_email),
    url(r'^getallsolveprob$', views.get_all_solved_status),
    url(r'^gettopicsparams$', views.get_topics_by_params),
]
