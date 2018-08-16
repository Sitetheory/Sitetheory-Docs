###########
Permissions
###########


********************
How Permissions Work
********************
[TODO] Provide a one paragraph overview.

Permissions on Sitetheory are extremely granular and powerful. They fall in line with a basic structure:
* Scope
* Identity
* Asset
* Sentinel


********
Entities
********

It's important to understand the entities and their relationships involved in controlling permission. Permissions are controled in the Core universal database (versus the Nest which is limited to a cluster, e.g. site content).

User
====
Users (`core.user`) are universal to the entire sitetheory system (NOTE: this may change). They can be granted permission to "assets" (site, bundle, entity), by defining their "UserPermissions". This allows a User, once authenticated, to assume other identities in the form of Roles as well as gain permissions for any shared or owned content.

UserPermissions
===============

Permissions (`core.user_permissions`) can be granted for any "identity" (user or role) to access any "asset" (site, bundle, entity), and confined to a specific "scope" (vendor, site).

Standard Fields for Permissions
-------------------------------

NOTE: normally siteId, vendorId & userId are the standard fields defining what site and user created the record the first time. But in the case of user permissions, that is not the case, since permissions are universal. When a user is first created by the system, it will define the site as the one where the user was created, and the user as itself. FYI, The normal "audit trail" fields are `editUserId` (if the permissions are changed by a user at some point, we record who made the change, but that isn’t related to the permission level.

Control Fields on UserPermissions
--------------

Control fields create "Locking Realms" for permissions. They contain:

- scope: Site or Vendor

- siteId, vendorId: these are the who "owns" the record when it was first created, they determine the scope.
master: This should be NULL for most permissions and only set to 1 if you want to elevate a user to have "root" access to all assets (SECURITY RISK!). Only some people on our internal team will have this ability, so that our support team can access sites without being granted specific access.

- Identity Fields - Authentication (either user or role, not both)

- identityUserid: the user being granted permissions.

- identityRoleId - the role being granted permissions.

Assets Fields - Correlate to Entity
-----------------------------------

- asset: a string defining a bundle, or an entity that an identity is being granted permissions for. If this is a bundle, all entities in the bundle are granted access. If this is an entity, all entity records are granted permissions, unless a specific assetId is set in the other field.
- assetId: the specific asset record id being granted access.

Access Control - Correlate to permissions
-----------------------------------------

- permission: a byte value (bitwise inclusive "OR")
- scopes: Site or Vendor

Role
====
Roles (core.user_role) are an "identity" (like User) that can be granted permissions. Role is a list of all the roles created for specific sites. Roles allow you to create premade permissions that can assign standard roles to users (and change permissions of entire groups of people assigned to that role, e.g. moderator, writer, editor, publisher, etc). The role then must have one or more permissions (user_permissions) assigned to it in order to define the access of that role.
AssignedRole (core.user_assigned_role): `AssignedRole` is a simple entity that associates a user with a specific role.


Settings
========
Settings (`core.user_settings`) is not currently used because most user settings are need to be unique for each site, so they are stored in the `nest.user_profile`.

UserProfile
===========
Every user stores profile and preferences uniquely for each site (`nest.user_profile`), these can vary from site to site, since users are global on our entire system.


*******************
AuthHelper Sentinel
*******************
The authHelper constructs a "Sentinel" for every asset that determines what a given user can do with it (e.g. create, read, update, delete, etc). The Sentinel access flags are based on the "Asset" (e.g. Site, Content, Media, etc) for the current "Scope" (e.g. Site or Vendor) and specifies what access is available to the "Identity" (User Role) based on the permissions for that Identity.

The Sentinel is requested "on demand" when the system needs to know, e.g. EnvironmentHelper needs to know the Sentinel for the current site, the APIController needs to know the Sentinel for the current asset/record being edited, etc.

The Sentinel Entity is very simple, it just contains true or false flags for the basic CRUD permissions (plus a few extra) of create, edit, delete, publish, design, dev. These can then be checked on a case by case basis, to know if a user has access to the asset.

Example: Site Permissions
=========================

A user has permissions defined which give access level to a specific site. In the EnvironmentHelper we create a Sentinel for the Site by calling AuthHelper#getSentinel()

AuthHelper#getSentinel() uses Fuzzy Logic (https://en.wikipedia.org/wiki/Fuzzy_logic) (learn more: https://plato.stanford.edu/entries/logic-fuzzy/#FuzzLogiVagu) to determine if someone should be allowed access based on their defined permissions. This requires fuzzy logic, because they may have permission to the site, but not specifically to the article. But if the article hasn’t been locked (e.g. a specific permission defined for that article) then their permission level to the site is used to give them access to the article. We just look up the tree to see the closest permissions they have. The priority order is:
- Site
- Bundle
- Entity
- Record

The AuthHelper#getSentinel() fetches permissions on the current asset that you passed. Which means it checks to see if there are any "permissions" set for the current asset. If there are no permissions defined, then there are no restrictions, which is why when we first create a site, we have to assign permissions to someone.

The **Sentinel** then contains true or false for each CRUD level, so it can easily be used to determine what kind of access is granted.

The EnvironmentHelper then checks to see if you have access to the Site, or the Page, or the APIController checks if you have access to view or edit a specific bundle, asset, record or field.

Debugging Permissions Issues
============================
The AuthHelper should never need "debugging", it’s just a tool that will always work the same way. But if you need to debug the authHelper, give Yourself "Auditor" (but be careful because it’s a TON of backtrace information that will be dumped). To give yourself "auditor" flag the "auditor" field in your "user" record (temporarily).

In most cases you will debug the use case where the getSentinel() is called, and then dump the values going into that, e.g. the Asset, Scope, and Identity, and then look at the sentinel that is returned. Then debug back up to figure why those values are wrong, e.g. why you don’t have "edit" permissions (or the permissions you expect).

Check the Permissions table to confirm what permissions you have.


*****************
Permission Levels
*****************

Permission Byte Values
======================
00000001 (001) - View
00000010 (002) - Create
00000100 (004) - Edit
00001000 (008) - Delete
00010000 (016) - Publish
00100000 (032) - Designer
01000000 (064) - Dev
10000000 (128) - Master (can do anything on the current asset)

====================================
Sample Permission for Standard Roles
====================================
00000001 (001) Authenticated - View
00000011 (003) Writer - View, Create
00000111 (015) Editor - View, Create, Edit, Delete
00001111 (031) Publisher - View, Create, Edit, Publish, Delete
00010101 (029) Moderator - View, Edit, Publish, Delete
10000000 (128) Admin - Full

*********************************
Example Use Cases for Permissions
*********************************

New User
========

Ownership of Self
-----------------
When a new user is created, they are granted `Permissions` to themselves (so they can edit their user account):

- vendorId & siteId: NULL (because ownership of your own user asset is not restricted to a specific site or vendor scope)
userId & identityUserId: equals the user.id

-asset: "SitetheoryUserBundle:User"

- assetId: equals their user.id
- permissions: 128 (full master ownership)

Association with a Site
-----------------------
The user is also associated with the site where they created their user account, by granting basic View access to this site. This allows the site to have permission to know which users were created on their site. If the same user creates an account on another site, a new user is not created, instead they just get another view permission on that site. The site will only have permission to view the username, email, and phone of the user (plus any other public information or information the user agreed to share).

- siteId: site.id (where user was created)
- userId: NULL (user scope not restricted)
identityUserId: equals their user.id (the owning identity)
- asset: "SitetheoryHostingBundle:Site"
- assetId: equals the site.id
- permissions: 1 (view only)


Site Permissions (created or invited to edit)
=============================================

Create New Site
---------------
When you create a new site you are granted full ownership permissions on the site.

- siteId: equals site.id just created
- userId: NULL (user scope not restricted)
- identityUserId: equals their user.id (the owning identity)
- asset: "SitetheoryHostingBundle:Site"
- assetId: equals site.id just created
- permissions: 128 (full master ownership)

Invite to Edit Site
-------------------
When you are invited to edit a site that you didn’t create, your permissions will be restricted to whatever access you were given by the administrator. See Proposal System for more info on workflow.

- siteId: equals site.id being invited to edit (where invitation was sent from)
- userId: NULL (user scope not restricted)
- identityUserId: equals their user.id (the owning identity)
- asset: "SitetheoryHostingBundle:Site"
- assetId: equals site.id being invited to edit
- permissions: byte value signifying permissions being granted
- Roles: Roles can be created (core.user_role) and granted to existing users who have accepted permission (e.g. have a permission record where the asset is for the current site), or users can be invited by granting a role. The process is the same as specifying permissions, it’s just that permissions are assigned to the role first (roleIdentityId versus userIdentityId), and then the user is granted that role in AssignedRoles (core.user_assigned_role).
- siteId: equals site.id being edited when the role is created
- userId: NULL (user scope not restricted)
- identityUserId: NULL (permissions for entire role, not an individual user)
- identityRoleId: equals their role.id (the owning identity)
- asset: "SitetheoryHostingBundle:Site"
- assetId: equals site.id being edited
- permissions: byte value signifying permissions being granted for the entire role.
