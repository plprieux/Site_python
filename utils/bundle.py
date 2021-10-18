from flask_assets import Environment, Bundle
from app.app import app

bundles = {
    'base_css': Bundle(
        'vendor/bootstrap-4.5.3/css/bootstrap.min.css',
        'css/main.css',
        output='gen/base.css'),

    'base_js': Bundle(
        'vendor/jquery-3.5.1/js/jquery.min.js',
        'js/global.js',
        output='gen/base.js')
}

assets = Environment(app)
assets.register(bundles)
