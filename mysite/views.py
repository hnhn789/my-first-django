from random import randint

from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.http import HttpResponse
import pytz
from datetime import datetime

import time
import datetime
from random import randint

import account.views
from .forms import SignupForm
from .models import UserProfile, ItemList, BoughtItems, QRCodeRecord, QRcodeStatus, QRcodeList, BoughtRecord
#from .serializers import StoryPointSerializer

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

'''
class StoryListView(ListView):
    template_name = "storyboard.html"
    model = Story

    def get_context_data(self, **kwargs):
        context = super(StoryListView, self).get_context_data(**kwargs)
        return context
'''

class ShopListView(ListView):
    template_name = "shop.html"
    model = ItemList
    def get_context_data(self, **kwargs):
        context = super(ShopListView, self).get_context_data(**kwargs)
        return context


class BuyItem(APIView):

    #
    # def get(self, request, uid, item_id):
    #     #uid = 'uid'
    #     #item_id = 'item_id'
    #     self.save_to_user(uid, item_id)
    #     #return HttpResponse('result')
    #
    # def update_item(self, item_id):
    #     item = ItemList.objects.get(pk=item_id)
    #     item.remain -= 1
    #     item.save()
    #
    # def save_to_user(self, uid, item_id):
    #     item = ItemList.objects.get(pk=item_id)
    #     if item.remain >= 1:
    #         self.update_item(item_id)
    #         buyer = UserProfile.objects.get(pk=uid)
    #         boughtitem = BoughtItems.objects.filter(item_name=item_id)
    #
    #         if boughtitem.filter(user=buyer).exists():
    #             bought_item_record = boughtitem.get(user=buyer)
    #             #return HttpResponse('222')
    #         else:
    #             bought_item_record = BoughtItems(item_name=item_id, user=buyer)
    #             #return HttpResponse('111')
    #
    #         bought_item_record.item_quantity += 1
    #         bought_item_record.save()
    #         a = BoughtRecord(user=buyer, item_name=item_id)
    #         a.save()
    #         buyer.usable_points -= item.price
    #         buyer.save()
    #         return HttpResponse('success') #return Response(status=status.HTTP_200_OK)  ##TODO proper response
    #     else:
    #         return HttpResponse('not enough item') #return Response(status=status.HTTP_409_CONFLICT) #TODO proper response
    def get(self, request, uid, item_id):
        if (ItemList.objects.filter(pk=item_id).exists()):
            if (UserProfile.objects.filter(pk=uid).exists()):
                item = ItemList.objects.get(pk=item_id)
                if item.remain >= 1:
                    self.update_item(item_id)
                    self.save_to_user(uid, item_id)
                    return HttpResponse('success')  # return Response(status=status.HTTP_200_OK)  ##TODO proper response
                else:
                    return HttpResponse('not enough item')  # return Response(status=status.HTTP_409_CONFLICT) #TODO proper response
            else:
                return HttpResponse('user not exist')
        else:
            return HttpResponse('item not exist')


    def update_item(self, item_id):
        item = ItemList.objects.get(pk=item_id)
        item.remain -= 1
        item.save()


    def save_to_user(self, uid, item_id):
        buyer = UserProfile.objects.get(pk=uid)
        boughtitem = BoughtItems.objects.filter(item_name=item_id)

        if boughtitem.filter(user=buyer).exists():
            bought_item_record = boughtitem.get(user=buyer)
        else:
            bought_item_record = BoughtItems(item_name=item_id, user=buyer)

        bought_item_record.item_quantity += 1
        bought_item_record.save()
        a = BoughtRecord(user=buyer, item_name=item_id)
        a.save()
        item = ItemList.objects.get(pk=item_id)
        buyer.usable_points -= item.price
        buyer.save()

class QRCode(APIView):

    def get(self, request, uid, qrcode):
        if (QRcodeList.objects.filter(code_content=qrcode).exists()):
            QRcode_status_data = self.got_correct_code(uid, qrcode)
            old_time = QRcode_status_data.last_read
            now = datetime.datetime.now(pytz.utc)
            time_delta = now - old_time
            if (time_delta.seconds >= 60):  # TODO QRcode cold down set here
                QRcode_status_data.last_read = datetime.datetime.now()
                QRcode_status_data.save()
                point_recieved = randint(10, 50)  # point range set here
                user = UserProfile.objects.get(pk=uid)
                user.usable_points += point_recieved
                user.save()
                a = QRCodeRecord(code_content=qrcode, user=user)
                a.save()
                return HttpResponse('successfully got points')  # TODO proper response
            else:
                return HttpResponse('not cold down yet')
        else:
            return HttpResponse('code nonexist')  #TODO proper response

    def got_correct_code(self, uid, qrcode):
        user = UserProfile.objects.get(pk=uid)
        QRcode_check_slug_list = QRcodeStatus.objects.filter(user=user)
        if QRcode_check_slug_list.filter(code=qrcode).exists():
            QRcode_status_data = QRcode_check_slug_list.get(code=qrcode)
        else:
            QRcode_status_data = QRcodeStatus(code=qrcode, user=user)
        return QRcode_status_data


'''
    # def aware_time_into_naive(self, time):
    #     est = pytz.timezone('Asia/Singapore')
    #     time.astimezone(est).replace(tzinfo=None)
'''


'''
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
        return render(request, 'storypoints.html', serializer.data)

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

'''





