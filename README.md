# Mail Service

This project is a backend service for my portfolio website, designed to send and receive emails.

## Features

- Contact form: Sends an auto-reply to the sender and forwards their message to you.
- CV request: Sends your CV as an email attachment to a provided email address.

## API Endpoints

### POST `/contact`

Send a contact message (name, email, message). Sender gets an auto-reply, you get their message.

### POST `/cv`

Send your CV to a provided email address.

## Setup Instructions

1. **Clone the repository:**

   ```sh
   git clone https://github.com/markoskatsi/mail-service.git
   cd mail-service
   ```

2. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   - Copy `.env.example` to `.env` and fill in the required values (SMTP credentials, etc).

4. **Run the service (local development):**

   ```sh
   uvicorn main:app --reload
   ```

5. **Docker (optional):**
   For Docker, use the provided `Dockerfile` and `compose.yml`.
   ```sh
   docker compose up --build
   ```

## Customization

- Update `config.py` for custom settings.
- Modify `routes.py` to add or change API endpoints and update recipient addresses or other information as needed.
- Modify `email_templates.py` to customise the email content to your preference.

## License

This project is for personal/portfolio use. Feel free to adapt it for your own portfolio or email needs.
