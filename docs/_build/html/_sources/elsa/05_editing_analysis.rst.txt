Editing an ELSA analysis run
============================

Naming ELSA analysis run 
------------------------

Upon clicking *NEW ANALYSIS RUN* (see :numref:`fig-create-run`), users will be able to view and edit a tentative analysis. Firstly, users must provide a new, unique name for their analysis run. While there are no restrictions on the name given to each run, we suggest that run names should include meaningful descriptions, ideally referencing the parameters used (e.g, include information like, BPF 10, or Protect 38%). 

This section provides detailed instructions for configuring all aspects of your ELSA analysis run, from naming conventions to feature weighting.

Selecting lock-in functions
---------------------------

Lock-in functionalities are applied to the protect zone. The lock-in layer consists of existing Protected Areas (PAs) within the country. Users can choose to lock-in or lock-out existing PAs for the Protect Zone (additionally the Restore Zone, if applicable). Locking in PAs ensures their inclusion in the analysis to identify priority areas where actions to protect nature should be undertaken. The percentage national land area covered by PAs is shown in the lock-in functionality to allow users to make an informed lock-in decision. 

Lock-in of PAs (:numref:`fig-lockin-options`):  

* Select "Lock-in Existing Protected Areas" if you want to force the analysis to include existing PAs within the "protection" action. 
* Select "Lock-in nothing" if you wish to independently assess the optimal location of new PAs in your country based on the resulting “Protect” Areas in the resulting ELSA Action map.

.. _fig-lockin-options:

.. figure:: images/create-analysis.png
   :alt: Lock-in functionalities
   :align: center
   
   Lock-in functionalities

As seen in :numref:`fig-lockin-options` for Kazakhstan, the existing protected area estate already covers 12.5% of the country. Therefore, when *Lock-in Existing Protected Areas* is selected a minimum *Protection* budget of at least 12.5% of the national territory is required for the optimisation model to be feasible.

Specifying objectives  
---------------------

This part of the tool allows users to set area-based budgets (targets) for protection, restoration, management and/or urban greening. Budgets can also be understood as the percentage of land area that can be allocated to each action within the country. The default values in any given ELSA tool are derived from land-based targets in the KMGBF, unless further customized for your country by the UNBL team based on the NBSAP or other national policy documents. 

Users can set any value greater than or equal to 0.001 for protection, restoration, management and/or urban greening objectives. The sum of the value for all objectives may be less than or equal to 100% but should not exceed 100%.  

Users should consider that if they want to lock-in existing PAs, the overall protection budget must be equal to or greater than the land area covered by existing PAs. For example, the land area covered by existing PAs in Kazakhstan is 12.5%. Therefore, the protect budget should be equal to or greater than 12.5%. 

.. figure:: images/setting-objectives.png
   :alt: Setting objectives
   :align: center
   
   Setting objectives

Specifying the boundary penalty factor 
--------------------------------------

The boundary penalty factor is used to promote spatial cohesion when prioritizing land use zones. The boundary penalty can be 0 or higher. The higher the value, the more connected and contiguous the ELSA action zones will be on the map. This adjustment is based on the idea that, for real-world planning, a more connected zone is usually easier to manage and execute actions. 

Steps: 

1. To set the limit penalty, start with a small number, e.g. 10.
2. Increase the number iteratively, i.e., rerun the analysis repeatedly, by an order of magnitude (e.g., 10 -> 100-> 1000), reducing the rate of increase as you approach solutions that lead to your desired level of clustering. Each time you change the penalty, you will have to rerun the optimization until you arrive at a map that is sufficiently contiguous to meet your needs.

.. note:: 
   Note: Increasing the boundary penalty factor from 0 will result in longer solve times; in some cases these can be much longer. 


.. figure:: images/setting-bpf.png
   :alt: Adjustment of the boundary penalty factor 
   :align: center
   
   Adjustment of the boundary penalty factor 

Editing the weights of planning features 
----------------------------------------

To edit planning feature weights, click on the *SET FEATURE WEIGHTS* button near the top-right corner of the analysis run pop-up window. 

Users should enter a weight for each planning feature in the input data list. We recommend a scale of 0 to 10 as follows, based on the priority level of each planning feature: 

*  0 - not important / excluded from the analysis 
*  1.0 - low importance / lower importance than average 
*  5.0 - medium importance 
*  10 - utmost importance  

To allow users to make the most informed decision possible, the theme (biodiversity/climate change/human well-being), impacted actions and proxy KMGBF policy target (or other relevant NBSAP/national policy target) are listed for each planning feature. Users can evaluate the priority level of each planning feature and assign an informed weight by deciding on the relative importance of each of the planning features used to map KMGBF targets (or other relevant NBSAP/national policy targets otherwise defined by their country) in their country. 

For example, if KMGBF Target 1 is of especially high importance for the user, then planning features such as intact ecosystems, high integrity forests, biodiversity habitat index and biodiversity intactness index should be given greater weight (\> 3).Alternatively, if the user believes threatened ecosystems in their country are particularly degraded and should be considered for identifying priority areas for restoration for KMGBF Target 2, then they can give a higher weight to the threatened ecosystems for restoration planning feature which specifically maps these areas (:numref:`fig-edit-weights`). 

For a full list of input data, as well as which KMGBF targets they are used to map, please see :ref:`Annex 2 <annex-2>`.

.. _fig-edit-weights:

.. figure:: images/create-analysis.png
   :alt: Editing weights
   :align: center
   
   Editing weights


View input layers  
-----------------

Users should consider that if they want to view input layers before setting weights, they will have to exit the initial analysis run pop-up window by clicking *SAVE FOR LATER* in the bottom-right corner. They can then come back to their saved draft analysis run after viewing the desired input features. 

To view original input layers into the data stack for the tool, users can click on the *INPUT LAYERS* option next to the *ANALYSIS RUNS* option in the left tool tab. Users can then toggle specific input layers to view them on UNBL. 

.. figure:: images/create-analysis.png
   :alt: Viewing action zones and planning features on UNBL
   :align: center
   
   Viewing action zones and planning features on UNBL

By clicking on the INPUT LAYERS tab, users can view each individual input planning feature layer included in the ELSA analysis; these inputs are specifically tailored to help identify priority areas for KMGBF implementation, as well as NBSAP/other national policy implementation, if specifically requested by the user’s country. Users can additionally view (optional) lock-in features (namely, existing protected areas) in their country, as well as action zones. 

Steps 

* Click the toggle button for each action zone/lock-in zone/input planning feature layer you want to display.
* Click the toggle button again to remove the selected layer from the view. 
* Users have the option to view additional information (description of the layer, original input layers, source) for currently toggled layers by clicking on the round ‘i’ icon either in the individual layer’s legend or next to the toggle button for each layer. 


.. figure:: images/create-analysis.png
   :alt: Viewing metadata
   :align: center
   
   Viewing metadata