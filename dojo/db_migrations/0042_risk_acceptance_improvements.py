# Generated by Django 2.2.12 on 2020-04-05 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    def set_name_from_created_date(apps, schema_editor):
        # We can't import the Risk_Acceptance model directly as it may be a newer
        # version than this migration expects. We use the historical version.
        Risk_Acceptance = apps.get_model('dojo', 'Risk_Acceptance')
        for ra in Risk_Acceptance.objects.all():
            ra.name = 'Legacy acceptance created on %s' % ra.created.strftime('%b %d, %Y, %H:%M:%S')
            ra.save()

    dependencies = [
        ('dojo', '0041_engagement_survey_import'),
    ]

    operations = [
        migrations.AddField(
            model_name='risk_acceptance',
            name='name',
            field=models.CharField(default="Legacy acceptance", max_length=100, help_text="Descriptive name which in the future may also be used to group risk acceptances together across engagements and products"),
        ),
        migrations.RunPython(set_name_from_created_date),
        migrations.AlterField(
            model_name='risk_acceptance',
            name='name',
            field=models.CharField(max_length=100, null=False, blank=False, help_text="Descriptive name which in the future may also be used to group risk acceptances together across engagements and products"),
        ),
        migrations.RenameField(
            model_name='risk_acceptance',
            old_name='reporter',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='risk_acceptance',
            name='owner',
            field=models.ForeignKey(editable=True, on_delete=django.db.models.deletion.CASCADE, to='dojo.Dojo_User', help_text="Only the owner and staff users can edit the risk acceptance."),
        ),
        migrations.AlterField(
            model_name='risk_acceptance',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='risk_acceptance',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]