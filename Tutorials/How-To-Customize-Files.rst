
######################
How To Customize Files
######################

The Sitetheory framework allows you to easily customize any Controller, Template, CSS, Javascript, etc. The framework will find the "best" version of Controllers (PHP) and Templates (Twig) depending on a cascading order of which priority folders contain customized files, e.g. core templates can overwrite core files, vendors can overwrite core vendor, master sites can overwrite the vendor, and custom site files can overwrite templates. NOTE: public assets like CSS, Javascript or images are not able to be found dynamically (see section below).

The core platform files are located in the :namespace:`Sitetheory\CoreBundle` (and other bundles in the ``Sitetheory`` vendor directory). These can be customized for a specific **Client Site** or a **Template** by adding custom files to the right location.

***********************************
Composer Autoloader for Controllers
***********************************

By default Symfony uses Composer autoloader, which is setup in ``app/autoload.php`` and looks at registered standard paths for custom files in the src/{VENDOR}/{BUNDLE} or app directories. We can register additional paths that contain files for namespaces that start with a name. But since we need to point to a dynamic directory that we only discover inside the :namespace:`Sitetheory\CoreBundle\Controller\InitController` (looking in the Master Vendor, Vendor, Template, Client Site, dev User), we have to modify the $loader after the fact with a reference to the ``$GLOBALS[‘loader’]`` (this works, although it is non-standard and not-recommended use of Globals). So in the ``InitController`` we register all namespaces that start with ``Sitetheory`` to point to the site's custom files with a priority the priority below:

-**Dev User**: for a developer testing new features (only accessible to this user).
-**Site Template**: the site's custom template or customization of a vendor template located in site's folder, e.g. a template may customize the UserBundle.
-**Site**: the custom version of any vendor and bundle file defined in generic site folder, e.g. customize the UserBundle's layout.
-**Vendor Template**: any customizations to the core that were made by the vendor's template.
-**Vendor**: any customizations in the vendor's folder structure
-**Vendor Master Template**: any customizations in the vendor's master site's template (e.g. Vendor Gutensite has a master Vendor of Sitetheory)
-**Vendor Master**: any customizations in the vendor's master site's folder structure (e.g. Vendor Gutensite has a master Vendor of Sitetheory)
-**Sitetheory Core**: the core Sitetheory files (often the same as "vendor master")

This has a cascading priority that lets you customize files in a very targeted manner by creating files with the same vendor and bundle namespace directory structure and matching filename to easily overwrite core functionality (controllers) and design (templates). The example below assumes a site (id 100) which may be a child site of a master site (id 9) is assigned to a vendor called "Foo" for the template "Bar" which is a child site of it's master "Sitetheory". Each of these paths looks into a folder that emulates the main Sitetheory 'src' folder, which lets you customize any file by specifying the vendor and bundle name via the folder structure of their original locations. We also look in here specifically for templates that have been customized for the CMS Edit pages.


Namespace                       Path
---------                       -----

user                            /var/www/vhosts/100/user/1/
siteTemplate                    /var/www/vhosts/100/src/Foo/TemplateBarBundle/src/
site                            /var/www/vhosts/100/src/
siteMasterTemplate              /var/www/vhosts/9/src/Foo/TemplateBarBundle/src/
siteMaster                      /var/www/vhosts/9/src/
siteVendorTemplate              /var/www/core/v/1/0/src/Foo/TemplateBarBundle/src/
siteVendor                      /var/www/core/v/1/0/src/Foo/
siteVendorMasterTemplate        /var/www/core/v/1/0/src/Sitetheory/TemplateBarBundle/src/
siteVendorMaster                /var/www/core/v/1/0/src/Sitetheory/
Core                            /var/www/core/v/1/0/src/Sitetheory/



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

Standard Location of Assets
===========================

Assets are stored in the standard Symfony bundle locations below root, e.g. for a Foo bundle:

