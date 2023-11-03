
"""

Tutorial from Real Python: https://realpython.com/django-user-management/

    users/templates/users/ ---> holds templates for the users application
    users/templates/registration ---> holds templates used by Django user management
    users/templates/base.html ---> the base template for the users application

    Sending Password Reset Links
        - To send password reset emails, use the ff command to start a simple SMTP  server at http://localhost:1025.
          The server will be used to confirm that emails are sent. It'll also show the content of the messages in the
          command line:
            " python3 -m smtpd -n -c DebuggingServer localhost:1025 "

          let Django know that you're going to use the SMTP server with the ff lines inside settings.py
            - EMAIL_HOST = "localhost"
            - EMAIL_PORT = "1025"

"""
