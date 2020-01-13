# a11yWebEdit
Online HTML/CS/Javascript code editor similiar in function to jsfiddle, but more accessible and additional features for testing code samples for accessibility
<hr>
<h3>Dependencies/build instructions:</h3>
<code>pip install -r requirements.txt</code>
<p>Install required dependencies</p>

## Apache Configuration Files

### Example with Shibboleth Support

```
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

