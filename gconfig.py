# Sample Gunicorn configuration file.
import multiprocessing

max_requests = 1000
max_requests_jitters = 50
bind = "0.0.0.0:9000"
backlog = 2048
workers = multiprocessing.cpu_count() * 2 + 1
# worker_class = 'sync'
worker_connections = 1000
timeout = 600
keepalive = 2
accesslog = "/var/log/crm/gunicorn-access.log"
errorlog = "/var/log/crm/gunicorn-error.log"
loglevel = "debug"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
