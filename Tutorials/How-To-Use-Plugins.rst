##################
How to Use Plugins
##################

Standard plugins are defined in the Stratus.js and are available on any page by adding a data-plugin="" attribute to any element. You may combine multiple plugins on one element by separating each plguin name with a space, e.g. data-plugin="AddClass Dim"


OnScreen
--------

The OnScreen plugin will detect when an element is visible on the screen and add classes that can be styled in CSS. It will add 'onScreen' or 'offScreen' as well as 'scrollUp' or 'scrollDown'. You can then target any combination of these two options, to do some fancy things like make a secondary header appear when the main header is 'offscreen' but you are scrolling up. Or make CSS animations start only when you scroll them into view.

**Example**

<div data-plugin="OnScreen">Fancy Area</div>

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

**Required**
- The button element needs an id, and the drawer needs an ID that matches with the suffix "-drawer".

**Example**
<div id="foo" data-plugin="Drawer">Open Drawer</div>
<div id="foo-drawer">
    <p>Drawer Content</p>
</div>



Dim
---

 Dim the page (by adding a 'dim' class to the body). The actual effect is determined by the styles you set in your CSS. The basic CSS recommended is:

  body.dim { background-color: #000; }
  body.dim #app { opacity: .2; }