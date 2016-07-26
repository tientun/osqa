from django.conf.urls import patterns, url, include
from django.http import  HttpResponse
from django.utils.translation import ugettext as _
import settings

urlpatterns = patterns('',
    url(r'^%s%s$' % (_('admin/'), _('slackbot/')),  slackbot, name='slackbot'),
)
