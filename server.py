#!/usr/bin/env python
from flask import Flask, jsonify
from configuration import *
import urllib2

app = Flask(__name__)

####################################################################
# Routes
####################################################################
@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'name': 'JIRA Secure Calendar',
        'author': 'Christopher Su',
        'website': 'http://christophersu.net',
        'source': 'https://github.com/csu/jira-secure-cal',
        'usage': 'GET /cal/<filter_id>/<date_field_name>/<show_version>'
    })

@app.route('/cal/<filter_id>/<date_field_name>/<show_version>/', methods=['GET'])
@app.route('/cal/<filter_id>/<date_field_name>/<show_version>', methods=['GET'])
def get_calendar_secure(filter_id, date_field_name, show_version):
    if show_version not in ['false', 'False', '0', '']:
        show_version = 'true'  # any value that isn't one of the above will result in versions shown
    else:
        show_version = 'false'
    return urllib2.urlopen(JIRA_BASE_URL + "/plugins/servlet/calendar?searchRequestId=" + filter_id + "&dateFieldName=" + date_field_name + "&showVersions=" + show_version + "&os_username=" + JIRA_USERNAME + "&os_password=" + JIRA_PASSWORD).read()

@app.route('/cal/<filter_id>/<date_field_name>/', methods=['GET'])
@app.route('/cal/<filter_id>/<date_field_name>', methods=['GET'])
def get_calendar_secure_default(filter_id, date_field_name):
    return get_calendar_secure(filter_id, date_field_name, 'true')

####################################################################
# Start Flask
####################################################################
if __name__ == '__main__':
    app.run(debug=True)
