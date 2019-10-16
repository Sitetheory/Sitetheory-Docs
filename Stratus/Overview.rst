########
Overview
########

Stratus is our own javascript library for managing the front end of websites. It allows us to use require.js to load the files we need when we need them. We use an Angular model to create Components, Controllers, Filters, Directives, etc. See our :doc:`Components documentation </1.0/Overview/Components>` for generic information about how we use components on the site.



Workflow
========
env.js - The site loads the Environment to set key variables about the environment.

config.js - Stratus has it's own core config.js that defines core stratus paths to components, services, filters, etc. And Sitetheory has a custom config.js that defines custom components for Sitetheory, or Stratus "extra" components that are being enabled for Sitetheory.

init.js - loads the Stratus boot.js and the merged config files.

See how we implement this loading of files in the CoreBundle:base.html.twig


Components
==========
See our :doc:`Stratus Components documentation </1.0/Overview/Stratus-Components>` for an overview of Component Architecture.

Filters
=======
See our :doc:`Stratus Filters documentation </1.0/Overview/Stratus-Filters>` for an overview of Filters Architecture.


Directives
==========
See our :doc:`Stratus Directives documentation </1.0/Overview/Stratus-Directives>` for an overview of Directives Architecture.