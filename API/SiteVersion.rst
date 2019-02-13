##############
Site Version
##############


Overview
========
NOTE: this is not enabled at this time.

SiteVersion contains related Site settings that are versionable, e.g. Theme, Style, etc. Normally when you fetch the Site information, the version will be joined so you don't need to fetch the SiteVersion independently in most cases.

API
===
/Api/SiteVersion

A generic call to this API will return ALL versions for ALL sites that you have access to edit. If you want to limit by a specific site, you will need to pass in the site ID, e.g. `/Api/Site/100/SiteVersion`