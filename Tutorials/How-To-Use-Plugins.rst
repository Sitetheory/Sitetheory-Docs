###################################
How to Use Plugins
###################################

Standard plugins are defined in the Stratus.js and are available on any page by adding a data-plugin="" attribute to any element.


OnScreen
-------------------

The OnScreen plugin will detect when an element is visible on the screen and add classes that can be styled in CSS. It will add 'onScreen' or 'offScreen' as well as 'scrollUp' or 'scrollDown'. You can then target any combination of these two options, to do some fancy things like make a secondary header appear when the main header is 'offscreen' but you are scrolling up. Or make CSS animations start only when you scroll them into view.

**Example**
<div data-plugin="OnScreen">

**Additional Options**
* data-target: the CSS selector of an alternative element that should have the classes added (instead of itself), e.g. a parent element. Defaults to the current element.

* data-spy: the CSS selector of an an alternative element that should be watched to check if it's on or off screen. Defaults to the current element.

* data-offset: an integer (positive or negative) that determines where the spy element begins on the page. So if you set this to 200, the element onScreen class would be added to the target after the spy element was 200 pixels onto the screen.

* data-event: one or more events names that can trigger actions. The only option at the moment is "reset" which allows the classes to be reset if the page is scrolled to the very top, or if the data-reset value is set when the page is scrolled to that position.

* data-reset: an integer representing a vertical (y) pixel position on the page that should trigger a reset when the page is scrolled to that point (defaults to 0).