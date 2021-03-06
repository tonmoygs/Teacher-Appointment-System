# Generated by Django 2.0.1 on 2018-04-14 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppointmentManagement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointmentinfo',
            old_name='slot1_course_name',
            new_name='slot1_discussion_topic',
        ),
        migrations.RenameField(
            model_name='appointmentinfo',
            old_name='slot2_course_name',
            new_name='slot2_discussion_topic',
        ),
        migrations.RenameField(
            model_name='appointmentinfo',
            old_name='slot3_course_name',
            new_name='slot3_discussion_topic',
        ),
        migrations.RenameField(
            model_name='appointmentinfo',
            old_name='slot4_course_name',
            new_name='slot4_discussion_topic',
        ),
        migrations.RenameField(
            model_name='appointmentinfo',
            old_name='slot5_course_name',
            new_name='slot5_discussion_topic',
        ),
        migrations.RenameField(
            model_name='appointmentinfo',
            old_name='slot6_course_name',
            new_name='slot6_discussion_topic',
        ),
        migrations.RemoveField(
            model_name='appointmentinfo',
            name='slot1_course_code',
        ),
        migrations.RemoveField(
            model_name='appointmentinfo',
            name='slot1_teacher_initial',
        ),
        migrations.RemoveField(
            model_name='appointmentinfo',
            name='slot2_course_code',
        ),
        migrations.RemoveField(
            model_name='appointmentinfo',
            name='slot2_teacher_initial',
        ),
        migrations.RemoveField(
            model_name='appointmentinfo',
            name='slot3_course_code',
        ),
        migrations.RemoveField(
            model_name='appointmentinfo',
            name='slot3_teacher_initial',
        ),
        migrations.RemoveField(
            model_name='appointmentinfo',
            name='slot4_course_code',
        ),
        migrations.RemoveField(
            model_name='appointmentinfo',
            name='slot4_teacher_initial',
        ),
        migrations.RemoveField(
            model_name='appointmentinfo',
            name='slot5_course_code',
        ),
        migrations.RemoveField(
            model_name='appointmentinfo',
            name='slot5_teacher_initial',
        ),
        migrations.RemoveField(
            model_name='appointmentinfo',
            name='slot6_course_code',
        ),
        migrations.RemoveField(
            model_name='appointmentinfo',
            name='slot6_teacher_initial',
        ),
        migrations.AddField(
            model_name='appointmentinfo',
            name='slot1_student_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='appointmentinfo',
            name='slot1_student_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='appointmentinfo',
            name='slot2_student_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='appointmentinfo',
            name='slot2_student_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='appointmentinfo',
            name='slot3_student_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='appointmentinfo',
            name='slot3_student_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='appointmentinfo',
            name='slot4_student_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='appointmentinfo',
            name='slot4_student_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='appointmentinfo',
            name='slot5_student_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='appointmentinfo',
            name='slot5_student_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='appointmentinfo',
            name='slot6_student_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='appointmentinfo',
            name='slot6_student_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
