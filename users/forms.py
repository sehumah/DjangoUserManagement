# utilizes Django's UserCreationForm to add an email address section when a new user is signing up

from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):

    # inner class keeps additional information about the form and in this case extends UserCreationForm.Meta, so almost
    # everything from Django's form will be reused
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)  # add email to include an email field
