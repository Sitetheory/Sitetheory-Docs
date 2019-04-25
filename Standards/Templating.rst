##################
Template Standards
##################

****
Twig
****
We use Twig because it's awesome. See: https://twig.symfony.com/doc/2.x/

Twig Extensions
===============
You can create useful methods that extend Twig with our own filters and functions. See Sitetheory/CoreBundle/Twig/Extensions/UtilityExtension.php (and other related). These need to be registered in the bundle's Resources/config/services.yml



Troubleshooting in Twig
=======================
It's often helpful to dump variables inside a Twig template, so that you know what variables exist, and what the values are. If you are in ?mode=dev (and you have the proper developer credentials) you will see a Symfony profiler bar, where dumps appear. In normal PHP, this is invoked like this:


.. code-block:: php
    :linenos:

    if(function_exists('dump')) dump('some string', $someObject, $otherArray);


In Twig, you can dump a variable to the profiler bar like this:

.. code-block:: html+twig
    :linenos:

    {% dump someVariable %}

Dumping in Twig Extension
---------------------------------
Extensions exist within their own scope, and so if you do a dump() within a PHP file that the Extension calls, you might expect it to appear in the profiler, but it never makes it out of this scope. So the solution is to include (temporarily) the TwigExtensionTrait in your extension and make it's dump function available to Twig.

.. code-block:: php
    :linenos:

    class FooExtension extends \Twig_Extension
    {
        // Include the Trait with the dump variable and method
        use TwigExtensionTrait;

        // Register the dump method along with the rest
        public function getFunctions() {
            return [
                // Existing Method
                new \Twig_SimpleFunction('foo', [$this, 'getFoo']),
                // Custom Dump Method: This should be called within twig, using {% dump extensionDump() %}
                // TODO: deactivate when not testing
                new \Twig_SimpleFunction('extensionDump', [$this, 'getExtensionDump'])
            ];
        }

        // The existing function you want to dump from.
        public function getFoo() {
            // Set a Variable you want to dump from the twig
            $this->addDump($myObject);
        }

    }


Then in the Twig template you can dump what you previously registered within the Extension.

.. code-block:: html+twig
    :linenos:

    {% dump extensionDump() %}




