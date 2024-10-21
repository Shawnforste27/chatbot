from django.urls import path
from .views import chatbot_view  # Import your view

urlpatterns = [
    path("", chatbot_view, name="chatbot"),  # Add the route for the chatbot view
]
