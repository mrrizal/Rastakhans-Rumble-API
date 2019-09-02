import random
from api.models import Card
from api.serializers import CardSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class CardViewSet(ViewSet):
    serializer_class = CardSerializer

    def list(self, request, *args, **kwargs):
        if 'player_class' not in request.query_params:
            return Response([])

        cards = Card.objects(
            __raw__={
                '$or': [{
                    'playerClass': request.query_params['player_class']
                }, {
                    'playerClass': 'Neutral'
                }]
            })

        result = []

        for card in cards:
            result.append({
                'dbf_id': card['dbfId'],
                'name': card['name'],
                'player_class': card['playerClass']
            })

        random.shuffle(result)
        result = result[0:30]
        return Response(result)
