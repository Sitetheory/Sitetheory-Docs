
######################
How To Customize Files
######################


The core platform files are located in the :namespace:`Gutensite\CmsBundle` (and other bundles in the ``Gutensite`` vendor directory). These can be customized for a specific **Client Site** or a **Design Template** by adding custom files to the right location.

***********************************
Composer Autoloader for Controllers
***********************************

By default Symfony uses Composer autoloader, which is setup in ``app/autoload.php`` and looks at registered standard paths for custom files in the src/{VENDOR}/{BUNDLE} or app directories. We can register additional paths that contain files for namespaces that start with a name. But since we need to point to a dynamic directory that we only discover inside the :namespace:`Gutensite\CmsBundle\Controller\InitController` (the Template and the Client Site), we have to modify the $loader after the fact with a reference to the ``$GLOBALS[‘loader’]`` (this works, although it is non-standard and not-recommended use of Globals). So in the ``InitController`` we register all namespaces that start with ``Gutensite`` to point to the site's custom or templates files with a priority of: Client Site > Template > Core.

This lets you add files with the same namespace, filename, classname and directory structure to easily overwrite core functionality. The namespace allows these files to be located and loaded with a prioritization of which to use.


*************************
Twig Loader for Templates
*************************

By default Symfony looks for templates to override third party vendor bundles in the ``src`` or ``app`` directories. But in the ``InitController`` we tell Twig to look in other directories through the use of the Twig loader, e.g.

.. code-block:: php

    $this->container->get('twig.loader')->prependPath($templatePathView, $viewBundleNamespaceShortcut);
    
Then as long as we put the files in the right directory, they will override the core templates.

******
Assets
******

We haven’t found or created a method to instantly override custom CSS, images, etc. To do that, we would either need to create some fancy Apache rewrite to look in alternative folders if no file is found, or else make a custom asset loader function that checks if ``file_exists()`` on every single asset. That would not be very efficient. So for now, we just require that the a custom Twig template is created which points to the custom asset. That means right now, you can’t just drop the images or css into the directory. 

The advantage with this method is that there is less "magic" and the CMS is more efficient on load. So to link to a custom file you would put it in the ``Resources/public`` directory in a directory named after the bundle you are overriding (this is strictly an organizational standard since you will manually link to this location manually). For example if you are customizing an image for the :namespace:`Gutensite/MenuBundle`, in the :namespace:`Templates/GutensiteAdminBundle` template, you would do something like this:

.. code-block:: html+jinja

    <img src="{{ asset('bundles/templatesgutensiteadmin/GutensiteMenu/images/Daniela-Avatar.jpg') }}">


*****************
Client Site Files
*****************

Client Site files are located in the ``/var/www/vhosts/{ID}/src`` directory which mimics the exact structure of the core Gutensite framework directory. To customize controllers or templates, just add the exact same file to the client’s site directory, e.g.

.. code-block::

    /var/www/vhosts/1/src/Gutensite/MenuBundle/Controller/MenuPrimary.php
    /var/www/vhosts/1/src/Gutensite/MenuBundle/Resources/views/MenuPrimary.html.twig
    /var/www/vhosts/1/src/Gutensite/MenuBundle/Resources/public/css/menu.css

Controllers must include the same namespace and object name as the original file as well. They literally are identical.

Customizing Unique Instances of a Page
======================================

If you need to customize a controller or template for a unique instance of a page, i.e. a specific ``View`` ID (not just the generic controller or template for every instance of that content type), you can do that too! Just put the file in the same location as the generic file, but append the id to the end of the name, e.g.

.. code-block::

    /var/www/vhosts/1/src/Gutensite/MenuBundle/Resources/views/MenuPrimary12345.html.twig

For Controllers, since you append the viewID to the filename you will also need to append it to the classname, e.g.

.. code-block::

    /var/www/vhosts/1/src/Gutensite/MenuBundle/Controller/MenuPrimary12345.php
    class MenuPrimary12345 extends ContentController Base
    {
        // rest of code here
    }


Client Site Assets
=============

.. note::
    **TODO:** We need to figure out where custom Client Site assets will be stored. Most likely they will need to go in the ``/var/www/vhosts/{ID}/web/`` directory in a structure that mimics the core. And then some sort of apache mod rewrite magic may need to happen to load these. Alternatively, instead of the web path being /gutensite/v/2/0/bundles/ the Client Site files could be located at /client/.


**************
Template Files
**************
The same principle applies to Design Template files, but there is a slight alternative structure for where to put the files in the Design Template bundle.

.. note::
    Templates are all located in a "Templates" vendor folder, with the name of the template as the vendor's name and the name of the template. So for template named "Admin" that the vendor "Gutensite" creates the bundle name would be ``Templates\GutensiteAdminBundle``

Controllers will be located in the Template’s src directory in subdirectories that mimic the core src directory, e.g.:

.. code-block::

    Templates/GutensiteAdminBundle/src/Gutensite/MenuBundle/Controller/MenuPrimaryController.php

Templates will be located in the same cloned structure, e.g.:

.. code-block::

    Templates/GutensiteAdminBundle/src/Gutensite/MenuBundle/Resources/views/MenuPrimary.html.twig


.. note::

    TODO: Assets

    The framework should reference asset files in the same namespace as the original, e.g. ``@GutensiteCmsBundle/Resources/public/css/dash.css`` should find files in ``@Templates/GutensiteAdminBundle/Resources/GutensiteCms/public/css/dash.css`` if they are customized and exist in that location.