from django.forms import ModelForm
from django.db import models


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


# Database TABLES

class Department(models.Model):
    dname = models.CharField(db_column='DName', primary_key=True, max_length=20)  # Field name made lowercase.
    location_no = models.IntegerField(db_column='Location_no')  # Field name made lowercase.
    manager_no = models.ForeignKey('Employee', models.DO_NOTHING, db_column='Manager_no', blank=True, null=True)  # Field name made lowercase.
    start_date = models.CharField(db_column='Start_date', max_length=11, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table= 'department'


class DeptLocations(models.Model):
    dlnumber = models.ForeignKey(Department, models.DO_NOTHING,related_name="dlnumber1", db_column='DLNumber')  # Field name made lowercase.
    locations = models.CharField(db_column='Locations', max_length=20)  # Field name made lowercase.
    dlname = models.ForeignKey(Department, models.DO_NOTHING, db_column='DLName', related_name="dlname1", blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dept_locations'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    fname = models.CharField(db_column='Fname', max_length=30, blank=True, null=True)  # Field name made lowercase.
    minit = models.CharField(db_column='Minit', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(db_column='Lname', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ssn = models.IntegerField(db_column='Ssn', primary_key=True)  # Field name made lowercase.
    bdate = models.CharField(db_column='Bdate', max_length=11)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=2, blank=True, null=True)  # Field name made lowercase.
    salary = models.IntegerField(db_column='Salary', blank=True, null=True)  # Field name made lowercase.
    works_for = models.IntegerField(db_column='Works_for', blank=True, null=True)  # Field name made lowercase.
    department_no = models.IntegerField(db_column='Department_no', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'


class Project(models.Model):
    pname = models.CharField(db_column='PName', primary_key=True, max_length=20)  # Field name made lowercase.
    pnumber = models.IntegerField(db_column='PNumber')  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dept_number = models.IntegerField(db_column='Dept_number', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project'
        unique_together = (('pname', 'pnumber'),)


class WorksOn(models.Model):
    employee_no = models.ForeignKey(Employee,  models.DO_NOTHING, db_column='employee_no')
    project_no = models.ForeignKey(Project, models.DO_NOTHING, related_name="pro_no1", db_column='project_no', blank=True, null=True)
    hours = models.FloatField(blank=True, null=True)
    woname = models.ForeignKey(Project, models.DO_NOTHING, related_name="woname_no1", db_column='WOName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'works_on'