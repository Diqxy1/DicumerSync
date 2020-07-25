from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField('Nome', max_length=150, blank=False)
    last_name = models.CharField('Sobrenome', max_length=150, blank=False)
    customer_address = models.CharField('Endedreço', max_length=350, blank=False)
    customer_district = models.CharField('Bairro', max_length=150, blank=False)
    reference_address = models.CharField('Referência', max_length=150, blank=False)
    customer_phone = PhoneNumberField('Telefone', region="BR", null=False, blank=False, unique=True)
    create_at = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Data de atualização', auto_now=True)


    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


    @property
    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()


    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clientes'
        ordering = ['first_name']
