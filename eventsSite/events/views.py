from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Event, Organization
from accounts.models import User

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer


class UserSerializer(serializers.ModelSerializer):
    organizations = serializers.SlugRelatedField(
        many=True,
        queryset=Organization.objects.all(),
        slug_field='name'
    )
    class Meta:
        model = User
        fields = '__all__'
        

class EventSerializer(serializers.ModelSerializer):
    #organizations = OrganizationSerializer( read_only=True, many=True)
    organization = serializers.SlugRelatedField(
        many=False,
        queryset=Organization.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Event
        fields = '__all__'
        


# class LazyEncoder(DjangoJSONEncoder):
#     def default(self, obj):
#         print('runn')
#         if isinstance(obj, Organization):
#             print(obj)
#             return serialize('json', obj)
#         return super().default(obj)


def index(request):
    serializer_event = EventSerializer(Event.objects.all(), many=True)
    serializer_user = UserSerializer(User.objects.filter(pk=request.user.id), many=True)
    #json_objects = serialize('json', Event.objects.all(), cls=LazyEncoder)
    return render(request, 'home.html', {'eventObjects': serializer_event.data,
                                         'events': Event.objects.all(),
                                         'userOrgsObjects': serializer_user.data
                                         })

