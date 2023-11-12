import subprocess
import datetime
import pyodbc

# MySQL configuration
db_host = 'localhost'
db_user = 'root'
db_password = '5002nevsmai!'
db_name = 'pythonlogin'

# Backup directory
backup_dir = '/path/to/backup/directory/'

# Generate a timestamp for the backup file
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
backup_file = f'{db_name}_backup_{timestamp}.sql'

# Create the mysqldump command
mysqldump_cmd = [
    'mysqldump',
    '--user=' + db_user,
    '--password=' + db_password,
    '--databases',
    db_name
]

# Run the mysqldump command and save the backup to a file
backup_path = backup_dir + backup_file
with open(backup_path, 'wb') as backup_file:
    subprocess.run(mysqldump_cmd, stdout=backup_file)

print(f'Backup saved to: {backup_path}')