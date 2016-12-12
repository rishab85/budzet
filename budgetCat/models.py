from django.db import models

class budgetCat(models.Model):
    budget_categories = models.CharField(max_length=25)

    def __str__(self):
        return self.budget_categories