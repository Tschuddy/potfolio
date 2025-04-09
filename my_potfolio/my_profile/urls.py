from django.urls import path
from .views import HomepageView, PortfolioView, ServiceView, QuitView, ComputerView, CyberView, ProductView, SoftView, MessageView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),  # Home Page
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),  # Portfolio Page
    path('service/', ServiceView.as_view(), name='service'),  # Service Page
    # path('starter/', StarterView.as_view(), name='starter'),  # Starter Page
    path('quit/', QuitView.as_view(), name='quit'),  # ✅ Quit Page (Fixed)
    path('software/', SoftView.as_view(), name='software'),  # software Page
    path('product/', ProductView.as_view(), name='product'),  # product Page
    path('cyber/', CyberView.as_view(), name='cyber'),  # cybersecurity Page
    path('computer/', ComputerView.as_view(), name='computer'),  # computer Page
    path('contact/message/', MessageView.as_view(), name='message'),  # message Page
]
