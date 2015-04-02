from flask import Blueprint, render_template

bp = Blueprint('bp', __name__, template_folder='templates')


@bp.route('/')
def home():
    return render_template('home.html')


@bp.route('/reply/')
def reply():
    return render_template('reply.html')


@bp.route('/reply/day/')
def reply_day():
    return render_template('reply_day.html')


@bp.route('/reply/evening/')
def reply_evening():
    return render_template('reply_evening.html')


@bp.route('/venue/')
def venue():
    return render_template('venue.html')


@bp.route('/runningorder/')
def runningorder():
    return render_template('runningorder.html')
