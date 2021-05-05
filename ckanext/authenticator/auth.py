import logging
from zope.interface import implementer
from repoze.who.interfaces import IAuthenticator
from ckan.model import User
import ckan.plugins as plugins

log = logging.getLogger(__name__)


@implementer(IAuthenticator)
class CustomAuthenticator(object):

    def authenticate(self, environ, identity):
        if not ('login' in identity and 'password' in identity):
            return None

        login = identity['login']
        user = User.by_name(login)

        is_email = plugins.toolkit.config.get('ckan.authenticator.email', '').strip().lower() == 'true'

        if user is None and is_email:
            users = User.by_email(login)
            try:
                user = users[0]
            except:
                user = None

        if user is None:
            log.debug('Login failed - {} not found'.format(login))
        elif not user.is_active():
            log.debug('Login as {} failed - user isn\'t active'.format(login))
        elif not user.validate_password(identity['password']):
            log.debug('Login as {} failed - password not valid'.format(login))
        else:
            return user.name

        return None