.. code-block:: shell
    /var/www/core/v/1/0/src/Sitetheory/FooBundle/Resources/public/css/
    /var/www/core/v/1/0/src/Sitetheory/FooBundle/Resources/public/js/
    /var/www/core/v/1/0/src/Sitetheory/FooBundle/Resources/public/images/

Since the website can't load these files below root, we have a script (see "Deployment of Files" below) which creates symlinks from the public web folder to each bundles public folder, e.g.

.. code-block:: shell
    /var/www/core/web/assets/1/0/bundles/sitetheoryfoo -> /var/www/core/v/1/0/src/Sitetheory/FooBundle/Resources/public/

So anything you put in the public folder, will be publicly accessible on the webserver.

Loading an Image
----------------

To load an image from this folder, you would link to the file in this bundle:

.. code-block:: html+twig
    :linenos:
    <img src="/assets/1/0/bundles/sitetheoryfoo/images/bar.jpg">


But from Twig, we prefer to use an asset function that lets us dynamically request the correct version:

.. code-block:: html+twig
    :linenos:
    <img src="{{ asset('bundles/sitetheoryfoo/images/bar.jpg') }}">


Loading CSS and Javascript
--------------------------
CSS and Javascript is loaded from the exact same structure, but we have a few extra functions to dynamically determine the best extension, to load the correct minified version on live sites or raw version when in development mode.

.. code-block:: html+twig
    :linenos:
        {% block link %}
            {{ parent() }}
            <link rel="{{ styleRel('less') }}" type="text/css" href="{{ asset('/bundles/sitetheoryfoo/css/foo.' ~ styleExt('less')) }}" data-file="foo.css">
        {% endblock link %}

         {% block scripts %}
            {{ parent() }}
            <script type="{{ scriptType('coffeescript') }}" src="{{ asset('/bundles/sitetheoryfoo/js/bar.' ~ scriptExt('coffee')) }}" data-file="bar.js"></script>
        {% endblock scripts %}


NOTE: we have Twig methods for compiling CSS and Javascript and adding the right extensions.

Twig Methods for CSS
--------------------
- styleExt(format)
    -'css': In dev, it wil load ".css" and in live it will load ".min.css".
    -'less': In dev, we will have the ".less" extension, but stratus will dynamically compile the file into CSS so that it works (this requires rel="{{ styleRel('less') }}" to tell stratus to compile it). In live mode, it will append ".min.css" and load like normal.
    -'sass': this will append ".scss" in dev mode (but currently will break because there is no compiler). In Live mode it will load ".min.css" and work like normal.
- styleRel(format): this will add "css", "less", "sass" to the `rel` attribute, which in dev mode triggers the compiling (if necessary).


Twig Methods for Javascript
---------------------------
-scriptExt(format)
    -'coffeescript': On dev mode this will append ".coffee" and on live mode it will append ".min.js".
    -'typescript':  On dev mode this will append ".ts" and on live mode it will append ".min.js".
    -'js':  On dev mode this will append ".js" and on live mode it will append ".min.js".
-scriptType(format)
    -'coffeescript': On dev mode this add type="text/coffeescript" and on live type="text/javascript".
    -'typescript': On dev mode this add type="text/typescript" and on live type="text/javascript".
    -'js':  ".js": On both dev and live mode this adds type="text/javascript"



Asset Management
================
Asset management is a little complex, because we allow designers and developers to use CSS helper languages like LESS and SASS, or javascript helper languages like CoffeeScript and TypeScript. So this requires compiling before deployment to the server. Plus we minify these for faster loading on the live server (but in keep non-minified in dev mode).

Right now we are using a customized configuration with Gulp to find files, pipe in a compiler and out web ready files before deploying to the server.
NOTE: We anticipate that in the future we will use Symfony's Encore bundle on the backend and Webpack on the front end.

Supported Formats
-----------------
- LESS 2: http://lesscss.org/
- SASS 3: https://sass-lang.com/
- CoffeeScript 2: http://coffeescript.org/
- TypeScript 2: https://www.typescriptlang.org/


