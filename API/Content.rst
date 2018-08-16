#######
Content
#######

********
Overview
********

Content is **routable** Content Type (e.g. pages with an attached URL like "/Team") and a special "meta" (e.g. Articles, Profiles, Events, Streams, etc). These related Content Types inherit all the standard functionality and features of the Content entity. Content is automatically versionable. This API fetches all content (NOTE: in fact, not all, just most, e.g. not Menu, Streams, etc). If you want to only fetch a specific Content Type like Article, you would use that API.

***
API
***
/Api/Content

****************
ADVANCED OPTIONS
****************

Include Only Specific Content Types
===================================
Limit by one or more content types
Example: `options[contentType][]=Article`

Exclude Content Types
=====================
Include all content types except the ones listed to exclude.
Example: `options[contentTypeExclude][]=Stream`

Show Usable Content Types
=========================
Include a list of content types that are available to be created. This would be used on a content list page, in order to generate a list of "add" buttons.
Example: `options[showUsableContentTypes]=true`

Show Used Content Types
=======================
Include a list of all content types that are used by this site. This would be used on a content list page, to create filters.
Example: `options[showUsedContentTypes]=true`

Show Routing
============
The routes are always included in the query, so that we can get the primary. But this will make sure that the full list of routes is included in the API results.
Example: `options[showRouting]=true`


Show Content Info
=================
Include the extra information about the Content, including the main image and icon (based on content type). This is used on list pages in the admin.
Example: `options[showContentInfo]=true`

Show Edit URL
=============
Fetch and show the correct edit URL (this is used in the admin list pages and live edit pages so we know where to go to edit the record).
Example: `options[showEditUrl]=true`

Show Menu Links
===============
Show the Menu Links for the current page.
Example: `options[showMenuLinks]=true`

Hide Pages in Menu
==================
Exclude pages that are already in the menu. Defaults to false, so it shows all pages.
NOTE: This is a very unique use case where we are joining menus on content in a special way and we have to limit this for some reason.
Example: `options[flagNotInMenu]=true`

Limit Menu to Specific ID
=========================
If set to showMenuLinks or flagNotInMenu, the default "main" menu will be used unless an alternative menuId is specified.
Example: `options[menuId]=true`

Limit Fields Selected
=====================
Only select the fields listed in this array.
Example: `options[select][]=title`

Avoid Selecting Specific Fields
=====================
Select all fields except the fields listed in this array.
Example: `options[unselect][]=name&options[unselect][]=title`



