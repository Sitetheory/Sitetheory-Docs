########
MenuLink
########


Overview
========

Menu Links are simply child entities that are defined by a particular Menu. If you fetch only the MenuLink, you will have to specify the the MenuId that they are associated with, otherwise you will get all versions of links for all menus (which is not helpful). Normally you will want to fetch the Menu content entity, in order to get the Best Version of the menu and menu links.

API
===
/Api/MenuLink