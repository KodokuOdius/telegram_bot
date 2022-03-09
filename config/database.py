import config.simplePostgrConnector as Connector
from . import settings

DB = Connector.PostgrDB(
    database_name=settings.database,
    user=settings.user,
    user_password=settings.user_password,
    host=settings.host,
    port=settings.port
)