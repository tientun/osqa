import os
import re
import datetime
import logging
from forum.models import User, Question, Comment, QuestionSubscription, SubscriptionSettings, Answer
from django.utils.translation import ugettext as _
from forum.actions import AskAction, AnswerAction, CommentAction, AcceptAnswerAction, UserJoinsAction, QuestionViewAction
import settings
from send import send_template_message
from forum import settings as fsettings
from django.db.models import Q, F
import urllib, urllib2, cookielib

def question_posted(action, new):
    question = action.node

    slack_hook_url = settings.SLACK_HOOK
    question_url = fsettings.APP_URL + question.get_absolute_url()
    data = send_template_message("modules/slackhook/new_question.json",{'answer': question, 'app_name': fsettings.APP_SHORT_NAME, 'url':question_url})
    if slack_hook_url:
        values = dict(payload=data)
        data = urllib.urlencode(values)
        req = urllib2.Request(slack_hook_url, data)
        rsp = urllib2.urlopen(req)
        content = rsp.read()

AskAction.hook(question_posted)

def answer_posted(action, new):
    answer = action.node
   
    slack_hook_url = settings.SLACK_HOOK
    question_url = fsettings.APP_URL + answer.question.get_absolute_url()
    data = send_template_message("modules/slackhook/new_answer.json",{'answer': answer, 'app_name': fsettings.APP_SHORT_NAME, 'url':question_url})
    if slack_hook_url:
        values = dict(payload=data)
        data = urllib.urlencode(values)
        req = urllib2.Request(slack_hook_url, data)
        rsp = urllib2.urlopen(req)
        content = rsp.read()

AnswerAction.hook(answer_posted)

def answer_accepted(action, new):
    question = action.node.question

    slack_hook_url = settings.SLACK_HOOK
    question_url = fsettings.APP_URL + question.get_absolute_url()
    data = send_template_message("modules/slackhook/answer_accepted.json",{'answer': action.node, 'app_name': fsettings.APP_SHORT_NAME, 'url':question_url})
    if slack_hook_url:
        values = dict(payload=data)
        data = urllib.urlencode(values)
        req = urllib2.Request(slack_hook_url, data)
        rsp = urllib2.urlopen(req)
        content = rsp.read()

AcceptAnswerAction.hook(answer_accepted)