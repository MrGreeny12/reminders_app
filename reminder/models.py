from django.db import models


class RemindType(models.TextChoices):
    """Remind type choices."""
    OTHER = "OT", "Other"
    WORK = "WR", "Work"
    FAMILY = "FM", "Family"
    HEALTH = "HE", "Health"
    PURCHASES = "PU", "Purchases"
    # TODO: update types (add all base types)
