####
Menu
####


Overview
========

Menus are technically a non-routable Content Type (they don't have a URL but they are based on the versionable Content entity). The reason for this is so that they can be utilized in many contexts (in the future). At the moment they are primarily used for site navigation. The main menu is marked as the primary menu and is editable in the Admin Control Panel. Menu's have associated entities MenuLinks.

By default the Menu is not auto-versioned, but it can be manually versioned if desired by passing the `?option[apiSpecialAction]=iterateVersion`.

API
===
/Api/Menu