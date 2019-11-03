# Generated by Django 1.11.23 on 2019-09-14 22:09


from django.db import migrations


DISCARDED_LOCALES = (
    'af', 'az', 'cs', 'ee', 'ff', 'fy-NL', 'ga-IE', 'ha', 'hr', 'ig', 'ka',
    'ln', 'mg', 'ml', 'ro', 'son', 'sq', 'sr', 'sr-Latn', 'sw', 'ta', 'te',
    'tl', 'tn', 'wo', 'xh', 'yo', 'zu'
)


def update_users_with_discarded_locales(apps, schema_editor):
    """
    Blank the preferred locale of all users with one of the DISCARDED_LOCALES.
    """
    User = apps.get_model('users', 'User')
    User.objects.filter(locale__in=DISCARDED_LOCALES).update(locale='')


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20190914_2208'),
    ]

    operations = [
        migrations.RunPython(update_users_with_discarded_locales),
    ]
