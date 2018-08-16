########
Overview
########

Aside from handling regular website page requests, Sitetheory also handles all API requests through the /Api url on any domain. Sitetheory is a RESTful API using the standard methods of (GET, PUT, POST, DELETE, etc) for interaction with all entities and standard actions for viewing, creating, editing, and deleting content. Everything is accessible through the API and can be requested in JSON or XML. Access is controlled through a robust permissions system (based on your user account), with granular role or user based access to assets (site, bundles, content type, specific records or even specific fields). Additional SOAP style requests are available in the API for advanced filtering, e.g. you can pass in options to a custom Entity API Controller, e.g. ContentApiController accepts "options" `?options[showContentInfo]=true.`


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
    {"meta":{"options":{"showContentInfo":true,"allRouting":true}}}


Payload
=======
The `payload` is the entity data that should be created or edited on the database. The entity may be a nested object of associated entities. The `payload` can also be a collection of entities.


Example of Full Convoy
======================
This could be a typical response from the API.

.. code-block:: javascript
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

We often need to customize the data for specific entities, e.g. if an Profile is requested (or any Content), by default we also want to fetch the Route, the best version, and the related meta data for profiles. So in each entity's custom API controller we extend methods from the `EntityApiController` to modify the database lookup (e.g. join additional tables). So each Entity API Controller has full control over the lifecycle of the request.

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
This is where the crazy starts. This persists changes to the entities (e.g. for PUT, POST and DELETE methods). This is smart enough to persist cross entity managers! It also references the Entity Annotations to determine CRUD access level on a per field basis.

- Uses Tree Building to Navigate Nested Entities (this is where the crazy starts)
- Hydrates any Entities that Haven't Been Fetched
- Merges in Changes for Persisting
- Validates CRUD permissions on every nested entity and field.
- Handles AutoVersioning of Versionable Entities

Many problems with the API are likely caused by issues in the Persister with permissions that result in changes to entities (or fields) to be discarded.

[TODO] Alex needs to explain Tree Building in more detail.


finalize()
----------
Finalize Structures the entity data that you send back from the API to the requesting script. It is called for all methods (e.g. GET, PUT, POST, etc). The `finalizeDefault()` is often customized to manipulate data before the request is returned. (see ContentApiController for example.)

manifest()
----------
This is a special functionality to "Manifest" an empty new entity and it's associated parents and/or children. This should be added entity API controllers that have manual associations that need to be manifested, e.g. Content Integration (see ContentApiController).



********************
Advanced API Options
********************


Limits and Paging
=================
[TODO]
You can limit the amount of records returned in each request by passing in options through the meta (see the list page component to see how we send these requests).