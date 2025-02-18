from django.urls import path
from .views import chatbot_view, get_chatbot_response

urlpatterns = [
    path('', chatbot_view, name='chatbot_home'),
    path('get_response/', get_chatbot_response, name='get_chatbot_response'),
]
