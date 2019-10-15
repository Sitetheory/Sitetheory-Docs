################################
How To Add Menus to Templates
################################

Menu Component
==============

We provide an easy way for a designer to insert the menu into any part of the Twig template design and determine how
the menu looks and functions.

Twig Method
-----------
{{
menu(content) }}

Caching
-------
Currently, we cache the menu in the RAM (Environment) so you can call upon it multiple times without causing extra overhead.
TODO: We need to create or delete/recreate a menu.json cache whenever a link is created, edited, or deleted in the main
menu (this could be a Menu or MenuLink listener).


Twig Extension Location
-----------------------
Twig Extension: Sitetheory/MenuBundle/Twig/Extension/MenuExtension.php
Twig Template: Sitetheory/MenuBundle/Resources/views/MenuExtension.html.twig
Twig Menu Component Macros: Sitetheory/MenuBundle/Resources/views/components.html.twig

Usage
-------
In a twig template we will call the menu function with desired options and directly insert the HTML into the page.
{{ menu(content) }}
or
{{ menu(content, {'scope': 'primary', 'limit': 6}) }}

Returns
-------
This will return standard formatted HTML that can be easily styled in CSS depending on the `type` of menu requested, or it will return an array if you have specified output='array'.


Arguments
---------
-`content` (mixed obj or integer) [required] - This should either be the content  object which is available in the twig template which describes the current page. Less common, it may also be an integer specifying a menu ID (if we specify a menu ID it will load that menu instead of the main menu which is default). The `content` object (if supplied) is used by the function to determine the current page's position in the menu, to set which section (and subsection) we are in (set active classes on the nested links or main level).

-`options` (object) [optional] - An object of options to override the defaults.


Options
--------
Note: all options will have defaults that may be overwritten by the specified menu "type" (since each will have different use cases). But of course the actual value may be modified by the manual options specified by the calling script.



**`scope` (str) [default: primary]** - a string defining the scope of the menu to create. Options include: primary, section.

- "primary" (default) - will find all top level links with no parents. Will default to type=simple, and return 1 level deep only by default. But you can specify other menu types and depths.

- "section" - will find the section where the link to the current page is nested, and will return only that section (not counting the top link). If you get a section link you can also call {{ getMenuSectionName() }} and {{ sectionLink() }} (see other methods below).


**`type` (str) [default: simple]** - a string defining the type of menu to create. Options include: simple, nested, sitemap, dropdown.

-"simple" (default) - This is a simple menu list typically used primarily for a main menu links in header. It is automatically limited to one level, which by default will be the top level (if `parent` is defaulted to null or 0).
[related defaults: `depth`=1;`count`=6;]

-"accordion"  - This works like a standard nested according menu (usually used for the sidebars to display section links because header shows main top level links). You can click to open subsections (if any nested menu links exist), when clicking a link on one level, it closes any other subsections that were previously open.
[related defaults: `parent`="section"; `depth`=3, `count`=null; `action`='click']

-"nested" - This is identical to "accordion" (reuse same logic) but there are no actions to open/close, it's permanently open. It's commonly used to for mobile menu drawer.
[related defaults: `parent`="section"; `depth`=3, `count`=null; `action`='open']

-"sitemap" - A list with a column for each top level link, with children nested below in column (mostly used for sitemaps in the footer).
[related defaults: `depth`=2; `count`=6]

-`dropdown` - This uses the Angular dropdown menu, which has slightly different HTML than the other menu types (e.g. md-menu tags). See Angular dropdown for reference.
[related defaults: `depth`=2; `count`=6; `action`="hover"]

**`depth` (int) [default: 1]** -  A depth of 1 means we only display menu links at the top level (usually parent=null or 0, but could be all links of a different parent if a parent is set for the section). While a depth of 2 would fetch links nested under each main link.
[Requirement: depth cannot exceed 4 under any circumstances]

