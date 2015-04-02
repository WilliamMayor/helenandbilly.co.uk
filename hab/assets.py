from flask.ext.assets import Environment, Bundle

assets = Environment()

css = Bundle(
    'css/main.scss',
    filters='scss,cssmin',
    output='main.min.css',
    depends=['css/*.scss', 'css/*/*.scss'])
assets.register('css', css)

js = Bundle(
    'js/vendor/jquery-1.11.2.min.js',
    Bundle(
        'js/hab.js',
        filters='rjsmin',
        depends=['js/*.js', 'js/*/*.js']),
    output='main.min.js')
assets.register('js', js)


def init_app(app):
    assets.init_app(app)
