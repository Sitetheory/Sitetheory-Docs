#####
Media
#####


Overview
========

Media are files that are files that are used on a site, which can be uploaded and hosted by Sitetheory  (e.g. image, MP3, PDF, etc) or linked externally (e.g. Youtube embed code or links, or third party file server URL.

* Image: multiple size versions stored on our file servers.
* Video: stored in database as a URL to the third party streaming service (e.g. Youtube, Vimeo).
* Audio: stored on our file servers or a URL to a third party file server
* Document:  stored on our file servers or a URL to a third party file server


API
===
/Api/Media


Filter
------
-Filter Media by Mime Type, e.g. /Api/Media?q=mime[:]video (mime field contains "video")