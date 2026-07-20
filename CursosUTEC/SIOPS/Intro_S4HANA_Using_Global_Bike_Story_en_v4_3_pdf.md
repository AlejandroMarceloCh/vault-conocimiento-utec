---
curso: SIOPS
titulo: Intro_S4HANA_Using_Global_Bike_Story_en_v4.3
slides: 11
fuente: Intro_S4HANA_Using_Global_Bike_Story_en_v4.3.pdf
---

                                                                            CASE STUDY




                     Global Bike Group
                     Background and overview of Global Bike strategy and operations.




Product                    MOTIVATION                             PREREQUISITES
SAP S/4HANA 2023           A general understanding of Global      None
Global Bike                Bike (the enterprise) prior to
                           embarking on hands-on exercises
Fiori 3.0                  and case studies in the SAP ERP        NOTES
                           client is critical for success.        None
Level
                           This narrative provides a historical
Beginner
                           background for how Global Bike
                           began and an overview of its
Focus                      operations and strategy.        This
Company Background         information will be used extensively
                           throughout the curriculum material.
Authors
Simha Magal
Stefan Weidner
Jeff Word

Version
4.3

Last Update
July 2025




                                                                         © SAP UCC Magdeburg
                                                                                     CASE STUDY

              Company History


  Task Get to know the company’s history.                                              Time 15 min
  Short Description Read the below narrative to learn about the company’s
  history.


  The Global Bike Group has a pragmatic design philosophy that comes from                     Notes
  its deep roots in both the off-road trail racing and long-distance road racing
  sports. Nearly 20 years ago, its founders designed their first bikes out of
  necessity – they had races to win and the bikes that were available at the time
  did not perform to their extremely high standards. So, they took matters into
  their own hands and built legendary bikes that would outlast and outperform
  the competition. From these humble origins, Global Bike Incorporated was
  born and continues to deliver innovative high-performance bicycles to the
  world’s most demanding riders.
  This heritage of entrepreneurial spirit and quest for design perfection is still
  the cornerstone of Global Bike’s corporate philosophy. Global Bike produces
  bikes for the most demanding competitors – whether the competition is on
  pavement or dirt, for money, fame or just bragging rights.
  John Davis earned his racing scars in the mountain racing circuit in America,
  where he won numerous downhill and cross-country championships. Early on,
  John realized that the mass-produced bicycles available were inadequate in
  many ways for the type of racing he was doing. So, John stripped four of his
  old bikes down to the bare metal and rebuilt them into a single “Frankenstein”
  bike that he rode to win the national championship. Once news of his
  Frankenstein bike got out, John’s friends and even his competitors began
  asking him to build them a Frankenstein bike too. While recovering from an
  injury in 1990, John started producing the first series of Frankenstein bikes in
  his garage – each one custom-built from cannibalized parts from other bikes.
  As more and more orders came in, John successfully expanded Frankenstein
  Bikes from his garage operations into a full-blown manufacturing facility in
  Dallas and began producing custom trail bikes which he sold through a
  network of specialized bike dealers throughout the country.
  At nearly the same time, halfway around the world in Heidelberg, Germany,
  Peter Schwarz was studying engineering and competing in regional touring
  races on weekends. In between his races and studies, Peter worked at a bike
  shop in Heidelberg, fixing student bikes and tuning the touring bikes that he
  and his friends rode for competitions. As Peter’s reputation as a fierce
  competitor and mechanical wizard grew, he also began to design and build
  road bikes based on an ultra-light composite frame that he had created for one
  of his engineering courses. Peter’s innovative use of carbon composite
  materials allowed him to build a frame that was significantly stronger and one
  tenth the weight of competing frames. As a student, Peter did not have a great
  deal of financial resources, so he partnered with a local company that
  manufactured his frame designs as a contract manufacturer. Soon, Peter’s
  frames were being used by racers all over Europe and he started Heidelberg
  Composites to market and design frames which would be fabricated by a
