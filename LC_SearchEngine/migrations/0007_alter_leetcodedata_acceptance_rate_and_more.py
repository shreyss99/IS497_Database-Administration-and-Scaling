# Generated by Django 4.2 on 2023-04-24 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LC_SearchEngine", "0006_alter_leetcodedata_acceptance_rate_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="leetcodedata",
            name="acceptance_rate",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="leetcodedata",
            name="accepted",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="leetcodedata",
            name="asked_by_faang",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="leetcodedata",
            name="companies",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="leetcodedata",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="leetcodedata",
            name="difficulty",
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name="leetcodedata",
            name="discuss_count",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="leetcodedata",
            name="dislikes",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="leetcodedata",
            name="frequency",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="leetcodedata",
            name="is_premium",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="leetcodedata",
            name="likes",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="leetcodedata",
            name="rating",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="leetcodedata",
            name="related_topics",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="leetcodedata",
            name="solution_link",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="leetcodedata",
            name="submissions",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="leetcodedata",
            name="title",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="leetcodedata",
            name="url",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
