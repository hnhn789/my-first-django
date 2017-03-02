from random import randint

from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

import account.views
from .forms import SignupForm
from .models import UserProfile, Story, ItemList
from .serializers import StoryPointSerializer, SuccessSerializer, ItemSerializer
class SignupView(account.views.SignupView):

    form_class = SignupForm

    def update_profile(self, form):
        UserProfile.objects.create(
            user=self.created_user,
            real_name=form.cleaned_data["real_name"]
        )

    def after_signup(self, form):
        self.update_profile(form)
        super(SignupView, self).after_signup(form)


class StoryListView(ListView):
    template_name = "storyboard.html"
    model = Story

    def get_context_data(self, **kwargs):
        context = super(StoryListView, self).get_context_data(**kwargs)
        return context

class ShopListView(ListView):
    template_name = "shop.html"
    model = ItemList
    def get_context_data(self, **kwargs):
        context = super(ShopListView, self).get_context_data(**kwargs)
        return context

class BuyItem(APIView):
    def get_object(self, pk):
        try:
            return Story.objects.get(pk=pk)
        except Story.DoesNotExist:
            raise Http404

    def get(self, request, uid, item_id, format=None):
        # self.save_to_user(uid, item_id)
        # self.update_item(item_id)
        # return redirect("",permanent=True)
        success = TrueFalse(True)
        serializer = SuccessSerializer(success)
        return Response(serializer.data  ,status=status.HTTP_200_OK)

    def update_item(self, item_id):
        item = ItemList.objects.get(pk=item_id)
        item.remain -= 1
        item.save()

    def save_to_user(self, uid, item_id):
        item = ItemList.objects.get(pk=item_id)
        user = UserProfile.objects.get(user_id=uid)
        user.bought_items += str(item_id) + ","
        user.usable_points -= item.price
        user.save()


class GetStoryPoints(APIView):


    def get_object(self, pk):
        try:
            return Story.objects.get(pk=pk)
        except Story.DoesNotExist:
            raise Http404

    def get(self, request, uid, format=None):
        story, random_story_index = self.generate_random_stroypoints()
        self.save_to_user(story.points, uid, random_story_index)
        serializer = StoryPointSerializer(story)
        return Response(serializer.data)

    def post(self, request, uid, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def generate_random_stroypoints(self):
        random_story_index = randint(1, 3)
        story = self.get_object(random_story_index)
        story.points = randint(0, 5)
        return story, random_story_index

    def save_to_user(self, points, uid, random_story_index):
        user = UserProfile.objects.get(user_id=uid)
        user.usable_points += points
        user.history_points += points
        user.opened_story += str(random_story_index) + ", "
        user.save()


class TrueFalse():
    def __init__(self, success):
        self.success = success





