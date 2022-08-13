# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# inspectdb로 불러온 기존 모델

class App(models.Model):
    app_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=65532)
    header_url = models.CharField(max_length=65532, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    basegame = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app'

class Developer(models.Model):
    developer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    class Meta:
        managed = False
        db_table = 'developer'

class AppDev(models.Model):
    #developer = models.OneToOneField('Developer', models.DO_NOTHING, primary_key=True)
    #app = models.ForeignKey(App, models.DO_NOTHING)
    app = models.OneToOneField('App', models.DO_NOTHING, primary_key=True)
    developer = models.ForeignKey(Developer, models.DO_NOTHING)
    class Meta:
        managed = False
        db_table = 'app_dev'
        unique_together = (('developer', 'app'),)

class AppGenre(models.Model):
    genre = models.OneToOneField('Genre', models.DO_NOTHING, primary_key=True)
    app = models.ForeignKey(App, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_genre'
        unique_together = (('genre', 'app'),)


class AppPub(models.Model):
    publisher = models.OneToOneField('Publisher', models.DO_NOTHING, primary_key=True)
    app = models.ForeignKey(App, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_pub'
        unique_together = (('publisher', 'app'),)


class Description(models.Model):
    app = models.OneToOneField(App, models.DO_NOTHING, primary_key=True)
    short_description = models.TextField(blank=True, null=True)
    min_requirement = models.TextField(blank=True, null=True)
    rec_requirement = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'description'





class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    genre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'genre'


class Price(models.Model):
    date = models.DateField(primary_key=True)
    store = models.ForeignKey('Store', models.DO_NOTHING)
    app = models.ForeignKey(App, models.DO_NOTHING)
    price = models.IntegerField()
    init_price = models.IntegerField()
    discount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'price'
        unique_together = (('date', 'store', 'app'),)


class Publisher(models.Model):
    publisher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publisher'


class Recommendation(models.Model):
    app = models.ForeignKey(App, models.DO_NOTHING, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recommendation'


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'store'

#################