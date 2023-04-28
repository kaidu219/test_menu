from django.db import models

# Create your models here.
from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

    def get_menu_items(self):
        children = self.children.all()
        if children:
            return {self.name: [child.get_menu_items() for child in children]}
        else:
            return self.name