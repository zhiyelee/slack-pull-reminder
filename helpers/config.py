
import os
import sys

# repositories list where we will listen to and run check on
repositories = os.environ.get('REPOSITORIES')
REPOSITORIES = [r.lower().strip() for r in repositories.split(',')] if repositories else []

usernames = os.environ.get('USERNAMES')
USERNAMES = [u.lower().strip() for u in usernames.split(',')] if usernames else []

# default slack channel when updates will be sent to
SLACK_CHANNEL = os.environ.get('SLACK_CHANNEL', 'GEXT4PWUC')

# python log level
LOGLEVEL = os.environ.get("LOGLEVEL", "INFO")
LOG_FILE = os.environ.get("LOG_FILE", "app.log")

# redis config
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get('REDIS_PORT', '6379')
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', '0')

try:
    SLACK_API_TOKEN = os.environ['SLACK_API_TOKEN']
    GITHUB_API_TOKEN = os.environ['GITHUB_API_TOKEN']
    ORGANIZATION = os.environ['ORGANIZATION']
except KeyError as error:
    sys.stderr.write('Please set the environment variable {0}'.format(error))
    sys.exit(1)