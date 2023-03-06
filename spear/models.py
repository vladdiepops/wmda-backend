from django.db import models

class Question(models.Model):
    RESPONSE_TYPES = (
        ("number", "number"),
        ("text", "text"),
        ("boolean", "boolean"),
    )

    question_text = models.TextField()
    question_order = models.PositiveIntegerField()
    question_response_type = models.CharField(max_length=10, choices=RESPONSE_TYPES)
