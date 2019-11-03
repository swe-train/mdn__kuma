

from django.db import migrations, models
import datetime
import django_extensions.db.fields
import django.utils.timezone
import django.db.models.deletion
from django.conf import settings
import taggit.managers
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('sites', '0001_initial'),
        ('waffle', '0001_initial'),
        ('attachments', '0001_squashed_0008_attachment_on_delete'),
        ('users', '0001_squashed_0008_update_locales_tz_help'),
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, db_index=True)),
                ('slug', models.CharField(max_length=255, db_index=True)),
                ('is_template', models.BooleanField(default=False, db_index=True, editable=False)),
                ('is_redirect', models.BooleanField(default=False, db_index=True, editable=False)),
                ('is_localizable', models.BooleanField(default=True, db_index=True)),
                ('locale', models.CharField(default=b'en-US', max_length=7, db_index=True, choices=[(b'af', 'Afrikaans'), (b'ar', '\u0639\u0631\u0628\u064a'), (b'az', 'Az\u0259rbaycanca'), (b'bn-BD', '\u09ac\u09be\u0982\u09b2\u09be (\u09ac\u09be\u0982\u09b2\u09be\u09a6\u09c7\u09b6)'), (b'bn-IN', '\u09ac\u09be\u0982\u09b2\u09be (\u09ad\u09be\u09b0\u09a4)'), (b'ca', 'Catal\xe0'), (b'cs', '\u010ce\u0161tina'), (b'de', 'Deutsch'), (b'ee', 'E\u028be'), (b'el', '\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac'), (b'en-US', 'English (US)'), (b'es', 'Espa\xf1ol'), (b'fa', '\u0641\u0627\u0631\u0633\u06cc'), (b'ff', 'Pulaar-Fulfulde'), (b'fi', 'suomi'), (b'fr', 'Fran\xe7ais'), (b'fy-NL', 'Frysk'), (b'ga-IE', 'Gaeilge'), (b'ha', 'Hausa'), (b'he', '\u05e2\u05d1\u05e8\u05d9\u05ea'), (b'hi-IN', '\u0939\u093f\u0928\u094d\u0926\u0940 (\u092d\u093e\u0930\u0924)'), (b'hr', 'Hrvatski'), (b'hu', 'magyar'), (b'id', 'Bahasa Indonesia'), (b'ig', 'Igbo'), (b'it', 'Italiano'), (b'ja', '\u65e5\u672c\u8a9e'), (b'ka', '\u10e5\u10d0\u10e0\u10d7\u10e3\u10da\u10d8'), (b'ko', '\ud55c\uad6d\uc5b4'), (b'ln', 'Ling\xe1la'), (b'ml', '\u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02'), (b'ms', 'Melayu'), (b'nl', 'Nederlands'), (b'pl', 'Polski'), (b'pt-BR', 'Portugu\xeas (do\xa0Brasil)'), (b'pt-PT', 'Portugu\xeas (Europeu)'), (b'ro', 'rom\xe2n\u0103'), (b'ru', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439'), (b'sq', 'Shqip'), (b'sw', 'Kiswahili'), (b'ta', '\u0ba4\u0bae\u0bbf\u0bb4\u0bcd'), (b'th', '\u0e44\u0e17\u0e22'), (b'tr', 'T\xfcrk\xe7e'), (b'vi', 'Ti\u1ebfng Vi\u1ec7t'), (b'wo', 'Wolof'), (b'xh', 'isiXhosa'), (b'yo', 'Yor\xf9b\xe1'), (b'zh-CN', '\u4e2d\u6587 (\u7b80\u4f53)'), (b'zh-TW', '\u6b63\u9ad4\u4e2d\u6587 (\u7e41\u9ad4)'), (b'zu', 'isiZulu')])),
                ('json', models.TextField(null=True, editable=False, blank=True)),
                ('html', models.TextField(editable=False)),
                ('rendered_html', models.TextField(null=True, editable=False, blank=True)),
                ('rendered_errors', models.TextField(null=True, editable=False, blank=True)),
                ('defer_rendering', models.BooleanField(default=False, db_index=True)),
                ('render_scheduled_at', models.DateTimeField(null=True, db_index=True)),
                ('render_started_at', models.DateTimeField(null=True, db_index=True)),
                ('last_rendered_at', models.DateTimeField(null=True, db_index=True)),
                ('render_max_age', models.IntegerField(null=True, blank=True)),
                ('render_expires', models.DateTimeField(db_index=True, null=True, blank=True)),
                ('deleted', models.BooleanField(default=False, db_index=True)),
                ('modified', models.DateTimeField(db_index=True, auto_now=True, null=True)),
                ('body_html', models.TextField(null=True, editable=False, blank=True)),
                ('quick_links_html', models.TextField(null=True, editable=False, blank=True)),
                ('zone_subnav_local_html', models.TextField(null=True, editable=False, blank=True)),
                ('toc_html', models.TextField(null=True, editable=False, blank=True)),
                ('summary_html', models.TextField(null=True, editable=False, blank=True)),
                ('summary_text', models.TextField(null=True, editable=False, blank=True)),
            ],
            options={
                'permissions': (('view_document', 'Can view document'), ('add_template_document', 'Can add Template:* document'), ('change_template_document', 'Can change Template:* document'), ('move_tree', 'Can move a tree of documents'), ('purge_document', 'Can permanently delete document'), ('restore_document', 'Can restore deleted document')),
            },
        ),
        migrations.CreateModel(
            name='DocumentAttachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('attached_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)),
                ('document', models.ForeignKey(related_name='attached_files', to='wiki.Document', on_delete=models.CASCADE)),
                ('file', models.ForeignKey(related_name='document_attachments', to='attachments.Attachment', on_delete=models.PROTECT)),
                ('is_linked', models.BooleanField(default=False, verbose_name='linked in the document content')),
                ('is_original', models.BooleanField(default=False, verbose_name='uploaded to the document')),
            ],
            options={
                'db_table': 'attachments_documentattachment',
            },
        ),
        migrations.CreateModel(
            name='DocumentDeletionLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.CharField(default=b'en-US', max_length=7, db_index=True, choices=[(b'en-US', 'English (US)'), (b'af', 'Afrikaans'), (b'ar', '\u0639\u0631\u0628\u064a'), (b'az', 'Az\u0259rbaycanca'), (b'bg', '\u0411\u044a\u043b\u0433\u0430\u0440\u0441\u043a\u0438'), (b'bm', 'Bamanankan'), (b'bn-BD', '\u09ac\u09be\u0982\u09b2\u09be (\u09ac\u09be\u0982\u09b2\u09be\u09a6\u09c7\u09b6)'), (b'bn-IN', '\u09ac\u09be\u0982\u09b2\u09be (\u09ad\u09be\u09b0\u09a4)'), (b'ca', 'Catal\xe0'), (b'cs', '\u010ce\u0161tina'), (b'de', 'Deutsch'), (b'ee', 'E\u028be'), (b'el', '\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac'), (b'es', 'Espa\xf1ol'), (b'fa', '\u0641\u0627\u0631\u0633\u06cc'), (b'ff', 'Pulaar-Fulfulde'), (b'fi', 'suomi'), (b'fr', 'Fran\xe7ais'), (b'fy-NL', 'Frysk'), (b'ga-IE', 'Gaeilge'), (b'ha', 'Hausa'), (b'he', '\u05e2\u05d1\u05e8\u05d9\u05ea'), (b'hi-IN', '\u0939\u093f\u0928\u094d\u0926\u0940 (\u092d\u093e\u0930\u0924)'), (b'hr', 'Hrvatski'), (b'hu', 'magyar'), (b'id', 'Bahasa Indonesia'), (b'ig', 'Igbo'), (b'it', 'Italiano'), (b'ja', '\u65e5\u672c\u8a9e'), (b'ka', '\u10e5\u10d0\u10e0\u10d7\u10e3\u10da\u10d8'), (b'kab', 'Taqbaylit'), (b'ko', '\ud55c\uad6d\uc5b4'), (b'ln', 'Ling\xe1la'), (b'mg', 'Malagasy'), (b'ml', '\u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02'), (b'ms', 'Melayu'), (b'my', '\u1019\u103c\u1014\u103a\u1019\u102c\u1018\u102c\u101e\u102c'), (b'nl', 'Nederlands'), (b'pl', 'Polski'), (b'pt-BR', 'Portugu\xeas (do\xa0Brasil)'), (b'pt-PT', 'Portugu\xeas (Europeu)'), (b'ro', 'Rom\xe2n\u0103'), (b'ru', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439'), (b'son', 'So\u014bay'), (b'sq', 'Shqip'), (b'sr', '\u0421\u0440\u043f\u0441\u043a\u0438'), (b'sr-Latn', 'Srpski'), (b'sv-SE', 'Svenska'), (b'sw', 'Kiswahili'), (b'ta', '\u0ba4\u0bae\u0bbf\u0bb4\u0bcd'), (b'th', '\u0e44\u0e17\u0e22'), (b'tl', 'Tagalog'), (b'tn', 'Setswana'), (b'tr', 'T\xfcrk\xe7e'), (b'uk', '\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430'), (b'vi', 'Ti\u1ebfng Vi\u1ec7t'), (b'wo', 'Wolof'), (b'xh', 'isiXhosa'), (b'yo', 'Yor\xf9b\xe1'), (b'zh-CN', '\u4e2d\u6587 (\u7b80\u4f53)'), (b'zh-TW', '\u6b63\u9ad4\u4e2d\u6587 (\u7e41\u9ad4)'), (b'zu', 'isiZulu')])),
                ('slug', models.CharField(max_length=255, db_index=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('reason', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Document Tag',
                'verbose_name_plural': 'Document Tags',
            },
        ),
        migrations.CreateModel(
            name='DocumentZone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url_root', models.CharField(help_text=b'alternative URL path root for documents under this zone', max_length=255, null=True, db_index=True, blank=True)),
                ('document', models.OneToOneField(related_name='zone', to='wiki.Document', on_delete=models.PROTECT)),
                ('css_slug', models.CharField(help_text=b'name of an alternative pipeline CSS group for documents under this zone (note that "zone-" will be prepended)', max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EditorToolbar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('default', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.TextField(max_length=2000)),
                ('creator', models.ForeignKey(related_name='created_toolbars', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='LocalizationTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Localization Tag',
                'verbose_name_plural': 'Localization Tags',
            },
        ),
        migrations.CreateModel(
            name='LocalizationTaggedRevision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReviewTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Review Tag',
                'verbose_name_plural': 'Review Tags',
            },
        ),
        migrations.CreateModel(
            name='ReviewTaggedRevision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, db_index=True)),
                ('slug', models.CharField(max_length=255, null=True, db_index=True)),
                ('summary', models.TextField()),
                ('content', models.TextField()),
                ('keywords', models.CharField(max_length=255, blank=True)),
                ('tags', models.CharField(max_length=255, blank=True)),
                ('toc_depth', models.IntegerField(default=1, choices=[(0, 'No table of contents'), (1, 'All levels'), (2, 'H2 and higher'), (3, 'H3 and higher'), (4, 'H4 and higher')])),
                ('render_max_age', models.IntegerField(null=True, blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, db_index=True)),
                ('comment', models.CharField(max_length=255)),
                ('is_approved', models.BooleanField(default=True, db_index=True)),
                ('is_mindtouch_migration', models.BooleanField(default=False, help_text=b'Did this revision come from MindTouch?', db_index=True)),
                ('based_on', models.ForeignKey(blank=True, to='wiki.Revision', null=True, on_delete=models.SET_NULL)),
                ('creator', models.ForeignKey(related_name='created_revisions', to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)),
                ('document', models.ForeignKey(related_name='revisions', to='wiki.Document', on_delete=models.CASCADE)),
                ('localization_tags', taggit.managers.TaggableManager(to='wiki.LocalizationTag', through='wiki.LocalizationTaggedRevision', help_text='A comma-separated list of tags.', verbose_name='Tags')),
                ('review_tags', taggit.managers.TaggableManager(to='wiki.ReviewTag', through='wiki.ReviewTaggedRevision', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='RevisionIP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(editable=False, max_length=40, blank=True, null=True, verbose_name=b'IP address', db_index=True)),
                ('revision', models.ForeignKey(to='wiki.Revision', on_delete=models.CASCADE)),
                ('referrer', models.TextField(verbose_name=b'HTTP Referrer', editable=False, blank=True)),
                ('user_agent', models.TextField(verbose_name=b'User-Agent', editable=False, blank=True)),
                ('data', models.TextField(verbose_name='Data submitted to Akismet', null=True, editable=False, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaggedDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', models.ForeignKey(to='wiki.Document', on_delete=models.CASCADE)),
                ('tag', models.ForeignKey(related_name='wiki_taggeddocument_items', to='wiki.DocumentTag', on_delete=models.CASCADE)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='reviewtaggedrevision',
            name='content_object',
            field=models.ForeignKey(to='wiki.Revision', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='reviewtaggedrevision',
            name='tag',
            field=models.ForeignKey(related_name='wiki_reviewtaggedrevision_items', to='wiki.ReviewTag', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='localizationtaggedrevision',
            name='content_object',
            field=models.ForeignKey(to='wiki.Revision', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='localizationtaggedrevision',
            name='tag',
            field=models.ForeignKey(related_name='wiki_localizationtaggedrevision_items', to='wiki.LocalizationTag', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='document',
            name='current_revision',
            field=models.ForeignKey(related_name='current_for+', to='wiki.Revision', null=True, on_delete=models.SET_NULL),
        ),
        migrations.AddField(
            model_name='document',
            name='files',
            field=models.ManyToManyField(to='attachments.Attachment', through='wiki.DocumentAttachment'),
        ),
        migrations.AddField(
            model_name='document',
            name='parent',
            field=models.ForeignKey(related_name='translations', blank=True, to='wiki.Document', null=True, on_delete=models.PROTECT),
        ),
        migrations.AddField(
            model_name='document',
            name='parent_topic',
            field=models.ForeignKey(related_name='children', blank=True, to='wiki.Document', null=True, on_delete=models.PROTECT),
        ),
        migrations.AddField(
            model_name='document',
            name='tags',
            field=taggit.managers.TaggableManager(to='wiki.DocumentTag', through='wiki.TaggedDocument', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AlterUniqueTogether(
            name='document',
            unique_together={('parent', 'locale'), ('slug', 'locale')},
        ),
        migrations.AlterField(
            model_name='document',
            name='locale',
            field=models.CharField(default=b'en-US', max_length=7, db_index=True, choices=[(b'af', 'Afrikaans'), (b'ar', '\u0639\u0631\u0628\u064a'), (b'az', 'Az\u0259rbaycanca'), (b'bm', 'Bamanankan'), (b'bn-BD', '\u09ac\u09be\u0982\u09b2\u09be (\u09ac\u09be\u0982\u09b2\u09be\u09a6\u09c7\u09b6)'), (b'bn-IN', '\u09ac\u09be\u0982\u09b2\u09be (\u09ad\u09be\u09b0\u09a4)'), (b'ca', 'Catal\xe0'), (b'cs', '\u010ce\u0161tina'), (b'de', 'Deutsch'), (b'ee', 'E\u028be'), (b'el', '\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac'), (b'en-US', 'English (US)'), (b'es', 'Espa\xf1ol'), (b'fa', '\u0641\u0627\u0631\u0633\u06cc'), (b'ff', 'Pulaar-Fulfulde'), (b'fi', 'suomi'), (b'fr', 'Fran\xe7ais'), (b'fy-NL', 'Frysk'), (b'ga-IE', 'Gaeilge'), (b'ha', 'Hausa'), (b'he', '\u05e2\u05d1\u05e8\u05d9\u05ea'), (b'hi-IN', '\u0939\u093f\u0928\u094d\u0926\u0940 (\u092d\u093e\u0930\u0924)'), (b'hr', 'Hrvatski'), (b'hu', 'magyar'), (b'id', 'Bahasa Indonesia'), (b'ig', 'Igbo'), (b'it', 'Italiano'), (b'ja', '\u65e5\u672c\u8a9e'), (b'ka', '\u10e5\u10d0\u10e0\u10d7\u10e3\u10da\u10d8'), (b'ko', '\ud55c\uad6d\uc5b4'), (b'ln', 'Ling\xe1la'), (b'ml', '\u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02'), (b'ms', 'Melayu'), (b'my', '\u1019\u103c\u1014\u103a\u1019\u102c\u1018\u102c\u101e\u102c'), (b'nl', 'Nederlands'), (b'pl', 'Polski'), (b'pt-BR', 'Portugu\xeas (do\xa0Brasil)'), (b'pt-PT', 'Portugu\xeas (Europeu)'), (b'ro', 'rom\xe2n\u0103'), (b'ru', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439'), (b'son', 'So\u014bay'), (b'sq', 'Shqip'), (b'sw', 'Kiswahili'), (b'ta', '\u0ba4\u0bae\u0bbf\u0bb4\u0bcd'), (b'th', '\u0e44\u0e17\u0e22'), (b'tl', 'Tagalog'), (b'tr', 'T\xfcrk\xe7e'), (b'vi', 'Ti\u1ebfng Vi\u1ec7t'), (b'wo', 'Wolof'), (b'xh', 'isiXhosa'), (b'yo', 'Yor\xf9b\xe1'), (b'zh-CN', '\u4e2d\u6587 (\u7b80\u4f53)'), (b'zh-TW', '\u6b63\u9ad4\u4e2d\u6587 (\u7e41\u9ad4)'), (b'zu', 'isiZulu')]),
        ),
        migrations.AddField(
            model_name='revision',
            name='tidied_content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='locale',
            field=models.CharField(default=b'en-US', max_length=7, db_index=True, choices=[(b'af', 'Afrikaans'), (b'ar', '\u0639\u0631\u0628\u064a'), (b'az', 'Az\u0259rbaycanca'), (b'bm', 'Bamanankan'), (b'bn-BD', '\u09ac\u09be\u0982\u09b2\u09be (\u09ac\u09be\u0982\u09b2\u09be\u09a6\u09c7\u09b6)'), (b'bn-IN', '\u09ac\u09be\u0982\u09b2\u09be (\u09ad\u09be\u09b0\u09a4)'), (b'ca', 'Catal\xe0'), (b'cs', '\u010ce\u0161tina'), (b'de', 'Deutsch'), (b'ee', 'E\u028be'), (b'el', '\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac'), (b'en-US', 'English (US)'), (b'es', 'Espa\xf1ol'), (b'fa', '\u0641\u0627\u0631\u0633\u06cc'), (b'ff', 'Pulaar-Fulfulde'), (b'fi', 'suomi'), (b'fr', 'Fran\xe7ais'), (b'fy-NL', 'Frysk'), (b'ga-IE', 'Gaeilge'), (b'ha', 'Hausa'), (b'he', '\u05e2\u05d1\u05e8\u05d9\u05ea'), (b'hi-IN', '\u0939\u093f\u0928\u094d\u0926\u0940 (\u092d\u093e\u0930\u0924)'), (b'hr', 'Hrvatski'), (b'hu', 'magyar'), (b'id', 'Bahasa Indonesia'), (b'ig', 'Igbo'), (b'it', 'Italiano'), (b'ja', '\u65e5\u672c\u8a9e'), (b'ka', '\u10e5\u10d0\u10e0\u10d7\u10e3\u10da\u10d8'), (b'ko', '\ud55c\uad6d\uc5b4'), (b'ln', 'Ling\xe1la'), (b'ml', '\u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02'), (b'ms', 'Melayu'), (b'my', '\u1019\u103c\u1014\u103a\u1019\u102c\u1018\u102c\u101e\u102c'), (b'nl', 'Nederlands'), (b'pl', 'Polski'), (b'pt-BR', 'Portugu\xeas (do\xa0Brasil)'), (b'pt-PT', 'Portugu\xeas (Europeu)'), (b'ro', 'rom\xe2n\u0103'), (b'ru', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439'), (b'son', 'So\u014bay'), (b'sq', 'Shqip'), (b'sv-SE', 'Svenska'), (b'sw', 'Kiswahili'), (b'ta', '\u0ba4\u0bae\u0bbf\u0bb4\u0bcd'), (b'th', '\u0e44\u0e17\u0e22'), (b'tl', 'Tagalog'), (b'tr', 'T\xfcrk\xe7e'), (b'vi', 'Ti\u1ebfng Vi\u1ec7t'), (b'wo', 'Wolof'), (b'xh', 'isiXhosa'), (b'yo', 'Yor\xf9b\xe1'), (b'zh-CN', '\u4e2d\u6587 (\u7b80\u4f53)'), (b'zh-TW', '\u6b63\u9ad4\u4e2d\u6587 (\u7e41\u9ad4)'), (b'zu', 'isiZulu')]),
        ),
        migrations.CreateModel(
            name='DocumentSpamAttempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created', db_index=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'Title')),
                ('slug', models.CharField(max_length=255, verbose_name=b'Slug')),
                ('document', models.ForeignKey(related_name='spam_attempts', on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'Document (optional)', blank=True, to='wiki.Document', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)),
                ('data', models.TextField(verbose_name='Data submitted to Akismet', null=True, editable=False, blank=True)),
                ('review', models.IntegerField(default=0, verbose_name="Review of Akismet's classification as spam", choices=[(0, 'Needs Review'), (1, 'Ham / False Positive'), (2, 'Confirmed as Spam'), (3, 'Review Unavailable')])),
                ('reviewed', models.DateTimeField(null=True, verbose_name='reviewed', blank=True)),
            ],
            options={
                'ordering': ('-created',),
                'abstract': False,
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='RevisionAkismetSubmission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sent', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, auto_now_add=True, verbose_name='sent at', db_index=True)),
                ('type', models.CharField(db_index=True, max_length=4, verbose_name='submission type', choices=[(b'spam', 'Spam'), (b'ham', 'Ham')])),
                ('revision', models.ForeignKey(related_name='akismet_submissions', on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'Revision', blank=True, to='wiki.Revision', null=True)),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)),
            ],
            options={
                'ordering': ('-sent',),
                'abstract': False,
                'get_latest_by': 'sent',
            },
        ),
        migrations.AlterModelOptions(
            name='revisionakismetsubmission',
            options={'verbose_name': 'Akismet submission', 'verbose_name_plural': 'Akismet submissions'},
        ),
        migrations.AlterField(
            model_name='revisionakismetsubmission',
            name='sent',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='sent at', db_index=True),
        ),
        migrations.AlterField(
            model_name='revisionakismetsubmission',
            name='type',
            field=models.CharField(db_index=True, max_length=4, verbose_name='type', choices=[(b'spam', 'Spam'), (b'ham', 'Ham')]),
        ),
        migrations.AlterField(
            model_name='document',
            name='locale',
            field=models.CharField(default=b'en-US', max_length=7, db_index=True, choices=[(b'af', 'Afrikaans'), (b'ar', '\u0639\u0631\u0628\u064a'), (b'az', 'Az\u0259rbaycanca'), (b'bm', 'Bamanankan'), (b'bn-BD', '\u09ac\u09be\u0982\u09b2\u09be (\u09ac\u09be\u0982\u09b2\u09be\u09a6\u09c7\u09b6)'), (b'bn-IN', '\u09ac\u09be\u0982\u09b2\u09be (\u09ad\u09be\u09b0\u09a4)'), (b'ca', 'Catal\xe0'), (b'cs', '\u010ce\u0161tina'), (b'de', 'Deutsch'), (b'ee', 'E\u028be'), (b'el', '\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac'), (b'en-US', 'English (US)'), (b'es', 'Espa\xf1ol'), (b'fa', '\u0641\u0627\u0631\u0633\u06cc'), (b'ff', 'Pulaar-Fulfulde'), (b'fi', 'suomi'), (b'fr', 'Fran\xe7ais'), (b'fy-NL', 'Frysk'), (b'ga-IE', 'Gaeilge'), (b'ha', 'Hausa'), (b'he', '\u05e2\u05d1\u05e8\u05d9\u05ea'), (b'hi-IN', '\u0939\u093f\u0928\u094d\u0926\u0940 (\u092d\u093e\u0930\u0924)'), (b'hr', 'Hrvatski'), (b'hu', 'magyar'), (b'id', 'Bahasa Indonesia'), (b'ig', 'Igbo'), (b'it', 'Italiano'), (b'ja', '\u65e5\u672c\u8a9e'), (b'ka', '\u10e5\u10d0\u10e0\u10d7\u10e3\u10da\u10d8'), (b'ko', '\ud55c\uad6d\uc5b4'), (b'ln', 'Ling\xe1la'), (b'mg', 'Malagasy'), (b'ml', '\u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02'), (b'ms', 'Melayu'), (b'my', '\u1019\u103c\u1014\u103a\u1019\u102c\u1018\u102c\u101e\u102c'), (b'nl', 'Nederlands'), (b'pl', 'Polski'), (b'pt-BR', 'Portugu\xeas (do\xa0Brasil)'), (b'pt-PT', 'Portugu\xeas (Europeu)'), (b'ro', 'Rom\xe2n\u0103'), (b'ru', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439'), (b'son', 'So\u014bay'), (b'sq', 'Shqip'), (b'sr', '\u0421\u0440\u043f\u0441\u043a\u0438'), (b'sr-Latn', 'Srpski'), (b'sv-SE', 'Svenska'), (b'sw', 'Kiswahili'), (b'ta', '\u0ba4\u0bae\u0bbf\u0bb4\u0bcd'), (b'th', '\u0e44\u0e17\u0e22'), (b'tl', 'Tagalog'), (b'tn', 'Setswana'), (b'tr', 'T\xfcrk\xe7e'), (b'uk', '\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430'), (b'vi', 'Ti\u1ebfng Vi\u1ec7t'), (b'wo', 'Wolof'), (b'xh', 'isiXhosa'), (b'yo', 'Yor\xf9b\xe1'), (b'zh-CN', '\u4e2d\u6587 (\u7b80\u4f53)'), (b'zh-TW', '\u6b63\u9ad4\u4e2d\u6587 (\u7e41\u9ad4)'), (b'zu', 'isiZulu')]),
        ),
        migrations.AddField(
            model_name='document',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='documentspamattempt',
            name='reviewer',
            field=models.ForeignKey(related_name='documentspam_reviewed', verbose_name='Staff reviewer', blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL),
        ),
        migrations.AlterField(
            model_name='documentspamattempt',
            name='review',
            field=models.IntegerField(default=0, verbose_name="Review of Akismet's classification as spam", choices=[(0, 'Needs Review'), (1, 'Ham / False Positive'), (2, 'Confirmed as Spam'), (3, 'Review Unavailable'), (4, 'Akismet Error')]),
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'permissions': (('view_document', 'Can view document'), ('move_tree', 'Can move a tree of documents'), ('purge_document', 'Can permanently delete document'), ('restore_document', 'Can restore deleted document'))},
        ),
        migrations.AlterField(
            model_name='document',
            name='locale',
            field=models.CharField(default=b'en-US', max_length=7, db_index=True, choices=[(b'en-US', 'English (US)'), (b'af', 'Afrikaans'), (b'ar', '\u0639\u0631\u0628\u064a'), (b'az', 'Az\u0259rbaycanca'), (b'bg', '\u0411\u044a\u043b\u0433\u0430\u0440\u0441\u043a\u0438'), (b'bm', 'Bamanankan'), (b'bn-BD', '\u09ac\u09be\u0982\u09b2\u09be (\u09ac\u09be\u0982\u09b2\u09be\u09a6\u09c7\u09b6)'), (b'bn-IN', '\u09ac\u09be\u0982\u09b2\u09be (\u09ad\u09be\u09b0\u09a4)'), (b'ca', 'Catal\xe0'), (b'cs', '\u010ce\u0161tina'), (b'de', 'Deutsch'), (b'ee', 'E\u028be'), (b'el', '\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac'), (b'es', 'Espa\xf1ol'), (b'fa', '\u0641\u0627\u0631\u0633\u06cc'), (b'ff', 'Pulaar-Fulfulde'), (b'fi', 'suomi'), (b'fr', 'Fran\xe7ais'), (b'fy-NL', 'Frysk'), (b'ga-IE', 'Gaeilge'), (b'ha', 'Hausa'), (b'he', '\u05e2\u05d1\u05e8\u05d9\u05ea'), (b'hi-IN', '\u0939\u093f\u0928\u094d\u0926\u0940 (\u092d\u093e\u0930\u0924)'), (b'hr', 'Hrvatski'), (b'hu', 'magyar'), (b'id', 'Bahasa Indonesia'), (b'ig', 'Igbo'), (b'it', 'Italiano'), (b'ja', '\u65e5\u672c\u8a9e'), (b'ka', '\u10e5\u10d0\u10e0\u10d7\u10e3\u10da\u10d8'), (b'kab', 'Taqbaylit'), (b'ko', '\ud55c\uad6d\uc5b4'), (b'ln', 'Ling\xe1la'), (b'mg', 'Malagasy'), (b'ml', '\u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02'), (b'ms', 'Melayu'), (b'my', '\u1019\u103c\u1014\u103a\u1019\u102c\u1018\u102c\u101e\u102c'), (b'nl', 'Nederlands'), (b'pl', 'Polski'), (b'pt-BR', 'Portugu\xeas (do\xa0Brasil)'), (b'pt-PT', 'Portugu\xeas (Europeu)'), (b'ro', 'Rom\xe2n\u0103'), (b'ru', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439'), (b'son', 'So\u014bay'), (b'sq', 'Shqip'), (b'sr', '\u0421\u0440\u043f\u0441\u043a\u0438'), (b'sr-Latn', 'Srpski'), (b'sv-SE', 'Svenska'), (b'sw', 'Kiswahili'), (b'ta', '\u0ba4\u0bae\u0bbf\u0bb4\u0bcd'), (b'th', '\u0e44\u0e17\u0e22'), (b'tl', 'Tagalog'), (b'tn', 'Setswana'), (b'tr', 'T\xfcrk\xe7e'), (b'uk', '\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430'), (b'vi', 'Ti\u1ebfng Vi\u1ec7t'), (b'wo', 'Wolof'), (b'xh', 'isiXhosa'), (b'yo', 'Yor\xf9b\xe1'), (b'zh-CN', '\u4e2d\u6587 (\u7b80\u4f53)'), (b'zh-TW', '\u6b63\u9ad4\u4e2d\u6587 (\u7e41\u9ad4)'), (b'zu', 'isiZulu')]),
        ),
        migrations.RunSQL(
            sql='SET FOREIGN_KEY_CHECKS=0;\nALTER TABLE taggit_tag\n  MODIFY name varchar(100)\n    CHARACTER SET utf8 COLLATE utf8_general_ci;\nALTER TABLE wiki_documenttag\n  MODIFY name VARCHAR(100)\n    CHARACTER SET utf8 COLLATE utf8_general_ci\n    DEFAULT NULL;\nALTER TABLE wiki_localizationtag\n  MODIFY name VARCHAR(100)\n    CHARACTER SET utf8 COLLATE utf8_general_ci\n    DEFAULT NULL;\nALTER TABLE wiki_reviewtag\n  MODIFY name VARCHAR(100)\n   CHARACTER SET utf8 COLLATE utf8_general_ci\n   DEFAULT NULL;\nSET FOREIGN_KEY_CHECKS=1;\n',
            reverse_sql='SET FOREIGN_KEY_CHECKS=0;\nALTER TABLE taggit_tag\n  MODIFY name varchar(100)\n    CHARACTER SET utf8 COLLATE utf8_distinct_ci;\nALTER TABLE wiki_documenttag\n  MODIFY name VARCHAR(100)\n    CHARACTER SET utf8 COLLATE utf8_distinct_ci\n    DEFAULT NULL;\nALTER TABLE wiki_localizationtag\n  MODIFY name VARCHAR(100)\n    CHARACTER SET utf8 COLLATE utf8_distinct_ci\n    DEFAULT NULL;\nALTER TABLE wiki_reviewtag\n  MODIFY name VARCHAR(100)\n   CHARACTER SET utf8 COLLATE utf8_distinct_ci\n   DEFAULT NULL;\nSET FOREIGN_KEY_CHECKS=1;\n',
        ),
        migrations.AlterField(
            model_name='document',
            name='locale',
            field=models.CharField(default=b'en-US', max_length=7, db_index=True, choices=[(b'en-US', 'English (US)'), (b'af', 'Afrikaans'), (b'ar', '\u0639\u0631\u0628\u064a'), (b'az', 'Az\u0259rbaycanca'), (b'bg', '\u0411\u044a\u043b\u0433\u0430\u0440\u0441\u043a\u0438'), (b'bm', 'Bamanankan'), (b'bn-BD', '\u09ac\u09be\u0982\u09b2\u09be (\u09ac\u09be\u0982\u09b2\u09be\u09a6\u09c7\u09b6)'), (b'bn-IN', '\u09ac\u09be\u0982\u09b2\u09be (\u09ad\u09be\u09b0\u09a4)'), (b'ca', 'Catal\xe0'), (b'cs', '\u010ce\u0161tina'), (b'de', 'Deutsch'), (b'ee', 'E\u028be'), (b'el', '\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac'), (b'es', 'Espa\xf1ol'), (b'fa', '\u0641\u0627\u0631\u0633\u06cc'), (b'ff', 'Pulaar-Fulfulde'), (b'fi', 'suomi'), (b'fr', 'Fran\xe7ais'), (b'fy-NL', 'Frysk'), (b'ga-IE', 'Gaeilge'), (b'ha', 'Hausa'), (b'he', '\u05e2\u05d1\u05e8\u05d9\u05ea'), (b'hi-IN', '\u0939\u093f\u0928\u094d\u0926\u0940 (\u092d\u093e\u0930\u0924)'), (b'hr', 'Hrvatski'), (b'hu', 'magyar'), (b'id', 'Bahasa Indonesia'), (b'ig', 'Igbo'), (b'it', 'Italiano'), (b'ja', '\u65e5\u672c\u8a9e'), (b'ka', '\u10e5\u10d0\u10e0\u10d7\u10e3\u10da\u10d8'), (b'kab', 'Taqbaylit'), (b'ko', '\ud55c\uad6d\uc5b4'), (b'ln', 'Ling\xe1la'), (b'mg', 'Malagasy'), (b'ml', '\u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02'), (b'ms', 'Melayu'), (b'my', '\u1019\u103c\u1014\u103a\u1019\u102c\u1018\u102c\u101e\u102c'), (b'nl', 'Nederlands'), (b'pl', 'Polski'), (b'pt-BR', 'Portugu\xeas (do\xa0Brasil)'), (b'pt-PT', 'Portugu\xeas (Europeu)'), (b'ro', 'Rom\xe2n\u0103'), (b'ru', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439'), (b'son', 'So\u014bay'), (b'sq', 'Shqip'), (b'sr', '\u0421\u0440\u043f\u0441\u043a\u0438'), (b'sr-Latn', 'Srpski'), (b'sv-SE', 'Svenska'), (b'sw', 'Kiswahili'), (b'ta', '\u0ba4\u0bae\u0bbf\u0bb4\u0bcd'), (b'te', '\u0c24\u0c46\u0c32\u0c41\u0c17\u0c41'), (b'th', '\u0e44\u0e17\u0e22'), (b'tl', 'Tagalog'), (b'tn', 'Setswana'), (b'tr', 'T\xfcrk\xe7e'), (b'uk', '\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430'), (b'vi', 'Ti\u1ebfng Vi\u1ec7t'), (b'wo', 'Wolof'), (b'xh', 'isiXhosa'), (b'yo', 'Yor\xf9b\xe1'), (b'zh-CN', '\u4e2d\u6587 (\u7b80\u4f53)'), (b'zh-TW', '\u6b63\u9ad4\u4e2d\u6587 (\u7e41\u9ad4)'), (b'zu', 'isiZulu')]),
        ),
        migrations.AlterField(
            model_name='documentdeletionlog',
            name='locale',
            field=models.CharField(default=b'en-US', max_length=7, db_index=True, choices=[(b'en-US', 'English (US)'), (b'af', 'Afrikaans'), (b'ar', '\u0639\u0631\u0628\u064a'), (b'az', 'Az\u0259rbaycanca'), (b'bg', '\u0411\u044a\u043b\u0433\u0430\u0440\u0441\u043a\u0438'), (b'bm', 'Bamanankan'), (b'bn-BD', '\u09ac\u09be\u0982\u09b2\u09be (\u09ac\u09be\u0982\u09b2\u09be\u09a6\u09c7\u09b6)'), (b'bn-IN', '\u09ac\u09be\u0982\u09b2\u09be (\u09ad\u09be\u09b0\u09a4)'), (b'ca', 'Catal\xe0'), (b'cs', '\u010ce\u0161tina'), (b'de', 'Deutsch'), (b'ee', 'E\u028be'), (b'el', '\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac'), (b'es', 'Espa\xf1ol'), (b'fa', '\u0641\u0627\u0631\u0633\u06cc'), (b'ff', 'Pulaar-Fulfulde'), (b'fi', 'suomi'), (b'fr', 'Fran\xe7ais'), (b'fy-NL', 'Frysk'), (b'ga-IE', 'Gaeilge'), (b'ha', 'Hausa'), (b'he', '\u05e2\u05d1\u05e8\u05d9\u05ea'), (b'hi-IN', '\u0939\u093f\u0928\u094d\u0926\u0940 (\u092d\u093e\u0930\u0924)'), (b'hr', 'Hrvatski'), (b'hu', 'magyar'), (b'id', 'Bahasa Indonesia'), (b'ig', 'Igbo'), (b'it', 'Italiano'), (b'ja', '\u65e5\u672c\u8a9e'), (b'ka', '\u10e5\u10d0\u10e0\u10d7\u10e3\u10da\u10d8'), (b'kab', 'Taqbaylit'), (b'ko', '\ud55c\uad6d\uc5b4'), (b'ln', 'Ling\xe1la'), (b'mg', 'Malagasy'), (b'ml', '\u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02'), (b'ms', 'Melayu'), (b'my', '\u1019\u103c\u1014\u103a\u1019\u102c\u1018\u102c\u101e\u102c'), (b'nl', 'Nederlands'), (b'pl', 'Polski'), (b'pt-BR', 'Portugu\xeas (do\xa0Brasil)'), (b'pt-PT', 'Portugu\xeas (Europeu)'), (b'ro', 'Rom\xe2n\u0103'), (b'ru', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439'), (b'son', 'So\u014bay'), (b'sq', 'Shqip'), (b'sr', '\u0421\u0440\u043f\u0441\u043a\u0438'), (b'sr-Latn', 'Srpski'), (b'sv-SE', 'Svenska'), (b'sw', 'Kiswahili'), (b'ta', '\u0ba4\u0bae\u0bbf\u0bb4\u0bcd'), (b'te', '\u0c24\u0c46\u0c32\u0c41\u0c17\u0c41'), (b'th', '\u0e44\u0e17\u0e22'), (b'tl', 'Tagalog'), (b'tn', 'Setswana'), (b'tr', 'T\xfcrk\xe7e'), (b'uk', '\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430'), (b'vi', 'Ti\u1ebfng Vi\u1ec7t'), (b'wo', 'Wolof'), (b'xh', 'isiXhosa'), (b'yo', 'Yor\xf9b\xe1'), (b'zh-CN', '\u4e2d\u6587 (\u7b80\u4f53)'), (b'zh-TW', '\u6b63\u9ad4\u4e2d\u6587 (\u7e41\u9ad4)'), (b'zu', 'isiZulu')]),
        ),
    ]
