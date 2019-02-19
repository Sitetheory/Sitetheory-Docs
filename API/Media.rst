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
Creating new Media is slightly more complicated than other content types because we need to upload a file first, then create a new Media record and associate that file with the Media record. Fortunately, we have a Media App server that handles the upload of files and it then it sends the POST command to the API from the server to create the Media record and associates the file with that record. Then after it successfully uploads the file and creates the media record, it will return a result. So your app should wait for an Asynchronous reply, which will include a standard Media object in JSON. You can use that information to followup with subsequent API calls to edit the record or add the media to some other entity association.

If you are using HTML, this is as simple as a form that posts like this:

.. code-block:: javascript
    :caption: API POST

    <form action="http://app.sitetheory.io:3000/?session=SESSIONID" method="post" enctype="multipart/form-data">
        <input type="file" name="file" id="file">
        <input type="submit" value="Upload" name="submit">
    </form>



**Required:**
- `session` - You must include the session ID in the post URL
- The body of the POST must be encoded as "multipart/form-data", with the fields and files split up with boundary separators.

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


**Sample Response**

.. code-block:: javascript
    :caption: API POST

    {
        "tags":[],
        "storageService":null,
        "priority":null,
        "authorId":null,
        "storageServiceId":null,
        "duplicateId":null,
        "name":"austin-schmid-134030-unsplash",
        "description":null,
        "embed":null,
        "prefix":"cdn.sitetheory.io/nest001/1000/foo-bar-baz",
        "url":"//cdn.sitetheory.io/nest001/1000/foo-bar-baz-xs.jpg?v=1550596025",
        "file":"sitetheorynest001.s3.us-west-2.amazonaws.com/nest001/1000/foo-bar-baz",
        "filename":"foo-bar-baz",
        "extension":"jpg",
        "mime":"image/jpeg",
        "bytes":977258,
        "bytesHuman":"954.35 KB",
        "ratio":"3:2",
        "dimensions":"2700,1800",
        "meta":[],
        "id":1000,
        "siteId":100,
        "time":1550596023,
        "timeEdit":1550596025,
        "status":1
    }



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