from django.apps import AppConfig
from flask import Flask, render_template

app = Flask(__name__)

# Bosh sahifa
@app.route('/')
def home():
    return "Bosh sahifa!"

# O'ylangan sahifa yo'qligi uchun 404 xatosi
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
