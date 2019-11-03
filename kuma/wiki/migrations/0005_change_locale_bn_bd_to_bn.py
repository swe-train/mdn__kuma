# Generated by Django 1.11.23 on 2019-09-11 09:26


from django.db import migrations


def change_locale_bn_bd_to_bn_and_remove_bn_in_forwards(apps, schema_editor):
    Document = apps.get_model('wiki', 'Document')
    DocumentDeletionLog = apps.get_model('wiki', 'DocumentDeletionLog')

    Document.objects.all().filter(locale='bn-BD').update(locale='bn')
    DocumentDeletionLog.objects.all().filter(locale='bn-BD').update(locale='bn')

    # Remove bn-IN
    bn_in_documents = Document.objects.all().filter(locale='bn-IN')
    # First set all parent_topic to None so it does
    # not raise error while deleting the parent topic
    bn_in_documents.update(parent_topic=None)
    # Then delete all the `bn-IN` documents
    bn_in_documents.delete()
    DocumentDeletionLog.objects.all().filter(locale='bn-IN').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0004_auto_20190708_1314'),
    ]

    operations = [
        migrations.RunPython(change_locale_bn_bd_to_bn_and_remove_bn_in_forwards)
    ]
