# import os
# from django.contrib.auth.models import User, Group
# from django.shortcuts import render
# from django.http import HttpResponse
# from config import settings




# def index(request):
#     try:
#         with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
#             return HttpResponse(f.read())
#     except FileNotFoundError:
#         return HttpResponse(
#             """
#             Please build the front-end using cd frontend && npm install && npm run build 
#             """,
#             status=501,
#         )