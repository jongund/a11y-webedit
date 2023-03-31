# a11y-webedit
Online HTML/CS/Javascript code editor similiar in function to jsfiddle, but more accessible and additional features for testing code samples for accessibility and supporting the use in online courses.



## Dependencies/build instructions

* Python 3.6
* Django 2.2
* Apache 2.4
* Postgres 9.4


### Installing Python Dependencies in a Virtual Envirobment

```
pip install -r requirements.txt
```

## Secrets File

The `secrets.json` file is used for configuring A11yWebEdit for a particular machine and URL.
It is also used to idenitfy if Shibboleth (inCommon) or the built-in Django registration system will be used for autheticating users.

### Example Secrets file

```
{
  "DEBUG":           true,
  "SITE_URL":        "{site URL}",
  "SHIBBOLETH_ENABLED": true | false,
  "SHIBBOLETH_URL": "{site URL}/Shibboleth.sso/Login",
  "SHIBBOLETH_NAME": "",
  "SHIBBOLETH_AUTH": "{urn:mace:incommon:uiuc.edu}",
  "SHIBBOLETH_SUPERUSER": "{email address of shibboleth super user}",
  "SITE_NAME":       "{name of site, for example WebEdit}",
  "FILENAME" :       "secrets.json",
  "SECRET_KEY" :     "{random string of characters used by Django}",
  "DATABASE_ENGINE": "django.db.backends.postgresql_psycopg2",
  "DATABASE_NAME":   "{databse name}",
  "DATABASE_USER":     "{database user name}",
  "DATABASE_PASSWORD": "{databased user password}",
  "DATABASE_HOST":     "localhost",
  "DATABASE_PORT":     "5432",
  "ALLOWED_HOSTS" :  ["{SITE_NAME}"],
  "EMAIL_HOST":      "localhost",
  "EMAIL_PORT":      25,
  "EMAIL_USE_TLS":   false,
  "EMAIL_HOST_USER": "no-reply@{site domain name}",
  "EMAIL_HOST_USER_PASSWORD": "{password for no-replay e-mail}",
  "ACCOUNT_ACTIVATION_DAYS" : 3,
  "CONTACT_EMAIL" :    "{email address}",
  "ADMIN_USERNAME":  "{username}",
  "ADMIN_EMAIL":  "{email}",
  "ADMIN_FIRST_NAME":  "{first name}",
  "ADMIN_LAST_NAME":  "{last name}",
  "ADMIN_PASSWORD":  "{intial password for admin}"
}
```

## Apache Configuration Files

### Example with Shibboleth Support

```
</VirtualHost>
(webedit-prod) [root@aitg conf.d]# more webedit-dev.conf
WSGISocketPrefix  /var/run/wsgi

<Location /Shibboleth.ss>
  AuthType shibboleth
  ShibUseHeaders On
  Require shibboleth
</Location>

<VirtualHost *:443 >

  Servername  webedit-dev.disability.illinois.edu
  ServerAlias webedit-dev.disability.illinois.edu

  SSLEngine on
  SSLCertificateFile      /etc/pki/tls/fae2/fae2.crt
  SSLCertificateKeyFile   /etc/pki/tls/fae2/fae2.key
  SSLCertificateChainFile /etc/pki/tls/fae2/in-common-bundle.crt

  CustomLog logs/webedit-dev-access_log common
  ErrorLog  logs/webedit-dev-error_log

  Alias /static /var/www/webedit/webedit-dev/WebEdit/static/

  <Directory /var/www/webedit/webedit-dev/WebEdit/static>
    Require all granted
  </Directory>

  <Directory /var/www/webedit/webedit-dev>
    <Files wsgi.py>
     AuthType shibboleth
     Require shibboleth
    </Files>
  </Directory>

  WSGIDaemonProcess webedit-dev python-path=/var/www/webedit/webedit-dev:/var/www/venv/webedit-dev/lib/python3.6/site-packages
  WSGIProcessGroup  webedit-dev

  WSGIScriptAlias / /var/www/webedit/webedit-dev/WebEdit/wsgi.py

</VirtualHost>
```

### Example with Django Registration System

```
WSGISocketPrefix  /var/run/wsgi

<VirtualHost *:443 >

  Servername  webedit-staging.disability.illinois.edu
  ServerAlias webedit-staging.disability.illinois.edu

  SSLEngine on
  SSLCertificateFile      /etc/pki/tls/fae2/fae2.crt
  SSLCertificateKeyFile   /etc/pki/tls/fae2/fae2.key
  SSLCertificateChainFile /etc/pki/tls/fae2/in-common-bundle.crt

  CustomLog logs/webedit-staging-access_log common
  ErrorLog  logs/webedit-staging-error_log

  Alias /static /var/www/webedit/webedit-staging/WebEdit/static/

  <Directory /var/www/webedit/webedit-staging/WebEdit/static>
    Require all granted
  </Directory>

  <Directory /var/www/webedit/webedit-staging>
    <Files wsgi.py>
     Require all granted
    </Files>
  </Directory>

  WSGIDaemonProcess webedit-staging python-path=/var/www/webedit/webedit-staging:/var/www/venv/webedit-staging/lib/python3.6/site-packages
  WSGIProcessGroup  webedit-staging

  WSGIScriptAlias / /var/www/webedit/webedit-staging/WebEdit/wsgi.py

</VirtualHost>
```

