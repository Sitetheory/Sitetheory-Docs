#########################
How To Create Admin Pages
#########################

Admin pages are going to be created slightly differently than regular pages, i.e. they aren't created through the Content page, but through a special page (Content Type restricted to CMS service) that gives full access to create new content types.


********************************
Steps to Create a Basic New Page
********************************


#. **Create Content Type**

    If this is going to be a new type of CMS admin page (which it probably will be since most admin pages are unique, i.e. one content type for one page), first create a new record using the Content Type list online.

    Select the Vendor and set the name of the Bundle as well as the name of the Controller that will contain the code for this page. This controller name will also be the standard common name for form types, templates, etc. In all but the most simple bundles, the controller name should include a folder prefix to keep the code files for your content organized, e.g. ``Content\contentSeoEdit`` (the suffix "Controller" is assumed and will be added automatically in the code).

#. **Create Content**

    Create a page in the system with a friendly URL: /Admin/CMS/Edit

    Use the prefix '/Admin/' in the friendly URL, so that all admin pages are prefixed consistently, and follow other established patterns so that our URLs all match a predictable standard.

#. **Create Controller**

    The controller will contain the code for the functionality of the page. If this is part of the core CMS, this will be located in a sub folder of :namespace:`Sitetheory\CoreBundle\Controller`, but if it's the admin controller for another bundle feature, it will go in whatever bundle where the related admin and public controllers and templates are located, e.g. :namespace:`Sitetheory\CoreBundle\Controller\Content\contentSeoEditController`

    This controller should follow standard Symfony standards for controllers, and the indexAction “should” in pass in Request and InitController (the CMS core controller), e.g.

    .. code-block:: php
        :linenos:

        <?php
        public function indexAction(Request $request, InitController $initController)


    If this page is going to be a list page it should probably extend the :namespace:`Sitetheory\CoreBundle\Controller\Cms\ListControllerBase` to utilize standard list, search and filtering features. See section about `How to Create List Pages`_ for details.

    If this page is going to be an edit page it should probably extend the `Sitetheory\CoreBundle\Controller\Cms\EditControllerBase` to utilize standard admin editing features. See section about `How to Create Editor Pages`_ for details.


#. **Create Template**

    Every page needs a template to provide the visual display for the controller. These are located in the standard Symfony locations, in the same Vendor and Bundle and the same naming convention and folder structure as the Controller, e.g. :namespace:`Sitetheory\CoreBundle\Resources\contents\Content\contentSeoEdit.html.twig`

    This template should extend the shell, e.g. ``{% extends content.contentVersion.shell %}`` (the selected for every view is set based on the design settings and applied to every view unless an alternative shell is specified for this page in the design layout settings).

    If this page is extending some standard functionality (e.g. List or Editor), then the template will extend the standard templates associated with that functionality which in turn extends the shell, e.g. ``{% extends 'SitetheoryCoreBundle:Cms:EditBase.html.twig' %}``

************************
How to Create List Pages
************************

In order to utilize standard functionality for building lists, you should extend the standard List Controller and Templates.

**[todo: add more details once we finalize this]**


**************************
How to Create Editor Pages
**************************

In order to utilize standard functionality for building editing pages, you should extend the standard Editor Controller and Templates.


Editor Controller
=================

If this is a generic editor for any entity, extend the standard edit controller :namespace:`Sitetheory\CoreBundle\Controller\Cms\EditControllerBase.php`.

If this is going to be a page that interacts with Content Types via the Content, extend the special version of this controller :namespace:`Sitetheory\CoreBundle\Controller\Content\contentEditControllerBase.php` which extends ``EditControllerBase`` with some additional functionality specific to Contents, e.g. publishing and versioning.

In both cases the base controller will load getForm() to return the path to the correct form type. By default this function will find the form based on the current page's controller (this works because everything follows the same common name of the controller).

Custom Editor Form
------------------

If you need an alternative form, you can write your own custom getForm() function to set your preferred form type.

.. code-block:: php
    :linenos:

    <?php
    public function getForm(InitController $initController) {
        return 'Sitetheory\CoreBundle\Form\Type\Content\contentSeoEditType';
    }

See example code for reference of implementation in the file ``    Sitetheory\CoreBundle\Controller\Content\contentSeoEditController.php``



Editor Templates
================

The template should extend the editor template (so that it has all the standard action buttons) and include it's own custom fields:

See example code for reference of implementation in the file :namespace:`Sitetheory\CoreBundle\Resources\views\Content\viewSeoEdit.html.twig`.