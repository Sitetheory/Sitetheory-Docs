##############
Sitetheory 1.0
##############

Sitetheory is a robust and scalable framework to build beautiful and highly functional platforms. It is built to empower vendors, developers and design partners to rapidly create cool websites and powerful mobile apps. Sitetheory is the first vendor among many, with an admin website that functions as a website builder, CMS (Content Management System) and CRM (Customer Relationship Management). But other vendors can leverage the existing UI, API, Content Types, and Functionality to create their own identical (white labeled) or distinct platforms or just to make individual websites.

=======
Backend
=======
On the backend, Sitetheory utilizes `Symfony`_ as a modern framework, `Doctrine`_ for database and entity management, and
`Twig`_ for HTML templating. As a CMS framework, Sitetheory just manages page requests on the server side. The current URL
determines the correct View (page) to load. Each View is associated with a specific Content Type, e.g. Article, Profile, Landing Page Stream, etc. Sitetheory will load the correct Controller for the current Content Type, as well as the appropriate Twig
Template. Individual Themes or websites can extend or overwrite the Controller or Templates to allow for endless
customization.

More details can be found in this documentation.

* :ref:`overview`
* :ref:`standards`
* :ref:`tutorials`


========
Frontend
========
On the front end, all default Sitetheory themes use a proprietary `Stratus`_ Javascript framework to manage the UI/UX
look, feel and functionality (custom themes can bypass everything if desired). Stratus has a few core features, and also
loads other dependencies through `RequireJs`_. Via RequireJS, Stratus loads some helpful javascript libraries used
extensively throughout the site, including `Underscore`_ and `Angular`_. Angular is used for model management
(fetching and persisting data/entities from the API). Angular was chosen over React because it gives designers absolute
and direct control over the look of everything from Twig template files (developers haven't hard coded bad design in obscure javascript files designers can't find). Empowering designers means faster and more beautiful design.

More details can be found at the `Stratus`_ Docs.

===
API
===
Aside from handling regular website page requests, Sitetheory also handles all API requests through the /Api url on any
domain. Sitetheory is a RESTful API using the standard methods of (GET, PUT, POST, DELETE, etc) for interaction with all
entities and standard actions for viewing, creating, editing, and deleting content. Everything is accessible through the
API. Access is controlled through a robust permissions system, with granular role or user based access to
assets (site, bundles, content type, specific records or even fields). Additional SOAP style requests are available in
the API for advanced filtering.

More details can be found at the `API`_ Docs.

========
Versions
========
A new version will only be created at the moment when `Backwards Compatibility`_ is broken.


================
Other References
================

* `API`_ Docs
* `Stratus`_ Docs



=================
Table of Contents
=================

.. _overview:

Overview
--------

.. toctree::
    :maxdepth: 1
    :glob:

    Overview/*

.. _standards:

Standards
---------

.. toctree::
    :maxdepth: 1
    :glob:

    Standards/*

.. _tutorials:

Tutorials
---------

.. toctree::
    :maxdepth: 1
    :glob:

    Tutorials/*





.. _API:: http://api.sitetheory.io/index.html
.. _Stratus: http://js.sitetheory.io/2/0/stratus.html
.. _Backwards Compatibility: http://en.wikipedia.org/wiki/Backward_compatibility
.. _Symfony: http://symfony.com/
.. _Doctrine: http://www.doctrine-project.org/
.. _Twig: http://twig.sensiolabs.org/
.. _RequireJs: http://requirejs.org/
.. _UnderscoreJs: http://underscorejs.org/
.. _AngularJs: https://angularjs.org/
.. _Angular Material: https://material.angularjs.org


