import datetime
from rest_framework import response
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from rest_framework import status
from random import randint
from django.db.models import Q

from select_learn.models import UserSentence, UserWord
from .serializers import UserSentenceSerializer, UserWordSerializer

from users.models import UserMeta
from users.api.serializers import UserMetaSerializer

from datetime import datetime
from datetime import timedelta, timezone

import pprint

import json
from functools import lru_cache

import requests
import select_learn.english_vocabulary as english_vocabulary


class UserWordsAll(APIView):

    def get(self, request):
        user_id = request.user.id
        sql_str = f"""select * from public.select_learn_userword
        where ('2.72'::real ^ -((SELECT EXTRACT(epoch FROM  (now() - updated_at::timestamptz)))/3600::real / strength)) < 0.5
        and user_id = {user_id} limit 20;"""
        words = UserWord.objects.raw(sql_str)
        # print(words)
        words = UserWordSerializer(words, many=True).data

        # parse definitions
        for i in range(len(words)):
            word = words[i]['word']
            words[i]['definition'] = english_vocabulary.get_definition(word)

        sentences_ids = set([item['sentence_id'] for item in words])
        sentences = []
        for sentence_id in sentences_ids:
            sentence = UserSentence.objects.filter(sentence_id=sentence_id)[0]
            sentences.append(sentence)
        # print(sentences)
        sentences = UserSentenceSerializer(sentences, many=True).data

        cards = []
        mapped_sentences = {}
        for sent in sentences:
            mapped_sentences[sent['sentence_id']] = sent['sentence_text']

        for word in words:
            card = {}
            sentence = str(mapped_sentences[word['sentence_id']])
            card['sentence'] = sentence.replace(word['word'], "_____")
            card['word'] = word['word']
            card['strength'] = word['strength']
            card['definition'] = word['definition']
            card['pos_definition'] = english_vocabulary.get_word_POS(
                sentence, word['word'])
            card['word_id'] = word['word_id']
            cards.append(card)
        cards = cards[:2]
        return Response(cards, status=status.HTTP_200_OK)

    def put(self, request):
        print(request.data)
        response = Response(status=status.HTTP_200_OK)
        if len(request.data) > 0:
            for word in request.data:
                server_word = UserWord.objects.filter(
                    word_id=word['word_id'])[0]
                server_word.strength = word['strength']
                server_word.save()
        else:
            response = Response(status=status.HTTP_400_BAD_REQUEST)
        return response


class UserSentenceAPIView(APIView):
    def post(self, request):
        user_id = request.user.id
        # print(request.data)
        sentence = request.data['sentence']
        words = request.data['words']

        response_status = status.HTTP_200_OK
        response_message = "ok"

        if len(words) > 0 and len(sentence):
            user_sentence = {}
            user_sentence['sentence_user'] = user_id
            user_sentence['sentence_text'] = sentence
            user_sentence = UserSentenceSerializer(data=user_sentence)

            if user_sentence.is_valid():
                user_sentence.save()
                # save words
                user_sentence = user_sentence.data

                for word in words:
                    user_word = {}
                    user_word['user_id'] = user_id
                    user_word['sentence_id'] = user_sentence['sentence_id']
                    user_word['word'] = word
                    user_word = UserWordSerializer(data=user_word)

                    if user_word.is_valid():
                        user_word.save()
                    else:
                        response_message = "invalid word data"
                        response_status = status.HTTP_400_BAD_REQUEST
                        break

            else:
                response_message = "invalid sentence data"
                response_status = status.HTTP_400_BAD_REQUEST

        else:
            response_message = "zero len words or sentence"
            response_status = status.HTTP_400_BAD_REQUEST

        return Response({"message": response_message},
                        status=response_status)
