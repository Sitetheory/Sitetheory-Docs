##################
Content Versioning
##################

Versioning allows an entity's revision history to be tracked and to control which version is published. The best example of this in action is seen when editing content (i.e. pages or modules on a site). Content versioning is triggered under two cases: 1) when Content is edited by a new user or 2) it has been more than a set period of time (e.g. 30 minutes) since the last time it was saved. If either condition is met, a new unpublished version of the content is created. The new version can be previewed on the site in "Preview" mode, but will not appear on the live site until the version is "Published".

************
Best Version
************
The website automatically chooses the best version of Content (and other versionable entities) to display based on the context. On the live site, the system always chooses the most recent published version (not in the future), which means it shows whatever version was manually published. But if you are browsing the site in "preview mode" (e.g. you click preview in the admin and the site has a preview bar in the header) then the site will show the last "edited" version (whether or not it was published). This lets you preview your content before publishing. For obvious reasons, the admin control panel will always show the last edited version (just like preview mode on the live site) so that you can see the current state of changes. If you need to edit the published version, you will view the version history and find the version marked as published, then edit that version (which will create a new version based on the published version).


*****************************
How Versions Work in the Code
*****************************


All pages of the website are a ``Content`` which has an association with on or more ``ContentVersion`` entities. These ``ContentVersion`` entities (and the content specific entities that are associated with that version) contain the unique content. See the :doc:`overview of how Pages work</1.0/Overview/Pages>` for more details.

Since versioning is a key part of the CMS, our framework makes it easy to make an entity "versionable". See the :namespace:`SitetheoryCoreBundle/Entity/Content/ContentVersion` or :namespace:`SitetheoryCoreBundle/Entity/Design/Design` as examples of how to implement this in different ways. We use special Traits to make this easy, and minimize redundant code.

*************************
Interacting with Versions
*************************

There are two ways to interact with versions: Fetching and Editing. The versionable entity can be setup to do one or both of these things, depending on needs of the parent.

#. **Fetch the Version**
    A versionable entity may only interface with a parent entity when the parent needs to fetch the data (e.g. displaying the correct version of information on the website).

#. **Edit the Version**
    Or a versionable entity may also need to be edited in conjunction with the parent.


*****************************
Types of Versionable Entities
*****************************

Independent Version
===================

Any entity can be made to be versionable, and doesn't require that it is accessed by one single parent. Other entities that call it can use it's repository to find the live or preview version of the entity in question. An example of an independent entity is the ``Design`` entity. There is only one Design instance at a time, but there may be many versions.

Fixed Version
=============

Fixed Version entities are versionable entities that need a fixed reference id (e.g. multiple Routing records point to one Content), but you need that entity to be versionable. To accomplish this, you will set a fixed parent entity (e.g. Content) that references a single versionable entity of itself (e.g. ContentVersion). The version holds all the data for the fixed entity. The parent version will then dynamically find the right version to edit or display.

*******************************
Parents of Versionable Entities
*******************************

Versionable entities are usually referenced by one or more parents. And the parent may reference multiple associated entities, which may include one or more versionable entities. For example, the ``Site`` entity references ``Design`` and ``Settings``. If ``Design`` is versionable, there won't be a specific association. ``Site`` will have a OneToMany association with all the ``Design`` versions, but it will only have a container for the single ``Design`` version (e.g. $site->design). This will have to be manually associated based on the version that is requested (e.g. Live, Preview, or version ID). The versionable entity's repository (``DesignRepository``) will use the VersionRepositoryTrait which will include the necessary method to associate the correct version based on the live or preview mode, i.e. associateVersion().

****************************
Editing Versionable Entities
****************************

When it comes to editing the versionable entity, they can be edited independently like any other entity (if that makes sense). So in cases like ``Design`` it makes sense to have an independent form to edit the design fields, without any reference to the ``Site``. And likewise, if you edit the ``Site`` you don't need to edit the ``Design``. So nothing more needs to be done.

But in cases you may want to edit both entities in the same form, or there is a fixed relationship between the parent and the versionable entity. In those cases, the parent will need to register the entities that it wants to display in it's own editing form (e.g. this is how ``Content`` references ``ContentVersion``). The parent entity will add a method for ``getEntityVersion()`` that returns an array with the key of the property containing the entity and the value including the full path to the entity namespace.

*******************************
Publishing Versionable Entities
*******************************

If an entity is only going to be edited from it's single parent (e.g ContentVersion) the custom form type for that versionable entity should not have a timePublish() field, because the parent will manage that when it dynamically loads the versionable entities that are registered in the getEntityVersion() method (this is all handled in the EditControllerBase).

But if an entity is going to be edited independently (e.g. Design), then it needs it's own publishTime in the custom form type. This will work great, because all publishing does is set a timestamp. 

******************************
How To Make an Entity Versionable
******************************

See the tutorial on :doc:`/1.0/Tutorials/How-To-Make-An-Entity-Versionable` for specific examples and instructions.