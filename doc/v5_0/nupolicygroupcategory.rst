.. _nupolicygroupcategory:

nupolicygroupcategory
===========================================

.. class:: nupolicygroupcategory.NUPolicyGroupCategory(bambou.nurest_object.NUMetaRESTObject,):

Policy Group Categories are used to group Policy Group tags of similar type (e.g., Application, App-Tier, Location etc.) to provide additional context for flow visualization and analytics


Attributes
----------


- ``name`` (**Mandatory**): Name of the Policy Group Cateogry

- ``last_updated_by``: ID of the user who last updated the object.

- ``default_tag``: Boolean which identifies if this is a default policy group category.

- ``description``: Describes the Policy Group Category.

- ``entity_scope``: Specify if scope of entity is Data center or Enterprise level

- ``external_id``: External object ID. Used for integration with third party systems




Children
--------

================================================================================================================================================               ==========================================================================================
**class**                                                                                                                                                      **fetcher**

:ref:`numetadata.NUMetadata<numetadata>`                                                                                                                         ``metadatas`` 
:ref:`nuglobalmetadata.NUGlobalMetadata<nuglobalmetadata>`                                                                                                       ``global_metadatas`` 
:ref:`nupolicygroup.NUPolicyGroup<nupolicygroup>`                                                                                                                ``policy_groups`` 
================================================================================================================================================               ==========================================================================================



Parents
--------


- :ref:`nuenterprise.NUEnterprise<nuenterprise>`

