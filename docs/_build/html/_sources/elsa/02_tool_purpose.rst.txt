What is the ELSA tool for? 
==========================


The ELSA tool enables diverse stakeholders to collaboratively assess national priorities for the KMGBF, explore trade-offs and synergies, and develop actionable spatial plans to support national implementation of Targets 1, 2, and 3 through identifying action areas that will have the highest impact based on a number of biogeographical features and constraints. Users with a UNBL workspace can modify and execute a customized national spatial prioritization as part of a participatory spatial planning process using the ELSA tool. They can: 

    - Display input layers (also known as planning features);
    - View and download resulting ELSA Action maps; 
    - Download resulting ELSA Action maps in raster format, which can be used for further analysis according to the needs of the interested parties in software from Geographic Information Systems (GIS);
    - Download results and parameters of an existing ELSA analysis run as a summary table, which is available in ``.xlsx``, ``.csv`` and ``.json`` formats;
    - Create and execute new ELSA analysis runs with different stakeholder groups. Users can modify and edit ELSA analysis runs through the following ways:
    - Modify the percentage of national territory that can be allocated for each nature-based action zone for protection (KMGBF Target 3), restoration (KMGBF Target 2), management (KMGBF Target 10) and/or urban greening (KMGBF Target 12) objectives. These configurations can be adapted to the country's political objectives in terms of conservation, restoration, and protection, among others;
    - Choose whether to lock-in existing Protected Areas for protection, ensuring existing Protected Areas are selected within the solution map;
    - Edit weights of each of the input layers (planning features) used to map KMGBF targets based on national importance of the mapped feature and confidence in the input data;
    - Edit the boundary penalty factor parameter according to the analysis needs; 

The ELSA tool **cannot** be used to: 

  - Add additional data layers for inclusion in the ELSA tool either as planning features or as zoning constraints; 
  - Directly replace input layers with other input layers; 
  - Add additional lock-in features. 

These modifications, as well as further custom analysis development to meet national needs, are available on a cost recovery basis from the UNBL team. To learn more and explore options, please contact support@unbiodiversitylab.org. 

The ELSA tool uses the *prioritizr* package in the back end as a spatial optimization tool to run an ELSA analysis. *prioritizr* supports a broad range of objectives, constraints and penalties to create a tailored analysis. It can execute optimizations quickly (often within 3-5 minutes). It can therefore be used to generate and refine conservation plans in real-time during stakeholder meetings, and contribute to a more transparent, inclusive, and participatory decision-making process to identify priority areas to support the implementation of KMGBF Targets 1, 2 and 3, with powerful co-benefits for Targets 4-12.  

.. note:: 
  Definitions of technical terminology mentioned in the guidance can be found in :ref:`Annex 1 <annex-1>`. 


.. figure:: picture.jpeg
   :alt: ELSA Results Map
   :align: center  

   Initial interface of the ELSA tool on UNBL