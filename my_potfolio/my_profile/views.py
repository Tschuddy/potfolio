from django.shortcuts import redirect, render
from django.views import View
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib import messages




# Create your views here.
class HomepageView(View):
    def get(self, request):
        return render(request, 'blog/index.html')

class PortfolioView(View):
    def get(self, request):
        return render(request, 'blog/portfolio-details.html')
    
class ServiceView(View):
    def get(self, request):
        return render(request, 'blog/service-details.html')
    
# class StarterView(View):
#     def get(self, request):
#         return render(request, 'blog/starter-page.html')

#Added QuitView (Fix)
class QuitView(View):
    def get(self, request):
        return render(request, 'blog/quit.html')  # Make sure quit.html exists

    
    def quit_view(request):
        return render(request, "blog/quit.html")
    



class SoftView(View):
    def get(self, request):
        return render(request, 'blog/software.html')
    
class ProductView(View):
    def get(self, request):
        return render(request, 'blog/product.html')
    
class CyberView(View):
    def get(self, request):
        return render(request, 'blog/cyber.html')
    
class ComputerView(View):
    def get(self, request):
        return render(request, 'blog/computer.html')
    


class MessageView(View):
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_content = request.POST.get('message')  # Renamed to avoid conflict
        
        try:
            # Process the form data
            send_mail(
                f"New Contact Form Submission: {subject}",
                f"From: {name} <{email}>\n\n{message_content}",
                email,
                ['skynetworks.inc@gmail.com'],
                fail_silently=False,
            )
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            else:
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('#contact')
                
        except Exception as e:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'error': str(e)}, status=400)
            else:
                messages.error(request, f'Error sending message: {str(e)}')
                return redirect('#contact')

    def get(self, request):
        """Handle GET requests if needed"""
        return render(request, 'blog/index.html')



