def generate_auto_reply(request):
    return f"""<div style="font-family: system-ui, sans-serif, Arial; font-size: 16px;">
                        <p>Hi {request.name},</p>
                        <p>Thank you for reaching out! I've received your message, and will get back to you as soon as I can.</p>
                        <p>Best regards,<br>Markos Katsi</p>
                        <p style="font-size: 12px; color: #888;">This is an automated reply</p>
                    </div>"""

def generate_admin_notification(request):
    return f"<p>{request.name}, {request.email}</p><p>{request.message}</p>"

def generate_cv_email():
    return f"<p>Hi,</p><p>Please find attached my CV.</p><p>Best regards,<br>Markos Katsi</p>"

def generate_cv_request_notification(email):
    return f"<p>CV requested by {email}</p>"
