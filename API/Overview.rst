########
Overview
########

Aside from handling regular website page requests, Sitetheory also handles all API requests through the /Api url on any domain. Sitetheory is a **REST**ful API using the standard methods of (GET, PUT, POST, DELETE, etc) for interaction with all entities and standard actions for viewing, creating, editing, and deleting content. Everything is accessible through the API and can be requested in JSON or XML. Access is controlled through a robust permissions system (based on your user account), with granular role or user based access to assets (site, bundles, content type, specific records or even specific fields). Additional SOAP style requests are available in the API for advanced filtering, e.g. you can pass in options to a custom Entity API Controller, e.g. ContentApiController accepts "options" `?options[showContentInfo]=true.`


********
SECURITY
********

IMPORTANT: All API calls should be to the HTTPS (SSL enabled) version of the URL (so you do not send information in plain text)!

The API will only allow you to interact with the data, based on your permissions. Some entities and records may be viewable by the public but not editable (e.g. Content) while others will be completely private (e.g. Billing). Others will be a mix, based on the annotation of the fields (e.g. User will expose the public username and avatar, but email and other private fields will be visible only to the user or a site administrator).



******
Basics
******

Methods
=======
Use the appropriate HTTP method to determine what kind of action you want to take. These RESTful methods are mapped to internal API methods that correlate with the default behavior.

`GET`: select one or more records, using our internal `getAction()` method.
`PUT`: edit one or more records, using our internal `setAction()` method.
`POST`: create one or more new entities, using our internal `newAction()` method.
`DELETE`: delete one or more entities, using our internal `delAction()` method.




Targeting a Specific Entity
===========================

You can target **any entity** by the specifying the entity name, e.g. Profile can be found at /Api/Profile, Users at /Api/User, etc.

For example, get all articles by doing a request for: `GET /Api/Article`
Or get a a specific article by appending the ID of the article: `Get /Api/Article/12345`


*************
API Structure
*************

Data is transferred to and from the API in a **payload**. When you receive a response from the API, you will receive a full **convoy** which will contain an outer object that will contain a `route`, `meta`, and `payload`. When you send to data to the API, the full convoy structure is optional (e.g. you don't need a `route` and `meta` because the essentials are specified in the Method and URI structure), so you could just send the payload as the top level (without a `payload` wrapper).


Route
=====

The `route` contains information for where the payload needs to go, whether it be a specific `controller`, `user`, or some other destination.  If this is filled out by using a `RESTful` request like `/Api/User` then we've already specified the controller in the URL and that is why it's not necessary to include a `route` when sending a request to the API.

Each API request is sent to a Controller based on the name of the Entity, e.g. if you want to edit the


Meta
====

The `meta` always contains a `method` and `status`, at the very least.  The methods are `get`, `set`, `new`, and `del`.  These can also be set by using a `RESTful` interface of `GET`, `PUT`, `POST`, and `DELETE`, respectively (which is why the Meta is not required for sending to the API).  There is also a `PATCH` option, but it is synonymous with `PUT`, as they are both designed to be a patchable request.  The `status` should not be set unless we encounter an error.  If nothing fails at the time of serialization, the system will automatically place a `SUCCESS` status into the correlating array.  There may be other bits of information inside the `meta` as required by the destination.

The `Meta` also be used to send data to the API, e.g. if an custom Entity API Controller needs extra `options` these can be put into the meta (instead of sending through the URL).

.. code-block:: javascript
    :caption: foo.js
    :name: bar.js

    {"meta":{"options":{"showContentInfo":true,"allRouting":true}}}


Payload
=======
The `payload` is the entity data that should be created or edited on the database. The entity may be a nested object of associated entities. The `payload` can also be a collection of entities.


Example of Full Convoy
======================
This could be a typical response from the API.

.. code-block:: javascript
    :caption: foo.js
    :name: bar.js

    {
        "route": {
            "controller": "User"
        },
        "meta": {
            "method": "get",
            "status": [
                {
                    "code": "SUCCESS",
                    "message": "Successfully executed request."
                }
            ]
        },
        "payload": [
            {
                "id": 1,
                "username": "Plato",
                "email": "plato@epistemology.edu"
            },
            {
                "id": 2,
                "username": "Aristotle",
                "email": "aristotle@metaphysics.edu"
            },
            {
                "id": 3,
                "username": "Socrates",
                "email": "socrates@maieutics.edu"
            },
            {
                "id": 4,
                "username": "Nietzsche",
                "email": "friedrich@nihilism.org"
            },
            {
                "id": 5,
                "username": "Kierkegaard",
                "email": "søren@existence.net"
            }
        ]
    }


Example of Simple Convoy
========================
This could be a typical PUT to the API to edit one field on the record. Note that there is no `payload` wrapper, it's just the single field (not even a full object). The API request would specify the `Route` Controller (User) and the ID being edited (so you don't need to include that in the payload):