© SAP UCC Magdeburg                                                                         Page 2
                                                                                                         CASE STUDY

  contract manufacturer on a larger scale. Heidelberg Composites sold its
  frames to specialized bike stores throughout Europe and directly to racing
  teams, eventually becoming the leader in lightweight touring frames in
  Europe.
  Through a twist of fate, Peter and John met each other in 2000 and
  immediately recognized their mutual passion for performance and
  complimentary business models. Each had been looking for a partner in
  another racing field and each had been looking for a partner in a different
  market. They quickly realized that a merger between their two companies
  would be extremely synergistic and that the combination of their product lines
  and regional distribution channels would generate a great deal of efficiencies.
  So, in 2001, Heidelberg Composites and Frankenstein Bikes merged to form
  Global Bike. Today, John and Peter share the responsibilities for managing
  Global Bike’s growing organization as co-CEO’s. John is responsible for
  sales, marketing, service & support, IT, finance and human resources groups
  and Peter is responsible for research, design, procurement and manufacturing
  groups from an organizational reporting perspective.

                                                                                                                        Figure 1:
                                                           Board of                                      Organizational Structure
                                                           Directors




                               John (Co-CEO)                                   Peter (Co-CEO)




                          Chief                                        VP Research
                                         Chief Financial   VP Human
       VP Marketing   Information                                          and           VP Operations
                                             Officer       Resources
                         Officer                                       Development




  However, Global Bike is a process-centric organization, so John and Peter
  prefer to think of the processes that they are responsible for, rather than the
  functional areas of the company that report to them. From this perspective,
  Peter is responsible for Idea-to-Market and Build-to-Stock and John is
  responsible for Order-to-Cash and Service & Support, as well as the
  supporting services for all four key processes. The simple way to look at their
  responsibilities would be to say that Peter spends money and builds products
  and John sells products and brings in money.




© SAP UCC Magdeburg                                                                                                     Page 3
                      CASE STUDY


                                     Figure 2:
                      Enterprise Process Map




© SAP UCC Magdeburg                  Page 4
                                                                                      CASE STUDY

              Corporate Overview


  Task Develop an organizational chart for Global Bike’s enterprise structure.           Time 15 min
  Short Description Read the below narrative to gather all relevant information
  for sketching Global Bike’s current company structure.


  Due to several tax and export issues, Global Bike Groups’s headquarters is                         Notes
  located in Dallas and Global Bike Inc. is registered as a US company,
  following US GAAP accounting standards. Global Bike Group operates a
  subsidiary company, Global Bike Germany GmbH, which is based in
  Heidelberg and is subject to IFRS accounting standards and German tax
  regulations.
  Material planning, finance, administration, HR and IT functions are
  consolidated at the Dallas headquarters. The Dallas facility manufactures
  products for the US and export markets and its warehouse manages product
  distribution for the central US and internet retailers. Global Bike Inc. also has
  warehouses for shipping and export in both San Diego and Miami. San Diego
  handles West Coast distribution and exports for Asia, while Miami handles
  East Coast distribution and Latin America exports.
  Global Bike Germany GmbH has its headquarters in Heidelberg Germany.
  The majority of research and development is housed in the Heidelberg offices.
  Heidelberg is also the main manufacturing facility for Global Bike in Europe.
  The Heidelberg warehouse handles all shipping for southern Europe. The
  Hamburg warehouse handles all shipping for the UK, Ireland, Middle East and
  Africa. Global Bike sells its bikes throughout the world and employs
  approximately 100 people, 2/3rds of the employees are in the US and the
  remaining 1/3 in Europe.

                                                                                       Organizational Chart




© SAP UCC Magdeburg                                                                               Page 5
                                                                                    CASE STUDY

              Product Strategy


  Task Get familiar with Global Bike’s product strategy.                               Time 15 min
  Short Description Read the below narrative about Global Bike’s product
  strategy.


  Global Bike is a world class bicycle company serving the professional and                        Notes
  “prosumer” cyclists for touring and off-road racing. Global Bike’s riders
  demand the highest level of quality, toughness and performance from their
  bikes and accessories.
  Product development is the most critical element of Global Bike’s past and
  future growth. Global Bike has invested heavily in this area, focusing on
  innovation, quality, safety and speed to market. Global Bike has an extensive
  innovation network to source ideas from riders, dealers and professionals to
  continuously improve the performance, reliability and quality of its bicycles.
  In the touring bike category, Global Bike’s handcrafted bicycles have won
  numerous design awards and are sold in over 10 countries. Global Bike’s
  signature composite frames are world-renowned for their strength, low weight
  and easy maintenance. Global Bike bikes are consistently ridden in the Tour
  de France and other major international road races. Global Bike produces two
  models of their signature road bikes, a deluxe and professional model. The
  key difference between the two models is the type of wheels used, aluminum
  for the basic model and carbon composite for the professional model.
  Global Bike’s off-road are also recognized as incredibly tough and easy to
  maintain. Global Bike trail bikes are the preferred choice of world champion
  off-road racers and have become synonymous with performance and strength
  in one of the most grueling sports in the world. Global Bike produces two
  types of off-road bike, a men’s and women’s model. The basic difference
  between the two models is the smaller size and ergonomic shaping of the
  women’s frame.

                                                                                                 Figure 3
                                                                                     Global Bike Finished
                                                                                                Products




  Global Bike also sells an accessories product line comprised of helmets, t-
  shirts and other riding accessories. Global Bike partners with only the highest
  quality suppliers of accessories which will help enhance riders’ performance
  and comfort while riding Global Bike bikes.




