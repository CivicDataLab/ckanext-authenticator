======================
ckanext-authenticator
======================

.. Put a description of your extension here:
   What does it do? What features does it have?
   Consider including some screenshots or embedding a video!

CKAN Authenticator for custom authentication usage

------------
Requirements
------------

Supports Python 2.7 and Python 3.8, tested with CKAN 2.8.4 / CKAN 2.9.1

------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-authenticator:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install extension into your virtual environment::

     python setup.py install

3. Follow step for Modifying Authenticator as metioned below in this documentation

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


-------------
Configuration
-------------

ckanext-authenticator has few custom configuration which is required before running::

      ckan.authenticator.email=true


----------------------------
Modifying Authenticator
----------------------------

In your ``who.ini`` (usually in ``/usr/lib/ckan/ckan-env/src/ckan/who.ini``) file add custom authenticator as::

      [authenticators]
      plugins =
          auth_tkt
          ckanext.authenticator.auth:CustomAuthenticator

This will enable CustomAuthenticator during all authenticator process, it allows you to do authentication via email (if username not found) if configuration enabled as mentioned above

------------------------
Development Installation
------------------------

To install ckanext-authenticator for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/civicdatalab/ckanext-authenticator.git
    cd ckanext-authenticator
    python setup.py develop

