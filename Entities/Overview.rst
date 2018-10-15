########
Overview
########

Sitetheory Entities use a mixture of MongoDB and Doctrine ORM's architecture to maintain a scalable endpoint for any
algorithmic needs.

*********
Structure
*********

Entities are associated with one of two databases (Core and Nest) in order to easier facilitate scaling. A bundle will be defined as belonging to one of these database, based on whether it's a universal entity or the data can be restricted to specific sites, e.g. the lookup for Site information must be universal but Content is site specific. There is one Core database, but clusters of Nest databases, that serve a group of sites.

Core Database
=============
We have one Core database that contains entities that need to be accessible from all websites. We want to limit what goes in the Core database, because a universal database will be a bottle neck for scaling. For example, the Site, User, Template entities are in the Core, because every website needs to reference information from these entities.


Nest Database
=============
The Nest database contains entities that are created by and for specific websites. For example, Content, Article, Routing, Media, etc. Every website is assigned to a specific Nest, which is a cluster of web and database servers. The entities on the Nest database, contain data specific to the websites associated with that nest. So one Nest may serve 1000 websites, and contain 5 web servers and 5 database servers accessed in round robin. The web servers and database read servers can scale horizontally to handle increased traffic, but the nest is prevented from getting too many sites on it, because the database write server cannot scale horizontally (unless you want to implement complex sharding). So we have one write server with as many read slaves as necessary.