from forum.settings.base import Setting, SettingSet
from django.forms.widgets import Textarea
from django.core.urlresolvers import reverse
from forum.settings import APP_URL

SLACKBOT_SET = SettingSet('slackbot', 'Slack bot', "Set up slack bot.", 3000)

SLACK_HOOK = Setting('SLACK_HOOK',
"", SLACKBOT_SET, dict(
label = "Slack webhook URL",
help_text = """
Enter slack incomming webhook URL.
"""))