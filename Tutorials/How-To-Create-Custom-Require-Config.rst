You can add custom Require.js config for your Vendor or vhost, which will be compiled with the core config. For example, if you need to load your own directives or components.

JAVASCRIPT
Create custom Require.js config, to tell Require.js (and Stratus) the location of your custom dependencies.


Example 1: Specify shim, paths, etc (full config structure)
`AcmeFooBundle/Resources/public/js/boot/config.js`
::

    boot.config({
        shim: {
            'angular-froala': { deps: ['angular', 'froala'] }
        },
        paths: {
            froala: boot.bundle + 'stratus/bower_components/froala-wysiwyg-editor/js/froala_editor.min',
            'angular-froala': boot.bundle + 'stratus/bower_components/angular-froala/src/angular-froala',
            'stratus.components.foo': 'acmefoo/js/foo'+boot.suffix
        }
    });

Example 2: Specify only paths (shortcut)
`AcmeFooBundle/Resources/public/js/boot/config.js`
::

    boot.config({
        'stratus.components.foo': 'acmefoo/js/components/foo'+boot.suffix
    });


Note: See `SitetheoryStratusBundle/Resources/public/stratus/boot/env.js` for available properties, e.g. `boot.suffix`. The Sitetheory config will load first and set the default values for these properties, which will be available for the custom config above.

If the path does not start with a slash, the config will automatically prefix the path provided with `boot.cdn` (which will be the path to the CDN if it's production or a relative '/' if it's dev) and the `boot.relative` (which is the path to the current version, e.g. 'assets/1/0/bundles'). So you only need to start with the vendor bundle name folder.

TWIG
Then in your twig file, just load your custom config, BEFORE

::

    {# Load Custom Vendor or Vhost Require Config #}
    {% block scriptConfig %}

        {% javascripts '@AcmeFooBundle/Resources/public/js/boot/config.js' filter='?uglifyjs2' %}
        <script src="{{ asset_url }}"></script>
        {% endjavascripts %}

        {# You MUST include the parent, so that it doesn't overwrite other instances of custom config by other vendors #}
        {{ parent() }}

    {% endblock scriptConfig %}

