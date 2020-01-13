# a11yWebEdit
Online HTML/CS/Javascript code editor similiar in function to jsfiddle, but more accessible and additional features for testing code samples for accessibility and supporting the use in online courses.



## Dependencies/build instructions

* Python 3.6
* Django 2.2


### Installing Python Dependencies in a Virtual Envirobment

```
pip install -r requirements.txt
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

