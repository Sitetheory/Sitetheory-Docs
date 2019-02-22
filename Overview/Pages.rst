#####
Pages
#####

Every page or module is a `Content` entity associated with a specific ContentType. ContentTypes are unique content like an Article, Profile, Form, Video, etc. The Content is a simple generic record that exists to provide a permanent id for each page. This permanent ID is necessary because a content (i.e. the page or content) can be versioned and each version will have a different ID, so there has to be one unifying ID that all other associated entities can reference.

********************
Content Associations
********************


Content (content)
=======
The `Content` entity is a :doc:`versionable </1.0/Overview/Versioning>` entity, so `Content`  which has a lot of associations with other entities that provide additional information about the page, but these are the most important associations to understand how a page is a built and how it interacts with the site

ContentType (content.contentType)
=================================
The `ContentType` entity defines the type of content of each Content, e.g. Article, Form, Map, Video, etc. These Content Types are defined in a master Content Type list, and are available based on the services that a site is subscribed to. The Content Types point to the Controller and Twig Templates that render the specific page. The ContentType also determines the correct Meta entity to associate with the version.

Routing (content.routing)
=========================
The `Routing` entity defines Friendly URLs that point to a specific Content (page). One or more Routing entities can be associated with a Content. There will always be one primary route and additional routes will be aliases that redirect to the primary route.

ContentVersion (content.version)
================================
The `ContentVersion` entity is the :doc:`versionable </1.0/Overview/Versioning>` part of the `Content` entity, whichthat contains the majority of the information about a `Content` which can change, e.g. Title, Author, Date, Content, Images, etc. Content will automatically version when new users edit them or after a specific period of time (or when manually requested), and a new `ContentVersion` is cloned from the current `ContentVersion`. This keeps a revision history for every page. When previewing a site, the **last modified version** is used, but when viewing the live site, the current **Published** version is used.

The `ContentVersion` contains the standard fields that most pages or modules will need, e.g. Title, Author, Date, main Content, main Image, etc. This is done so that it is easier to reference the content of each entity in a list without having to attach a lot of other associated entities. These ContentVersion fields should be used by the Content Type whenever possible, i.e. some Content Types like "Article" may not even have any custom fields in the associate Article (Content Type) entity. But many Content Types do need unique fields, so all ContentVersions reference a related Content Type entity.

ContentVersion Associations
---------------------------
``Tag``
    The Content can be associated with one or more tags that are themselves associtaed with one or more :doc:`Streams </1.0/Overview/Streams>`, (list pages that display all the content associated with the tags).

``ContentShell``
    A content can specify a unique template shell design to use (the look of the container around the content), and this preference is associated with the ContentVersion so that it can be previewed before the ContentVersion is published.

``ContentLayout``
    A content can specify a unique layout design to use (the look of the content area), and this preference is associated with the ContentVersion so that it can be previewed before the ContentVersion is published.

Meta (content.version.meta)
===========================
The `Meta` entity is a dynamic attachment point for different ContentType entities where unique data is stored for this type of content (e.g. `Article` will have slightly different data storage needs than `Profile` so we the meta lests us keep the `ContentVersion` entity focused on just the most commonly stored data relevant to all Content). `Content.ContentType` specifies which kind of Meta entity should be joined and then our code finds finds the correct ContentType entity (e.g. `Article`) and joins it to the ContentVersion. Therefore the meta entity iterates a new record everytime the `ContentVersion` changes.



