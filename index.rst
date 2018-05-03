##############
Sitetheory 1.0
##############

Sitetheory is a robust and scalable framework to build beautiful and highly functional platforms. It is built to empower vendors, developers and design partners to rapidly create cool websites and powerful mobile apps. Sitetheory is the first vendor among many, with an admin website that functions as a website builder, CMS (Content Management System) and CRM (Customer Relationship Management). But other vendors can leverage the existing UI, API, Content Types, and Functionality to create their own identical (white labeled) or distinct platforms or just to make individual websites.

========
Frontend
========
On the front end, all default Sitetheory themes use a proprietary `Stratus`_ Javascript framework to manage the UI/UX
look, feel and functionality (custom themes can bypass everything if desired). Stratus has a few core features, and also
loads other dependencies through `Require.js`_. Via Require.js, Stratus loads some helpful javascript libraries used
extensively throughout the site, including `Angular.js`_, which is used for model management
(fetching and persisting data/entities from the API). Angular was chosen over React because it gives designers absolute
and direct control over the look of everything from Twig template files (developers haven't hard coded bad design in obscure javascript files that designers can't find). Empowering designers means faster and more beautiful design.

More details can be found at the `Stratus`_ Docs. (TODO: broken link)

=======
Backend
=======
On the backend, Sitetheory utilizes `Symfony`_ as a modern framework, `Doctrine`_ for database and entity management, and
`Twig`_ for HTML templating. As a CMS framework, Sitetheory just manages page requests on the server side. The current URL
determines the correct View (page) to load. Each View is associated with a specific Content Type, e.g. Article, Profile,
Landing Page Stream, etc. Sitetheory will load the correct Controller for the current Content Type, as well as the appropriate
Twig Template. Individual Themes or websites can extend or overwrite the Controller or Templates to allow for endless
customization.

More details can be found in the documentation below.

========
Versions
========
A new version will only be created at the moment when `Backwards Compatibility`_ is broken.

========
Overview
========

.. toctree::
    :maxdepth: 1
    :glob:

    Overview/*

=========
Standards
=========

.. toctree::
    :maxdepth: 1
    :glob:

    Standards/Overview
    Standards/*

=========
Tutorials
=========

.. toctree::
    :maxdepth: 1
    :glob:

    Tutorials/Quick-Overview
    Tutorials/*

========
Security
========

.. toctree::
    :maxdepth: 1
    :glob:

    Security/Overview
    Security/*

========
Entities
========

.. toctree::
    :maxdepth: 1
    :glob:

    Entities/Overview
    Entities/*

===
API
===

.. toctree::
    :maxdepth: 1
    :glob:

    API/Overview
    API/*

===
Vendors
===

.. toctree::
:maxdepth: 1
        :glob:

        Vendors/Overview
        Vendors/*


================
Other References
================

* `Framework`_ Docs
* `Stratus`_ Docs



.. _Framework: http://api.sitetheory.io/index.html
.. _Stratus: http://js.sitetheory.io/1/0/stratus.html
.. _Backwards Compatibility: http://en.wikipedia.org/wiki/Backward_compatibility
.. _Symfony: http://symfony.com/
.. _Doctrine: http://www.doctrine-project.org/
.. _Twig: http://twig.sensiolabs.org/
.. _Require.js: http://Require.js.org/
.. _Angular.js: https://Angular.js.org/
.. _Angular Material: https://material.Angular.js.org

