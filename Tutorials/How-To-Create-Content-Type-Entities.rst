How To Create Content Type Entities
===================================

:doc:`Content Types </2.0/Overview/Content-Types>` are a critical part of the CMS because they determine what Controller should be executed for each page (what that page should do and how that page should look). When a creating an :ref:`Entity Content Type <overview-entity-content-types>` which will be a piece of content (e.g. an Article) the Content Type needs to specific the Entity name and the Entity must be created in a specific way.

Create Entity Class
-------------------

An Entity class should be created for each Entity Content Type, whether or not you need unique fields for this Content Type (beyond what is included in the :doc:`ViewVersion </2.0/Overview/Pages>` already). The reason for this is so that all Content Types follow the same predictable structure, i.e. we always know that there will be an entity at ``$View->getViewVersion()->getContent()``. Most entities will need custom content fields, but either way we include it for consistency in case we need to add a custom field in the future and don’t want to have to create new records for every existing record.

Register Searchable Fields
--------------------------

The Entity class should register the entity properties (fields) that are "searchable". These will be made available for filtering on list pages. This registration happens in the entity repository. See the ``GutensiteCmsBundle:View\ViewVersionRepository`` as an example.

* **Searchable Fields**
    These are the fields that should be searched on a regular generic search (the most common fields).

* **Valid Fields**
    These are the fields that can be searched against with the special field search syntax. The Searchable Fields will be added to this list to create a full list of valid fields. So the Valid Fields are extra fields not included in the standard searchable fields.

* **Alias Fields**
    These are alias names for the valid fields, e.g. ``id`` is an alias for ``viewId``. This makes it more intuitive for the end user to use the special field search syntax, e.g. they can search for ``id:100``	 instead of having to know that the content list page is actually displaying ViewVersion and so you have so search for ``viewId:100`` (which would give the same results since it's aliased).