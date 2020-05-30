# LittleSnitchTool

Reads in a local copy of [easyList-blacklist.json](https://raw.githubusercontent.com/mozilla-services/shavar-prod-lists/master/easyList-blacklist.json) that is hosted on Mozilla's [github repo](https://github.com/mozilla-services/shavar-prod-lists), and generates a little snitch rule file (.lsrules) which blacklists all websites in that file for all processes in the system.

This blocks a number of websites (e.g. twitter), and breaks a number of other ones (e.g. a few that use the blocked CDNs to actually deliver content rather than track).


