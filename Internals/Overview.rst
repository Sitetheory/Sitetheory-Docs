########
Overview
########


==============================
Entity & Event Listener Timing
==============================

We regularly use Entity and Event listeners to execute specific actions. It is critical that we create those actions in the right type of listener, so that they are able to modify the entity at the right sequence. Failure to execute your code could result in your changes not being persisted, or other dirty states that will create errors.

NOTE: we have customized Doctrine's UnitOfWork file to add custom listeners that were lacking, and this has not been accepted by Doctrine's team (yet).

Below is a summary of the timing and order of operations for the UnitOfWork.php (not real PHP code) to help you understand what order methods are executed for the Listeners:


.. code-block:: php
    :linenos:

    em->persist() {
        prePersist()
    }

    em->remove() {
        preRemove()
        ->scheduleForDelete
    }

    em->flush() {
        preFlush()

        ->computeChangeSets() || ->computeSingleEntityChangeSet

        onFlush()

        ->MySQL Connection

        if (new) {
            ->executeInserts()
            postPersist()
        }

        if (update) {
            preUpdate()
            ->executeUpdates()
            postUpdate()
        }

        ->associationDelete()
        ->associationUpdate()

        if (remove) {
            ->executeDeletions()
            postRemove()
        }

        PostFlush()
    }