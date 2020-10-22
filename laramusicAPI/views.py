# Django
from users.models import User

# Rest_framework
from rest_framework import viewsets, mixins
from rest_framework import permissions

# LaramusicAPI
#from laramusicAPI.models import Profile
#from laramusicAPI.serializers import ProfileSerializer, UserSerializer


"""class UserViewSet(viewsets.ModelViewSet):
    
    API endpoint that allows users to be viewed or edited.
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet, mixins.UpdateModelMixin):
    
    API endpoint that allows profiles to be viewed or edited.
    
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
"""