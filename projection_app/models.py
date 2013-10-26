from django.contrib.gis.db import models


class State(models.Model):
    class Meta:
        app_label = 'projection_app'
        db_table = 'careermap_state'

    def __unicode__(self):
        return self.state_name

    state_name = models.CharField(max_length=100, unique=True)
    sub_region = models.CharField(max_length=100)
    geometry = models.MultiPolygonField(db_column='geom')
    objects = models.GeoManager()


class Occupation(models.Model):
    # "AreaName","Code","Name","Base","Proj","Change","PercentChange","AvgAnnualOpenings"
    class Meta:
        app_label = 'projection_app'
        db_table = 'careermap_occupation'

    def __unicode__(self):
        return self.name

    area_name = models.ForeignKey(State, to_field='state_name', null=True, blank=True)
    name = models.CharField(max_length=255)
    base = models.IntegerField()
    proj = models.IntegerField()
    change = models.IntegerField()
    percentchange = models.IntegerField()
    avgannualopenings = models.IntegerField()