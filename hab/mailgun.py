from flask import current_app, render_template
import requests


def send_emails(form):
    if form.email.data:
        requests.post(
            '%s/messages' % current_app.config['MAILGUN_URL'],
            auth=('api', current_app.config['MAILGUN_API_KEY']),
            data={
                'from': 'Helen and Billy <thecouple@helenandbilly.co.uk>',
                'to': form.email.data,
                'subject': 'RSVP Confirmation',
                'text': render_template(
                    'emails/rsvp_confirmation.txt', form=form)})
    requests.post(
        '%s/messages' % current_app.config['MAILGUN_URL'],
        auth=('api', current_app.config['MAILGUN_API_KEY']),
        data={
            'from': 'RSVP Bot <rsvpbot@helenandbilly.co.uk>',
            'to': 'thecouple@helenandbilly.co.uk',
            'subject': 'You Got an RSVP',
            'text': render_template(
                'emails/rsvp_forward.txt', form=form)})
