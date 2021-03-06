######
Stream
######


Overview
========

Streams are a Content Type that displays content associated with specific tags. Streams come in many different layouts to fit different needs, e.g. a landing page with a big slideshow and other dynamic modules below, a blog style page with images and words flowing down the page, a grid of photos, or a simple compact text list, etc.

Streams are technically just another content type like Article, since they are essentially just a page on the website with a URL. But since they have a very specific functionality to display other content types (rather than being content themselves), it makes more sense to separate them in the normal workflow of creating content. So in the admin they exist in a separate section and when we fetch all content we generally exclude Streams (and other unique content like Menu).


API
===

List of Stream Pages
--------------------
**/Api/Stream** - Get All Streams (pages that are Content Type "Stream" with contentType.collection=1)
Example: https://dev.sitetheory.io/Api/Stream


Get Content for a specific Stream
---------------------------------
**/Api/[contentType]/[contentId]/Asset/Content** - Get all Content that is tagged with the Asset for a specific stream content type (e.g. Collection, Landing, etc). This finds all the tags that a Stream is set to display, and then all content that is associated with those tags.

Example: https://dev.sitetheory.io/Api/Collection/12345/Asset/Content

Limit Content by Tag
-----------------------------
**/Api/[contentType]/Content?tags=100** - Limit the content for a stream by specific tags that may be associated with that content (unrelated to the main tag that links it to the current stream). For example, you may have 10 articles tagged "foo" and a stream that is set to display the "foo" articles. But these articles may also contain secondary descriptive tags like "bar", "baz". This lets us filter the 10 articles on the stream, by additional unrelated tags.

Example: https://dev.sitetheory.io/Api/Content?tags=100
Or Limit Only Articles by Tag: Example: https://dev.sitetheory.io/Api/Article?tags=100

NOTE: you can also further limit an existing stream by only some of the tags, e.g. if you want to have filters on the side. This would find a subset of the stream's content, based on whether any of that content ALSO had the requested overlapping or extra tags, e.g. https://dev.sitetheory.io/Api/Collection/12345/Asset/Content?tags=[100,101]

NOTE: to filter more than one tag, pass in a comma separated value for the "tags" variable, e.g. ?tags=[100,200]

/Api/Tag/537/Content
/Api/Content?tags=537
/Api/Content?tags=[537]
/Api/Content?tags=[535,536,537,538]

Note: the Variable is plural ("tags")