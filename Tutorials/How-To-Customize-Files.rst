
######################
How To Customize Files
######################


The core platform files are located in the :namespace:`Sitetheory\CoreBundle` (and other bundles in the ``Sitetheory`` vendor directory). These can be customized for a specific **Client Site** or a **Design Template** by adding custom files to the right location.

***********************************
Composer Autoloader for Controllers
***********************************

By default Symfony uses Composer autoloader, which is setup in ``app/autoload.php`` and looks at registered standard paths for custom files in the src/{VENDOR}/{BUNDLE} or app directories. We can register additional paths that contain files for namespaces that start with a name. But since we need to point to a dynamic directory that we only discover inside the :namespace:`Sitetheory\CoreBundle\Controller\InitController` (the Template and the Client Site), we have to modify the $loader after the fact with a reference to the ``$GLOBALS[‘loader’]`` (this works, although it is non-standard and not-recommended use of Globals). So in the ``InitController`` we register all namespaces that start with ``Sitetheory`` to point to the site's custom or templates files with a priority of: Client Site > Template > Core.

This lets you add files with the same namespace, filename, classname and directory structure to easily overwrite core functionality. The namespace allows these files to be located and loaded with a prioritization of which to use.


*************************
Twig Loader for Templates
*************************

By default Symfony looks for templates to override third party vendor bundles in the ``src`` or ``app`` directories. But in the ``InitController`` we tell Twig to look in other directories through the use of the Twig loader, e.g.

.. code-block:: php
    :linenos:

    <?php
    $this->container->get('twig.loader')->prependPath($templatePathView, $viewBundleNamespaceShortcut);
    
Then as long as we put the files in the right directory, they will override the core templates.

******
Assets
******

We haven’t found or created a method to instantly override custom CSS, images, etc. To do that, we would either need to create some fancy Apache rewrite to look in alternative folders if no file is found, or else make a custom asset loader function that checks if ``file_exists()`` on every single asset. That would not be very efficient. So for now, we just require that the a custom Twig template is created which points to the custom asset. That means right now, you can’t just drop the images or css into the directory. 

The advantage with this method is that there is less "magic" and the CMS is more efficient on load. So to link to a custom file you would put it in the ``Resources/public`` directory in a directory named after the bundle you are overriding (this is strictly an organizational standard since you will manually link to this location manually). For example if you are customizing an image for the :namespace:`Sitetheory/MenuBundle`, in the :namespace:`Templates/SitetheoryAdminBundle` template, you would do something like this:

.. code-block:: html+twig
    :linenos:

    <img src="{{ asset('bundles/templatessitetheoryadmin/SitetheoryMenu/images/Daniela-Avatar.jpg') }}">

If you need to link to your own custom CSS for a site, the vhost needs to have a web folder that points to the public resources. That means that it should have the same folder structure as a normal Assetic dump, e.g. /var/www/vhosts/100/web/sitetheory/v/2/0/bundles/. This folder will contain symbolic links to the bundles public folder.

.. code-block:: shell
    :linenos:

    mkdir /var/www/vhosts/100/web/sitetheory/v/2/0/bundles/
    ln -s /var/www/vhosts/100/src/Sitetheory/ArticleBundle/Resources/public /var/www/vhosts/100/web/sitetheory/v/2/0/bundles/sitetheoryarticle

 Unfortunately, the Template will not be able to use Assetic, and must just have a direct link.

 .. code-block:: html+twig
    {% block link %}
        {{ parent() }}
        <link rel="stylesheet" href="/sitetheory/v/2/0/bundles/sitetheoryarticle/css/Article1000-Welcome.css">
    {% endblock link %}



************
Vendor Files
************

