# JIRA Secure Calendar
What does this do? This allows you to securly generate and access calendars from JIRA JQL queries and date fields (including custom date fields) through a web interface.

## Features
* Make calendars from JQL queries and issue date fields
* Make calendars available to external calendar clients without exposing JIRA login credentials

## Requirements
* Python 2.x
* JIRA installation with the JIRA Calendar plugin installed

## Dependencies
* Flask

## Usage
* (Install dependencies using with with `pip install -r requirements.txt`.)
* Modify `configurations.py.sample` and add your JIRA configuration information. Rename it to `configurations.py`.
* Start the web server by running `python server.py`.
* Subscribe your calendar client to `http://YOUR_WEB_SERVER/cal/<JQL saved filter id>/<date field name>/<show versions>`
* For example, http://my.web.server/cal/10000/duedate/false

## Notes
* The date field name can be a custom field (ex. customfield_10000)
* The "show versions" option defaults to true (anything that isn't 'false', 'False', or '0' will make it true)
* The `http://<web server>/cal/<JQL saved filter id>/<date field name>` endpoint also exists and defaults show versions to true

## License
JIRA Secure Calendar is open-source licensed under the Free Software Foundation's GNU Affero General Public License (AGPL). For proprietary applications, a commercial license may be purchased. [Contact me](mailto:christophersu9@gmail.com) for more information.