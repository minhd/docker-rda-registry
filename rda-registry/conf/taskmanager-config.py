#### CONFIGURATION FILE FOR ARDC's Task Manager (Docker ENV) #####
################################################################

# how ofter the taskmanager checks for a new PENDING tasks
polling_frequency = 5

# howmany tasks can be running concurrently 
max_thread_count = 2

# how long (in seconds) a sigle task can run before alarm is raised and task termineted (4 hours)
max_up_seconds_per_task = 21600

# the location of the code
run_dir = '/opt/apps/taskmanager/current/'

# not used variables as of (2020)
admin_email_addr = "minh.nguyen@ardc.edu.au"
response_url='http://localhost/api/task/exe/'
maintenance_request_url = 'http://localhost/api/task/run/'
data_store_path = '/var/data/taskmanager/result_contents'

# the log directory the taskmanager is writing its daily logs
log_dir= '/var/log/taskmanager/'

#log lever verbosity
log_level = "INFO"

# database connection
db_host='mysql'
db_user='webuser'
db_passwd='webuser'
db='dbs_registry'
db_port=3306
tasks_table='tasks'

# the installation folder of the registry
php_shell_working_dir="/opt/apps/registry/current/"