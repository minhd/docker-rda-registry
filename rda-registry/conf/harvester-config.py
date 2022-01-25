import ssl

# harvester config
test_limit = 999999
polling_frequency = 30
max_up_seconds_per_harvest = 7200

# registry response url
response_url='http://localhost/api/registry/import'

# directories
run_dir = '/opt/apps/harvester/current/'
data_store_path= '/var/data/harvester/harvested_contents/'
data_dir='/var/data/harvester/'
log_dir= '/var/log/harvester/'

# logging
log_level='DEBUG'
redis_poster_host = 'redis'

# admin email
admin_email_addr = "minh.nguyen@ardc.edu.au"

# java & saxon library
java_home='/usr/bin/java'
saxon_jar='/usr/share/java/saxon-8.9.0.3.jar'

# database connection
db_host='mysql'
db_user='webuser'
db_passwd='webuser'
db='dbs_registry'
db_port=3306

# database configuration
harvest_table = 'harvests'
harvester_specific_datasource_attributes = "'xsl_file','title','harvest_method','uri','provider_type'," \
                                           "'advanced_harvest_mode','oai_set', 'last_harvest_run_date', " \
                                           "'harvest_params','user_defined_params', 'harvest_frequency'"
# ssl
context = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
#context.load_cert_chain(certfile="<pathto:cert.pem>")

# max number of  asynchronous connection that the harvester will hit any given client increase it too much and they might just blacklist us
tcp_connection_limit=5