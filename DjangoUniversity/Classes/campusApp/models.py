from django.db import models


# Create model of campus information

class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=25, default="", blank=False, null=False)
    campus_id = models.IntegerField(default="", blank=False, null=False)
    campus_state = models.CharField(max_length=10, default="", blank=True, null=False)


    # Creates model manager
    object = models.Manager()



    def __str__(self):

        display_campus = '{0.campus_state}: {0.campus_name}'
        return display_campus.format(self)


    class Meta:
        verbose_name_plural = "University Campus"




