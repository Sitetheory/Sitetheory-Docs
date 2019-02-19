####
Review
####

********
Overview
********

Review entity contains the information about a Review that is associated with a Content record (e.g. Product, Profile, Article, etc).


API SAMPLES
===========

Create Review and Associate with Media
--------------------------------------
Note: You can just send only the fields you want to set, the rest will set to default values.

**Required:**
- `content` - content is required because the review has to be associated with some content that is being reviewed.


**URL:** POST /Api/Review

.. code-block:: javascript
    :caption: API POST

    {
        "content": {
            "id":36518
        },
        "title":"Sample Title",
        "text":"Sample Description",
        "images":[{"id":100},{"id":101},{"id":102},{"id":103}],
        "documents":[{"id":104}],
        "latitude":"100.0000",
        "longitude":"50.000",
        "analysis":"{\"status\":\"good\"}",
        "device":"{\"device\":\"iphone\"}",
        "ip":"198.168.1.1",
        "rating":4,
        "isPurchased":true,
        "enableMarketing":false,
        "isReference":true,
        "barcode":"1234567890",
        "meta":"{\"customKey\":\"customValue123\"}"
    }


Fetch All Reviews (with paging)
-------------------------------
**URL:** GET  /Api/Review

Fetch Specific Review by ID
---------------------------
**GET**  /Api/Review/2


Edit Review
-----------
Note: You can just send only the fields you want to update
Required:
- `id` - you must specify the ID you are editing (best practice is to include it in the PUT URL).

**URL:** PUT /Api/Review/2

.. code-block:: javascript
    :caption: API POST

    {
        "title":"Update Title",
        "isPurchased":true
    }







"images":[{"tags":[],"storageService":null,"priority":null,"authorId":null,"storageServiceId":null,"duplicateId":null,"name":"Welcome-To-Agile","description":null,"embed":null,"prefix":"cdn.sitetheory.io/nest001/3034/Welcome-To-Agile","url":"//cdn.sitetheory.io/nest001/3034/Welcome-To-Agile-xs.jpg?v=1550289029","file":"sitetheorynest001.s3.us-west-2.amazonaws.com/nest001/3034/Welcome-To-Agile","filename":"Welcome-To-Agile","extension":"jpg","mime":"image/jpeg","bytes":98485,"bytesHuman":"96.18 KB","ratio":"200:129","dimensions":"1000,645","service":null,"meta":[],"id":3034,"siteId":9,"vendorId":null,"time":1550289028,"timeEdit":1550289029,"timeStatus":null,"status":1,"vendor":null,"editUser":null,"sentinel":{"view":true,"create":true,"edit":true,"delete":true,"publish":true,"design":true,"dev":true,"master":true,"summary":["View","Create","Edit","Delete","Publish","Design","Dev","Master"]},"lookupValues":[],"syndicated":0,"overwriteId":null,"selectedClass":true,"$$hashKey":"object:620"}],