Dev Mode
--------
In dev mode only, we run Webpack on the front end to compile files dynamically (with minimal overhead), so that you can test your work in dev mode without constantly compiling and deploying compiled files.


Deployment of Assets
====================

Compiling Files
---------------
Prior to deploying files to the production server, Gulp must be run to compile web ready versions of all the files. For example, this converts a LESS file into a CSS file that can be run from a browser, or a CoffeeScript into javascript, and minifies JS and CSS for optimized loading.

NOTE: Designers do not need to worry about using Gulp, since when testing in the dev mode the system can use the raw versions of the files. Eventually Gulp compiling will be done automatically on the server. But at the moment, we run gulp on a local git repository to compile the files, then we commit to git, and deploy the latest files to the server.

Deploying Files
---------------
Sitetheory has a Python Script that runs on a server cronjob (every 2 minutes) to ensure web access to assets. This script checks all the bundles in the core src and vendor and vhost, finds which have public assets in their Resources folder and then creates symlinks from the public /web/ folder to the below root Resources folder where these are all stored. This is necessary so that these below root files can be loaded from the web.

.. code-block:: shell
    /var/www/core/web/assets/1/0/bundles/sitetheoryfoo -> /var/www/core/v/1/0/src/Sitetheory/FooBundle/Resources/public/

For nested emulated bundles (where bundles customize another bundle) we make special symlinks via the following convention:

.. code-block:: shell
    /var/www/core/web/assets/1/0/bundles/sitetheoryfoo-siteheorybaz -> /var/www/core/v/1/0/src/Sitetheory/FooBundle/src/Sitetheory/BazBundle/Resources/public/

For vhosts with customized files, we must also make symlinks:

.. code-block:: shell
    /var/www/vhosts/100/assets/1/0/bundles/sitetheoryfoo -> /var/www/vhosts/100/src/Sitetheory/FooBundle/Resources/public/
    /var/www/vhosts/100/assets/1/0/bundles/sitetheorybar -> /var/www/vhosts/100/src/Sitetheory/BarBundle/Resources/public/


Customization of Assets
=======================
Unlike Controllers and Templates, currently the framework will not automatically find the "best" version public asset files (e.g. CSS, JS, Images).

We haven’t found or created a method to instantly override custom CSS, images, etc. To do that, we would either need to create some fancy Apache rewrite to look in alternative folders if no file is found, or else make a custom asset loader function that checks if ``file_exists()`` on every single asset. That would not be very efficient. So for now, we just require that the a custom Twig template is created which points to the custom asset. That means right now, you can’t just drop the images or css into a directory. The advantage with this method is that there is less "magic" and the CMS is more efficient on load. NOTE: The only time a website will automatically load a custom version of a file, is if a specific website has saved a file (in their vhost folder) in the exact same web folder location as the core files (in these cases Apache will load the custom version). But this isn't the recommended method of customizing files.

Templates load public assets like CSS, Javascript and images by pointing to hard coded source locations in their bundle's public web folder. So if you make a customized version of an asset, you have to manually update the template to point to the custom location. These assets could technically be located anywhere, but for consistency, we put them in the bundle's `src` folder, emmulating the Vendor and Bundle name of the file we are overwriting, e.g. if you are editing a template called "Foo" and you want to overwrite the some CSS, Javascript or Image sfile located in the core UserBundle, you would put them in nested emulated bundle structure (within the `FooBundle/src` folder), e.g. you would save these files in the following locations:

.. code-block:: shell
    /var/www/core/1/0/src/Sitetheory/FooBundle/src/Sitetheory/BarBundle/Resources/public/css/baz.css
    /var/www/core/1/0/src/Sitetheory/FooBundle/src/Sitetheory/BarBundle/Resources/public/js/shaz.js
    /var/www/core/1/0/src/Sitetheory/FooBundle/src/Sitetheory/BarBundle/Resources/public/images/jazz.jpg


Customize CSS and Javascript
----------------------------

