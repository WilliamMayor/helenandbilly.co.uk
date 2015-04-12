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

    def __repr__(self):
        return u'<RSVP Evening from:%s email:%s response:%s song:%s>' % (
            self.name.data,
            self.email.data or 'Unknown',
            'Yes' if self.response.data else 'No',
            'Yes' if self.song.data else 'No')


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

    def __repr__(self):
        return u'<RSVP Day from:%s email:%s response:%s song:%s speech:%s mehndi:%s>%s</RSVP>' % (
            self.name.data,
            self.email.data or 'Unknown',
            'Yes' if self.response.data else 'No',
            'Yes' if self.song.data else 'No',
            'Yes' if self.speech.data else 'No',
            'Yes' if self.mehndi.data else 'No',
            self.diet.data)
