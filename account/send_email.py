from django.core.mail import send_mail


def send_confirmation_email(user):
    code = user.activation_code
    full_link = f'http://localhost:8000/api/v1/account/activate/{code}/'
    to_email = user.email
    send_mail(
        'Hello, please activate your account!', 
        f'To activate your account, follow the link: {full_link}',
        'turdumamatov2024@gmail.com',
        [to_email,],
        fail_silently=False
    )


def send_reset_password(user):
    code = user.activation_code
    to_email = user.email
    send_mail(
        'Subject', f'Your code for reset password: {code}', 
        'admin@admin.com',[to_email,], fail_silently=False 
    )