`PUT /Api/User/1`

.. code-block:: javascript
    :caption: foo.js
    :name: bar.js

    {
        "email": "plato@epistemology.edu"
    }



*********************
API Request Lifecycle
*********************

1. The Request
==============
Send a request to the /Api and specify the HTTP **method** (required), **controller** (required), **ID** (optional), and **convoy** (optional).

2. The APIController
====================
All requests to /Api are routed to the **ApiController** (`\Sitetheory\CoreBundle\Controller\ApiController.php`) instead of the InitController that is normally executed for regular page loads. Like the InitController it controllers the high level routing and environment. It will detect the method being used (e.g. GET, PUT), as well as what entity you are targeting so that it loads the correct entity API controller. It passes this information to the custom entity API controller. It also interprets the convoy being requested or assembles it to send back to the requestor.

Initialize()
------------
This runs the `initialize()` method on the API controller which does the initial setup of the API (extended from the shared EntityApiController, see #4 below).

[METHOD]Action()
---------
Based on your requested method (e.g. GET) this will run the related action on the the Content Entity API Controller, e.g. `getAction()` (extended from the shared EntityApiController, see #4 below).

Finalize()
----------
This runs the `finalizer()` method on the API controller which does the initial setup of the API (extended from the shared EntityApiController, see #4 below).


3. Custom Entity API Controllers
================================

Every entity that is accessible in the API will have a controller, e.g. Article has a custom API controller found at **ArticleApiController** (`\Sitetheory\ArticleBundle\Controller\ArticleApiController.php`). This controller may just be a stub, because not every entity needs special API functionality (the default behavior is sufficient). But in this case the articles are a ContentType that function as a routable page on the site (e.g. like Profile, Event, Stream, etc), so this controller actually extends the shared **ContentApiController** (`\Sitetheory\CoreBundle\Controller\Content\ContentApiController.php`) because it shares a lot of similar functionality with all other page related Content.

**All** API controllers also extend the **EntityApiController** (`\Sitetheory\ComponentBundle\Controller\EntityApiController.php`), which does the heavy lifting for managing the lifecycle of an API request for selecting, editing, creating, and deleting records, e.g. standard searching/filtering, permissions control, etc.

We often need to customize the data for specific entities, e.g. if a Profile is requested (or any Content), by default we also want to fetch the Route, the best version, and the related meta data for profiles. So in each entity's custom API controller we extend methods from the `EntityApiController` to modify the database lookup (e.g. join additional tables). So each Entity API Controller has full control over the lifecycle of the request.

Custom Actions
--------------
Be aware that the bulk of the code referenced below are actually in related "default" methods, e.g. `initialize()` calls `initializeDefault()`. The default versions of these methods are used **most of the time**, but you can create custom actions, by telling the API to use a custom API action, e.g. `?options[action]=fancy` or `{"meta":{"options":{"action":"fancy"}}}`. This would make initialize() execute `initializeFancy()` which would also execute `getActionFancy()` instead of `getActionDefault()`. Then you can define these custom methods in your custom entity API controller.



4. The EntityApiController
==========================

This is a very high level overview of the lifecycle of the `EntityApiController`. We don't want to document this here in case there are changes. Instead, the code is heavily documented so you can read what it does there.


initialize()
------------
-Merge Default Options from Custom Controller (if exist)
-Get Options from Request URL, and Convoy Meta
-Manage Access Control (allowed actions for this Entity)


If no custom `action` is specified, the default version `initializeDefault()` method is run. This default method is often extended to instruct the API fetch additional associated entities. See `ContentApiController` for example.

Method Specific Actions
-----------------------
Depending on the type of Method requested, the relevant method will be used. Each action will verify that you have the right CRUD permissions to act on the entities, based on your permissions and the **Sentinel** (See :doc:`/1.0/Security/Overview` for more details about security and permissions).

- **GET** `getAction()`: This gets the requested records and return frames, which are then set in the convoy payload.

- **PUT** `setAction()`: This fetches the records being edited and then executes the `persist()` method to apply the changes to the records it just fetched and persist the changes to the database.

- **DELETE** `delAction()`: This deletes the requested records.

- **POST** `newAction()`: This creates new records.


persist()
---------
This persists changes to the entities (e.g. for PUT, POST and DELETE methods). This is smart enough to persist cross entity managers! It also references the Entity Annotations to determine CRUD access level on a per field basis.

This is where the crazy starts. You will have to step through this method line by line (and really it's the persister() that does the recursive "Tree Building").

- Uses "Tree Building" to recurse through nested entities.
- Hydrates Associated Entities (when an ID changes, e.g. Site.SiteVersion.theme changes to a new template).
- Validates CRUD permissions to edit on every nested entity and field.
- Merges in Changes for Persisting
- Handles AutoVersioning of Versionable Entities

Many problems with the API are likely caused by issues in the complex `persister()` with permissions that result in changes to entities (or fields) to be discarded.


finalize()
----------
Finalize Structures the entity data that you send back from the API to the requesting script. It is called for all methods (e.g. GET, PUT, POST, etc). The `finalizeDefault()` is often customized to manipulate data before the request is returned. (see ContentApiController for example.)


manifest()
----------
This is a special functionality to "Manifest" an empty new entity and it's associated parents and/or children. This should be added entity API controllers that have manual associations that need to be manifested, e.g. Content Integration (see ContentApiController).


***********
Admin Lists
***********

For the purpose of editing (e.g. on List Pages) in the admin context, the API adds the editUrl in the meta data it returns, so that you can know where entities should be edited. This is based on the entity's controller, but sometimes you need to specify an alternative URL. That can be easily customized for an entire entity by editing the entity's custom ApiController, e.g. for the Site entity, you edit the SiteApiController and add options like this:


.. code-block:: php
    :linenos:

    protected $options = [
            'altEditUrl' => [
                'bundle' => 'Hosting',
                'controller' => 'SiteSettingsEdit'
            ]
        ];

Or if you just want an alternative editUrl in specific widgets, just add it to the data attribute like this:


.. code-block:: javascript
    :caption: GET Variable

    data-api='{"options”:{“altEditUrl":{"bundle":"Hosting", "controller":"SiteSettingsEdit"}}}'


********************
Advanced API Options
********************


Limits and Paging
=================
The `meta` object of the response contains pagination information that describes how the total records, current records on this page, and total pages.

.. code-block:: javascript
    :caption: Pagination

    {
        "pagination": {
            "countCurrent": 25,
            "countTotal": 100,
            "pageCurrent": 2,
            "pageTotal": 4
        }
    }


You can modify the how many records are returned and which page you want to view by passing variables to the API either through the URL or through the meta.

.. code-block:: javascript
    :caption: Meta

    {"meta":{"options":{"page":2,"limit":10}}}

.. code-block:: javascript
    :caption: GET Variables

    /Api/Content?page=2&limit=10



Paging
------
By default the API loads the first page (if more records than one page exist), so you can pass in a variable to specify the page you wish to receive.

Variable: `page` or `p`
Type: integer
Example: `/Api/{ENTITY}/?p=2`

Paging Type
-----------
By default all content will be paged after a specific max limit.
TODO: this may not be implemented yet (or relevant since infinite scroll is really just the front end UI making paging requests as you scroll.
Variable: `pagingType`
Values: `pager` (default), `infiniteScroll`
Example: `/Api/{ENTITY}/?pagingType=infiniteScroll`


Limit
-----
By default the API returns a fixed number of results (e.g. 25). If you wish to modify the number, you can pass in a limit.

Variable: `limit` or `ql` ("query limit")
Value: integer
Example: `/Api/{ENTITY}/?ql=10

Offset
-----
By default the API returns a fixed number of results (e.g. 25). If you wish to modify the number, you can pass in a limit.

Variable: `offset` or `qlo` ("query limit offset")
Value: integer
Example: `/Api/{ENTITY}/?qlo=5


Sort
====
By default the API sorts by timeEdit DESC (most recent).

Variable: `sort` or `qs` ("query sort")
Value: string of valid field name, which are visible in the meta.searchable fields list in the API meta object.
Example: `/Api/{ENTITY}/?qs=versions.title

If you need to sort by more than one field, you can pass a comma separated list of sort options.
Example: `/Api/{ENTITY}/?qs=versions.title ASC, versions.pullout DESC

Sort Order
==========
By default the API sorts by DESC. If you don't want to modify the field that is sorting and only want to modify the order, you can pass in just the sortOrder.

Variable: `sortOrder` or `qso` ("query sort order")
Value: `ASC`, `DESC`
Example: `/Api/{ENTITY}/?qso=ASC




Output Format
=============
By default all content will be returned in JSON format, but if you prefer XML, RSS, ICS, or other relevant formats you can specify the output format
Variable: `output`
Values: json (default), xml, rss, ics
Example: `/Api/{ENTITY}/?output=xml`


Keyword Search Queries
==============
The query parameter lets you search all the entity records, on all fields annotated as "searchable". This allows you to pass a string from a user search field exactly as formatted (giving the user more power to do complex searches). (NOTE: if you want to do searches on the API from a programmatic perspective, you should use the `filter` format specified later in this document.)

Variable: `query` or `q`
Values: string
Example: `/Api/{ENTITY}/?q=foobar`

TODO: specify the format for limiting search to specific fields

Advanced Keyword Search Filtering
------------------
You can pass in specific fields through the query field, e.g. "title=my title". This removes the filters that were found, so other parsing will not reference them. To search for strings for all searchable fields, in addition to value for a specific field, put the general string at the front of the search and put the field searches at the end


Comparison Shortcuts
--------------------
[=] or [!=] - comparison means the values exactly equal or do not exactly equal each other. e.g. title="my title"
[>] or [<] or [>=] or [<=] - comparison means the values are greater than or equal. e.g. timeEdit>2014-10-14
[:] or [!:] or [LIKE] or [NOT LIKE] - comparison means "contains" instead of '=' which means "exactly equal".
[?] or [!?] or [REGEXP] or [NOT REGEXP] - comparison means the following is a regular expression.
[#] or [!#] or [IN] or [NOT IN] - comparison means the following is an IN comparison and the value should be separated by commas,
[!#] - comparison means the values are NOT IN the field.


You can do advanced searches on one or more specific fields by using a special field syntax ``FIELD[=]VALUE``, where ``FIELD`` is the field name (or a registered alias) and ``VALUE`` is the value (one or more words). The comparison can be:


- **exactly equals:** ``[=]`` or ``[!=]``
    Example: ``title[=]foo bar stache`` *(the title is exactly "foo bar stache")*

- **contains:** ``[:]`` or ``[!:]``
    Example: ``title[:]foo`` *(the title contains "foo" anywhere, e.g. "foobar" or "barfoodo")*

- **greater or less than:** ``[>]`` or ``[<]`` ``[>=]`` or ``[<=]``
    Note: if searching a time field, the human readable formats will be converted to a unix time stamp.
    Example: ``time[>]2015-05-01``


- **regular expression:** ``[?]`` or ``[!?]``
    Note: reserved Regular Expression special characters need to be commented out with a backslash "\".
    Examples:
        ``title[?]^foo[a-z]+ar`` (the title starts with "foo" followed by any character a-z followed by "ar", e.g. "foobar" or "foojar")
        ``title[!?]\(copy\)$`` (anything with a title that doesn't end in "(copy)")

- **in list:** ``[#]`` or ``[!#]`` *(the value is in the list of options)*
    Note: the value should be a comma separated list.
    Example: ``id[#]1,2,3`` *(id equals 1,2 or 3)*

Multi Part Filters
------------------
_**title[:]foo bar time[>]2014-10-14**_ - finds where title contains "foo bar" **and** time is greater than the date
_**baz shazam title[:]foo bar**_ - finds where content includes baz and shazam in any field **and** "foo bar" only in the title field.


Target Nested Fields
--------------------
Many fields you want to search are on nested entities, so you must specify the field name in dot notation, e.g. when searching the /Api/Content the main Content entity has very few fields of interest, most of what you search is the contentVersion, so your search would be on the nested version entity, e.g. to search the title:

.. code-block:: javascript
    :caption: GET Variables

    /Api/Content?q=version.title[:]foo



Select and Unselect
======
NOTE: this shouldn't hurt UPDATES, since the API just updates the fields you provide, and if you are missing specific fields it won't modify them.

By default all readable fields will be returned in the API. If you only want to return specific fields, you can select which fields are returned.

Variable: `select` or `unselect`
Values: array of field names

Examples:

- `/Api/{ENTITY}/?select[]=foo&select[]=bar`
- `/Api/{ENTITY}/?unselect[]=baz&select[]=fuzz`


Filter
======
The simple string query parameter (above) can allow you to search all searchable fields. But if you want to search one or more fields specifically, you can pass in a filter as a single JSON array/object, or as key value pairs.

Variable: `filter`
Values: array with field name and value (for exact match) or JSON string as an array with `field`, `value` and `comparison`

Examples:

- `/Api/{ENTITY}/?filter[title]=foo&filter[price]=1000`
- `/Api/{ENTITY}/?filter=[{"field":"foo","value":"bar", "comparison":"LIKE"},{"field":"extension","value":"jpg"}]`
- `/Api/{ENTITY}/?filter={"field":"mime","value":"image", "comparison":"LIKE"}`

NOTE: the EntityApiController will compile these filters and confirm that you have permissions to search each requested field.


Flatten
=======

Variable: `flatten`

Alternative Edit URL
====================
If you need to lookup the URL for a content other than the current controller's corresponding Edit page, just pass in a bundle and controller.
Variable: `altEditUrl`
Value: Array of bundle and controller names.
Example: /Api/Content?altEditUrl[bundle]=foo&altEditUrl[controller]=bar


Special API Action
==================
Specify a special API action to run, e.g. "duplicate".
Variable: `apiSpecialAction`

Options:

 - "duplicate" - triggers duplication of an entity
 - "iterateVersion - iterates a versionable entity

Example: /Api/Content/12345?apiSpecialAction=duplicate


API Action
==========
Specify an alternative action (besides the default API action). This is an advanced feature if you have created a custom API controller that needs to do unique SOAP style actions that don't use the normal REST methods.

Variable: `action`


Show Assets
===========
Specify whether to show assets or not. By default assets are shown on the main entity if they exist, but in some contexts they may not be.
Variable: `showAssets`
Value: boolean (default: true, but depends on context)

Manifest a Version Parent
=========================
When manifesting a new entity that is versionable, it will twiddle the entity and manifest a version parent by default. But if you need to return the version entity directly, set this to false.

Variable: `manifestVersionParent`
Value: boolean (default: false)