########
Overview
########

We have a set of fuzzy logic that brings varied levels of granularity.

Restricting Access
==================

If you create a permission (or role with permissions) for a specific Asset (Site, User, Bundle, Entity, content record, etc),
then that entity is immediately made private and can only be accessed by other Identities with the same permissions
(or role with permissions).

For example, if you create a page on your site called "Member Dashboard" and you want to restrict access
to this page, then you would create a role called "Member" and give it permission to view this new page (as well as other
pages that you want restricted to members). As soon as you give one identity (Vendor, Site, or User) access to a
specific Asset, that asset is no longer public anymore.



Admin Restrictions
==================

If you have a website and someone creates an account on that site, most likely they will be assigned to a predefined
"member" role. You would have created that role, and given that role view access to a specific group of pages that only
"members" could access. But the user will not have any "edit" permissions. So if they sign in to the admin control panel
(e.g. admin.sitetheory.io) the system will not recognize that they have access to edit any sites, the sites dropdown
menu at the top of the page will not show any sites to switch to, and going to ?siteEditId=x will not work because they
do not have edit permissions for any site. They can create their own site and edit that, but simply having "member" role
on the site doesn't give them editing permissions on any website.


Entity Restrictions
===================

By default all Assets (Vendor, Site, User, Bundle, Entity or Content Records) are viewable by the public. So if you have
an entity for BillingBundle\BillingMethod, and someone went to /Api/BillingMethod then they would be able to see all
billing method records for the current site. But as soon as we create a permission (or role with permissions)
restricting the BillingBundle, then this content is restricted. The same is true of /Api/User, but fortunately whenever
a new user is created, we create a permission that makes them the owner of their own user, which renders all their
information private.

That means we have to be very careful to always create permissions for anything that could be private. Fortunately we
also have field based restrictions defined/hardcoded on the entity itself.


Field Restrictions
==================

When an entity is defined, the individual fields have annotations that specify whether each individual field is readable,
searchable, or writable. So we need to remember when creating entities to always protect fields to be readable only by
those with edit permissions.

See Sitetheory\CoreBundle\Annotation\Api for details about annotation options.

.. code-block:: php
    * @Sitetheory\Api(writable=true, searchable={"edit"}, readable={"edit"}, level=1)


The above code means this field is writable (but of course only ever by anyone with "edit" permissions), and searchable
and readable only by those with "edit" permissions. This is useful for entities like User, which you might want to give
public readable access to the public anonymous username, but want to make the email field only readable by those with
edit permissions (thus not public information in the API).


