
# coding: utf-8

import mailbox
from email.utils import parsedate
from dateutil.parser import parse
import itertools
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('kaz', '9r6pr9gncf')

# Download GMAIL inbox and point the path to your downloaded file
path = '/home/kaazim/Downloads/Takeout/Mail/All mail Including Spam and Trash.mbox'

# Open the mbox file with mailbox
mbox = mailbox.mbox(path)

# Function to sort the mail by date
def extract_date(email):
    date = email.get('Date')
    return parsedate(date)

sorted_mails = sorted(mbox, key=extract_date)
mbox.update(enumerate(sorted_mails))
mbox.flush()

# Organize the dates of email receipt as a list
all_dates = []
mbox = mailbox.mbox(path)
for message in mbox:
    all_dates.append( str( parse( message['date'] ) ).split(' ')[0] )

# Count the emails
email_count = [(g[0], len(list(g[1]))) for g in itertools.groupby(all_dates)]

# Output the first element
email_count[0]

# Graph the data using plotly
x = []
y = []
for date, count in email_count:
    x.append(date)
    y.append(count)

py.iplot( Data([ Scatter ( x=x, y=y )]) )

# Restyling of the graph
import plotly.tools as tls

tls.embed('https://plot.ly/~kaz/65')
