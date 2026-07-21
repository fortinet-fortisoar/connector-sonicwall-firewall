"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

from connectors.core.connector import Connector, get_logger, ConnectorError

from .operations import operations, SonicWallFirewall

logger = get_logger('sonicwall-firewall')


class SonicWallConnector(Connector):
    def execute(self, config, operation, params, **kwargs):
        client = SonicWallFirewall(config)
        try:
            logger.debug('Executing connector action: {}'.format(operation))
            action = operations.get(operation)
            logger.info(f"Invoking Action: {action}")
            return action(client, params)
        except Exception as err:
            logger.error(str(err))
            raise ConnectorError(str(err))
        finally:
            if client:
                client.logout_user()

    def check_health(self, config):
        client = SonicWallFirewall(config)
        if client:
            logger.info('connector is available')
            client.logout_user()

