from pathlib import Path

TEMPLATES_DIR = Path(__file__).parent / "templates"


def generate_auto_reply(request):
    html = (TEMPLATES_DIR / "auto_reply.html").read_text(encoding="utf-8")
    return html.replace("{{name}}", request.name)

def generate_admin_notification(request):
    return f"<p>{request.name}, {request.email}</p><p>{request.message}</p>"

def generate_cv_email():
    return (TEMPLATES_DIR / "cv_email.html").read_text(encoding="utf-8")

def generate_cv_request_notification(email):
    return f"<p>CV requested by {email}</p>"
