#################################
How to Make an Entity Versionable
#################################

Before you make an entity versionable, be sure to read the :doc:`overview documentation for Versioning </1.0/Overview/Versioning>` to understand how versioning works.


************************************
How to Create the Versionable Entity
************************************

Add Common Trait to Versionable Entity
======================================

The versionable entity registers the name of the parent entity and then the trait dynamically references the parent in a getParent() method. This same Interface and Trait is used on all versionable entities, regardless if the parent references one or multiple versionable entities.

.. code-block:: php
    :linenos:

    <?php
    class ContentVersion extends Base implements VersionEntityInterface {
        /**
         * Use Shared Versionable Traits
         */
        use Sitetheory\CoreBundle\Entity\VersionEntityTrait;

        /**
         * Register the name of this entity, as it's referenced in the parent.
         * @return string
        */
        public function getEntityName() {
            return ‘contentVersion';
        }


        /**
         * Register Parent Entity Name
         */
        public function getParentName() {
            return 'content';
        }


        /**
         * @ORM\ManyToOne(targetEntity="\Sitetheory\CoreBundle\Entity\Content\content", inversedBy="contentVersion")
         * @ORM\JoinColumn(name="contentId", referencedColumnName="id", nullable=true, onDelete="SET NULL")
         */
        protected $content;

        /**
         * @ORM\Column(type="integer", nullable=true)
         */
        protected $contentId = NULL;
    }


Add Clone Method to Versionable Entity
======================================

The entity will be cloned every time an version is iterated. So some standard functionality should be added.

.. code-block:: php
    :linenos:

    <?php
    public function __clone() {
        if($this->id) {
            $this->setId(null);
            $this->setSiteId(null);
            $this->setLockVersion(1);
        }
    }


*****************************************************
How to Create a Parent Entity of a Versionable Entity
*****************************************************

Add Common Trait to Parent
==========================

If this parent entity has only one versionable entity (e.g. Content with ContentVersion), then use the ``VersionParentInterface`` and ``VersionParentTrait``. If this parent references more than one versionable entity, use ``MultipleVersionParentInterface`` and ``MultipleVersionParentInterface``

.. code-block:: php
    :linenos:

    <?php
    class Content extends Base implements VersionParentInterface {
        /**
         * Use Shared Versionable Traits.
         */
        use Sitetheory\CoreBundle\Entity\VersionParentTrait;

        /**
         * Define the Container Manually
         */
        protected $contentVersion;

        /*
         * Manually define the versionable entities, required for generic EditControllerBase
         */
        public function getEntityVersion() {
                return array(
                    ‘contentVersion'
                );
            }


        /**
         * Manually define the getters/setters for container (required for symfony functions that reference this, e.g. form type)
         */
        public function getContentVersion() {
                return $this->contentVersion;
            }
            public function setContentVersion($contentVersion) {
                $this->contentVersion = $contentVersion;
                return $this;
            }

        /**
         * @ORM\OneToMany(targetEntity="\Sitetheory\CoreBundle\Entity\Content\ContentVersion", mappedBy="content", cascade={"persist", "remove", "detach"}, orphanRemoval=true)
         */
        protected $contentVersions;
        Versionable Entity Repository
        Implement Trait Interface & Custom Interface Methods
        class ContentVersionRepository extends EntityRepository implements VersionRepositoryInterface
        {

        /**
         * Use Shared Version Trait Methods
         */
        use Sitetheory\CoreBundle\Entity\VersionRepositoryTrait;

        public function getPreview($id) {}
        public function getLive($id) {}
    }

********************************************
Registering Information for Dynamic Versions
********************************************

If a parent entity has a "Fixed Version" relationship with a versionable entity, the parent must register the versionable entities via an array returned in ``getEntityVersion()``. And the parent entity implements the VersionParentTrait that includes a getVersion() method. This lets you pass in the the name of the property where the dynamic version is stored (e.g. ``getVersion(‘contentVersion')``) and that aliases to the ``getContentVersion()`` method.

But in some cases, you may not know what the versionable entity is offhand, but you just need to know whether it's published or not, e.g. in a generic edit template. So in those cases you can just call that method without an entity name and it will fetch the first versionable entity. For example, when editing a content (e.g. ``ArticleEdit``), the editor will be set to edit the Content entity. The editControllerBase will put this Content entity into ``$initController->content[‘entities'][‘editor']`` which is accessible in the template as ``{{ content.entities.editor }}``. So if you call ``{{ content.entities.editor.version.timePublish }}``, it will get the timePublish for the ``content.contentVersion`` entity, since that is the first (and only) versionable entity.

Entities Associated with the Versionable Entity
===============================================

The sub entities associated with the versionable entity (e.g. each content type, ContentSettings, etc), need to register their rootParent so that we can update the rootParent's mod time, e.g. update Content when Article is edited.

.. code-block:: php
    :linenos:

    <?php
    public function getParent() {
        return $this->getContentVersion();
    }
    public function getRootParent() {
        return $this->getParent()->getParent();
    }

Find the Entity Version
=======================

The VersionParentTrait provides methods for interacting with the version, by specifying the dynamic entity name, e.g. ``$content->getVersion(‘contentVersion')``. However, the parent entity MUST define the getters and setters for the associated versionable entity anyway, in order for symfony to function properly. So this dynamic method should NOT be used (it's slower). It's ONLY needed for some dynamic internal reasons. You should always use the custom defined getter/setter, e.g. ``$content->getContentVersion()``, ``$site->getDesign()``, etc.

Associate the Correct Entity Version
====================================

Once you've set up an entity correctly, your controller can simply call the correct method on that entities repository. This will find the correct version based on the environment mode (live or preview). You can use the default repository methods to find the version by a specific id.

.. code-block:: php
    :linenos:

    <?php
    /**
     * VERSIONING
     * Get the Best ContentVersion of the Content based on the environment view mode
     */
    $contentVersionRepo = $em->getRepository('SitetheoryCoreBundle:Content\ContentVersion');
    $contentVersionRepo->associateVersion(‘ContentVersion', $content, $this->env->getMode());

Iterate Versions
================
Version iterations happen in the IsVersionableListener, which calls the onFlush event in the entity repository. We need to see if we can make a generic version of this.

TODO:
* Parent entity clone needs to clone the associated entities. Child entities need a clone.
* addVersion needs to be part of trait.