If you have a "Foo" bundle, and you want to overwrite the core CSS and Javascript assets of another bundle, you can place these new assets in the correct nested emulated folder structure. But since these are in a sub 'src' folder that emulates the nested bundle structure, you need to use the correct symlink, that was created for this non-standard location. We do that by just referencing the original bundle with a dash and then the second bundle, e.g. `sitetheoryfoo-sitetheorybar`


.. code-block:: html+twig
    :linenos:
    {% block link %}
        {{ parent() }}
        <link rel="{{ styleRel('less') }}" type="text/css" href="{{ asset('/bundles/sitetheoryfoo-sitetheorybar/css/baz.' ~ styleExt('less')) }}" data-file="foo.css">
    {% endblock link %}

     {% block scripts %}
        {{ parent() }}
        <script type="{{ scriptType('js') }}" src="{{ asset('/bundles/sitetheoryfootemplate-sitetheorybar/js/shaz.' ~ scriptExt('js')) }}" data-file="bar.js"></script>
    {% endblock scripts %}



Customize Image Location
------------------------

The template file would look like this:

.. code-block:: html+twig
    :linenos:

        <img src="{{ asset('bundles/sitetheoryfoo-sitetheorybar/images/jazz.jpg') }}">


Custom Assets for Client Sites
-------------------

When you are customizing files from one bundle to overwrite another, you have to make a custom template that points to a special custom file location. But when you are customizing assets in a client's website, you can take advantage of a web server (Apache) feature that will load the "best" version of the file. The system looks first in the vhost folder before looking in the core framework folders. So if you just create and save files in an emulated src folder with vendor and bundle names. The framework system will load custom Controllers and Templates from these locations.

So to overwrite the FooBundle file from:

.. code-block:: shell
    /var/www/core/v/1/0/src/Sitetheory/BarBundle/Resources/public/css/baz.css

You would put a file here:
.. code-block:: shell
    /var/www/vhosts/100/src/Sitetheory/BarBundle/Resources/public/css/baz.css










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

Sometimes you want to customize the edit interface for a specific content type, this can be accomplished by just adding a custom file in any of the cascading priority paths, e.g. if your vendor is "Foo" and you want to customize the "Sitetheory" vendor's files

.. code-block:: shell

    /var/www/core/v/1/0/src/Foo/Sitetheory/ProfileBundle/Resources/views/ProfileEdit.html.twig

.. code-block:: html

    {% extends 'SitetheoryProfileBundle::ProfileEdit.html.twig' %}


Custom Vendor Content Type Edit Pages
============================

At the moment, if you want to have a custom content type (e.g. an edit page for a new vendor Content Type) it requires a bit of work:

#1 Make a Content Type for the edit page, e.g. ComponentEventListEdit
#2 Make a Controller and Template for this edit page.
#3 Subscribe the Vendor's Admin site to this new Content Type
#4 Create a new page on the Vendor's Admin site with a routing URL.

So for a lot of pages that don't require custom meta (e.g. a page to create an edit page, or a non-configurable content type usually in the admin) we allow you to create and edit generic pages at /Cms/Edit which is (Content\ContentEdit) page.

But in many cases, we do need to have some custom template for the contentType edit page, but we don't want to go through the entire process above. So we need to be able to just create the template for the edit page and the system should use that if it exists rather than the generic. Just add it to the vendor's folder with the name structure of the Content Type, e.g.

.. code-block:: shell

    src/Foo/ComponentBundle/Controllers/ComponentEventListEditController.php
    src/Foo/ComponentBundle/Resources/views/ComponentEventListEdit.html.twig



Custom Vendor ContentTypes
===================

If the vendor creates their own ContentType, they would need to create a Bundle namespace, and then a Content Type namespace (assigned to that bundle), and put their files in that bundle, e.g. for a "Component" bundle with a Content Type called "VolunteerForm" create these files

.. code-block:: shell

    src/Foo/ComponentBundle/Controllers/VolunteerFormController.php
    src/Foo/ComponentBundle/Resources/views/VolunteerForm.html.twig

