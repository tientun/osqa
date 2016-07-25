from django.template import loader, Context, Template

def send_template_message(template, context):
    return loader.render_to_string(template, Context(context))
