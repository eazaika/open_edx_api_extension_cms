from django.apps import AppConfig

class OpenEdxApiExtensionCmsConfig(AppConfig):
    name = 'open_edx_api_extension_cms'
    verbose_name = "OpenEdxApiExtensionCms"

    def ready(self):
        import open_edx_api_extension_cms.signals
