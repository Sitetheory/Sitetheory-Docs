#################
Styling Standards
#################

*************
CSS Standards
*************

We suggest you follow the styling guide located at: https://github.com/necolas/idiomatic-css and declare files in the normal methods for Twig using Assetic in Sitetheory.

.. code-block:: html+twig
    :linenos:

    <link rel="stylesheet" href="{{ asset('bundles/sitetheorystratus/stratus/bower_components/angular-material/angular-material' ~ minified ~ '.css') }}">

So, ideally, it will use the unminified version when you’re in design mode, otherwise the min version will be supplied to production.

**************
LESS Standards
**************

Using LESS is always a bit more complex, but allows for a level of dynamism that can provide a much simple updating, alteration, and maintenance scheme in the long run.  For example:

.. code-block:: less
    :linenos:

    background: url('@{asset}/bundles/sitetheorytemplatesencha/images/socialSlash.png') no-repeat right center;

We highly recommend using LESS, when applicable.  Compilation and compression of these files works out of the box in most Sitetheory contexts.

****************
Twig Compilation
****************

This methodology allows for your LESS files to easily compile and compress appropriately within Sitetheory's ecosystem.

.. code-block:: html+twig
    :linenos:

    {% stylesheets '@SitetheoryTemplateBundle/Resources/public/css/common.less' filter='less' filter='?uglifycss' filter='cssrewrite' %}
        <link rel="stylesheet" href="{{ asset_url }}">
    {% endstylesheets %}