##################
How to Use Plugins
##################

Standard plugins are defined in the Stratus.js and are available on any page by adding a data-plugin="" attribute to any element. You may combine multiple plugins on one element by separating each plguin name with a space, e.g. data-plugin="AddClass Dim"

NOTE: we are converting these plugins to the Angular method, e.g. data-plugin="onscreen" is now `stratus-on-screen`. The rest should be ported soon.


Lazy Load Correct Sized Images
------------------------------

This plugin allows you to load the best sized image based on the size of the container (XS, S, M, L, XL, HQ) so that it fills that area (which means it doesn't load images larger than mobile devices need).

NOTE: this plugin requires Backbone and jQuery (which can conflict with some sites). We have an angular version of this function which is identical but triggered with `stratus-src` instead. The Angular version is necessary to use in contexts where the path to the image is dynamically loaded. Use the Angular version whenever you are already loading Angular (it's better). Use this plugin when you do not want to be tied to Angular.

**Example**

<!-- Load a default image, and then use the src path to find the best version of image -->
<img data-plugin="lazy" src="foo-xs.jpg">

<!-- Do not load a default image, use data-src to find the best version of the the iamge -->
<img data-plugin="lazy" data-src="foo.jpg">

<!-- Angular version of lazy loader -->
<img stratus-src="lazy" src="foo.jpg">


If you want a placeholder image to appear on the page, you can just enter that as the regular image src. It is usually recommended to specify the smallest version of the image, so that the image's native ratio will be available to the CSS so that the height is correctly proportional to the width (which means when the real image loads the page isn't going to shift as element heights change).

If you use the lazy loading on images in your design (not created by the system so they don't automatically have the different size options, e.g. XS, S, M, L, XL, HQ, you will need to create these versions of your images that the plugin can load. Your sizes should be the standard sizes, since we check the container and load the best size based on the expected size of the images.

**Classes**
- placeholder: When the image is first collected for lazy-loading a 'placeholder' class will be added to it, so that you can style default look of an image that isn't loaded, e.g. gray background with a loading icon.

- loading: when the image is on screen and is in the process of loading, a 'loading' class will be added.

- loaded: when the image is loaded, the 'loading' class will be replaced by 'loaded'.

**Attribute Options:**

- stratus-src: the stratus-src should point to the image that you want to lazy-load. If you have specified a regular img src as a placeholder image (e.g. a small version), and you want to lazy load the best size of that image, than you can avoid typing out the path a second time and just specify data-src="lazy" and the system will load the best version of the current image src.

- data-spy: By default the image will load when it is "on screen". But in some cases (like a Bootstrap Carousel) you need to specify a CSS selector for an alternative element on the screen that should trigger the loading, e.g. the container div.

- data-ignore-visibility: normally it will look for the size of the container and load the correct image that will fill the container (assuming a 100% width is set on CSS). But if the container is invisible, it will try to go up the element tree to the first parent that is visible. This is often desirable because the parent is collapsed. However, in some cases, like a Bootstrap Carousel, if you have the parent width set explicitly on a containing element, you want to use that (not the outer carousel width). So you set data-ignoreVisibility="true" and it will use the parent container width.

- data-disable-fadein: All images will fade in from opacity 0 to 1, when the placeholder class is replaced with the loaded class. If you have specified a src because you want a default placeholder image to show up, then obviously you don't want the placeholder image to go invisible. So you should add a "disable-fadein" class to the image.



OnScreen
--------

The OnScreen plugin will detect when an element is visible on the screen and add classes that can be styled in CSS. It will add 'onScreen' or 'offScreen' as well as 'scrollUp' or 'scrollDown'. You can then target any combination of these two options, to do some fancy things like make a secondary header appear when the main header is 'offscreen' but you are scrolling up. Or make CSS animations start only when you scroll them into view.

**Example**

<div stratus-on-screen>Fancy Area</div>

**Additional Options**

* data-target: the CSS selector of an alternative element that should have the classes added (instead of itself), e.g. a parent element. Defaults to the current element.

* data-spy: the CSS selector of an an alternative element that should be watched to check if it's on or off screen. Defaults to the current element.

* data-offset: an integer (positive or negative) that determines where the spy element begins on the page. So if you set this to 200, the element onScreen class would be added to the target after the spy element was 200 pixels onto the screen.

* data-event: one or more events names that can trigger actions. The only option at the moment is "reset" which allows the classes to be reset if the page is scrolled to the very top, or if the data-reset value is set when the page is scrolled to that position.

* data-reset: an integer representing a vertical (y) pixel position on the page that should trigger a reset when the page is scrolled to that point (defaults to 0).


AddClass
--------

The AddClass plugin will allow you to add a class to any target element when hovering or clicking on an element. This is much more useful than a simple :hover css pseduo selector, because you can add the class to another element, e.g. a parent of another area that contains an animation that should trigger when you mouse over a button.

 **Example**
 <div data-plugin="AddClass">My Fancy Button</div>

 **Additional Options**

 * data-target: the CSS selector of an alternative element that should have the classes added (instead of itself), e.g. a parent element. Defaults to the current element.

 * data-class: the CSS class that should be added to the target element. This defaults to "active", but can be one or more classes. The plugin also also adds the event that triggered it to the current element as well as the target element, e.g. 'hover', 'click', so you can target different styles depending on hover or click.

* data-event: these are the events that the plugin will listen for on the element, in order to add the class. By default this is based on 'hover', but it can also be 'click'. If you want to have it listen to both events you can include both, e.g. data-event="hover click", and then target your CSS based on .active.hover or .active.click. The hover adds the class on mouse over and removes it on mouse leave. The click events toggles the class on and off each time the click takes place.

 * data-classinitialized: the CSS class that should be added to the target element (and the element that triggers the event) the first time it is initialized. This defaults to the generic 'initialized' but will also add a unique version based on the CSS class, e.g. if your css Class is 'fooBar', it will add initializedFooBar do distinguish it from other plugins that are adding classes to the same target.


MoreBox
-------
This plugin provides a consistent way to use the AddClass plugin to create a simple box that pops up to provide more information when you click or hover a button. CClicking the plugin button, will add an "active" class to the target moreBox. The basic styling makes the .moreBox { display: none; } by default, and then changes it to display:block when it's active. The positioning of the box will be relative to wherever the box is in the DOM, but you can easily create custom CSS to make positioning absolute or fixed to any part of the page, and add your own animations, etc.

Any options for AddClass plugin will work on this plugin as well. You can also double other other plugins like Dim.

**Required**
- The button element needs an id, and the moreBox needs an ID that matches.

**Example**
<div id="foo" data-plugin="moreBox">Click for More</div>
<div id="foo-moreBox">
    <p>Content that Appears</p>
</div>


Drawer
------
Make a drawer slide in and out of the side of the website. The core plugins.css has basic styling that makes the drawer and the app container slide in together, but you can customize specifics in your own CSS.

**Data Options**
- mobileonly: set to true if this drawer should only kick in at mobile sizes. This is useful because if the drawer is opened and the browser resized larger, the drawer will suck back into the sidebar and return the desktop look (e.g. usually a visible sidebar)

**Required**
- The button element needs an id, and the drawer needs an ID that matches with the suffix "-drawer".
- If you need to toggle one drawer from more than one button (element) then the second element needs to have the identical id base but with a suffix "-*" (dash anything), e.g. if the original ID is "sidebarToggle" the second ID can be "sidebarToggle-2" or "sidebarToggle-retractableHeader".

**Example**

.. code-block:: html
    :linenos:

    <div id="foo" data-plugin="Drawer">Open Drawer</div>
    <div id="foo-drawer">
        <p>Drawer Content</p>
    </div>



Dim
---

 Dim the page (by adding a 'dim' class to the body). The actual effect is determined by the styles you set in your CSS. The basic CSS recommended is:

  body.dim { background-color: #000; }
  body.dim #app { opacity: .2; }


Carousel
--------
The current carousel uses Bootstrap's Carousel, but we standardize how it is evoked and also allow an easy way to specify how many frames (item elements) to appear in each slide. This is useful when you want to display a gallery with several items per slide. We also allow lazy loading of images inside the slideshow by toggling a Stratus.Environment.viewPortChange after the slide appears (otherwise the images will never appear unless you are simultaneously scrolling. And finally, we force the carousel to be paused until it's onscreen so that you don't arrive at a carousel half way through the cycle. So overall, it's better to call the carousel via our standard plugin.

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