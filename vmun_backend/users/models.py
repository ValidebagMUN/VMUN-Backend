from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from conferences.models import Committee, Institution


class User(AbstractUser):
    """
    Default custom user model for vmun_backend.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    USER_CHOICES = (
        ("DEL", "Delegate"),
        ("CHA", "Chair"),
        ("ADV", "Advisor"),
        ("ADM", "Admin"),
    )
    type = CharField(max_length=10, choices=USER_CHOICES, default="DEL")
    phone = models.CharField(max_length=10, blank=True, null=True)
    institution = models.ForeignKey(
        Institution, on_delete=models.CASCADE, blank=True, null=True
    )
    committee = models.ForeignKey(
        Committee, on_delete=models.CASCADE, blank=True, null=True
    )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
