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
    class ViewVersion extends Base implements VersionEntityInterface {
        /**
         * Use Shared Versionable Traits
         */
        use Sitetheory\CoreBundle\Entity\VersionEntityTrait;

        /**
         * Register the name of this entity, as it's referenced in the parent.
         * @return string
        */
        public function getEntityName() {
            return ‘viewVersion';
        }


        /**
         * Register Parent Entity Name
         */
        public function getParentName() {
            return 'view';
        }

        /**
         * Register the Entity FormType so that versions can be loaded dynamically in the parent form.
         * @return string
         */

        public function getEntityForm() {
            return 'Sitetheory\CoreBundle\Form\Type\View\ViewVersionType';
        }


        /**
         * @ORM\ManyToOne(targetEntity="\Sitetheory\CoreBundle\Entity\View\View", inversedBy="viewVersion")
         * @ORM\JoinColumn(name="viewId", referencedColumnName="id", nullable=true, onDelete="SET NULL")
         */
        protected $view;

        /**
         * @ORM\Column(type="integer", nullable=true)
         */
        protected $viewId = NULL;
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

If this parent entity has only one versionable entity (e.g. View with ViewVersion), then use the ``VersionParentInterface`` and ``VersionParentTrait``. If this parent references more than one versionable entity, use ``MultipleVersionParentInterface`` and ``MultipleVersionParentInterface``

.. code-block:: php
    :linenos:

    <?php
    class View extends Base implements VersionParentInterface {
        /**
         * Use Shared Versionable Traits.
         */
        use Sitetheory\CoreBundle\Entity\VersionParentTrait;

        /**
         * Define the Container Manually
         */
        protected $viewVersion;

        /*
         * Manually define the versionable entities, required for generic EditControllerBase
         */
        public function getEntityVersion() {
                return array(
                    ‘viewVersion'
                );
            }


        /**
         * Manually define the getters/setters for container (required for symfony functions that reference this, e.g. form type)
         */
        public function getViewVersion() {
                return $this->viewVersion;
            }
            public function setViewVersion($viewVersion) {
                $this->viewVersion = $viewVersion;
                return $this;
            }

        /**
         * @ORM\OneToMany(targetEntity="\Sitetheory\CoreBundle\Entity\View\ViewVersion", mappedBy="view", cascade={"persist", "remove", "detach"}, orphanRemoval=true)
         */
        protected $viewVersions;
        Versionable Entity Repository
        Implement Trait Interface & Custom Interface Methods
        class ViewVersionRepository extends EntityRepository implements VersionRepositoryInterface
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

If a parent entity has a "Fixed Version" relationship with a versionable entity, the parent must register the versionable entities via an array returned in ``getEntityVersion()``. And the parent entity implements the VersionParentTrait that includes a getVersion() method. This lets you pass in the the name of the property where the dynamic version is stored (e.g. ``getVersion(‘viewVersion')``) and that aliases to the ``getViewVersion()`` method.

But in some cases, you may not know what the versionable entity is offhand, but you just need to know whether it's published or not, e.g. in a generic edit template. So in those cases you can just call that method without an entity name and it will fetch the first versionable entity. For example, when editing a View (e.g. ``ArticleEdit``), the editor will be set to edit the View entity. The editControllerBase will put this View entity into ``$initController->view[‘entities'][‘editor']`` which is accessible in the template as ``{{ view.entities.editor }}``. So if you call ``{{ view.entities.editor.version.timePublish }}``, it will get the timePublish for the ``view.viewVersion`` entity, since that is the first (and only) versionable entity.

Entities Associated with the Versionable Entity
===============================================

The sub entities associated with the versionable entity (e.g. each content type, ViewSettings, etc), need to register their rootParent so that we can update the rootParent's mod time, e.g. update View when Article is edited.

.. code-block:: php
    :linenos:

    <?php
    public function getParent() {
        return $this->getViewVersion();
    }
    public function getRootParent() {
        return $this->getParent()->getParent();
    }

Find the Entity Version
=======================

The VersionParentTrait provides methods for interacting with the version, by specifying the dynamic entity name, e.g. ``$view->getVersion(‘viewVersion')``. However, the parent entity MUST define the getters and setters for the associated versionable entity anyway, in order for symfony to function properly. So this dynamic method should NOT be used (it's slower). It's ONLY needed for some dynamic internal reasons. You should always use the custom defined getter/setter, e.g. ``$view->getViewVersion()``, ``$site->getDesign()``, etc.

Associate the Correct Entity Version
====================================

Once you've set up an entity correctly, your controller can simply call the correct method on that entities repository. This will find the correct version based on the environment mode (live or preview). You can use the default repository methods to find the version by a specific id.

.. code-block:: php
    :linenos:

    <?php
    /**
     * VERSIONING
     * Get the Best ViewVersion of the View based on the environment view mode
     */
    $viewVersionRepo = $em->getRepository('SitetheoryCoreBundle:View\ViewVersion');
    $viewVersionRepo->associateVersion(‘ViewVersion', $view, $this->env->getMode());

Iterate Versions
================
Version iterations happen in the IsVersionableListener, which calls the onFlush event in the entity repository. We need to see if we can make a generic version of this.

TODO:
* Parent entity clone needs to clone the associated entities. Child entities need a clone.
* addVersion needs to be part of trait.