import os

oracle_username = os.getenv('ORACLE_USERNAME', 'system')
oracle_password = os.getenv('ORACLE_PASSWORD', 'oracle')
oracle_service_name = os.getenv('ORACLE_SERVICE_NAME', 'FREEPDB1')
oracle_hostname = os.getenv('ORACLE_HOSTNAME', 'localhost')
oracle_port = int(os.getenv('ORACLE_PORT', 1521))
