NOTE: See our :doc:`Components documentation </1.0/Overview/Stratus-Components>` for an overview of Component Architecture if you want to build your own.

Stratus components are available on any page by adding the stratus component name, e.g. "[TODO]". A few basic Stratus components are defined in the Stratus.js library. And Sitetheory has created custom Stratus Components which are specific to our platform. These are located in the most relevant related bundle in the Resources/public/js/stratus/ folder and defined in Sitetheory's stratus config file (CoreBundle/Resources/public/js/boot/config.js, e.g. `stratus-carousel`.


############################
Components For Functionality
############################


Lazy Load Correct Sized Images
==============================

`stratus-src`

This stratus internal component allows you to load the best sized image based on the size of the container (XS, S, M, L, XL, HQ) so that it fills that area (which means it doesn't load images larger than mobile devices need).

**Example**

Load a default small image, and then use the src path to find the best version of image.

.. code-block:: html
    :linenos:

            <img stratus-src src="foo-xs.jpg">


    Do not load a default image, use stratus-src to find the best version of the the image.

.. code-block:: html
    :linenos:

            <img stratus-src="foo.jpg">


    If you want a placeholder image to appear on the page, you can just enter that as the regular image src. It is usually recommended to specify the smallest version of the image, so that the image's native ratio will be available to the CSS so that the height is correctly proportional to the width (which means when the real image loads the page isn't going to shift as element heights change).

    NOTE: If you use the lazy loading on images in your hard coded design template assets (not created by the CMS system so they don't automatically have the different size options, e.g. XS, S, M, L, XL, HQ), you will need to create these versions of your images that the component can load. Your sizes should be the standard sizes, since we check the container and load the best size based on the expected size of the images.

    XS: 200px
    S:  400px
    M:  600px
    L:  800px
    XL: 1000px
    HQ: 1200px


**Classes**

- placeholder: When the image is first collected for lazy-loading a 'placeholder' class will be added to it, so that you can style default look of an image that isn't loaded, e.g. gray background with a loading icon.

- loading: when the image is on screen and is in the process of loading, a 'loading' class will be added.

- loaded: when the image is loaded, the 'loading' class will be replaced by 'loaded'.

**Attribute Options:**

- stratus-src: the stratus-src should point to the image that you want to lazy-load. If you have specified a regular img src as a placeholder image (e.g. a small version), and you want to lazy load the best size of that image, than you can avoid typing out the path a second time and just specify data-src="lazy" and the system will load the best version of the current image src.

- data-spy: By default the image will load when it is "on screen". But in some cases (like a Carousel) you need to specify a CSS selector for an alternative element on the screen that should trigger the loading, e.g. the container div.

- data-ignore-visibility: normally it will look for the size of the container and load the correct image that will fill the container (assuming a 100% width is set on CSS). But if the container is invisible, it will try to go up the element tree to the first parent that is visible. This is often desirable because the parent is collapsed. However, in some cases, like a Carousel, if you have the parent width set explicitly on a containing element, you want to use that (not the outer carousel width). So you set data-ignoreVisibility="true" and it will use the parent container width.

- data-disable-fadein: All images will fade in from opacity 0 to 1, when the placeholder class is replaced with the loaded class. If you have specified a src because you want a default placeholder image to show up, then obviously you don't want the placeholder image to go invisible. So you should add a "disable-fadein" class to the image.



OnScreen
========

The OnScreen component will detect when an element is visible on the screen and add classes that can be styled in CSS.


Initiate the onScreen component by adding `stratus-on-screen` to any element.

.. code-block:: html
    :linenos:

            <div stratus-on-screen>Fancy Area</div>

    This component will add classes to the element depending on the user's actions: 'on-screen' or 'off-screen' as well as 'scroll-up' or 'scroll-dDown'. You can then target any combination of these two options, to do some fancy things like make a secondary header appear when the main header is 'offscreen' but you are scrolling up. Or make CSS animations start only when you scroll them into view.

.. code-block:: html
    :linenos:

            <div stratus-on-screen class="on-screen scroll-down">Fancy Area</div>


**Additional Options**

* data-target: the CSS selector of an alternative element that should have the classes added (instead of itself), e.g. a parent element. Defaults to the current element.

* data-spy: the CSS selector of an an alternative element that should be watched to check if it's on or off screen. Defaults to the current element.

* data-offset: an integer (positive or negative) that determines where the spy element begins on the page. So if you set this to 200, the element onScreen class would be added to the target after the spy element was 200 pixels onto the screen.

* data-event: one or more events names that can trigger actions. The only option at the moment is "reset" which allows the classes to be reset if the page is scrolled to the very top, or if the data-reset value is set when the page is scrolled to that position.

* data-reset: an integer representing a vertical (y) pixel position on the page that should trigger a reset when the page is scrolled to that point (defaults to 0).



Carousel
========
The current carousel uses `Swiper <https://idangero.us/swiper/>`_ .

Swiper Natively Supports:
-lazy loading
-autoplays (has transition times to set if needed)
-loop
-mouse/finger swiping (or keyboard),
-swipe up/down
-pagination/counter
-transition types/effects
-html frames

Implementation
--------------
The component is rendered as a dedicated element using `stratus-carousel` element.

.. code-block:: html
    :linenos:

         <stratus-carousel></stratus-carousel>


Options
------------
In addition to the standard Swiper options (listed in their documentation) we have additional options for our stratus component implementation.


Each slide will either be an image, video, or html. So a slide can be defined as an ARRAY with simple image URLs, or as an array with multiple OBJECT elements. If it is defined as an Object (in different contexts) the slide object has standard elements.

**Slide Object Reference:**
    - src: URL to image
    - link: URL to load on click
    - target: standard `browser target <https://www.w3schools.com/tags/att_a_target.asp>`_ (where to open the link), defaults to "_self".
    - title: Unused currently
    - description: Unused currently


- data-model (JSON Array)
    - TODO: this is not yet implemented. This should be a Collection object that will contain information for the slides. These variables should resemble the standard Slide Object defined above.
- data-images (JSON Array)
    - TODO: consider changing this to 'data-slides' and allow passing in String as URL or HTML, and Object can specify 'src' or 'html' so that we can put anything we want in each slide.
    - This may be either a JSON Array of Strings or Objects.
    - Strings: Array of URLS to an image, e.g. ["https://domain.com/image1.jpg", "https://domain.com/image2.jpg"]
    - Objects: Array of standard Slide Objects (see reference above), e.g. [{src: "https://domain.com/image1", link:"http://domain.com/foo"}]
- data-loop (boolean - default: true)
    - During pagination, allows a the last slide to return to the very first slide
- data-autoplay (boolean or JSON object - defaults to false)
    - Automatically changes the slide at set time intervals.
    - JSON:
        - TODO: specify format for options of object, time (seconds or milliseconds?)
- data-transition-effect (string - default: 'slide')
    - Options: 'slide','fade,'cube,'coverflow','flip'
    - TODO: Some transitions seem to have trouble with lazyLoad that we'll need to work on
- data-pagination (boolean or JSON Object - default: false)
    - `See Swiper Documentation <http://idangero.us/swiper/api/#pagination>`_
    - JSON: TODO
        - clickable (boolean - default: false)
        - dynamicBullets (boolean - default: false)
        - dynamicMainBullets (integer - default: 1)
        - render (String): 'fraction', 'customFaction' (not complete), 'progressbar', 'progressbarOpposite', 'numberBullet', 'bullet'
- data-init-now (Javascript variable)
    - Specify a variable to watch. Delays initialization until provided variable exists/if not empty.
- data-images-link-target (string - default: "_self")
    - If data-images doesn't have a `browser target <https://www.w3schools.com/tags/att_a_target.asp>`_, uses this option as it's default instead of "_self".
- data-direction (String - default: 'horizontal')
    - Determine direction of slide movement.
    - Options: 'horizontal', 'vertical'
- data-round-lengths (boolean - default: true)
    - Set to true to round values of slides width and height to prevent blurry texts on usual resolution screens (if you have such)
- data-scale-height (boolean - default: true)
    - Scales an image 'out' if it is too big for a the containing element to match to fit. Also centers all images that don't fit perfectly
- data-allow-zoom (boolean - default: false)
    - Allow Zooming into an image by double clicking or pinching on Mobile. Requires and force enabled scaleHeight
- data-stretch-width (oolean - default: false)
    - Allow image to stretch wider than the image provided to fill the element. May cause expected blurriness.
- data-auto-height (boolean - default: false)
    - Resizes the entire element to match the height of the current slide. WARNING: May cause resizing of this part of the page every time slide changes!
- data-allow-touch-move (boolean - default: true)
    - Allow moving the slides using a finger of mouse
- data-lazy-load (boolean or JSON Object - default: true)
    - Enable Lazy Loading to prevent everything from being fetched at once. This will lazy-load images only for the next and previous images to give a buffer.
    TODO: Determine if Alex's other stratus lazyloading conflicts
- data-navigation (boolean - default: true)
    - TODO: implement
- data-scrollbar (boolean - default: true)
    - TODO: implement
- data-slides-per-group (boolean - default: false)
    - TODO: implement
- data-autoplay-delay
    - TODO: no longer an option?


Multi-Colunns
-------------
The Swiper Carousel has many `advanced api options <http://idangero.us/swiper/api/#parameters>`_, including to control grouped/multiple slides in view (See section for "Slides Grid").

Demos:
`Multiple Slides Per View <http://idangero.us/swiper/demos/110-slides-per-view.html>`_
`Slide Multiple Per Group <http://idangero.us/swiper/demos/210-infinite-loop-with-slides-per-group.html>`_

init-now="model.completed"

Examples
--------

.. code-block:: html
    :linenos:

            <stratus-carousel
                data-images='["https://google.com/image1","https://google.com/image2","https://google.com/image3"]'
            ></stratus-carousel>

.. code-block:: html
    :linenos:

            <stratus-carousel
               data-images='[{"src":"https://google.com/image1", "link":"https://google.com/", "target":"_blank"}]'
            ></stratus-carousel>

.. code-block:: html
    :linenos:

            <stratus-carousel
               data-images='["https://google.com/image1"]'
               data-autoplay="true"
               data-transition-effect="fade"
               data-pagination='{"clickable":true, "render":"bullet"}'
               data-direction="vertical"
            ></stratus-carousel>



HOW TO USE STANDARD ANGULAR TO DO COMMON COMPONENT-LIKE FEATURES
================================================================

We do not need specific components to do common design template features anymore, instead we just use standard Angular. And we have a core components.css that applies basic styles to the examples below.


Add a Class
***********

ng-class
--------
Use ng-class to add a class based on a conditions, e.g. `ng-class="{'my-class': myVariable}"` will add "my-class" if "myVariable" is true.

ng-click or ng-hover
--------
Use ng-click or ng-hover to modify variables that can be used on other elements that conditionally add a class with ng-class

**Example**

.. code-block:: html
    :linenos:
            <div ng-click="showArea1=true">See More</div>
            <div ng-class="{'show':showArea1}">
                Content of Hidden Area
            </div>



Add a "More Box"
****************
We use a "More Box" for various popups on the site, e.g. immersive popups that dim the screen and show a popup in the middle of the site, or local popup that just covers a button locally.


**Examples**

For the **Local Popup** the button can contain the popup inside it.

.. code-block:: html
    :linenos:
            <div ng-class="{'show':myVariable}">
                <a ng-click="myVariable=true">
                    My Button
                    <div class="more-box local opens-right">
                        <!--Optional Close Button-->
                        <button type="button" class="btn-close" ng-click="myVariable=false">
                            <md-icon ng-class="{'show':myVariable}" md-svg-src="/Api/Resource?path=@SitetheoryCoreBundle:images/icons/actionButtons/close.svg" aria-hidden="true" role="img"></md-icon>
                        <button>
                        <!--Popup Content Here-->
                    </div>
                </a>
                <!--Transparent close button that covers the whole site behind the popup-->
                <div ng-class="{'show':myVariable}" ng-click="myVariable=false" class="more-box-site-cover"></div>
            </div>



    For the **Immersive Popup** the popup must be outside of the button and main site HTML (e.g. at bottom of <body> tag).

.. code-block:: html
    :linenos:
            <!--Place button anywhere-->
            <a ng-click="myVariable=true">
                My Button
            </a>

            <!--Place popup directly above closing body tag-->
            <div ng-class="{'show':myVariable}" class="more-box-position">
                <div class="more-box immersive">
                    <!--Optional close button-->
                    <button type="button" class="btn-close" ng-click="myVariable=false">
                        <md-icon ng-class="{'show':myVariable}" md-svg-src="/Api/Resource?path=@SitetheoryCoreBundle:images/icons/actionButtons/close.svg" aria-hidden="true" role="img"></md-icon>
                    <button>
                    <!--Popup content here-->
                </div>
                <div ng-click="myVariable=false" class="more-box-dimmer"></div>
            </div>





Add a Drawer
************


It is often necessary to make a drawer slide in and out of the side of the website (e.g. a toolbar, or a responsive mobile menu drawer).  This works basically exactly like a More Box, but with slightly different CSS. The core plugins.css has basic styling that makes the drawer and the app container slide in together, but you can customize specifics in your own CSS.


.. code-block:: html
    :linenos:

            <!--Place button anywhere-->
            <a ng-click="myVariable=true">
                Toggle Drawer
            </a>

            <!--Place popup directly above closing body tag-->
            <div ng-class="{'show':myVariable}" class="drawer-position">
                <div class="drawer">
                    <!--Optional close button-->
                    <button type="button" class="btn-close" ng-click="myVariable=false">
                        <md-icon ng-class="{'show':myVariable}" md-svg-src="/Api/Resource?path=@SitetheoryCoreBundle:images/icons/actionButtons/close.svg" aria-hidden="true" role="img"></md-icon>
                    <button>
                    <!--Drawer content here-->
                </div>
            </div>



######################
Components For Editing
######################

**TODO: this needs to be updated**

Generally we use Angular Material components for enabling editing on a page. But Sitetheory has created custom Editing Components that are specifically intended to allow a designer to render controller elements on the page to give editing functionality. A component can be a simple display field to show the value of an entity, a text field that allows editing the value of an entity property, or it can be like a complex media selector that shows you all the elements you have selected and allows you to upload or select new media. Components render a template and add functionality to the page so the designer can control the user experience. Most components are set to auto-save changes, so the experience is much more responsive than traditional forms. Components are used extensively throughout the CMS admin and Live Edit mode.

See the Javascript documentation for detailed specs of each widget.
TODO: update link to documentation once we move these to Sitetheory
http://js.sitetheory.io/1/0/stratus.html


***********************
Standard Widget Options
***********************

** TODO: update these to Stratus Components and document**

data-property (string): This is the model property that is being edited.

data-label (string): The label for the information being edited.

data-help (string): Additional information to help users, which will appear as a popover on a help icon.

data-template (string): This would be a full web path to a template file or a template key from config.js.

data-templates (JSON): This is a JSON object with names of the templates and a key or web path to the template that should be used for each part of the widget. Usually most components have only one template, but in cases like the Collection widget, there may be a list, container, and entity template, and this allows you to customize all of them, e.g. {"list": "/path-to-list", "container": "/path-to-container", "entity": "/path-to-entity"


.. _overview-display:

*******
Display
*******
TODO: determine if this is used

.. _overview-text:

****
Text
****
TODO: determine if this is used

.. _overview-toggle:


.. _overview-editor:

******
<stratus-redactor>
******
TODO: add documenation for our Editor


.. code-block:: html
    :linenos:

        <stratus-redactor></stratus-redactor>




.. _overview-pagination:

**********
<stratus-pagination>
**********
Add pagination for a specific collection.
TODO: Explain how stratus knows which Collection to paginate (does this need to be inside the parent element?)
.. code-block:: html
    :linenos:

        <stratus-pagination></stratus-pagination>


.. _overview-collection:

**********
Collection
**********
**TODO: is this still valid?**
data-meta: this allows you to pass in data to the collection widget so that it will be accessible in the template, e.g. when defining the widget on the DOM, add an attribute for data-meta='{"foo":"bar"}' will pass in values to the template to be accessed as {{ globals.meta.foo }}


.. _overview-save:

****
Save
****
This adds a save button to the page to save current version.
** TODO: update these to Stratus Components and document**


.. _overview-publish:

*******
Publish
*******
This adds a publish button to the page to publish the current version.
** TODO: update these to Stratus Components and document**


.. _overview-delete:

******
Delete
******
This adds a delete button to the page to delete current record.
** TODO: update these to Stratus Components and document**


****************
`<stratus-help>`
****************

Add a "Help" icon that reveals more information on hover.

Example
-------

.. code-block:: html
    :linenos:

        <stratus-help flex="5">This field allows you to explain how awesome you are.</stratus-help>


************************
`<stratus-option-value>`
************************

Add different types of dynamic fields that allow you to enter a value and select a label to describe what kind of infromation this is, e.g. an email field, that lets you select "Main", "Work", "Personal" or enter your own custom label.

Options
-------

* **data-type** (*string*): a string of one of the valid field types. A valid field type will add special styling, functionality, and validation relevant to that type of data. Valid options include: "phone", "email", "url", "location", "date". If no valid type is specified it will just be a simple field.
* **data-options** (*array: required*) an array of labels to choose from for this field e.g. ["Main", "Mobile", "Work", "Personal"]
* **data-custom** (*boolean*): specify `true` if you want users to be able to enter a custom value for the label. (*default: true*)
* **data-multiple** (*boolean*): specify `true` if you want users to be able to add more than one version of this type of field, e.g. multiple phone numbers. (*default: true*)

Additional Features for Type
----------------------------

- location: when saved, a location will attempt to do a geolocation lookup and store the latitude/longitude of the address.


Example
-------

.. code-block:: html
    :linenos:

        <stratus-option-value flex="95" ng-show="model.completed"
            ng-model="model.data.contentVersion.meta.phones"
            data-options='["Main", "Mobile", "Work", "Personal"]'
            data-type="phone"
            data-custom="true"
            data-multiple="true">
        </stratus-option-value>


Backend Info
------------

The label/value pairs are stored in the AssetManager, which allows for multiple dynamic fields to be attached to any entity.