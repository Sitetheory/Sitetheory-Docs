Readable/Writable Properties
============================
When defining an entity you should define which properties are readable and writable.
You can specify different values for each definition beyond just the name, e.g. ['attribute' => 'view', 'alias' => 'SitetheoryCoreBundle:View\View']

attribute: the property name

alias: The path to an associated entity. This is usually not necessary if the property is a valid associated entity because the tree builder will find this based on the target's repo->classMetaData()->getAssociation Mapping(). But in cases like view.viewVersion where there is no doctrine association, but we want to tree build the viewVersion readable properties, we need to include this.

searchable: true|false determines if the field is searchable

joinable: true|false determines if the field should be auto-joined when the field is searched. If it's not searchable, it will never be joinable. You don't need to mark joinable=>false if searchable=>false already.

level: integer determines whether the field is searchable or readable (API finalizer) if it's found as a readable property on nested entities, beyond a certain level. With a value of 1, it will be searchable/readable only on the first level, e.g. routing.timeEdit is set as direct=>1 because we don't want to see the timeEdit of routing when we fetch the view.

sentinel: an array that contains the sentinel required in order to interact with the field, e.g. viewVersionNotes has sentinel=>['edit']