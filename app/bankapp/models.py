from django.db import models

import uuid

class Branch(models.Model):

    class Meta:
        verbose_name_plural = 'Branches'
    location_name = models.CharField(max_length=30)
    city_name = 
        ('fresno','FRESNO'),
        ('oakland','OAKLAND')
        ('austin','AUSTIN')
    )

    city_name_params = models.CharField(
        max_length = 8,
        choices = city_name,
        default = city_name [0],
    )

    location_id = str(uuid.uuid4())

    def_str_(self):
        return (
            f'Location Name : {self.location_name} City Name : {self.location_name}'
        )



class Customer(models.Model):
    first_name = models.CharField(
        max_length=30,
        default=''
        )

    last_name = models.CharField(
        max_length=30,
        default=''
    )

    connect_to_branch = models.ForeignKey(
        Branch,
        on_delete = models.CASCADE
    )

    def_str_(self):
        return(
            f"{self.Customer} {self.connect_to_branch}"
    )
    
    class Account (models.Model):
        account_types = (
            ('checking', 'CHECKING')
            ('savings', 'SAVINGS')
            ('none', 'NONE')
    )

    

    
