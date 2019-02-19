#######
Product
#######


Overview
========

The Product entity is a *routable* Content Type (i.e. "page"). This API lets you fetch all Product content specifically (without other types of content mixed in), which is useful in many cases where you only want products. It inherits all the standard functionality and features of a Content entity. See Content API for more details :doc:`/1.0/API/Content`.


API SAMPLES
===========

Create Product and Associate with Media
--------------------------------------
Note: You can just send only the fields you want to set, the rest will set to default values.

**Required:**
- `contentType` - contentType is required (in order to specify what type of content you are creating, e.g. Product, Article, etc). Product is contentType.id = 181.
- `version` - the version object is required because the review has to be associated with some content that is being reviewed.
- `version.meta` - the meta object is associated with the version. It is not actually required, but it includes specific fields that make the Product unique from other content, e.g. price. So it's basically required if you are creating a product.


Products, like all content must be published in order to be publicly visible. You can set the `version.timePublish` manually or set it to the current time with the value "API::NOW"

**URL:** POST /Api/Review

.. code-block:: javascript
    :caption: API POST

    {
        "contentType":{
            "id": 181
        }
        "version": {
            "meta":{
                "price": 100.00
                "isOrganic": true
            }
            "title":"Foo Bar Title",
            "subtitle":"Lorem ipsum dolor",
            "text":"Some text describing the product.",
            "timePublish":"API::NOW",
            "timeCustom":null,
            "images": [{"id":100},{"id":101},{"id":102},{"id":103}]
        }
    }


Fetch All Products (with paging)
-------------------------------
**URL:** GET  /Api/Product

Fetch Specific Product by ID
---------------------------
**GET**  /Api/Product/2


Edit Product
-----------
Note: You can just send only the fields you want to update
Required:
- `id` - you must specify the ID you are editing (best practice is to include it in the PUT URL).

**URL:** PUT /Api/Product/2

.. code-block:: javascript
    :caption: API PUT

    {
        "version": {
            "title":"Update Title",
            "meta": {
                "price": 99.99
            }
    }







