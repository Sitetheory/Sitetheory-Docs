###################################
How To Create Content Type Entities
###################################

:doc:`Content Types </2.0/Overview/Content-Types>` are a critical part of the CMS because they determine what Controller should be executed for each page (what that page should do and how that page should look). When a creating an :ref:`Entity Content Type <overview-entity-content-types>` which will be a piece of content (e.g. an Article) the Content Type needs to specific the Entity name and the Entity must be created in a specific way.

Create Entity Class
-------------------

An Entity class should be created for each Entity Content Type, whether or not you need unique fields for this Content Type (beyond what is included in the :doc:`ViewVersion </2.0/Overview/Pages>` already). The reason for this is so that all Content Types follow the same predictable structure, i.e. we always know that there will be an entity at ``$View->getViewVersion()->getContent()``. Most entities will need custom content fields, but either way we include it for consistency in case we need to add a custom field in the future and don’t want to have to create new records for every existing record.

Register API Accessibility
--------------------------

The Entity class should register the entity properties (fields) that are readable, writable, and searchable by using Sitetheory\Api annotation. This registration happens in the entity field declaration. See the :namespace:`SitetheoryCoreBundle:View\ViewVersion` as an example. See `Sitetheory\CoreBundle\Annotations\Api.php` for details.

* **Readable**
    All fields are readable by default. Set to false if you don't want them displaying. Set level="x" if you don't want
    the API traversing beyond a certain level. You can specify a sentinel of permissions to
    limit who can read, e.g. readable="false" or readable={"edit"}

* **Searchable**
    Fields are not searchable by default, you must enable them explicitly. You can specify a sentinel of permissions to
    limit who can search, e.g. searchable="true" or searchable={"edit"}

* **Writable**
    Fields are not writable by default, you must enable them explicitly. You can specify a sentinel of permissions to
    limit who can write, e.g. writable="true" or writable={"create","edit"}
