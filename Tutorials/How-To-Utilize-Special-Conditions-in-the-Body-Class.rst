###################################################
How To Utilize Special Conditions in the Body Class
###################################################

The Stratus.js adds a lot of useful CSS classes to the HTML body, which can assist you with styling under certain conditions.

.. code-block:: html
    <body class="SitetheoryArticleBundle-Article viewId-12345 layout-Main mac chrome version47 loaded">

Browser
-------
The OS, and Browser and version is specified, e.g. mac chrome version47. This lets you customize special styling rules for specific browsers (usually as a fallback if a browser doesn't support some desired styling).

Load Status
-----------

-loading: when the page is in the process of loading (the HTML structure is there, but the image resources are not). This is useful if you want to make an element look a certain way while the page is loaded, e.g. a page loader animation.

-loaded: when the DOM is finished loading and the images are fully loaded. This is useful if you don't want an animation to start until after all the images are loaded.

-unloaded: when the DOM is unloaded (e.g. link out or reload). This is useful if you want to trigger an animation when the page is unloading.


Content Type
------------
The Content Type of this page, e.g. SitetheoryArticleBundle-Article. This lets you style some common element differently on specific types of pages, e.g. make the page title look differently on Articles.

ID
--
The id of the page, e.g. viewId-12345. This is useful if you need to style something differently for one specific page.