**`startDepth` (int) [default: 2]** -  A starting depth of 1 means we are displaying top level links and their children, while starting depth of 2 means we are only displaying the links of nested elements. This only applies to menu scope of "section" (i.e. a primary menu must always start at top level). That means that for a section menu, level 2 is the children of the current primary menu section.

**`parent` (mixed int or str) [default: null]** - This defaults to null which means it will get all top level links without a parent. If another integer is specified, it will find links nested under the specified link ID (if it exists). Alternatively the value of "section" can be passed in to tell the script to fetch all links for the current main section. That means the current page (denoted by `content`) will be used to find the current main website section and we will only fetch the links that are nested under the current section. Section is defined as the highest level related link where parent=null or 0, e.g. If you have a site will main links: About, Resources, Products, each of those links are "sections" with parent=0 and if they have nested links, a "section" value would find all links underneath the "About" section.

**`limit` (int) [default: 6]** - This limits the total number of links for the top level. There is no limit for subsequent levels. This is most used when a designer needs the ability to limit how are displayed in a main header links.

**`action` (str) [default: click]** - Specify the type of action to trigger the opening of a menu subsection. Nested (accordion) menus should default to "click" while the Angular dropdown will default to "hover".  The option for "open" should only be used by the "nested" menu type if you want the nested menu structure to be fixed open without any opening/closing capabilities.  Options include:  "click", "hover", "open".

**`output` (str) [default: html]** - specify whether you want to return finished HTML or the raw array of links. Options include: "html", "array".

**`menu` (str) [default: null]** - specify a specific menu id that you want to fetch, if none specified, it will find the "main" menu.

**`template` (str - default: 'SitetheoryMenuBundle::MenuExtension.html.twig')** - specify an alternative template Alias (vendorBundle syntax) to use for rendering HTML of the menu. The default used is very flexible and can be easily styled in the CSS for every type of menu.

**`components` (str - default: 'SitetheoryMenuBundle::components.html.twig')** - specify an alternative components template that is used for the repeating menu elements. This is useful if you just want to customize part of the menu.

**`ulClass` (str - default: null)** - specify additional custom CSS Class names for the ul (all menu types except dropdown).

**`liClass` (str - default: null)** specify additional custom CSS Class names for the li (all menu types except dropdown).

**`menuClass` (str - default: null)** - specify additional custom CSS Class names for the md-menu (dropdown type only).

**`menuContentClass` (str - default: null)** - specify additional custom CSS Class names for the md-menu-content (dropdown type only).

**`menuItemClass` (str - default: null)** - specify additional custom CSS Class names for the md-menu-item (dropdown type only).


Other Features:
===============

**Styling** - The HTML for "simple", "accordion" and "sitemap" are all identical, but they just change styling based on CSS. The CSS is already in the common.css file. The appropriate type class should be set on the parent container based on the "type" name, e.g. `.menu-simple`, `.menu-sitemap`, `.menu-nested`, and `.menu-accordion`, `.menu-dropdown`.

The layout is set in the MenuBundle/Resources/views/MenuExtension.html.twig (which can be customized for a specific template). But most of the elements are actually in the MenuBundle/Resources/views/components.html.twig, which can also be customized for a template, just point the options to that custom file, e.g. {{ menu(content, {'components': 'SitetheoryTemplateCustomBundle::components.html.twig'} ) }}. That's is the guts of the styling. However, if you just want to include some extra classes, you can see the options above to include classes in the <li> <ul> and <a>.

**Section Name** - In cases where we use a section menu (e.g. {"scope": "section"} on a sidebar) we often want to know what section we are in (e.g. to put the name above the menu).

**Section Name** - In cases where we use a section menu (e.g. `parent`="section" on a sidebar) we often want to know what section we are in (e.g. to put the name above the menu). So when we fetch that, we insert that information into the Twig Environment for the designer to access in the template. {{ section }} will contain an object that includes {'name', 'url'}. For getting section name,url we need to call {% set sectionName = sectionName(content,parent) %} where content can be object or menuId and parent will be nestParentId of the section for which we want to show the section name.

