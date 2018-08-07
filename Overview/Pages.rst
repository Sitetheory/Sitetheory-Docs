#####
Pages
#####

Every page or module is a content entity associated with a specific Content Type. Content Types are unique content like an Article, Form, Map, Video, etc. The Content is a simple generic record that exists to provide a permanent id for each page. This permanent ID is necessary because a content (i.e. the page or content) can be versioned and each version will have a different ID, so there has to be one unifying ID that all other associated entities can reference.

*****************
Content Associations
*****************

The Content has a lot of associations with other entities that provide additional information about the page, but these are the most important associations to understand how a page is a built and how it interacts with the site:

ContentType
    The Content Type defines the type of content of each Content, e.g. Article, Form, Map, Video, etc. These Content Types are defined in a master Content Type list, and are available based on the services that a site is subscribed to. The Content Types point to the Controller and Twig Templates that render the specific page.

Routing
    The Routing entity defines Friendly URLs that point to a specific Content (page). One or more Routing entities can be associated with a Content. There will always be one primary route and additional routes will be aliases that redirect to the primary route.

ContentVersion
    The ContentVersion is a :doc:`versionable </1.0/Overview/Versioning>` entity that contains the standard information about a content, e.g. Title, Author, Date, main Content, main Image, etc. Content will automatically version when new users edit them or after a specific period of time (or when manually requested), and a new ContentVersion is cloned from the current ContentVersion. This keeps a revision history for every page. When previewing a site, the **last modified version** is used, but when viewing the live site, the current **Published** version is used.

************************
ContentVersion Associations
************************

The ContentVersion contains the standard fields that most pages or modules will need, e.g. Title, Author, Date, main Content, main Image, etc. This is done so that it is easier to reference the content of each entity in a list without having to attach a lot of other associated entities. These ContentVersion fields should be used by the Content Type whenever possible, i.e. some Content Types like "Article" may not even have any custom fields in the associate Article (Content Type) entity. But many Content Types do need unique fields, so all ContentVersions reference a related Content Type entity.

Related ``Content`` Entity
    The ContentVersion has a placeholder to attach a dynamic entity for the specific related Content Type, e.g. an Article page, will attach the Article entity. But a Form page will attach a Form entity. So this related content entity is dynamically associated with the ContentHelper when a content (and it's correct version) is fetched.

``Streams``
    The Content can be tagged with one or more :doc:`Streams </1.0/Overview/Streams>`, which are list pages that display all the content associated with it.

``ContentShell``
    A content can specify a unique template shell design to use (the look of the container around the content), and this preference is associated with the ContentVersion so that it can be previewed before the ContentVersion is published.

``ContentLayout``
    A content can specify a unique layout design to use (the look of the content area), and this preference is associated with the ContentVersion so that it can be previewed before the ContentVersion is published.

