# open_edx_api_extension_cms

API extension for Open edX CMS 
Also set info about available proctoring services in the table proctoring_proctoredcourse and proctoring_proctoredcourseproctoringservice

Installation:
```bash
sudo -Hu edxapp /edx/bin/pip.edxapp install -e git+https://github.com/eazaika/open_edx_api_extension_cms@hawthorn#egg=open_edx_api_extension_cms
sudo -u edxapp /edx/bin/pip.edxapp install venvs/edxapp/src/open-edx-api-extension-cms/ 
```

Set `EDX_API_KEY` in `cms.auth.json`

Add into file `cms/envs/aws.py`
```python
EDX_API_KEY = AUTH_TOKENS.get("EDX_API_KEY")
INSTALLED_APPS += (
    'open_edx_api_extension_cms.apps.OpenEdxApiExtensionCmsConfig',
)
```

Add into file `cms/urls.py`
```python
urlpatterns += (
    url(r'^api/extended/', include('open_edx_api_extension_cms.urls', namespace='api_extension')),
)
```