Vendors can customize their version of core files (so all their clients will get their customized version instead of the owning vendor's version). Vendors can also create their own custom Content Type Layouts (shared with any of their clients) or Content Types (shared via subscriptions).

Customized Vendor Layouts
=========================

All Vendor bundles are stored in the platform version ``src`` folder under their own namespace, e.g. ``/var/www/core/v/1/0/src/Sitetheory`` (Sitetheory is just one vendor among many). So if a vendor called "Foo" wants to customize the Sitetheory core Profile layout, they would add the following file

.. code-block:: shell

    /var/www/core/v/1/0/src/Foo/Sitetheory/ProfileBundle/Resources/views/Profile.html.twig

Note: normally, inside the ``Foo`` namespace you would have bundles only. but if the vendor needs to overwrite another vendor, they can add the vendor's namespace directly to the bundle level.

And then the actual Twig template itself can extend the core version, by including an extends at the top. NOTE: this targets the Sitetheory vendor and the Profile bundle. Twig will look for the best version of this file according to namespace paths we've registered by priority in the InitController.

.. code-block:: html

    {% extends 'SitetheoryProfileBundle::Profile.html.twig' %}


Customized Vendor Edit Pages
============================

Sometimes you want to customize the edit interface for a specific content type, this can be accomplished by just adding a custom file, e.g.

.. code-block:: shell

    /var/www/core/v/1/0/src/Foo/Sitetheory/ProfileBundle/Resources/views/ProfileEdit.html.twig

.. code-block:: html

    {% extends 'SitetheoryProfileBundle::ProfileEdit.html.twig' %}



Custom ContentTypes
===================

If the vendor creates their own ContentType, they would need to create a Bundle namespace, and then a Content Type namespace (assigned to that bundle), and put their files in that bundle, e.g. for a "Component" bundle with a Content Type called "VolunteerForm" create these files

.. code-block:: shell

    /var/www/core/v/1/0/src/Foo/ComponentBundle/Controllers/VolunteerFormController.php
    /var/www/core/v/1/0/src/Foo/ComponentBundle/Resources/views/VolunteerForm.html.twig

If this is a custom controller, then you will just either extend the base content, or the shill directly

.. code-block:: html

    {% extends content.templates.shell %}

or

.. code-block:: html

    {% extends "SitetheoryCoreBundle:Core:ContentBase.html.twig" %}


If one of your vendor Content Type templates needs to extend another vendor template, then you need to target the vendor path in a slightly different manner to point Twig to the right vendor, by using the ``@`` notation.

.. code-block:: html

    {% extends '@FormComponent/VolunteerForm.html.twig' %}


*****************
Client Site Files
*****************

Client Site files are located in the ``/var/www/vhosts/{ID}/src`` directory which mimics the exact structure of the core Sitetheory framework directory. To customize controllers or templates, just add the exact same file to the client’s site directory, e.g.

.. code-block:: shell

    /var/www/vhosts/1/src/Sitetheory/MenuBundle/Controller/MenuPrimary.php
    /var/www/vhosts/1/src/Sitetheory/MenuBundle/Resources/views/MenuPrimary.html.twig
    /var/www/vhosts/1/src/Sitetheory/MenuBundle/Resources/public/css/menu.css

Controllers must include the same namespace and object name as the original file as well. They literally are identical.


Customizing a Vendor Version
============================

Whether the vendor has created a custom Content Type, or just customized a version of some other vendor's layout, the site can make their own custom version of the same file and the system will give preference to the Site's version. However, sometimes the site wants to use the Vendor's file, but just customize part of it. In this case, the site would create their own version of the template, but at the top "extend" the vendor's version. In order to do that, they must properly target the Twig template they are extending, by pointing to the vendor's version with the ``@`` notation. In this case it has the Vendor "Foo" and then the the vendor "Sitetheory" (which the Foo vendor is overwriting when it created it's version), and then the bundle name (without the word "Bundle").

.. code-block:: shell

    {% extends '@FooSitetheoryStream/Profile.html.twig' %}


Customizing Unique Instances of a Page
======================================

If you need to customize a controller or template for a unique instance of a page, i.e. a specific ``View`` ID (not just the generic controller or template for every instance of that content type), you can do that too! Just put the file in the same location as the generic file, but append the id to the end of the name, e.g.

.. code-block:: shell
    :linenos:

    /var/www/vhosts/1/src/Sitetheory/MenuBundle/Resources/views/MenuPrimary12345.html.twig

For Controllers, since you append the viewID to the filename you will also need to append it to the classname, e.g.

.. code-block:: php
    :linenos:

    /var/www/vhosts/1/src/Sitetheory/MenuBundle/Controller/MenuPrimary12345.php
    <?php
    class MenuPrimary12345 extends ContentController Base
    {
        // rest of code here
    }


Client Site Assets
==================

.. note::
    **TODO:** We need to figure out where custom Client Site assets will be stored. Most likely they will need to go in the ``/var/www/vhosts/{ID}/web/`` directory in a structure that mimics the core. And then some sort of apache mod rewrite magic may need to happen to load these. Alternatively, instead of the web path being /sitetheory/v/2/0/bundles/ the Client Site files could be located at /client/.


**************
Template Files
**************
The same principle applies to Design Template files, but there is a slight alternative structure for where to put the files in the Design Template bundle.

.. note::
    Templates are all located in a "Templates" vendor folder, with the name of the template as the vendor's name and the name of the template. So for template named "Admin" that the vendor "Sitetheory" creates the bundle name would be ``Templates\SitetheoryAdminBundle``

Controllers will be located in the Template’s src directory in subdirectories that mimic the core src directory, e.g.:

.. code-block::

    Templates/SitetheoryAdminBundle/src/Sitetheory/MenuBundle/Controller/MenuPrimaryController.php

Templates will be located in the same cloned structure, e.g.:

.. code-block::

    Templates/SitetheoryAdminBundle/src/Sitetheory/MenuBundle/Resources/views/MenuPrimary.html.twig


.. note::

    TODO: Assets

    The framework should reference asset files in the same namespace as the original, e.g. ``@SitetheoryCoreBundle/Resources/public/css/dash.css`` should find files in ``@Templates/SitetheoryAdminBundle/Resources/SitetheoryCms/public/css/dash.css`` if they are customized and exist in that location.


*************************
Custom Layout Controllers
*************************


Templates
---------

If a template requires a special customized controller, you can create that controller in the template bundle, e.g. `Sitetheory\TemplateCustomBundle\Controller\TemplateController.php`. This will load and execute before the ContentType controller.


Layouts
-------

Some layouts may require a custom controller. This can be accomplished by creating special files that the system looks for. If we look at the StreamBundle `Landing` contentType, the normal files will be:
- Controller: `Sitetheory\StreamBundle\Controller\LandingController.php`
- Layout Template: `Sitetheory\StreamBundle\Resources\views\Landing.html.twig`

Let's say we created a custom layout for the Landing ContentType and gave it the variable of `Candidate`. The system will then look for the specific Candidate layout controller and twig:
- Controller: `Sitetheory\StreamBundle\Controller\LandingCandidateController.php`
- Layout Template: `Sitetheory\StreamBundle\Resources\views\Landing-Candidate.html.twig`

A Client may customize the layout controller as well by using the same naming convention in their vhost folder.

