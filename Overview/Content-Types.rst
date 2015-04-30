Content Types
=============

What Is a Content Type
----------------------

Every :doc:`page is a View </2.0/Overview/Pages>` which is associated with a specific Content Type, e.g. Article, Map, Form, Video, etc. A Content Type is owned by a specific Vendor, and references a Controller that resides in a specific Bundle. The Controller is the PHP code that determines the actions for a specific page (and usually tells the page to display the content of the page according to the layout of a Twig template by the same name).

.. _overview-restricting-to-services:

Restricting to Services
-----------------------

A Content Type is also associated with a specific service, and sites will have access to any Content Types belonging to services that they are subscribed to. For example, **Article** is Content Type that is available to everyone. But **CMS** is a service with a lot of Content Types that are only available to Gutensite, and all those content types are the pages that power the CMS Control Panel, e.g. Dash, Aerial Menu, Content List, Editing pages, etc.


.. _overview-functionality-content-types:

Functionality Content Types
---------------------------

Many Content Types are pages that interact with multiple entities, e.g. a Stream is a list page that shows all the content that is tagged to that Stream, which may include Articles, Videos, Maps, Images, etc. Or a User Sign-In page authenticates a specific User from the User entity, but it isn't creating or displaying information about that entity.


.. _overview-entity-content-types:

Entity Content Types
--------------------

Other Content Types will actually be the entity itself, e.g. the details page of an Article is an Article entity that displays just that one article's content. Entity Content Types must have define an Entity associated with it, so that multiple instances of this entity can be persisted to the database, e.g. if you plan on writing more than one article each article will be a separate database record for each.