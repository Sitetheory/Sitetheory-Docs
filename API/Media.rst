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


API SAMPLES
===========

Create Media
--------------------------------------
Creating new Media is slightly more complicated than other content types because we need to upload a file first, then create a new Media record and associate that file with the Media record. Fortunately, we have a Media App server that handles the upload of files and it then it sends the POST command to the API to create the Media record and associates the file. The Media App server returns the results and you can do subsequent GET or PUT commands to interact with the media.

Our Media App server supports Multipart file uploads if you want to upload multiple files at once.

**Required:**
- `session` - You must include the session ID in the post URL
- Body of Post must be formatted as a Multipart file upload, with the fields and files split up with boundary separators.

**URL:** POST https://app.sitetheory.io:3000/?session=SESSIONID


.. code-block:: javascript
    :caption: API POST

    ------WebKitFormBoundaryyNWzAjJ1ALa1ZByI
    Content-Disposition: form-data; name="key"

    Avocado.jpg
    ------WebKitFormBoundaryyNWzAjJ1ALa1ZByI
    Content-Disposition: form-data; name="acl"

    private
    ------WebKitFormBoundaryyNWzAjJ1ALa1ZByI
    Content-Disposition: form-data; name="Content-Type"

    image/jpeg
    ------WebKitFormBoundaryyNWzAjJ1ALa1ZByI
    Content-Disposition: form-data; name="filename"

    Avocado.jpg
    ------WebKitFormBoundaryyNWzAjJ1ALa1ZByI
    Content-Disposition: form-data; name="file"; filename="Avocado.jpg"
    Content-Type: image/jpeg


    ------WebKitFormBoundaryyNWzAjJ1ALa1ZByI--


Fetch All Media (with paging)
-------------------------------
**URL:** GET  /Api/Media

Fetch Specific Media by ID
---------------------------
**GET**  /Api/Media/2


Edit Media
-----------
Note: You can just send only the fields you want to update
Required:
- `id` - you must specify the ID you are editing (best practice is to include it in the PUT URL).

**URL:** PUT /Api/Media/2

.. code-block:: javascript
    :caption: API PUT

    {
       "title": "New Foo Title for Image"
    }







Filter
------
-Filter Media by Mime Type, e.g. /Api/Media?q=mime[:]video (mime field contains "video")