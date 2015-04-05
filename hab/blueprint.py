from flask import Blueprint, render_template, redirect, url_for

from hab import mailgun
from hab.forms import RSVPDayForm, RSVPEveningForm

bp = Blueprint('bp', __name__, template_folder='templates')


@bp.route('/')
def home():
    return render_template('home.html')


@bp.route('/reply/')
def reply():
    return render_template('reply.html')


@bp.route('/reply/day/', methods=['GET', 'POST'])
def reply_day():
    form = RSVPDayForm()
    if form.validate_on_submit():
        mailgun.send_emails(form)
        return redirect(url_for('bp.home'))
    return render_template('reply_day.html', form=form)


@bp.route('/reply/evening/', methods=['GET', 'POST'])
def reply_evening():
    form = RSVPEveningForm()
    if form.validate_on_submit():
        mailgun.send_emails(form)
        return redirect(url_for('bp.home'))
    return render_template('reply_evening.html', form=form)


@bp.route('/venue/')
def venue():
    return render_template('venue.html')


@bp.route('/runningorder/')
def runningorder():
    return render_template('runningorder.html')
