from django.contrib.auth import get_user_model, logout
from django.contrib.sites.shortcuts import get_current_site
from django.db.models.query_utils import Q
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import TemplateView
from multipage_form.views import MultipageFormView
from .forms import ReportForm
from .token import account_activation_token
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SetPasswordForm, PasswordResetForm
from django.core.mail import EmailMessage

from vinanpetreport import settings


def home(request):
    return render(request, "home.html")

def logout_view(request):
    logout(request)
    return redirect('home')


class ReportView(MultipageFormView):
    template_name = 'report.html'
    form_class = ReportForm
    success_url = reverse_lazy("report_submitted")


class ReportSubmissionRemarkView(TemplateView):
    template_name = 'submitted.html'


@login_required
def password_change(request):
    user = request.user             # This get the current logged in user
    if request.method == "POST":    # This receives post method from form (registration/password_change_done.html)
        form = SetPasswordForm(user, request.POST)      # This take in the user and populate form with data user entered
        if form.is_valid():         # This checks if user entry is valid
            form.save()             # This save form to database
            messages.success(request, "Your password has been changed successfully") # This message is passed to registration/password_change_done.html through the password_change_done below
            return redirect('password_change_done')     # This is redirected to after successful login
        else:                                           # This else condition checks if form is not valid
            for error in list(form.errors.values()):    # looping through form.errors.values() -> Note: form is dictionary holding user data (dictionary name), form.errors is the dictionary key (dictionary field) and form.errors.values() is the dictionary value (actual error)
                messages.error(request, error)          # Passsing message (error being looped through above to registration/password_change_done.html through password_change redirect
                return redirect("password_change")      # Redirecting to password_change url and passing respective errors to registration/password_change_done.html
    form = SetPasswordForm(user)                        # Unbound form if request.method is not post i.e the unbound form will be rendered first when user click on reset password, then when user enters data and send, it becomes post method and bound found above is rendered.
    return render(request, 'registration/password_change_form.html', {'form': form}) # This renders the unbound form above

def password_change_done(request):
    return render(request, "registration/password_change_done.html")    # After successful password change, the password_change_done url is redirected to, hence registration/password_change_done.html is rendered with success message


# If user is not authenticated or logged in, i.e, forgotten password
def password_reset_request(request):
    if request.method == 'POST':                        # Receiving post request from form
        form = PasswordResetForm(request.POST)          # Populating form with user entry (request.POST)
        if form.is_valid():                             # Validating user entry
            user_email = form.cleaned_data['email']     # Getting cleaned data of user email entered
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()      # Quering database and checking if user email exist in database
            if associated_user:                         # If true that user email exist run code block
                subject = "Password Reset Request"      # Composing email subject to send reset link
                message = render_to_string("password_reset_email.html", {    # Rending tempalate containing reset link as string (render_to_string function)
                    'user': associated_user,            # Associated user
                    'domain': get_current_site(request).domain,     # Getting current site domain (get_current_site(request).domain) and that is vinanpet.ltd
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),      # Encoding unique ID generated with user primary key
                    'token': account_activation_token.make_token(associated_user),      # Passing generated token
                    'protocol': 'https' if request.is_secure() else 'http'              # Passing protocol
                    }
                )
                email = EmailMessage(subject, message, from_email=settings.EMAIL_HOST_USER,to=[associated_user.email])      # Sending email using EmailMessage
                if email.send():        # If email is sent successfully
                    messages.success(request, "Email Sent")
                else:       # If message is not sent pass the message below
                    messages.error(request, "Problem sending reset password email, <b>SERVER PROBLEM</b>")      # Error message

            return render(request, "password_reset_done.html")

        # else of if form.is_valid() above, i.e., if form is not valid
        for key, error in list(form.errors.items()):        # if form is not valid, loop through the form for form key and value (key and error), i.e., items()
            if key == 'captcha' and error[0] == 'This field is required.':
                messages.error(request, "You must pass the reCAPTCHA test")
                continue

    form = PasswordResetForm()
    return render(
        request=request,
        template_name="registration/password_reset_form.html",
        context={"form": form}
    )

def passwordResetConfirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been set")
                return redirect("login")
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
        form = SetPasswordForm(user)
        return render(request, 'password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "Link is expired")

    messages.error(request, "Something went wrong, redirecting back to Homepage")
    return redirect("home")