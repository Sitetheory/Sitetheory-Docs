####
Content
####


Overview
========

A content is simply a page that is attached to a Dynamic Route (i.e. /Home).


SOAP
====

options[contentType][]
----------------------
Limit by one or more content types.

options[contentTypeExclude][]
-----------------------------
Include all content types except the ones listed to exclude.


options[showUsableContentTypes]=true
------------------------------------
Include a list of content types that are available to be created. This would be used on a content list page, in order to generate a list of "add" buttons.


options[showUsedContentTypes]=true
----------------------------------
Include a list of all content types that are used by this site. This would be used on a content list page, to create filters.


options[showRouting]=true
-------------------------
The routes are always included in the query, so that we can get the primary. But this will make sure that the full list of routes is included in the API results.


options[showContentInfo]
------------------------
Include the extra information about the content, including the main image and icon (based on content type). This is used on list pages.


options[showEditUrl]=true
-------------------------


options[showMenuLinks]=true
---------------------------

options[flagNotInMenu]=true
---------------------------

options[menuId]=true
--------------------
If set to showMenuLinks or flagNotInMenu, the default "main" menu will be used unless an alternative menuId is specified.


options[select][]
-----------------
Only select the fields listed in this array.


options[unselect][]
-------------------
Select all fields except the fields listed in this array.




