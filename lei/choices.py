from django.db.models import IntegerChoices


class UserAuthorityChoices(IntegerChoices):
    MEMBER = 0, "Member of board"
    POWER = 1, "Power of attorney"
