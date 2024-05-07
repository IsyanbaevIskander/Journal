from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def get_datetime(request):
    curr_datetime = f'''<html>
                    <body bgcolor="black">
                        <h1 style="color:white">Время и дата</h1>
                        <h2 style="color:white">{datetime.today().strftime("%Y-%m-%d")}</h2>
                        <h2 style="color:white">{datetime.today().strftime("%H:%M:%S")}</h2>
                        <a style="color:blue" href="http://127.0.0.1:8000/admin">Ссылочка на Django administration</a>
                        <h1 style="color:white">Pedro</h1>
                        <div style="width: 90%" class="tenor-gif-embed" data-postid="6468110209143744316" data-share-method="host" data-aspect-ratio="1" data-width="100%"><a href="https://tenor.com/view/pedropedropedro-gif-6468110209143744316">Pedropedropedro GIF</a>from <a href="https://tenor.com/search/pedropedropedro-gifs">Pedropedropedro GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>
                    </body>
                </html>'''
    return HttpResponse(curr_datetime)
