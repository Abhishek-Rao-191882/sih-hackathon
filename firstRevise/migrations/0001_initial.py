# Generated by Django 4.0.3 on 2022-03-12 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collegeName', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=40)),
                ('pinCode', models.IntegerField()),
                ('totalPhdStudents', models.IntegerField()),
                ('totalStudentsApproved', models.IntegerField()),
                ('totalStudents', models.IntegerField()),
                ('numOfFaculties', models.IntegerField()),
                ('facultyExpLT8', models.IntegerField()),
                ('facultyExp8To15', models.IntegerField()),
                ('facultyExpGT15', models.IntegerField()),
                ('avgAnnualCapPerStd', models.FloatField()),
                ('operExp', models.IntegerField()),
                ('numOfPublication', models.IntegerField()),
                ('numOfCitation', models.IntegerField()),
                ('totalPatentPublished', models.IntegerField()),
                ('totalPatentGranted', models.IntegerField()),
                ('totalResearchFunding', models.IntegerField()),
                ('annualConsultancyAmount', models.IntegerField()),
                ('totalExecutiveEarning', models.IntegerField()),
                ('totalPhdStudentPassed', models.IntegerField()),
                ('studentFromOtherStates', models.IntegerField()),
                ('percOfWomenFaculty', models.FloatField()),
                ('womenStudentNumbers', models.IntegerField()),
                ('totalStudentPassed', models.IntegerField()),
                ('physChallengedStd', models.IntegerField()),
                ('eAndSociallyChallengedStd', models.IntegerField()),
            ],
        ),
    ]