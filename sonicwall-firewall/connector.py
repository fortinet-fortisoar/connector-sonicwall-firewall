"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from connectors.core.connector import Connector, get_logger, ConnectorError

from .operations import _check_health, operations, SonicWallFirewall

logger = get_logger('sonicwall-firewall')


class SonicWallConnector(Connector):
    def execute(self, config, operation, params, **kwargs):
        client = SonicWallFirewall(config)
        try:
            action = operations.get(operation)
            return action(client, params)
        except Exception as err:
            logger.error(str(err))
            raise ConnectorError(str(err))
        finally:
            if client:
                client.logout_user()

    def check_health(self, config):
        client = SonicWallFirewall(config)
        return _check_health(client)
