import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuestSerializer, PendingBanSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Item
from toast_auth.models import User


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def new_item(request):
    print(request.data)
    Item.objects.create(name = request.data['name'], prep = request.data['prep'])
    return Response("added Item")

from .models import Quest, Item, PendingBan
from registry.models import Log
import random

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def quests_data(request):
    quests = Quest.objects.all().filter(killer=request.user)

    while quests.count() < 3:
        rand_item = random.choices(Item.objects.all(), [1/item["frequency"] for item in Item.objects.values("frequency")], k=1)[0]
        rand_item.frequency += 1
        rand_item.save()
        already_victim_names = [quest.victim.username for quest in quests]
        victim_user = random.choice(User.objects.exclude(username__in=already_victim_names).exclude(username=request.user.username))
        Quest.objects.create(item=rand_item, killer=request.user, victim=victim_user)
        quests = Quest.objects.filter(killer=request.user)
    
    serializer = QuestSerializer(quests, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def ban_data(request):

    bans = PendingBan.objects.exclude(id__in=json.loads(request.user.voted_bans))
    serializer = PendingBanSerializer(bans, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def killval_data(request):
    quests = Quest.objects.filter(victim=request.user).filter(await_valid=True)
    serializer = QuestSerializer(quests, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def killval_submit(request):
    quest = Quest.objects.get(id=request.data['quest_id'])
    if (request.data['valid']):
        new_log = Log.objects.create(item=quest.item,
                                     killer=quest.killer,
                                     victim=quest.victim,
                                     message=quest.killer.username + " hat " + quest.victim.username + " mit " + quest.item.prep + quest.item.name + quest.verb.pastpart,
                                     distance=10)  # TODO
        new_log.save()
        quest.delete()
        return Response("kill validated")
    else:
        quest.pending_valid = False
        quest.save()
        return Response("kill prevented")