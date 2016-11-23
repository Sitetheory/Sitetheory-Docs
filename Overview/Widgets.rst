@DEPRECATED (for short term reference only)
TODO: DELETE

#######
Widgets
#######

Sitetheory has many core widgets that allow a designer to render controller elements on the page to give editing functionality. A widget can be a simple display field to show the value of an entity, a text field that allows editing the value of an entity property, or it can be like a complex media selector that shows you all the elements you have selected and allows you to upload or select new media. Widgets render a template and add functionality to the page so the designer can control the user experience. Most widgets are set to auto-save changes, so the experience is much more responsive than traditional forms. Widgets are used extensively throughout the CMS admin and Live Edit mode.

See the Javascript documentation for detailed specs of each widget.
http://js.sitetheory.io/2/0/stratus.html


***********************
Standard Widget Options
***********************

data-property (string): This is the model property that is being edited.

data-label (string): The label for the information being edited.

data-help (string): Additional information to help users, which will appear as a popover on a help icon.

data-template (string): This would be a full web path to a template file or a template key from config.js.

data-templates (JSON): This is a JSON object with names of the templates and a key or web path to the template that should be used for each part of the widget. Usually most widgets have only one template, but in cases like the Collection widget, there may be a list, container, and entity template, and this allows you to customize all of them, e.g. {"list": "/path-to-list", "container": "/path-to-container", "entity": "/path-to-entity"


.. _overview-display:

*******
Display
*******

.. _overview-text:

****
Text
****


.. _overview-toggle:

******
Toggle
******


.. _overview-select:

******
Select
******



data-multiple (boolean): This determines if people can select one or multiple options. BEWARE: the entity property being edited needs to support multiple, otherwise this obviously won't save properly.

data-ui (string): specify the way the select should display, either as a "list" where you can see all the options on the page (as radio, checkboxes or image buttons), or as a "menu" where the options are hidden in a drop down menu to conserve space.

data-placeholder (string): If this select has ui set to display "menu" this is the value that will appear in the dropdown when there are no options selected.

data-choices (JSON): If you want to manually set the options, you can pass in a JSON object. This can be either a simple array (e.g. ["value1", "value2"] where the values will be used for key and label), or an array of objects (e.g. [{value: "foo", label: "Foo", image: "//www.sitetheory.io/images/foo.jpg"}, {value: "bar", label: "Bar", image: "//www.sitetheory.io/images/foo2.jpg"}]). Allowed Properties include: value, label, image, containerClass, checked.

data-source (string): If you want the options to be pulled from an API source, you can specify the entity, e.g. "Layout" will initiate a call to /Api/Layout, and this will in turn pull all Layouts.

data-sourcetarget (JSON): If you need to limit the API call you can pass in additional target limits, e.g. a value like {"entity":"contentType", "id":100} will cause the API to actually send a limiting request like /Api/ContentType/100/Layout which will only return layouts that are assigned to contentType 100. If you don't know the content type, but that exists on the model of the current entity you are editing, you can pass in a dynamic "idAttribute" like {"entity":"contentType", "idAttribute":"contentType.id"} and the current entity will look up it's value for contentType.id and use that value.

data-sourcelabelattribute (string): When the API returns the model, it needs to know what field to use as the label for the options. So you would specify "name" or "title" or whatever the field is on that model.


data-sourceImageAttribute (string): When the API returns the model, it needs to know what field to find the images. This will default to 'images'.

data-sourceidattribute (string): When the API returns the model, it needs to know what field to use as the value for the options. So you would specify "id" or whatever the field is on that model. It defaults to 'id'.

 data-sourcelimit (integer): This determines the limit of how many options should appear at a time.

data-showSearch (boolean): This determines whether a search box appears to filter the options. This is only available if the options are sourced from the API, and will only appear if there are more than 1 page of results.

data-showselected (boolean): this allows you to specify that a collection will appear that shows all the elements selected. If the choices for the select are dynamically populated from a data-source (API) than the selected list will be a collection.

data-textSelectedNoContent (string): This determines what appears in the "selected" zone when there are no options selected. Depending on context, this message needs to change frequently. This area can also be customized with a template
data-cssSelectedNoContent="addAnimation"







.. _overview-datetime:

********
DateTime
********


.. _overview-editor:

******
Editor
******



.. _overview-link:

****
Link
****



.. _overview-popover:

*******
Popover
*******



.. _overview-pagination:

**********
Pagination
**********



.. _overview-collection:

**********
Collection
**********

data-meta: this allows you to pass in data to the collection widget so that it will be accessible in the template, e.g. when defining the widget on the DOM, add an attribute for data-meta='{"foo":"bar"}' will pass in values to the template to be accessed as {{ globals.meta.foo }}


.. _overview-save:

****
Save
****



.. _overview-publish:

*******
Publish
*******



.. _overview-delete:

******
Delete
******



.. _overview-seo:

***
Seo
***


.. _overview-routing:

*******
Routing
*******