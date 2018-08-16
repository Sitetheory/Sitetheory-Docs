########
Overview
########

Our Standards are carefully established to provide a decrease in faux pas while increasing legibility, maintainability, and scalability.

Symfony Framework
=================

Symfony is an MVC framework we utilize to maintain optimal abstract logic.  The internal application kernel maintains requests, responses, and configurations, then sends this information off to a Controller for business logic.  Any common routines utilize dependency injection for optimal usage.  With that in mind, we utilize controllers, services, and bundles based on particular feature sets to maintain a modular design.  The only bundle that we have dependence on, at this time, is the CoreBundle.  This may change down the road as more of these pieces get fragmented out.

Doctrine ORM
============

You may ask yourself, what is an ORM?  For that I say, an Object Relational Manager is a system that maintains object persistence without directly querying and storing each property and their constraints separately.  They also allow the use of multiple querying languages to handle said persistence.

Release Cycles
==============

We use `Semantic Versioning`_ to determine when and how to set version numbers.




.. _Semantic Versioning: http://semver.org/spec/v2.0.0.html