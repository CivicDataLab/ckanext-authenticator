import ckanext.emailauth.actions.create as create
import ckanext.emailauth.actions.get as get
import ckanext.emailauth.actions.update as update
import ckanext.emailauth.actions.auth as auth
import ckanext.emailauth.logic.register_auth as authorize
import ckanext.emailauth.logic.validators as validators
import ckanext.emailauth.model as users_model
import ckanext.emailauth.user_extra_model as user_extra_model
from ckanext.emailauth import blueprint
from ckanext.emailauth.settings import BLUEPRINT, IS_FLASK_REQUEST

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from pylons import config


class AutheticatorPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurable)
    plugins.implements(plugins.IConfigurer, inherit=False)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.IActions)
    plugins.implements(plugins.IAuthFunctions)
    plugins.implements(plugins.IValidators)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')

    def get_helpers(self):
        return {}

    def is_fallback(self):
        return False


    def before_map(self, map):
        map.connect('userreset', '/user/reset',
                    controller='ckanext.authenticator.controllers.user:UserNewController',
                    action='request_reset')
        return map

    def after_map(self, map):
        return map

    def get_actions(self):
        return {

        }

    def get_auth_functions(self):
        return {

        }

    def configure(self, config):
	pass

    def get_validators(self):
        return {
            u'user_email_validator': validators.user_email_validator,
            u'user_name_validator': validators.user_name_validator
        }
