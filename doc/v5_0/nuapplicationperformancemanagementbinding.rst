.. _nuapplicationperformancemanagementbinding:

nuapplicationperformancemanagementbinding
===========================================

.. class:: nuapplicationperformancemanagementbinding.NUApplicationperformancemanagementbinding(bambou.nurest_object.NUMetaRESTObject,):

Association object for maintaining the priority of AppliationGroup(s) associated to a Domain


Attributes
----------


- ``last_updated_by``: ID of the user who last updated the object.

- ``read_only``: Determines whether this entity is read only.  Read only objects cannot be modified or deleted.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``priority``: Priority of the associated Application Group

- ``associated_application_performance_management_id`` (**Mandatory**): Associated Application Group ID

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nudomain.NUDomain<nudomain>`

- :ref:`nul2domain.NUL2Domain<nul2domain>`

