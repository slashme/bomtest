from django.db import models

# Create your models here.

class Ingredient(models.Model):
    #A raw material, not made up of other materials.
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]
    def get_absolute_url(self):
        return "/ingredient/%i/" % self.id
    name        = models.CharField('Ingredient name, not including supplier', max_length=100)
    description = models.TextField('Description of the ingredient')
    vendor      = models.CharField('Supplier of the ingredient', null=True, blank=True)
    moisture    = models.FloatField('Total moisture expressed as a fraction, not percent')
    fat         = models.FloatField('Total fat (lipids incl. phospholipids) expressed as fraction of ingredient', null=True, blank=True)
    satfat      = models.FloatField('Saturated fat expressed as fraction of ingredient', null=True, blank=True)
    monounsat   = models.FloatField('Cis mono-unsaturated fat expressed as fraction of ingredient', null=True, blank=True)
    polyunsat   = models.FloatField('Cis polyunsaturated fat expressed as fraction of ingredient', null=True, blank=True)
    carbs       = models.FloatField('Digestible carbohydrate including polyols expressed as fraction of ingredient', null=True, blank=True)
    sugar       = models.FloatField('Mono and disaccharides expressed as fraction of ingredient', null=True, blank=True)
    polyols     = models.FloatField('Polyols expressed as fraction of ingredient', null=True, blank=True)
    starch      = models.FloatField('Total starch expressed as fraction of ingredient', null=True, blank=True)
    fibre       = models.FloatField('Undigestible carbs DP>3 expressed as fraction of ingredient', null=True, blank=True)
    protein     = models.FloatField('Protein (Kjeldahl N × 6.25) expressed as fraction of ingredient', null=True, blank=True)
    salt        = models.FloatField('Salt equiv (Na × 2.5) expressed as fraction of ingredient', null=True, blank=True)
    orgacid     = models.FloatField('Organic acids expressed as fraction of ingredient', null=True, blank=True)

