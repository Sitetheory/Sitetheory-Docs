########
Features
########


********
Platform
********

Sitetheory is the primary vendor of the CMS, but it will have a site like any other client. And the admin that all its clients use will be pages from its website (associated with Sitetheory's siteId #1). But any client could theoretically be subscribed to the "platform" features, and get their own pages as well. This would allow designers and developers to have their own clients using their version of the pages.

********
Accounts
********

Shared Accounts
===============

- All accounts are shared across the entire platform, but restricted to one or more sites, with specific privileges granted by the administrator. 
- If an account is created on one site, and then the user visits another site on the Sitetheory platform, the user can register on the new site. But instead of creating a new account, the user's existing account (associated with the email) will be granted basic access to the second site. This allows them to keep a single identity across all the sites. There could be edge cases where a user may want a different profile for a special site (e.g. to mask their identity), in that case they can create a new account for a different email address (but that should be rare, and is a small inconvenience for the overall benefit of a shared account system).
- By default a new account has basic access to the site that it was created on, but the administrator can promote the user to be a moderator on the site, or an administrator with varying degrees of CRUD access on a page by page basis, or an administrator over multiple sites.


**************
Administration
**************

Multiple Sites
==============

A user may create one or sites and have access to edit them all by viewing their Sites list. A site may be shared with one or more additional users, so that the owner can give different levels of administrative access to a team of people. And other users can share their site with you so that you have specific permissions to edit their site. All accounts are equal, so you can promote a visitor's account to become a moderator or an administrator of your site, or of multiple sites.

Billing
=======

- A user may create one or more billing methods, which can be associated with one or more sites. This allows an agency, broker, or other organization to manage the billing for multiple sites.

- Subscriptions will be managed for each site, and billed to the billing record selected. This allows each site to have unique subscriptions, but they can all associate with a single billing record. Or each site could be associated with different combinations of billing records. This allows billing to be kept up to date in one location, but serve multiple sites.

- Access to billing records may also be shared with one or more additional users if you want to delegate billing updates to other members of the team.


*******
Editing
*******

Versioning
==========

- When you are save a page the CMS will create a new version if it's been more than 30 minutes since you last saved or if it was last saved by someone else. This ensures that you don't overwrite other people's work and that you have a record of previous versions that you can revert back to or reference if necessary.

- You can view all the previous revisions of a page in the versions tab. You can load any version to reference previous work or revert to that version. If you edit a previous version it will save as a new version, which will be the latest staged version. If you want to publish a previous version (make it the live version), you simply click the publish button and select the current date and time.

Auto Save
=========

The CMS will also auto save your changes as long as you are on the page. That means if you are working on a page, and your power goes out, your changes will still be saved (even if you never manually saved). These auto-saved changes will create new versions if it's been more than 30 minutes since you manually saved. So when you first start working a new version will be saved. And then after you have been working for 30 minutes a new version will be saved. If you make a mistake 15 minutes later, this will allow allow you to review previous versions.

Publishing
==========

- You can easily see if you are editing the live published version of a page by looking at the publish button. If this version is the latest published version, the button will be green and will say "Published". Otherwise the publish button will be orange to alert you that there are unpublished changes. 
- When you publish your changes, you can select a date to publish. This will default to the current time, if no publish date is set. But it will only publish on this date if you click the "Save and Publish". If you select a date, and only click the "Save" button, it will not be published and the date will not be saved.
- If you made changes and published, and then realized it was a mistake and want to rollback to a previously published version, you can simply delete the publish date and click "Save and Publish". This will unset the publish date, and the latest published version of the page will be used instead. This will still be the latest "staged" version, and you can publish it again when you are ready.

Duplicate
=========

If you want to make another page similar to an existing page you can duplicate it. This can be done while editing an existing page, by clicking the duplicate button. If you have made any unsaved changes to your page before you duplicate it, they will be saved to the existing record before a new duplicate page is created.

Routing
=======
For SEO and Human Optimization, every page can have one or more Friendly URLs ("routes"). Addtional routes are aliases that will redirect to the primary route.


*****
Lists
*****

Filtering
=========

- You can filter list pages with one or more keywords. Individual keywords will be treated as additional requirements that limit the search, so a search for ‘mango good' will only return records that have both those words in any combination at least one of the searchable fields (a single field must contain both words, you cannot have ‘mango' in the title and ‘good' in the article. To search for the exact phrase "good mango" surround the words with quotes.
- You can combine individual words and phrases in one search.

Field Specific Filters
======================

You can do advanced searches on one or more specific fields by using a special field syntax ``FIELD:VALUE``, where ``FIELD`` is the field name (or a registered alias) and ``VALUE`` is the value (one or more words). The comparison can be:


- **exactly equals:** ``=`` or ``!=`` *(does not equal)*
    Example: ``title=foo bar stache`` *(the title is exactly "foo bar stache")*

- **contains:** ``:``
    Example: ``title:foo`` *(the title contains "foo" anywhere, e.g. "foobar" or "barfoodo")*

- **greater or less than:** ``>`` or ``<``
    Example: ``time>2015-05-01``

- **regular expression:** ``[?]`` or ``[!?]`` *(Regular Expression match or not matched)*

    Note: reserved Regular Expression special characters need to be commented out with a backslash "\".

    Examples:
        ``title[?]^foo[a-z]+ar`` (the title starts with "foo" followed by any character a-z followed by "ar", e.g. "foobar" or "foojar")
        ``title[!?]\(copy\)$`` (anything with a title that doesn't end in "(copy)")

- **in list:** ``[#]`` or ``[!#]`` *(the value is in the list of options)*

    Note: the value should be a comma separated list.

    Example: ``id[]1,2,3`` *(id equals 1,2 or 3)*


*************
Customization
*************

The framework allows you to customize the generic PHP controller or Twig template for any content type by adding an identical file to the client's site ``/var/wwww/vhosts/{ID}/src/`` directory. Design Templates can also be customized in the same way by adding files to the ``Sitetheory/Template{TEMPLATE-NAME}Bundle/src/`` directory. Individual pages can have a unique controller only for that view ID by adding a similar file with the additional view ID appended to the name.

Learn more about :doc:`File Customizations </1.0/Tutorials/How-To-Customize-Files>`.
