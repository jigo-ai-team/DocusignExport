

## Introduction

This repo is a Python 3 application that supports the following authentication workflows:

* Authentication with Docusign via [Authorization Code Grant](https://developers.docusign.com/platform/auth/authcode).
When the token expires, the user is asked to re-authenticate. The refresh token is not used.

  
## Installation

### Prerequisites

1. A free [Docusign developer account](https://go.docusign.com/o/sandbox/); create one if you don't already have one.
2. Docusign app and integration key that is configured to use either [Authorization Code Grant](https://developers.docusign.com/platform/auth/authcode/) 

   For authentication flows:  
   
   If you use this launcher on your own workstation, the integration key must include a redirect URI of http://localhost:3000/ds/callback

   If you host this launcher on a remote web server, set your redirect URI as   
   
   {base_url}/ds/callback
   
   where {base_url} is the URL for the web app.

3. Install Python 3.8

### Installation steps

1. In your command-line environment, switch to the folder:  
   `cd <DocuSign_PyCharm-FINAL>
2. To install dependencies, run: `pip3 install -r requirements.txt`  (or pipenv can be used)
3. To configure the app/ds_config.py.
   **+ Integration Key** GUID and save it in ds_config.py as your `ds_client_id`.
   **+ ADD SECRET KEY**. Copy the secret key and save it in ds_config.py as your `ds_client_secret`.
   **+ ADD URI**, and set a redirect URI of http://localhost:3000/ds/callback. 

4. Run the launcher:`python run.py`  
   **Note:** You will need to alias the python command to run Python 3 or use `python3 run.py`
5. Open a browser to http://localhost:3000

