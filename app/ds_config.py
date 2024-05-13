# ds_config.py
#
# DocuSign configuration settings

DS_CONFIG = {
    "ds_client_id": "",  # The app's DocuSign integration key
    "ds_client_secret": "",  # The app's DocuSign integration key's secret
    "organization_id": "{ORGANIZATION_ID}", # A GUID value that identifies the organization
    "app_url": "http://localhost:3000",  # The URL of the application. Eg http://localhost:5000
    # NOTE: You must add a Redirect URI of appUrl/ds/callback to your Integration Key.
    #       Example: http://localhost:5000/ds/callback
    "authorization_server": "https://account-d.docusign.com",
    "allow_silent_authentication": False,  # a user can be silently authenticated if they have an
    # active login session on another tab of the same browser
    "target_account_id": None,  # Set if you want a specific DocuSign AccountId,
    "github_example_url": "https://github.com/docusign/code-examples-python/tree/master/app/eSignature/examples/",
    "example_manifest_url": "https://raw.githubusercontent.com/docusign/code-examples-csharp/master/manifest/CodeExamplesManifest.json",
    "documentation": "",  # Use an empty string to indicate no documentation path.
}