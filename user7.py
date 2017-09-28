#Message using twitter
#!/usr/bin/python

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys
import StringIO
import atexit

# Back up stdout and stderr. We'll overwrite them by StringIO to save the
# output to a string.
stdout_copy = sys.stdout
stderr_copy = sys.stderr

f = StringIO.StringIO()

sys.stdout = f
sys.stderr = f

# The MIME message we're going to wrap the program's output in.
msg = MIMEMultipart()

# This is the boundary I set in my crontab file. Kludgy, but I knew no other
# way to send multipart files from cron. To reproduce it, add the following
# to your crontab:
#
# CONTENT_TYPE='multipart/mixed; boundary="------------040907050602020300000601"'

msg.set_boundary('------------040907050602020300000601')


# At exit, print f's contents as a MIME message.
def flush_f():

    # Rewind the f StringIO so that f.read() will read all the data.
    f.seek(0)