**Active Menu** - The method needs to determine which menu link is currently active for the current page, as well as all the related parents up to level 1 (so we can set an active class on the each active link). So we check the `content` and find the menu link that points to the current page. Then we keep make a list of that link ID and all the link IDs of it's parent up to level 1. When we create the HTML we add the "active" (if it's an active link) and "activeParent" (if it's a parent, not the actual active link) class to each link in that nested tree and make sure that accordion menus stay open if it has the active class.

The menuLinks array will specify `active` = true if the current link is active, and `activeParent`=true if the current link is a parent of an active link (up the tree). So HTML should add the appropriate classes and styles for active links versus the parent of active links. Most likely you'll want them all to say 'active' and just style them differently.

**Actions** - For accordion ng-click and ng-class should add class .see-children only to the parent <li> of the link clicked.. There should be ng-click to open on levels 1-3. Clicking another menu open should close (collapse) all other menus already open. When a link is clicked with an ng-click (opening up a submenu) it should add the "active" class and remove the active class from all others at this current level or in other branches (keeping the active on it's own parent so it stays open and shows where we are in the menu).

**Nesting Levels** - HTML should dynamically add the relevant level number in nested menus, e.g. list-level3 (so we can style)

**HTML Output** - All the menu types share the same HTML except Dropdown uses Angular dropdown md-menu and md-link tags.
Below is the recommended structure of the menus (which is already styled in the common.css).

NOTE: The menuHelper->getMenuLinksNested() function we use, actually gets the FULL menu (4 levels deep) and stores that in a cache. Then each menu that is requested, is parsed from that. This is necessary so that we can find the right "section" of a page that might be nested. Even though we only want to show one or two levels publicly, we still need to get the full menu so we can find that info.


.. code-block:: html+twig
    :linenos:
        <ul class="list-level1 clearfix">
            <li ng-class="{ 'see-children1' : seeChildren1 }">
                <a href="{{ link.route }}" ng-click="seeChildren1=!seeChildren1"  id="{{ link.name|lower }}-nav1"
                   class="site-nav-link font-primary{% if link.active is defined and link.active == true %} active{% endif %}" data-level="1">{{ link.name }}
                    <div class="link-extra"></div>
                </a>
                <ul class="list-level2">
                    <li>
                        <a href="" class="site-nav-link" data-level="2">
                            Link Level Two
                            <div class="link-extra"></div>
                        </a>
                        <ul class="list-level3">
                            <li>
                                <a href="" class="site-nav-link" data-level="3">
                                    Link Level Three
                                    <div class="link-extra"></div>
                                </a>
                                <ul class="list-level4">
                                    <li>
                                        <a href="" class="site-nav-link" data-level="4">
                                            Link Level Four
                                        </a>
                                    </li>
                                </ul>
                            </li>
                        </ul>
                    </li>
                </ul>
            </li>
        </ul>



Menu Section Component
======================

If you have loaded a "section" menu e.g. `{{ menu(content, {'scope': 'section'}) }}` then you can also get the section Name and full Link object, in case you want to create a header, or cookie crumbs.

Get Section Name
----------------
You can just get the section name as a string.
.. code-block:: html+twig
    :linenos:

    <h2 class="section-name">{{ menuSectionName() }}</h2>



Get Section Link
----------------
You can get the entire Link object of the current section in case you want to get the name, route, and even all the children to cycle through and create a cookie crumb.

.. code-block:: html+twig
    :linenos:

    {% set menuSectionLink = menuSectionLink() %}
    <h2 class="menu-section-name"><a href="{{ menuSectionLink.route }}">{{ menuSectionLink.name }}</a></h2>



Menu HTML Component
======================

If you have a manual array of menuLinks objects, and you just want the get the HTML, you can pass those in to this function and get the results.

.. code-block:: html+twig
    :linenos:

        {{ menuHtml($menuLinks, {'scope': 'section', 'type': 'simple}) }}