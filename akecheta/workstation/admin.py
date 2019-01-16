from django.contrib import admin

# Register your models here.
from django.forms import TextInput, Textarea
from django.db import models
from .models import Pod, Registry, Secret, ConfigMap, Namespace, Deployment, DaemonSet
from django.utils.safestring import mark_safe


class PodAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'image_responstry',
        'image_package',
        'image_name',
        'image_versiontag',
        'image_pull_policy',
        #'launch_env',
        #'launch_volume',
        'launch_command',
        'launch_args',
    ]
    list_display_links = []
    search_fields = ['name']


class RegistryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'address',
    ]


class SecretAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'namespace',
        'env_format',
    ]

    def env_format(self, obj):
        table_template = '''
        <table style="text-align:left width:20%%">
          %s
        </table>
        '''

        content = ''
        for kv in obj.key_value_dict.split(','):
            k, v = kv.split('=')
            env_data = '''
              <tr>
                <th>%s</th>
                <td>%s</td>
              </tr>
              ''' % (k, v)
            content += env_data
        return mark_safe(table_template % content)


class NamespaceAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


class ConfigMapAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'namespace',
        'filepath',
        'sub_path',
    ]


class DaemonSetAdmin(admin.ModelAdmin):
    list_display = []


class DeploymentAdmin(admin.ModelAdmin):
    list_display = ['name', 'namespace', 'pod', 'init_pod']


admin.site.register(Pod, PodAdmin)
admin.site.register(Registry, RegistryAdmin)
admin.site.register(Secret, SecretAdmin)
admin.site.register(ConfigMap, ConfigMapAdmin)
admin.site.register(Namespace, NamespaceAdmin)
admin.site.register(DaemonSet, DaemonSetAdmin)
admin.site.register(Deployment, DeploymentAdmin)
