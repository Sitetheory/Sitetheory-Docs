NOTE: See our :doc:`Stratus documentation </1.0/Overview/Stratus>` for an overview of how Stratus works.

###############
Stratus Filters
###############

Like Stratus Components, you can create Angular style filters for processing data on a page.


Available Filters
=================

assetPath
*********
This allows you to specify a relative bundle bath for a local image, and automatically add the correct full path to the local web asset for the current version, e.g. providing input of `sitetheorybildtemplate/images/placeholder-square.png` would output `/assets/1/0/bundles/sitetheorybildtemplate/images/placeholder-square.png`.

NOTE: This is intended for use with images, SVG, and other local files that are not minified (e.g. not css or javascript, those should be loaded through components which already have a system for finding the best version based on environment.

Usage
-----

.. code-block:: html+twig
    :linenos:

    <img ng-src="sitetheorybildtemplate/images/placeholder-square.png | assetPath">

Will output on the page:

.. code-block:: html+twig
    :linenos:

    <img src="/assets/1/0/bundles/sitetheorytemplate/images/foo.png?v=12249595">


Options
-------

  // NOTE: if we wanted to make this more fancy, we should make a service that this references.
  // OPTIONS:
  // options.disableCacheBusting - (boolean - default: false) by default we add cache busting to the end of files.
  // options.enableMin - (boolean - default: false) by default we do not add min