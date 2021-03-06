# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Information(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=38, blank=True, null=True)
    stu_id = models.CharField(max_length=20, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=15, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    usedname = models.CharField(db_column='usedName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    major = models.CharField(max_length=20, blank=True, null=True)
    idcard = models.CharField(db_column='id',max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=30, blank=True, null=True)
    birth = models.CharField(max_length=30, blank=True, null=True)
    nation = models.CharField(max_length=30, blank=True, null=True)
    polity = models.CharField(max_length=30, blank=True, null=True)
    nationality = models.CharField(max_length=30, blank=True, null=True)
    province = models.CharField(max_length=30, blank=True, null=True)
    nativeplace = models.CharField(db_column='nativePlace', max_length=30, blank=True, null=True)  # Field name made lowercase.
    stutypeb = models.CharField(db_column='stuTypeb', max_length=30, blank=True, null=True)  # Field name made lowercase.
    stutypex = models.CharField(db_column='stuTypex', max_length=30, blank=True, null=True)  # Field name made lowercase.
    loan = models.CharField(max_length=30, blank=True, null=True)
    domplace = models.CharField(db_column='domPlace', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dommove = models.CharField(db_column='domMove', max_length=30, blank=True, null=True)  # Field name made lowercase.
    domplacenew = models.CharField(db_column='domPlaceNew', max_length=30, blank=True, null=True)  # Field name made lowercase.
    registplace = models.CharField(db_column='registPlace', max_length=30, blank=True, null=True)  # Field name made lowercase.
    highschool = models.CharField(db_column='highSchool', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=30, blank=True, null=True)
    qq = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)
    postcode = models.CharField(max_length=30, blank=True, null=True)
    homephone = models.CharField(db_column='homePhone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    faname = models.CharField(db_column='faName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    faworkunit = models.CharField(db_column='faWorkUnit', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fajob = models.CharField(db_column='faJob', max_length=30, blank=True, null=True)  # Field name made lowercase.
    faphone = models.CharField(db_column='faPhone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    maname = models.CharField(db_column='maName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    maworkunit = models.CharField(db_column='maWorkUnit', max_length=30, blank=True, null=True)  # Field name made lowercase.
    majob = models.CharField(db_column='maJob', max_length=30, blank=True, null=True)  # Field name made lowercase.
    maphone = models.CharField(db_column='maPhone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    othermember = models.CharField(db_column='otherMember', max_length=30, blank=True, null=True)  # Field name made lowercase.
    otherrelation = models.CharField(db_column='otherRelation', max_length=30, blank=True, null=True)  # Field name made lowercase.
    otherworkunit = models.CharField(db_column='otherWorkUnit', max_length=30, blank=True, null=True)  # Field name made lowercase.
    otherjob = models.CharField(db_column='otherJob', max_length=30, blank=True, null=True)  # Field name made lowercase.
    otherphone = models.CharField(db_column='otherPhone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    campus = models.CharField(max_length=30, blank=True, null=True)
    building = models.CharField(max_length=30, blank=True, null=True)
    room = models.CharField(max_length=30, blank=True, null=True)
    grade = models.TextField(blank=True, null=True)
    roll = models.CharField(max_length=30, blank=True, null=True)
    stipend = models.TextField(blank=True, null=True)
    scholarship = models.TextField(blank=True, null=True)
    honour = models.TextField(blank=True, null=True)
    leader = models.TextField(blank=True, null=True)
    abroad = models.TextField(blank=True, null=True)
    academic = models.TextField(blank=True, null=True)
    practice = models.TextField(blank=True, null=True)
    talk = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    career = models.TextField(blank=True, null=True)
    specialty = models.CharField(max_length=30)
    url = ''

    def set_url(self,q):
        self.url=q
    class Meta:
        managed = False
        db_table = 'information'


class Power(models.Model):
    pwid = models.CharField(max_length=32)
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=20)
    rname = models.CharField(max_length=32)
    status = models.IntegerField()
    gid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'power'


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    stu_id = models.CharField(max_length=13)
    password = models.CharField(max_length=32)
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'user'
class portrait(models.Model):
    uid = models.IntegerField()
    portrait=models.CharField(max_length=32)
    class Meta:
        managed= False
        db_table = 'portrait'