© SAP UCC Magdeburg                                                                             Page 6
                      CASE STUDY


                                  Figure 4
                       Global Bike Trading
                                    Goods




© SAP UCC Magdeburg              Page 7
                                                                                      CASE STUDY

              Manufacturing Strategy


  Task Get familiar with Global Bike’s manufacturing strategy.                          Time 10 min
  Short Description Read the below narrative about Global Bike’s
  manufacturing strategy.


  Global Bike operates two production facilities, Dallas and Heidelberg. Each                       Notes
  facility has three assembly lines and can produce around 1000 bikes per year.
  Total production capacity is roughly 6000 bikes per year, but can be increased
  by 15%-20% by using overtime hours and part-time workers.
  Global Bike has outsourced the production of both off-road and touring frames
  and the carbon composite wheels to trusted partners who have specialty
  facilities to fabricate the complex materials used. Global Bike maintains very
  collaborative research and design relationships with these specialty partners
  to ensure that innovations in both material and structural capabilities are
  incorporated into the frames. Global Bike primarily assembles semi-finished
  goods into finished goods at its production facilities. Finished goods are either
  stored in the local warehouse or shipped to other regional distribution centers
  to fulfill customer orders.

                                                                                                  Figure 5
                                                                                         Global Bike Raw
                                                                                                 Materials
                                                                                        Global Bike Semi-
                                                                                          Finished Goods




© SAP UCC Magdeburg                                                                              Page 8
                                                                                     CASE STUDY

              Distribution Network


  Task Get familiar with Global Bike’s distribution network.                             Time 10 min
  Short Description Read the below narrative about Global Bike’s distribution
  network.


  Given the highly specialized nature of Global Bike’s bicycles and the                              Notes
  personalized needs of riders, Global Bike sells its bikes exclusively through
  well-known and respected Independent Bicycle Dealers (IBDs). These dealers
  employ staff members who are experts in off-road and tour racing to help
  consumers choose the right Global Bike bike and accessories for their
  individual needs.

                                                                                                   Figure 6
                                                                                     Global Bike Customers
                                                                                                         in
                                                                                          US and Germany




  Due to the highly technical nature of its products, Global Bike has embraced
  the Internet primarily as an information channel, maximizing its potential for
  educating consumers and partners and marketing its products to a large
  audience.
  Since Global Bike’s main sales channel is through specialty resellers and there
  are complex tax issues associated with selling in multiple states and countries,
  they have a limited amount of internet sales.




© SAP UCC Magdeburg                                                                               Page 9
                                                                                    CASE STUDY

              Partner Network


  Task Get familiar with Global Bike’s partner network.                                 Time 10 min
  Short Description Read the below narrative about Global Bike’s partner
  network.


  Global Bike has established an extensive partner operation to ensure process                      Notes
  continuity between Global Bike and its partners to deliver best-in-class
  products for its customers. Special attention has been paid to nurturing strong
  relationships with suppliers and Global Bike is generally the largest customer
  of its main suppliers.

                                                                                                  Figure 7
                                                                                    Global Bike Vendors in
                                                                                         US and Germany




© SAP UCC Magdeburg                                                                             Page 10
                                                                                     CASE STUDY

              IT Strategy


  Task Get familiar with Global Bike’s IT strategy.                                     Time 5 min
  Short Description Read the below narrative about Global Bike’s information
  technology strategy.


  During 2009, Global Bike integrated a shared services model for all IT                      Notes
  functions, located in the Dallas office. Along with this move to centralized IT,
  Global Bike also implemented SAP ERP (version 6.0). Prior to this, divisions
  were running multiple, independent application environments. All ERP
  functions are centralized with the primary objectives to reduce costs and
  deliver best-in-class technology to all divisions globally. This centralized
  approach offers Global Bike an advanced business platform under a highly
  controlled environment, which enables consistency of operations and process
  integrity across the globe. In 2017, the company’s management decided to
  move to SAP S/4HANA to accelerate the digital transformation.




© SAP UCC Magdeburg                                                                        Page 11
