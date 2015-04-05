from flask.ext.wtf import Form
from wtforms import TextField, RadioField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Optional, Email


class RSVPEveningForm(Form):
    name = TextField(
        u'Your Name', validators=[DataRequired()],
        description=u'You can reply individually, or as a group')
    email = TextField(
        u'Your Email', validators=[Optional(), Email()],
        description=u'If you leave an email address we\'ll send you a confirmation of your RSVP')
    response = RadioField(
        u'I/We...',
        choices=[
            (u'accept', u'would be delighted to accept'),
            (u'decline', u'must unfortunately decline')])
    song = BooleanField(u'Perform a Song')

    def fields(self):
        return [
            self.name,
            self.email,
            self.response,
            self.song
        ]


class RSVPDayForm(RSVPEveningForm):
    diet = TextAreaField(
        u'Your Dietry Requirements',
        description='Please use this space to tell us if you\'re vegetarian or if you have any allergies.')
    speech = BooleanField(u'Make a Speech')
    mehndi = BooleanField(u'Attend Helen\'s Mehndi Party')

    def fields(self):
        return [
            self.name,
            self.email,
            self.response,
            self.speech,
            self.song,
            self.mehndi,
            self.diet
        ]
