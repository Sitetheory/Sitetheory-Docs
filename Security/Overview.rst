########
Overview
########



Menu Component
==============

We provide an easy way for a designer to insert the menu into any part of the Twig template design and determine how
the menu looks and functions.

Caching
-------
Everything is cached after the first call on a page, so you can call upon it multiple times without causing extra overhead.


Parameters
----------

-Entity (1st parameter):
    -pass in the content entity for the current page, so the menu can determine this page's position in the menu.
-Type (2nd parameter):
    -'full': all the nested links of a menu (e.g. for a sitemap at bottom of page)
    -'primary': show links from the top level (e.g. for top of page)
    -'section': detect what "section" the current page belongs to by looking up where the 'content' is located in the
    menu links, recording the parents up to the top level, and then displaying all the links in the current section.
    For example, the "About" section may have 5 sublinks, and even sub-sublinks under reach, so we would show all the
    initial 5 sublinks in a sidebar "section" which will probably be an accordion that when you open up shows the active
    link path styled (bold) at each level of nesting so when you look at the menu you know what page you are currently
    on and how it relates to the other menu links.

Parameters (planned)
--------------------
-style: accordion (e.g. side menu links), dropdown (e.g. top menu links), sitemap (sitemap would be show everything in one block, e.g. in the footer).

-limit: how many links to show on the top level (e.g. 6 or null)

-depth: how many levels deep to show menu (e.g. main links may only have 1 level, with no sublinks, but side links or drop down may be designed to allow 4 levels of nested menu links). [default accordion: 3 levels deep; default dropdown: 2; default sitemap: 3]

-parentId (optional): if you want the menu to only show links that are children of a specific link parent, e.g. this the logic of how type="section" works ( except that automatically finds the section you are in, whereas here you are manually specifying the parent).

-menuId (optional): if you want to show links that belong to another menu (aside from the default main menu, you can specify an alternative ID).


Twig Extension Location
-----------------------

Sitetheory\MenuBundle\Twig\Extension\MenuExtension



Example
-------
.. code-block:: html+twig
    :linenos:
    {% set menuExample = menu(content) %}
    {% set menuExample = menu(content, 'full') %}
    {% set menuExample = menu(content, 'primary') %}
    {% set menuExample = menu(content, 'section') %}

Other Requirements
------------------

    -determine which menu link is currently active for the current page, as well as all the related parents up to level 1 (so we can set an active class on the each active link)
    -Data attributes added to each link so that they can be targeted in CSS to change active states.
    -HTML outputted as <ul> that is easy to style in CSS, with standard classes that specify things like "level", "active", so that designers can easily style menus consistently in any template.