If this is a custom controller, then you will just either extend the base content, or the file directly

.. code-block:: html

    {% extends content.templates.shell %}

or

.. code-block:: html

    {% extends "SitetheoryCoreBundle:Core:ContentBase.html.twig" %}


If one of your vendor Content Type templates needs to extend another vendor template, then you need to target the vendor path in a slightly different manner to point Twig to the right vendor, by using the ``@`` notation to target the bundle name.

.. code-block:: html

    {% extends '@FooComponent/VolunteerForm.html.twig' %}

If you are customizing a site and need to customize the vendor's custom Content Type, you can use the following non-standard extending format (no @ symbol targetting):

.. code-block:: html
    {% extends 'FooComponentBundle::VolunteerForm.html.twig' %}


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



**************
Template Files
**************
The same principle applies to Design Template files, but there is a slight alternative structure for where to put the files in the Design Template bundle.

.. note::
    Templates are all located as bundles in their vendor's folder, e.g. the Sitetheory vendor has an "Admin" template, so it's located in ``src\Sitetheory\TemplateAdminBundle``.

If you need to customize the Controller of another bundle (regardless of the vendor owner of that bundle) then you will simply put a file in the Template’s src directory in subdirectories that mimic the core src directory, e.g.:

.. code-block::

    src/Sitetheory/TemplateAdminBundle/src/Sitetheory/CoreBundle/Controller/User/UserSignInController.php

Templates will be located in the same cloned structure, e.g.:

.. code-block::

    src/Sitetheory/TemplateAdminBundle/src/Sitetheory/CoreBundle/Resources/views/User/UserSignIn.html.twig

.. note::

    TODO: Assets

    The framework should reference asset files in the same namespace as the original, e.g. ``@SitetheoryCoreBundle/Resources/public/css/dash.css`` should find files in ``@SitetheoryTemplateAdminBundle/src/Sitetheory/CoreBundle/Resources/public/css/dash.css`` if they are customized and exist in that location.


*************************
Custom Layout Controllers
*************************

In order to allow flexibility with executing custom functionality for each layer of design, we load 3 different types of controllers (if they exist) and execute their indexAction() (usually only the content type controller will exist). These can all load independently (they are not exclusive):

#1 Template: add an initController.php#indexAction() method in the template to execute on every page (e.g. to control template or entire site)
#2 Layout: add an initController.php#indexAction() method in a Content Type layout, to give added functionality for every instance of when a particular layout is loaded.
#3 Content Type: add an initController.php#indexAction() method in a ContentType controller for every instance of Content Type (regardless of layout).
#4 Unique Content ID: add an initController.php#indexAction to a specific contentId instance, e.g. Profile12345.php.

We only load one Template for the contentType, and that template extends other templates upward to the shell and base templates. But we need to find the best type of template, e.g. the contentType could be customized for:

#1 ContentType
#2 Specific ID of page
#3 Specific EditID of content being Edited

Each of these controllers and templates needs to look for the "Best" version in cascading location priority (See cascading priority list at top of page):



Templates
=========

If a template requires a special customized controller, you can create that controller in the template bundle, e.g. `Sitetheory\TemplateCustomBundle\Controller\TemplateController.php`. This will load and execute before the ContentType controller.


Layouts
=======

Some layouts may require a custom controller. This can be accomplished by creating special files that the system looks for. If we look at the StreamBundle `Landing` contentType, the normal files will be:
- Controller: `Sitetheory\StreamBundle\Controller\LandingController.php`
- Layout Template: `Sitetheory\StreamBundle\Resources\views\Landing.html.twig`

Let's say we created a custom layout for the Landing ContentType and gave it the variable of `Candidate`. The system will then look for the specific Candidate layout controller and twig:
- Controller: `Sitetheory\StreamBundle\Controller\LandingCandidateController.php`
- Layout Template: `Sitetheory\StreamBundle\Resources\views\Landing-Candidate.html.twig`

A Client may customize the layout controller as well by using the same naming convention in their vhost folder.


