#############################
How to Use Stratus Components
#############################

Standard components are defined in the Stratus.js and are available on any page by adding a the stratus component name, e.g. `stratus-carousel`.



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

NOTE: If you use the lazy loading on images in your hard coded design template assets (not created by the CMS system so they don't automatically have the different size options, e.g. XS, S, M, L, XL, HQ), you will need to create these versions of your images that the plugin can load. Your sizes should be the standard sizes, since we check the container and load the best size based on the expected size of the images.

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

The OnScreen plugin will detect when an element is visible on the screen and add classes that can be styled in CSS.


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





Bootstrap Carousel (DEPRECATED)
===============================
The current carousel uses Bootstrap Carousel, but we standardize how it is evoked and also allow an easy way to specify how many frames (item elements) to appear in each slide. This is useful when you want to display a gallery with several items per slide. We also allow lazy loading of images inside the slideshow by toggling a Stratus.Environment.viewPortChange after the slide appears (otherwise the images will never appear unless you are simultaneously scrolling. And finally, we force the carousel to be paused until it's onscreen so that you don't arrive at a carousel half way through the cycle. So overall, it's better to call the carousel via our standard plugin.

 **Data Options**
- group: the number of frames to group together and show in each slide (this will apply to both desktop and mobile, unless groupmobile is set).
- groupmobile: the number of items to group together and show in each slide when loaded on a mobile device.
- colminsize: the css to add to the nested items so that they properly align, e.g. if you specify data-group="3" data-colminsize="sm" then the class for the nestedItem will be 'col-sm-4'.
- All Standard Bootstrap data options: interval, pause, wrap, keyboard

**Example**

.. code-block:: html
    :linenos:

    <div id="slideshow" class="carousel slide" data-plugin="carousel" data-group="3" data-colminsize="sm" data-interval="4000">
        <div class="carousel-inner">
            <div class="item"></div>
            <div class="item"></div>
            <div class="item"></div>
            <div class="item"></div>
            <div class="item"></div>
            <div class="item"></div>
        </div>
        <div class="designSelectorControls">
        <a class="carousel-control left" href="#slideshow" role="button" data-slide="prev" data-scroll="false"></a>
        <a class="carousel-control right" href="#slideshow" role="button" data-slide="next" data-scroll="false"></a>
        </div>
    </div>

**NOTE:**
The data-scroll="false" is added to prevent our anchor script from scrolling to the new position.


Carousel
========
The current carousel uses Swiper (https://idangero.us/swiper/).

Swiper Natively Supports
-lazy loading
-autoplays (has transition times to set if needed)
-loop
-mouse/finger swiping (or keyboard),
-swipe up/down
-pagination/counter,
-transition types/effects,
-html frames

 **Data Options**
See Swiper documentation for all standard options. Additional Options listed below:

**Example**

.. code-block:: html
    :linenos:

        <stratus-carousel init-now="model.completed" images="
        [{"src":"https://foo.com/1.jpg"},
        {"src":"https://foo.com/2.jpg"}]" >
        </stratus-carousel>

TODO: Describe how to use the carousel component.
TODO: port features and explanations from Bootstrap Carousel above into this documentation once it's completed.





HOW TO USE STANDARD ANGULAR TO DO COMMON PLUGIN-LIKE FEATURES
====================================================

We do not need specific plugins to do common design template features anymore, instead we just use standard Angular. And we have a core plugins.css that applies basic styles to the examples below.


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

