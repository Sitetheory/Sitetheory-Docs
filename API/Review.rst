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
- `rating` - rating is required so the review has some numerical value.


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
- `id` - you must specify the ID you are editing in the PUT URL.

**URL:** PUT /Api/Review/2

.. code-block:: javascript
    :caption: API POST

    {
        "title":"Update Title",
        "isPurchased":true
    }


Add Media
-----------
Note: You can just send only the fields you want to update
Required:
- `id` - you must specify the ID you are editing in the PUT URL.

**URL:** PUT /Api/Review/2

.. code-block:: javascript
    :caption: API POST

    {
        "images":[{"id":100},{"id":101},{"id":102},{"id":103}],
        "documents":[{"id":104}],
    }
