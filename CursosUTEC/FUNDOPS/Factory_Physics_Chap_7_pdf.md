---
curso: FUNDOPS
titulo: Factory-Physics-Chap. 7
slides: 38
fuente: Factory-Physics-Chap. 7.pdf
---

C           H                   A                  P                   T                  E                   R



       7             Basic Factory Dynamics




                     I do not know what I may appear to the world; but to myself I seem to have been only
                     like a boy playing on the seashore, and diverting myself in now and then ﬁnding a
                     smoother pebble or a prettier shell than ordinary, whilst the great ocean of truth lay all
                     undiscovered before me.
                                                                                                   Isaac Newton



7.1   Introduction
                     In the previous chapter, we argued that manufacturing management needs a science of
                     manufacturing. In this chapter, we begin the development of such a science by examining
                     some basic behavior of production lines. Our intent here is not to specify how to optimize
                     or improve manufacturing systems, but instead to simply describe how they can and do
                     behave. Using the descriptive understanding of the factors that inﬂuence performance
                     we develop in Part II, we will address the prescriptive problem of how to improve
                     performance in Part III.
                          In this and other chapters of Part II we will adopt the reductionist viewpoint com-
                     mon to science. That is, we will reduce the complexity of manufacturing systems to a
                     manageable level by restricting our attention to speciﬁc components and behaviors. In
                     particular, throughout Part II we will focus almost exclusively on production lines. The
                     reason for this is that lines are simple enough to analyze but complex enough to provide
                     a realistic link between operational and ﬁnancial measures. In contrast, a single station
                     is analytically simple, but only distantly connected to overall ﬁnancial performance. On
                     the other end of the spectrum, an entire factory is obviously directly associated with
                     ﬁnancial performance, but extremely difﬁcult to analyze. For this reason, the dynamics
                     of production lines (or process ﬂows) represent the foundation of manufacturing science.
                          In this chapter, we ﬁrst characterize production lines in terms of three parameters.
                     Two of these are simple measurable descriptors of the line, while the third is a more
                     abstract characterization of the line’s efﬁciency. Then we examine the extremes of be-
                     havior (i.e., efﬁciency) that are possible for a given pair of measurable descriptors. This
                     leads us to a method for classifying production lines in terms of their efﬁciency. Finally,
                     we illustrate by means of a realistic case how this classiﬁcation scheme can be used to
                     give an “internal benchmark” against which actual performance can be compared.
                          But, before we can do all this, we must deﬁne our terms.

                                                                                                            227
228                  Part II   Factory Physics


7.2     Deﬁnitions and Parameters
                     The scientiﬁc method requires precise terminology. Unfortunately, manufacturing terms
                     in industry and the operations management literature are far from standardized. This can
                     make it extremely difﬁcult for managers and engineers from different companies (and
                     even the same company) to communicate and learn from one another. What it means for
                     us is that the best we can do is to deﬁne our terms carefully and warn the reader that other
                     sources will use the same terms differently or use different terms in place of ours.


7.2.1   Deﬁnitions
                     In Part II, we focus on the behavior of production lines, because these are the links
                     between individual processes and the overall plant. Therefore, the following terms are
                     deﬁned in a manner that allows us to describe lines with precision. Some of these terms
                     also have broader meanings when applied to the plant, as we note in our deﬁnitions and
                     will occasionally adopt in Part III. However, to develop sharp intuition about production
                     lines, we will maintain these rather narrow deﬁnitions for the remainder of Part II.
                          A workstation is a collection of one or more machines or manual stations that
                     perform (essentially) identical functions. Examples include a turning station made up
                     of several vertical lathes, an inspection station made up of several benches staffed by
                     quality inspectors, and a burn-in station consisting of a single room where components
                     are heated for testing purposes. In process-oriented layouts, workstations are physically
                     organized according to the operations they perform (e.g., all grinding machines located
                     in the grinding department). In product-oriented layouts they are organized in lines
                     making speciﬁc products (e.g., a single grinding machine dedicated to an individual line).
                     The terms station, workcenter, and process center are synonymous with workstation.
                          A part is a piece of raw material, a component, a subassembly, or an assembly that
                     is worked on at the workstations in a plant. Raw material refers to parts purchased from
                     outside the plant (e.g., bar stock). Components are individual pieces that are assembled
                     into more complex products (e.g., gears). Subassemblies are assembled units that are
                     further assembled into more complex products (e.g., transmissions). Assemblies (or ﬁnal
                     assemblies) are fully assembled products or end items (e.g., automobiles). Note that one
                     plant’s ﬁnal assemblies may be another’s raw material. For instance, transmissions are the
                     ﬁnal assemblies of a transmission plant, but are raw materials or purchased components
                     to the automotive assembly plant.
                          A part that is sold directly to a customer, whether or not it is an assembly, is called an
                     end item. The relationship between end items and their constituent parts (raw materials,
                     components, and subassemblies) is maintained in the bill of material (BOM), which
                     Chapter 3 presented in detail.
                          For the most part, consumables are materials such as bits, chemicals, gases, and
                     lubricants that are used at workstations but do not become part of a product that is
                     sold. More formally, we distinguish between parts and consumables in that parts are
                     listed on the bill of material, while consumables are not. This means that some items
                     that do become part of the product, such as solder, glue, and wire, can be considered
                     either parts if they are recorded on the bill of material or consumables if they are not.
                     Since different purchasing schemes are typically used for parts and consumables (e.g.,
                     parts might be ordered according to an MRP system, while consumables are purchased
                     through a reorder point system), this choice may inﬂuence how such items are managed.
                          A routing describes the sequence of workstations passed through by a part. Routings
                     begin at a raw material, component, or subassembly stock point and end at either an
Chapter 7   Basic Factory Dynamics                                                      229

intermediate stock point or ﬁnished-goods inventory. For instance, a routing for gears
may start at a stock point of raw bar stock; pass through cutting, hobbing, and deburring;
and end at a stock point of ﬁnished gears. This stock of gears might in turn feed another
routing that builds gear subassemblies. The bill of material and the associated routings
contain the basic information needed to make an end item. We frequently use the terms
line and routing interchangeably.
     A customer order is a request from a customer for a particular part number, in a
particular quantity, to be delivered on a particular date. The paper or electronic purchase
order sent by the customer might contain several customer orders. Henceforth, we will
refer to a customer order as simply an order. Inside the plant, an order can also be an
indication that certain inventories (e.g., safety stocks) need to be replenished. While
timing may be more critical for orders originating with customers, both types of orders
represent demand.
     A job refers to a set of physical materials that traverses a routing, along with the
associated logical information (e.g., drawings, BOM). Although every job is triggered by
either an actual customer order or the anticipation of a customer order (e.g., forecasted
demand), there is frequently not a one-to-one correspondence between jobs and orders.
This is because (1) jobs are measured in terms of speciﬁc parts (uniquely identiﬁed by
a part number), not the collection of parts that may make up the assembly required to
satisfy an order, and (2) the number of parts in a job may depend on manufacturing
efﬁciency considerations (e.g., batch size considerations) and thus may not match the
quantities ordered by customers.
     With the above terminology in hand, we can now deﬁne the key performance mea-
sures in which we are interested.
     The average output of a production process (machine, workstation, line, plant) per
unit time (e.g., parts per hour) is deﬁned as the system’s throughput (TH), or sometimes
throughput rate. At the ﬁrm level, throughput is deﬁned as the production per unit time
that is sold. However, managers of production lines generally control what is made rather
than what is sold. Therefore, for a plant, line, or workstation, we deﬁne throughput to be
the average quantity of good (nondefective) parts (the manager does have control over
quality) produced per unit time. In a line made up of workstations in tandem dedicated
to a single family of products and where all products pass through each station exactly
once, the throughput at every station will be the same (provided there is no yield loss). In
a more complex plant, where workstations service multiple routings (e.g., a job shop),
the throughput of an individual station will be the sum of the throughputs of the routings
passing through it (where throughput is measured in dollars or standard parts to allow
summation of the separate ﬂows). When throughput is measured in cost dollars (rather
than in prices), it is typically called cost of goods sold.
     An upper limit on the throughput of a production process is its capacity. In most
cases, releasing work into the system at or above the capacity causes the system to become
unstable (i.e., build up WIP without bound). Only very special systems can operate stably
at capacity. Because this concept is subtle and important, we will investigate it more
thoroughly later in this chapter, once we have introduced the appropriate concepts.
     As noted, the physical inputs at the start of a production process are typically called
raw material inventory (RMI). This could represent bar stock that is cut up and then
milled into gears, sheets of copper and ﬁberglass that are laminated together to make
circuit boards, wood chips that become pulp and then paper stock, or rolls of sheet steel
that are pressed into automobile fenders. Typically, the stock point at the beginning of
a routing is termed raw material inventory even though the material may have already
undergone some processing.
230   Part II   Factory Physics

            The stock point at the end of a routing is either a crib inventory location (i.e., an
      intermediate inventory location) or ﬁnished goods inventory (FGI). Crib inventories
      are used to gather different parts within the plant before further processing or assembly.
      For instance, a routing to produce gear assemblies may be fed by several crib inventories
      containing gears, housings, crankshafts, and so on. Finished goods inventory is where
      end items are held prior to shipping to the customer.
            The inventory between the start and end points of a product routing is called work
      in process (WIP). Since routings begin and end at stock points, WIP is all the product
      between, but not including, the ending stock points. Although in colloquial use WIP
      often includes crib inventories, we make a distinction between crib inventory and WIP
      to help clarify the discussion.
            A commonly used measure of the efﬁciency with which inventory is used is inven-
      tory turns, or the turnover ratio, which is deﬁned as the ratio of throughput to average
      inventory. Typically, throughput is stated in yearly terms, so that this ratio represents the
      average number of times the inventory stock is replenished or turned over. Exactly which
      inventory is included depends on what is being measured. For instance, in a warehouse,
      all inventory is FGI, so turns are given by TH/FGI. In a plant, we generally consider
      both WIP (inventory still in the line) and FGI (inventory waiting to ship), so turns are
      given by TH/(WIP + FGI). In any case, it is essential to make sure that throughput and
      inventory are measured in the same units. Since inventory is usually measured in cost
      dollars (i.e., rather than price or sales dollars), throughput should also be measured in
      cost dollars (i.e., cost of goods sold).
            The cycle time (CT), which is also called variously average cycle time, ﬂow time,
      throughput time, and sojourn time, of a given routing is the average time from release
      of a job at the beginning of the routing until it reaches an inventory point at the end of
      the routing (i.e., the time the part spends as WIP).1 Although this is a precise deﬁnition
      of cycle time, it is also narrow, allowing us to deﬁne cycle time only for individual
      routings. It is common for people to refer to the cycle time of a product that is composed
      of many complex subassemblies (e.g., automobiles). However, it is not clear exactly what
      is meant by this. When does the clock start for an automobile? When the chassis starts
      down the assembly line? When the engine begins production? Or, as in Henry Ford’s
      terms, when the ore is mined from the ground? We will discuss measuring cycle time
      for such assembled parts later, but for now we restrict our deﬁnition to single routings.
            The lead time of a given routing or line is the time allotted for production of a part
      on that routing or line. As such, it is a management constant.2 In contrast, cycle times
      are generally random. Therefore, in a line functioning in a make-to-order environment
      (i.e., it produces parts to satisfy orders with speciﬁc due dates), an important measure of
      line performance is service level, which is deﬁned as

                                  Service level = P{cycle time ≤ lead time}

      Notice that this deﬁnition implies that for a given distribution of cycle time, service level
      can be inﬂuenced by manipulating lead time (i.e., the higher the lead time, the higher
      the service level).
           If the line is functioning in a make-to-stock environment (i.e., it ﬁlls a buffer from
      which customers or other lines expect to be able to obtain parts without delay), then a

           1 Cycle time also has another meaning in assembly lines as the time allotted for each station to complete

      its task. It can also refer to the processing time of an individual machine (e.g., the time for a punch press to
      cycle). We will avoid these other uses of the term cycle time to prevent confusion.
           2 Recall that the time phasing function of MRP is critically dependent on the choice of such lead times.
                     Chapter 7     Basic Factory Dynamics                                                                        231

                     different performance measure may be more appropriate than service level. A logical
                     choice is ﬁll rate, which is deﬁned as the fraction of orders that are ﬁlled from stock and
                     was discussed in Chapter 2. Since ﬁll rate and many other performance measures are
                     often referred to as “service levels,” the reader is cautioned to look for a precise deﬁnition
                     whenever this term is encountered. We will consistently use the former deﬁnition of
                     service level throughout Part II, but will return to the ﬁll rate measure in Chapter 17.
                          The utilization of a workstation is the fraction of time it is not idle for lack of parts.
                     This includes the fraction of time the workstation is working on parts or has parts waiting
                     and is unable to work on them because of a machine failure, setup, or other detractor.
                     We can compute utilization as

                                                                             arrival rate
                                                   Utilization =
                                                                      effective production rate

                     where the effective production rate is deﬁned as the maximum average rate at which the
                     workstation can process parts, considering the effects of failures, setups, and all other
                     detractors that are relevant over the planning period of interest.3


7.2.2   Parameters
                     Parameters are numerical descriptors of manufacturing processes and therefore vary in
                     value from plant to plant. Two key parameters for describing an individual line (routing)
                     are the bottleneck rate and the raw process time. We deﬁne these below, along with a
                     third parameter, the critical WIP level, that can be computed from them.
                          The bottleneck rate (rb ) of the line, rb , is the rate (parts per unit time or jobs per unit
                     time) of the workstation having the highest long-term utilization. By long term we mean
                     that outages due to machine failures, operator breaks, quality problems, and so forth,
                     are averaged out over the time horizon under consideration. This implies that the proper
                     treatment of outages will differ depending on the planning frequency. For example, for
                     daily replanning, outages typically experienced during a day should be included; but
                     unplanned long outages, such as those resulting from a major breakdown, should not. In
                     contrast, for planning over a year-long horizon, time lost to major breakdowns should
                     be included, if such occurrences are not unlikely over the course of a year.
                          In lines consisting of a single routing in which each station is visited exactly once
                     and there is no yield loss, the arrival rate to every workstation is the same. Hence, the
                     workstation with the highest utilization will be that with the least long-term capacity (i.e.,
                     slowest effective rate). However, in lines with more complicated routings or yield loss, the
                     bottleneck may not be at the slowest workstation. A faster workstation that experiences
                     a higher arrival rate may have higher utilization. For this reason, it is important to deﬁne
                     the bottleneck in terms of utilization as we have done here.
                          To see this, consider the line in Figure 7.1 with arrival rate r parts per minute and
                     processing time of 1 and 2 minutes, respectively, at stations 1 and 2. Since station 2
                     processes parts at a rate of 0.5 per minute, while station 1 processes them at a rate of

                        3 It is not uncommon to ﬁnd utilization deﬁned without consideration of detractors. That is, effective

                     production rate is replaced in the above equation by maximum production rate. We do not do this because it
                     can distort the picture of where capacity is tightest. For instance, a machine may have a fairly low utilization
                     relative to its maximum possible rate, but be very highly utilized once detractors are taken into consideration.
                     Looking at utilization relative to maximum production rate would therefore not give an indication that the
                     machine is liable to become overloaded if the arrival rate increases only slightly. Hence, in order to give an
                     accurate picture of the capacity situation, we will consistently make use of utilization as deﬁned above.
232                       Part II       Factory Physics

Figure 7.1                      1 min              2 min
Bottleneck in line with   r         A               B
                                               y
yield loss.
                                           1–y



                          1 per minute, station 2 is clearly the slower of the two. So by rate alone, it would be the
                          bottleneck. However,
                          bottleneck. However, because         percentofofthe
                                                 because1y– ypercent        theparts
                                                                                partsprocessed
                                                                                      processedatatstation
                                                                                                    station 11 are scrapped
                          before reaching station 2, station 1 processes a heavier load than does station 2. To
                          accurately gauge which station is more heavily loaded, we compute their utilizations,
                          which are:

                                                                            r
                                                                     u(1) =   =r
                                                                            1
                                                                            yr
                                                                     u(2) =     = 2yr
                                                                            0.5
                                If y < 0.5 then the utilization of station 1 is higher than that of station 2 and hence
                          it is the bottleneck. The reason is that when more than half of the output from station
                          1 is scrapped, station 1 must process more than twice as much as station 2. This more
                          than offsets the fact that station 1 is twice as fast. Hence, if we progressively increase
                          the arrival rate r when y < 0.5, station 1 will become overloaded before station 2 does.
                          Since the bottleneck is the resource with the least “slack” in its capacity, station 1 is
                          reasonably defined as the bottleneck in this case.
                                The raw process time (T0 ) of the line is the sum of the long-term average process
                          times of each workstation in the line. Alternatively, we can define raw process time as
                          the average time it takes a single job to traverse the empty line (i.e., so it does not have to
                          wait behind other jobs). Again, we must be concerned about the length of the planning
                          horizon when deciding what to include in the “average” process times. Over the long
                          term, T0 should include infrequent random and planned outages, while over a shorter
                          term it should include only the more frequent delays.
                                The critical WIP (W0 ) of the line is the WIP level for which a line with given values
                          of rb and T0 but having no variability achieves maximum throughput (rb , that is) with
                          minimum cycle time (T0 ). We show below that critical WIP is defined by the bottleneck
                          rate and raw process time by the following relationship:

                                                                        W0 = rb T0


7.2.3    Examples
                          We now illustrate these definitions with two simple examples.

                          Penny Fab One. Penny Fab One consists of a simple production line that makes giant
                          one-cent pieces used exclusively in Fourth of July parades. As illustrated in Figure 7.2,

Figure 7.2                      Head              Tail
                              stamping         stamping    Rimming     Deburring
Penny Fab One.

                                    2h             2h        2h           2h
                 Chapter 7   Basic Factory Dynamics                                                      233

                 this line consists of four machines in sequence; the ﬁrst machine is a punch press that
                 cuts penny blanks, the second stamps Lincoln’s face on one side and the Memorial on
                 the back, the third places a rim on the penny, and the fourth cleans away any burrs. Each
                 machine takes exactly two hours to perform its operation. (We will relax this unrealistic
                 assumption that process times are deterministic later.) After each penny is processed, it
                 is moved immediately to the next machine. The line runs 24 hours per day and the market
                 for giant pennies is unlimited, so that all product made is sold. Hence, more throughput
                 is unambiguously better for this system.
                      Since this is a tandem line with no yield loss, the arrival rate to each station is
                 the same. Hence, the bottleneck (highest-utilization station) is the slowest workstation.
                 However, the capacity of each machine is the same and equals one penny every 2 hours, or
                 one-half part per hour. Hence, any of the four machines can be regarded as the bottleneck
                 and

                                                      rb = 0.5 penny per hour

                 or 12 pennies per day. Such a line is said to be balanced, since all stations have equal
                 capacity.
                      Next, note that the raw process time is simply the sum of the processing times at the
                 four stations, so

                                                           T0 = 8 hours

                      The critical WIP level is given by

                                              W0 = rb T0 = 0.5 × 8 = 4 pennies

                 We will illustrate later that this is indeed the level of WIP that causes the line to achieve
                 throughput of rb = 0.5 penny per hour and cycle time of T0 = 8 hours. Notice that W0 is
                 equal to the number of machines in the line. This is always the case for balanced lines,
                 since having one job per machine is just enough to keep all machines busy at all times.
                 However, as we will see, it is not true for unbalanced lines.

                 Penny Fab Two. Now consider a somewhat more complex Penny Fab Two, which
                 represents an unbalanced line with multimachine stations. As illustrated in Figure 7.3,
                 Penny Fab Two still produces giant pennies in four steps: punching, stamping, rim-
                 ming, and deburring; but the workstations now have different numbers of machines and
                 processing times.


Figure 7.3                                   Rimming
Penny Fab Two.
                                    Tail
                       Head      stamping                  Deburring
                     stamping


                       2h
                                    5h                        3h



                                                10 h
234   Part II   Factory Physics


                         Table 7.1 Penny Fab Two: An Unbalanced Line
                           Station      Number of      Process      Station Capacity
                           Number       Machines     Time (hours)   (Jobs per hour)

                                  1         1             2               0.50
                                  2         2             5               0.40
                                  3         6            10               0.60
                                  4         2             3               0.67




           The presence of multimachine stations complicates the capacity calculations some-
      what. For a single machine, the capacity is simply the reciprocal of the process time
      (e.g., if it takes one-half hour to do one job, the machine can do two jobs per hour). The
      capacity of a station consisting of several identical machines in parallel must be calcu-
      lated as the individual machine capacity times the number of machines. For example, in
      Penny Fab Two, the capacity per machine at station 3 is
                                                 1
                                                10
                                                   penny per hour

      so the capacity of the station is

                                         6 × 10
                                             1
                                                = 0.6 penny per hour

      Notice that the station capacity can be computed directly by dividing the number of
      machines by the process time. This is done for each station in Table 7.1.
           The capacity of the line with multimachine stations is still deﬁned by the rate
      of the bottleneck, or slowest station in the line. In Penny Fab Two, the bottleneck is
      station 2, so

                                           rb = 0.4 penny per hour

      Notice that the bottleneck is neither the station that contains the slowest machines
      (station 3) nor the one with the fewest machines (station 1).
           The raw process time of the line is still the sum of the process times. Notice that
      adding machines at a station does not decrease T0 , since a penny can be worked on by
      only one machine at a time. Hence, the raw process time for Penny Fab Two is

                                       T0 = 2 + 5 + 10 + 3 = 20 hours

         Regardless of whether the line has single- or multiple-machine stations, the critical
      WIP level is always deﬁned as

                                      W0 = rb T0 = 0.4 × 20 = 8 pennies

      In Penny Fab Two, as in Penny Fab One, W0 is a whole number. This, of course, need
      not be the case. If W0 comes out to a fraction, it means that there is no constant WIP
      level that will achieve throughput of exactly rb jobs per hour and cycle time of T0 hours.
      Furthermore, notice that the critical WIP level in Penny Fab Two (eight pennies) is
      less than the number of machines (11). This is because the system is not balanced (i.e.,
      stations have different amounts of capacity), and therefore some stations will not be fully
      utilized.
                      Chapter 7    Basic Factory Dynamics                                                                  235

Figure 7.4
Penny Fab One with    t=0
WIP = 1.




                      t=2




                      t=4




                      t=6




7.3     Simple Relationships
                      Now, in the pursuit of a science of manufacturing, we ask the fundamental question, What
                      are the relationships among WIP, throughput, and cycle time in a single production line?
                      Of course, the answer will depend on the assumptions we make about the line. In this
                      section, we will give a precise (i.e., quantitative) description of the range of possible
                      behavior. This will serve to sharpen our intuition about how lines perform and will give
                      us a scale on which to benchmark actual systems.
                           A problem with characterizing the relationship between measures such as WIP and
                      throughput is that in real systems they tend to vary simultaneously. For instance, in an
                      MRP system, the line may be ﬂooded with work one month (due to a heavy master
                      production schedule) and very lightly loaded the next. Hence, both WIP and throughput
                      are apt to be high during the ﬁrst month and low during the second. For clarity of
                      presentation, we will eliminate this problem by controlling the WIP level in the line so
                      as to hold it constant over time. For instance, in the Penny Fabs, we will start the lines
                      with a speciﬁed number of pennies (jobs) and then release a new penny blank into the
                      line each time a ﬁnished penny exits the line.4

7.3.1   Best-Case Performance
                      To analyze and understand the behavior of a line under the best possible circumstances,
                      namely, when process times are absolutely regular, we will simulate Penny Fab One.
                      This is easily done by using a piece of paper and several pennies, as shown in Figure 7.4.
                           We begin by simulating the system when only one job is allowed in the line. The
                      ﬁrst penny spends 2 hours successively at stations 1, 2, 3, and 4, for a total cycle time of
                      8 hours. Then a second penny is released into the line, and the same sequence is repeated.
                      Since this results in one penny coming out of the line every 8 hours, the throughput is
                          4 We say that such a line is operating under a CONWIP (Constant WIP) protocol, which is treated more

                      thoroughly in Chapters 10 and 14.
236                  Part II   Factory Physics

Figure 7.5
Penny Fab One with   t=0
WIP = 2.




                     t=2




                     t=4




                     t=6




                     1
                     8
                       penny per hour. Notice that the cycle time is equal to the raw process time T0 = 8,
                     while the throughput is one-fourth of the bottleneck rate rb = 0.5.
                          Now we add a second penny to the line (where both are released simultaneously into
                     the line). After 2 hours, the ﬁrst penny completes processing at station 1 and starts on
                     station 2. At the same time, the second penny starts processing on station 1. Thereafter,
                     the second penny will follow the ﬁrst, switching stations every 2 hours, as shown in
                     Figure 7.5. After the initial wait experienced by the second penny, it never waits again.
                     Hence, once the system is running in steady state, every penny released into the line still
                     has a cycle time of exactly 8 hours. Moreover, since two pennies exit the line every 8
                     hours, the throughput increases to 28 penny per hour, double that when the WIP level was
                     1 and 50 percent of line capacity (rb = 0.5).
                          We add a third penny. Again, after an initial transient period in which pennies wait
                     at the ﬁrst station, there is no waiting, as shown in Figure 7.6. Hence, cycle time stays at
                     8 hours. Since three pennies exit in any 8-hour interval, throughput increases to 38 part
                     per hour, or 75 percent of rb .
                          When we add a fourth penny, we see that all the stations stay busy all the time once
                     steady state has been reached (see Figure 7.7). Because there is no waiting at the stations,
                     cycle time is still T0 = 8 h. Since the last station is busy all the time, it completes one
                     penny every other hour, so throughput becomes 12 penny per hour, which equals the line
                     capacity rb . This very special behavior, in which cycle time is T0 (its minimum value)
                     and throughput is rb (its maximum value) is only achieved when the WIP level is set at
                     the critical WIP level, which we recall for Penny Fab One is

                                                 W0 = rb T0 = 0.5 × 8 = 4 pennies

                          Now we add a ﬁfth penny to the line. Because there are only four machines, a penny
                     will wait at the ﬁrst station, even after the system has settled into steady state. Since we
                     measure cycle time as the time from when a job is released (the time it enters the queue
                     at the ﬁrst station) to when it exits the line, it now becomes 10 hours, due to the extra two
                     hours of waiting time in front of station 1. Hence, for the ﬁrst time, cycle time becomes
                     Chapter 7   Basic Factory Dynamics                                                      237

Figure 7.6
Penny Fab One with
WIP = 3.             t=0




                     t=2




                     t=4




                     t=6




                     larger than its minimal value T0 = 8. However, since all stations are always busy, the
                     throughput remains at rb = 0.5 penny per hour.
                          Finally, consider what happens when we allow 10 pennies in the line. In steady state,
                     a queue of six pennies persists in front of the ﬁrst station, meaning that an individual
                     penny spends 12 hours from the time it is released to the line until it begins processing at

Figure 7.7
Penny Fab One with
WIP = 4.             t=0




                     t=2




                     t=4




                     t=6




                     t=8
238                         Part II        Factory Physics


                                                     Table 7.2 WIP, Cycle Time, and Throughput of
                                                               Penny Fab One
                                                        WIP      CT      % T0          TH      % rb

                                                             1    8      100         0.125       25
                                                             2    8      100         0.250       50
                                                             3    8      100         0.375       75

                                                             4    8      100         0.500      100

                                                          5      10      125         0.500      100
                                                          6      12      150         0.500      100
                                                          7      14      175         0.500      100
                                                          8      16      200         0.500      100
                                                          9      18      225         0.500      100
                                                         10      20      250         0.500      100




                            station 1. Hence, the cycle time is 20 hours (12 queueing plus 8 processing). As before,
                            all machines remain busy all the time, so throughput is still rb = 0.5 penny per hour. It
                            should be clear at this point that each penny we add increases cycle time by 2 hours with
                            no increase in throughput.
                                 We summarize the behavior of Penny Fab One with no variability for various WIP
                            levels in Table 7.2, and present the results graphically in Figure 7.8. From a performance
                            standpoint, it is clear that Penny Fab One runs best when there are four pennies in WIP.
                            Only this WIP level results in minimum cycle time T0 and maximum throughput rb —any
                            less and we lose throughput with no decrease in cycle time; any more and we increase
                            cycle time with no increase in throughput. This special WIP level is the critical WIP
                            (W0 ).
                                 In this particular example, the critical WIP is equal to the number of machines. This
                            is always the case when the line consists of stations with equal capacity (i.e., a balanced
                            line). For unbalanced lines, W0 will be less than the number of machines, but still has
                            the property of being the WIP level that achieves maximum throughput with minimum
                            cycle time, and is still deﬁned by W0 = rb T0 .
                                 It is important to note that while the critical WIP is optimal in the case with zero
                            variability, it will not be optimal in other cases. Indeed, the concept of an optimal WIP


Figure 7.8                        0.6                                             26
                                                                                  24
Cycle time and throughput    rb 0.5                                               22
versus WIP for Penny Fab                                                          20
One.                              0.4                                             18
                                                                                  16
                                                                                  14
                             TH   0.3                                           CT12
                                                                                  10
                                  0.2                                              8
                                                                                   6
                                  0.1                                           T0 4
                                                                                   2
                                      0                                            0
                                          0 1 2 3 4 5 6 7 8 9 10 11 12                 0 1 2 3 4 5 6 7 8 9 10 11 12
                                              W0     WIP                                    W0    WIP
Chapter 7   Basic Factory Dynamics                                                      239

level is not even well deﬁned when processing times are variable; in general, increasing
WIP will increase both throughput (good) and cycle time (bad).

Little’s Law. Close examination of Table 7.2 reveals an interesting, and fundamental,
relationship among WIP, cycle time, and throughput. At every WIP level, WIP is equal to
the product of throughput and cycle time. This relation is known as Little’s law (named
for John D. C. Little, who provided the mathematical proof) and represents our ﬁrst
Factory Physics relationship:

Law (Little’s Law):

                                     WIP = TH × CT

     It turns out that Little’s law holds for all production lines, not just those with zero
variability. As we discussed in Chapter 6, Little’s law is not a law at all but a tautology.
For special cases (e.g., the case where time goes to inﬁnity), the relationship can be
proved mathematically. However, it does not hold precisely for less-than-inﬁnite times
(which, of course, are the only times we can observe in real life) except under very
special circumstances. Nonetheless, we will use it as a conjecture about the nature of
manufacturing systems and use it as an approximation when it is not exact.
     In this approximate sense Little’s law is very broadly applicable, in that it can be
applied to a single station, a line, or an entire plant. As long as the three quantities
are measured in consistent units, the above relationship will hold over the long term.
This makes it immensely applicable to practical situations. Some straightforward uses
of Little’s law include these:
     1. Queue length calculations. Since Little’s law applies to individual stations, we
        can use it to calculate the expected queue length and utilization (fraction of time
        busy) at each station in a line. For instance, consider Penny Fab Two, which was
        summarized in Table 7.1, and suppose it is running at the bottleneck rate (that is,
        0.4 job per hour). From Little’s law, the expected WIP at the ﬁrst station will be

                    WIP = TH × CT = 0.4 job per hour × 2 hour = 0.8 job

        Since there is only one machine at station 1, this means it will be utilized 80
        percent of the time. Similarly, at station 3, Little’s law predicts an average WIP
        of four jobs. Since there are six machines, the average utilization will be
        4/6 = 66.7 percent. Notice that this is equal to the ratio of the rate of the
        bottleneck to the rate of station 3 (that is, 0.4/0.6), as we would expect.
     2. Cycle time reduction. Since Little’s law can be written as

                                                  WIP
                                           CT =
                                                  TH
        it is clear that reducing cycle time implies reducing WIP, provided throughput
        remains constant. Hence, large queues are an indication of opportunities for
        reducing cycle time, as well as WIP. We will discuss speciﬁc measures for WIP
        and cycle time reduction in Chapter 17.
     3. Measure of cycle time. Measuring cycle time directly can sometimes be
        difﬁcult, since it entails registering the entry and exit times of each part in the
240   Part II   Factory Physics

               system. Since throughput and WIP are routinely tracked, it might be easier to
               use the ratio WIP/TH as a perfectly reasonable indirect measure of cycle time.
            4. Planned inventory. In many systems, jobs are scheduled to ﬁnish ahead of their
               due dates in order to ensure a high level of customer service. Because, in our
               era of inventory consciousness, customers often refuse to accept early
               deliveries, this type of “safety lead time” causes jobs to wait in ﬁnished goods
               inventory prior to shipping. If the planned inventory time is n days, then
               according to Little’s law, the amount of inventory in FGI will be given by nTH
               (where TH is measured in units per day).
            5. Inventory turns. Recall that inventory turns are given by the ratio of throughput
               to average inventory. If we have a plant in which all inventory is WIP (i.e.,
               product is shipped directly from the line so there is no ﬁnished goods inventory),
               then turns are given by TH/WIP, which by Little’s law is simply 1/CT. If we
               include ﬁnished goods, then turns are TH/(WIP + FGI). But Little’s law still
               applies, so this ratio represents the inverse of the total average time for a job to
               traverse the line plus the ﬁnished goods crib. Hence, intuitively, inventory turns
               are one divided by the average residence time of inventory in the system.
            6. Multiproduct systems. So far, we have talked as if inventory must be measured
               in units of parts and throughput in units of parts per day (or some other time
               interval). But Little’s law does not require this. If we have many different types
               of parts with different WIP, CT, and TH levels, we can certainly apply Little’s
               law to each one separately. But we can also measure stocks and ﬂows in units of
               dollars. For instance, if we measure TH in cost of goods sold (dollars per day),
               and WIP in dollars, then Little’s law can be applied to compute average cycle
               time across all products as CT = WIP/TH. Note, however, that we must measure
               throughput as cost of goods sold, instead of in units of prices, in order to match
               the units of WIP.
          In a sense, Little’s law is the “F = ma” of Factory Physics. It is a broadly applicable
      equation that relates three fundamental quantities. At the same time, Little’s law can be
      viewed as a truism about units. It merely indicates the obvious fact that we can measure
      WIP level in a station, line, or system in units of jobs or time. For instance, a line that
      produces 100 crankcases per day and has a WIP level of 500 crankcases has 5 days of
      WIP in it. Little’s law is a statement that this conversion is valid for average WIP, cycle
      time, and throughput, so

                                                      WIP
                                              CT =
                                                      TH
      or
                                                 500 crankcases
                                   5 days =
                                              100 crankcases per day

          We can now generalize the results shown in Table 7.2 and Figure 7.8 to achieve
      our original objective of giving a precise summary of the relationship between WIP and
      throughput for a “best-case” (i.e., zero-variability) line. We can then apply Little’s law to
      extend this to describe the relationship between WIP and cycle time. Since these relation-
      ships were derived for perfect lines with no variability, the following expressions indicate
      the maximum throughput and minimum cycle time for a given WIP level for any system
      having parameters rb and T0 . The resulting equations are our next Factory Physics law.
                     Chapter 7   Basic Factory Dynamics                                                        241

                     Law (Best-Case Performance):          The minimum cycle time for a given WIP level w is
                     given by

                                                                        if w ≤ W0
                                                             ⎧
                                                             ⎨ T0
                                                             ⎪
                                                     CTbest = w
                                                             ⎪
                                                             ⎩          otherwise
                                                               rb

                     The maximum throughput for a given WIP level w is given by
                                                        ⎧w
                                                        ⎨       if w ≤ W0
                                               THbest = T0
                                                          rb    otherwise
                                                        ⎩

                          One conclusion we can draw from this is that, contrary to the popular slogan,
                     zero inventory is not a realistic goal. Even under perfect deterministic conditions, zero
                     inventory yields zero throughput and therefore zero revenue. A more realistic “ideal”
                     WIP is the critical WIP W0 .
                          Penny Fab One represents an ideal (zero-variability) situation, in which it is optimal
                     to maintain a WIP level equal to the number of machines. Of course, in the real world
                     there are not many factories that run with such low WIP levels. Indeed, in many of the
                     production lines we have seen, the WIP-to-machines ratio is closer to 20 : 1. If this ratio
                     were to hold for Penny Fab One, the cycle time would be almost 7 days with 80 jobs in
                     WIP. Obviously, this is much worse than a cycle time of 8 hours at a WIP level of four
                     jobs (i.e., the “optimal” level). Why, then, do actual plants operate so far from the ideal
                     of the critical WIP level?
                          Unfortunately, Little’s law offers little help. Since TH = WIP/CT, we can have the
                     same throughput with large WIP levels and long cycle times, or with low WIP levels
                     and short cycle times. The problem is that Little’s law is only one relation among three
                     quantities. We need a second relation if we are to uniquely determine two quantities,
                     given the third (e.g., predict both WIP and cycle time from throughput). Sadly, there is
                     no universally applicable second relationship among WIP, cycle time, and throughput.
                     The best we can do is to characterize the behavior of a line under speciﬁc assumptions. In
                     addition to the best case, which we considered above, we will treat two other scenarios,
                     which we term the worst case and the practical worst case.


7.3.2   Worst-Case Performance
                     In sharp contrast to the best possible behavior of a line, we now consider the worst.
                     Speciﬁcally, we seek the maximum cycle time and minimum throughput possible for a line
                     with bottleneck rate rb and raw process time T0 . This will enable us to bracket the behavior
                     and gauge the performance of real lines. If a line is closer to the worst case than to the best
                     case, then there are some real problems (or opportunities, depending on your perspective).
                          To facilitate our discussion of the worst case, recall that we are assuming a constant
                     amount of work is maintained in the line at all times. Whenever a job ﬁnishes, another
                     is started. One way that this could be achieved in practice would be to transport jobs
                     through the line on pallets. Whenever a job is ﬁnished, it is removed from its pallet and
                     the pallet immediately returns to the front of the line to carry a new job. The WIP level,
                     therefore, is equal to the (ﬁxed) number of pallets.
                          Now, imagine yourself sitting on a pallet riding around and around a best-case line
                     with WIP equal to the critical WIP (e.g., Penny Fab One with four jobs). Each time you
242                       Part II   Factory Physics

                          arrive at a station, a machine is available to begin work on the job immediately. It is
                          precisely because there is no waiting (queueing) that this line achieves the minimum
                          possible cycle time of T0 .
                               To get the longest possible cycle times for this system, we must somehow increase
                          the waiting time without changing the average processing times (otherwise we would
                          change rb and T0 ). The very worst we could possibly make waiting time would be that
                          every time our pallet reached a station, we found ourselves waiting behind every other
                          job in the line. How could this possibly occur?
                               Consider the following. Suppose that you are riding on pallet number 4 in a modiﬁed
                          Penny Fab One with four pallets. However, instead of all jobs requiring exactly 2 hours
                          at each station, suppose that jobs on pallet 1 require 8 hours, while jobs on pallets 2, 3,
                          and 4 require 0 hours. The average processing time at each station is

                                                          8+0+0+0
                                                                  = 2 hours
                                                             4
                          as before, and hence we still have rb = 0.5 job per hour and T0 = 8 hours. However,
                          every time your pallet reaches a station, you ﬁnd pallets 1, 2, and 3 ahead of you (see
                          Figure 7.9). The slow job on pallet 1 causes all the other jobs to pile up behind it at all
                          times. This is the absolute maximum amount of waiting time it is possible to introduce,
                          and hence this represents the worst case.
                              The cycle time for this system is

                                                          8 + 8 + 8 + 8 = 32 hours

Figure 7.9
                                      4
Evolution of worst-case
line.                                 3
                          t=0         2      1


                                                      4
                                                      3
                          t=8                         2   1


                                                                      4
                                                                      3
                          t = 16                                      2          1


                                                                                     4
                                                                                     3
                          t = 24                                                     2   1


                                                              rb = 0.5, T0 = 8
Chapter 7   Basic Factory Dynamics                                                      243

or 4T0 , and since four jobs are output each time pallet 1 ﬁnishes on station 4, the
throughput is

                                     4
                                     32
                                        = 18   job per hour

or 1/T0 jobs per hour. Notice that the product of throughput and cycle time is 18 × 32 = 4,
which is the WIP level, so, as always, Little’s law holds.
     We summarize these results for a general line as our next Factory Physics law.

Law (Worst-Case Performance):           The worst-case cycle time for a given WIP level w
is given by

                                       CTworst = w T0

The worst-case throughput for a given WIP level w is given by

                                                    1
                                        THworst =
                                                    T0

     It is interesting to note that both the best-case and worst-case performances occur
in systems with no randomness. There is variability in the worst-case system, since jobs
have different process times; but there is no randomness, since all process times are com-
pletely predictable. The literature on quality management stresses the need for variability
reduction, but sometimes implies that variability and randomness are synonymous. The
above Factory Physics results show that this is not the case; variability can be the result
of randomness or bad control (or both). We will examine this distinction in greater depth
after we have developed the tools for treating variability in Chapters 8 and 9.
     Finally, the reader may be justiﬁably skeptical about the realism of the worst case.
After all, we arrived at this case by forcing the maximum amount of waiting time (in
order to make cycle times as long as possible) by making the processing times as variable
as possible. To do this, we assumed jobs on one of the pallets had long processing times,
while all the others had zero processing times. Surely this could never happen in real life.
     But it can and (at least to some extent) does happen. To see how, suppose that the four
pallets used to carry jobs in Penny Fab One (when WIP equals four jobs) are themselves
moved between stations with a forklift. Further, suppose that because the forklift has
other obligations, it cannot afford to make the number of trips necessary to move each
pallet individually. Instead, it waits until all four jobs are ﬁnished on a station and then
moves them as a group to the next station. Similarly, it waits until all four pallets are
empty at the end of the line to bring them back to the front to receive new jobs. Assuming
that processing times of each job at each station are 2 hours (as in the original Penny Fab
One), and that move times on the forklift are sufﬁciently short as to be reasonably treated
as zero, the progress of the system will be exactly the same as that shown in Figure 7.9.
Hence, worst-case behavior can result from batch moves.
     Of course, it is rare to ﬁnd real plants in which batch moves are so extreme as to
cause every job in the line to travel together. More commonly, the WIP in a line will
be transported in several batches, possibly of varying size. While this kind of more
modest batching will not produce worst-case behavior, it is one factor that can push the
performance of a line closer to that of the worst case than the best case. Consequently,
batching is a genuine problem (opportunity) in many production systems.
244                   Part II   Factory Physics


7.3.3   Practical Worst-Case Performance
                      Virtually no real-world line behaves literally according to either the best case or the worst
                      case. Therefore, to better understand the behavior between these two extreme cases, it is
                      instructive to consider an intermediate case. We do this by means of a case that, unlike
                      the previous two, involves randomness. In fact, in a sense, it represents the “maximum
                      randomness” case. We term this the practical worst case to express our belief that
                      virtually any system with worse behavior is a target for improvement.
                           To describe the practical worst case and show why it can be regarded as the maximum
                      randomness case, we must ﬁrst deﬁne the concept of a system state. The state of the
                      system is a complete description of the jobs at all the stations: how many there are and
                      how long they have been in process. Under special conditions, which we assume here
                      and describe below, the only information needed is the number of jobs at each station.
                      Hence, we can give a concise summary of a state by using a vector with as many elements
                      as there are stations in the line.
                           For instance, in a line with four stations and three jobs, the vector (3, 0, 0, 0)
                      represents the state in which all three jobs are at the ﬁrst station, while the vector
                      (1, 1, 1, 0) represents the state in which there is one job each at stations 1, 2, and 3.
                      There are 20 possible states for a system consisting of four machines and three jobs,
                      which are enumerated in Table 7.3.
                           Depending on the speciﬁc assumptions about the line, not all states will necessarily
                      occur. For instance, if all processing times in the four-station, three-job system are 1 hour
                      and it behaves according to the best case, then only four states—(1, 1, 1, 0), (0, 1, 1, 1),
                      (1, 0, 1, 1), and (1, 1, 0, 1)—will be repeated as illustrated in Figure 7.10. Similarly, if it
                      behaves according to the worst case, then four different states—(3, 0, 0, 0), (0, 3, 0, 0),
                      (0, 0, 3, 0), and (0, 0, 0, 3)—will be repeated, as illustrated in Figure 7.11. Because both
                      of these systems have no randomness, other states are never reached.
                           When randomness is introduced into a line, more states become possible. For in-
                      stance, suppose the processing times are deterministic, but every once in a while a
                      machine breaks down for several hours. Then most of the time we will observe “spread-
                      out” states, like those in Figure 7.10, but occasionally we will see “clumped-up” states,
                      like those in Figure 7.11. If there is only a little randomness (e.g., machine failures
                      are very rare), then the frequency of the spread-out states will be very high, whereas if
                      there is a lot of randomness (e.g., machines fail frequently), then all the states shown in



                                            Table 7.3 Possible States for a System with
                                                      Four Machines and Three Jobs
                                              State      Vector         State        Vector

                                                   1   (3, 0, 0, 0)      11        (1, 0, 2, 0)
                                                   2   (0, 3, 0, 0)      12        (0, 1, 2, 0)
                                                   3   (0, 0, 3, 0)      13        (0, 0, 2, 1)
                                                   4   (0, 0, 0, 3)      14        (1, 0, 0, 2)
                                                   5   (2, 1, 0, 0)      15        (0, 1, 0, 2)
                                                   6   (2, 0, 1, 0)      16        (0, 0, 1, 2)
                                                   7   (2, 0, 0, 1)      17        (1, 1, 1, 0)
                                                   8   (1, 2, 0, 0)      18        (1, 1, 0, 1)
                                                   9   (0, 2, 1, 0)      19        (1, 0, 1, 1)
                                                  10   (0, 2, 0, 1)      20        (0, 1, 1, 1)
                          Chapter 7   Basic Factory Dynamics                                                   245

Figure 7.10
States in best-case,                                                             t = 2, 6, 10, . . .
four-machine, three-job
line.



                                                                                 t = 3, 7, 11, . . .




                                                                                 t = 4, 8, 12, . . .




                                                                                 t = 5, 9, 13, . . .




                          Table 7.3 may occur quite often. Hence, we deﬁne the maximum randomness scenario
                          to be that which causes every possible state to occur with equal frequency.
                               In order for all states to be equally likely, three special conditions are required:
                               1. The line must be balanced (i.e., all stations must have the same average process
                                  times).
                               2. All stations must consist of single machines. (This assumption also allows us to
                                  avoid the complexities of parallel processing and jobs passing one another.)
                               3. Process times must be random and occur according to a speciﬁc probability
                                  distribution known as the exponential distribution. The exponential is the only


Figure 7.11
States in worst-case,
four-machine, three-job                                                            t = 0, 12, 24, . . .
line.




                                                                                   t = 3, 15, 27, . . .




                                                                                   t = 6, 18, 30, . . .




                                                                                   t = 9, 21, 33, . . .

246   Part II   Factory Physics

                continuous distribution that has a special property known as the memoryless
                property (see Appendix 2A). What this means is that if the processing time on
                a machine is exponentially distributed, then knowledge of how long a part has
                been in process offers no information about when it will be ﬁnished. For
                instance, if process times on a machine are exponential with mean 1 hour and
                the current job has been in process for 5 seconds, then the expected remaining
                process time is 1 hour. If the current job has been in process for 1 hour, the
                remaining process time is 1 hour. If the current job has been in process for 942
                hours, the expected remaining process time is 1 hour.5 It is as if the machine
                forgets its past work when predicting the future—hence the term memoryless.
                Thus, if process times are exponentially distributed, there is no need to know
                how long a job has been in process to completely deﬁne the system state.
            To understand how the practical worst case (PWC) works, return to the thought
      experiment in which you envisioned yourself riding around on a pallet that cycles through
      the line again and again. Suppose there are N (single-machine) stations, each with average
      processing times of t, and a constant level of w jobs in the line. Thus, the raw process
      time is T0 = N t, and the bottleneck rate is rb = 1/t for this line.
            Since the above three conditions guarantee that all states are equally likely, then,
      from your vantage point on a pallet, you would expect to see on average the w − 1 other
      jobs equally distributed among the N stations each time you arrive at a station. So the
      expected number of jobs ahead of you upon arrival is (w − 1)/N . Since the average time
      you spend at the station will be the time for the other jobs to complete processing plus
      the time for your job to be processed, we can write

                  Average time at a station = time for your job + time for other jobs
                                                            w−1
                                                   =t+          t
                                                             N
                                                        w −1
                                                            
                                                   = 1+        t
                                                          N

           By assuming that the (w − 1)/N jobs ahead of you require an average of
      [(w − 1)/N ]t time to complete, we are ignoring the fact that the job in process at the
      station was partially ﬁnished when you arrived. It is the memoryless property of the
      exponential distribution that enables us to do this.
           Finally, since all stations are assumed identical, we can compute the average cycle
      time by simply multiplying the average time at each station by the number of stations
      N , to get

                                                        w −1
                                                            
                                             CT = N 1 +        t
                                                          N
                                                  = N t + (w − 1)t
                                                             w −1
                                                  = T0 +
                                                              rb


          5 Although it may be a stretch to imagine processing times behaving in this way, there certainly seem to

      be examples of this type of behavior in daily life, for instance, times until departure of delayed ﬂights, times
      until the arrival of trains on certain railways, times until some contractors ﬁnish home improvement jobs, etc.
Chapter 7   Basic Factory Dynamics                                                       247

Here we used the facts that rb = 1/t and T0 = N t because the line is balanced. To get
the corresponding throughput, we simply apply Little’s law:
                                           WIP
                                TH =
                                           CT
                                                w
                                       =
                                         T0 + (w − 1)/rb
                                                  w
                                       =
                                         W0 /rb + (w − 1)/rb
                                              w
                                       =             rb
                                         W0 + w − 1

     This provides our deﬁnition of practical worst-case performance.

Deﬁnition (Practical Worst-Case Performance):               The practical worst-case (PWC)
cycle time for a given WIP level w is given by
                                                      w −1
                                      CTPWC = T0 +
                                                       rb
The PWC throughput for a given WIP level w is given by
                                                     w
                                     THPWC =                rb
                                                 W0 + w − 1
     Notice that the behavior of this case is reasonable for both extremely low and
extremely high WIP levels. At one extreme, when there is only one job in the system
(w = 1), cycle time becomes raw process time T0 , as we would expect. At the other
extreme, as the WIP level grows very large (that is, w → ∞), throughput approaches
capacity rb , while cycle time increases without bound. The intuition behind this latter
result is that achieving throughput close to capacity in systems with high variability
requires high WIP levels, to ensure that the bottleneck(s) (i.e., all stations in the balanced
case) never starve for lack of work. But high WIP also ensures a great deal of waiting
and hence high cycle times.
     The throughput and cycle time of the practical worst case are always between those
of the best case and the worst case. As such, the PWC provides a useful midpoint that
approximates the behavior of many real systems. By collecting data on average WIP,
throughput, and cycle time (actually, because of Little’s law, any two of these will sufﬁce)
for a real production line, we can determine whether it lies in the region between the best
and practical worst cases, or between the practical worst and worst cases. Systems with
better performance than the PWC (i.e., that have larger throughput and smaller cycle
time for a given WIP level) are “good” (lean), and systems with worse performance are
“bad” (fat). It makes sense to focus our improvement efforts on the bad lines because
they are the ones with room for improvement. Thus, our three cases offer a sort of
internal benchmarking methodology (i.e., as opposed to external benchmarking in
which comparisons are made against outside systems). We will illustrate the internal
benchmarking procedure explicitly in Section 7.3.5.
     If internal benchmarking indicates that a line is bad, we can get some guidance on
how to improve it by looking at the three assumptions under which the PWC was derived:
     1. Balanced line
     2. Single-machine stations
     3. Exponential (memoryless) processing times
248                   Part II   Factory Physics

                      Since these three conditions were chosen to maximize randomness in the line, improving
                      any of them will tend to improve the performance of the line.
                           First, we could unbalance the line by adding capacity at a station. This could be
                      accomplished by adding physical equipment, reducing downtime due to worker breaks
                      or equipment failures, speeding up the process through more efﬁcient work methods,
                      and so on. Obviously, if we increase capacity at all stations, throughput will increase.
                      But even if we increase capacity at only some stations, so that rb does not change, this
                      serves to reduce randomness (i.e., the states in Table 7.3 are no longer equally likely)
                      and therefore causes the throughput-versus-WIP curve to increase more rapidly (i.e., less
                      WIP in the system achieves the same throughput). We realize that line unbalancing is
                      somewhat counter to the traditional industrial engineering emphasis on line balancing.
                      However, as we will see in Chapter 18, line balancing is primarily applicable to paced
                      assembly lines, not a line of independent workstations like those we are considering here.
                           Second, we could make use of parallel machines in place of single machines
                      at workstations. If this is accomplished by adding extra machines, then it serves to
                      increase capacity and therefore has essentially the same effects as those discussed
                      above. But even replacing single machines with parallel ones with the same capacity
                      can improve performance in some cases. For instance, reconsider Penny Fab One
                      under the assumption that process times are exponential instead of deterministic and
                      average process times are still 2 hours at each station. Suppose stations 3 and 4
                      (rimming/deburring) are collapsed into a single station with two parallel machines,
                      where the machines perform both rimming and deburring in a single step and take
                      twice as long as before (i.e., an average of 4 hours per penny). Since the capacity of the
                      station is 12 penny per hour, the bottleneck rate of the line is still rb = 0.5. Also, the raw
                      process time remains T0 = 8 hours. But in the former arrangement, two pennies could
                      have wound up at either rimming or deburring, with the consequence that one has to
                      wait. In the revised line, anytime there are two pennies in rimming or deburring, we are
                      guaranteed that both are being worked on. The result will be less waiting, and hence
                      shorter cycle times, for a given WIP level in the revised system with parallel machines.
                           Finally, we could reduce the variability of the processing times to less than that
                      implied by the exponential distribution. Reducing the likelihood of jobs clumping up be-
                      hind stations, and hence waiting, will improve throughput and cycle time for a given WIP
                      level. We will examine what is meant by variability reduction relative to the exponential
                      in Chapter 8, and we will discuss practical methods for achieving it in Part III.
                           Figures 7.12 and 7.13 illustrate some of these concepts by plotting cycle time and
                      throughput as a function of WIP level for Penny Fab Two under the assumption of expo-
                      nentially distributed process times at all stations. For comparison, we have also plotted
                      the best, worst, and practical worst cases for the same bottleneck rate and raw process
                      time (i.e., for rb = 0.4 and T0 = 20). Even though processing times are exponential,
                      because Penny Fab Two has an unbalanced line and parallel machine stations, it out-
                      performs the practical worst case. If we were to reduce the variability of the processing
                      times, this would improve it even more.


7.3.4   Bottleneck Rates and Cycle Time
                      Since the 1980s, a great deal of attention has been focused on the importance of bot-
                      tlenecks in production systems (see, e.g., Goldratt and Cox 1984). Our discussion here
                      certainly conﬁrms that the bottleneck rate rb is important, since it establishes the capacity
                      of the line. But the Factory Physics laws also give us insights into the role of bottlenecks
                      beyond this obvious conclusion.
                           Chapter 7              Basic Factory Dynamics                                                249

Figure 7.12                     80
Cycle time versus WIP in                                           Bad region
                                70
Penny Fab Two.                                      Worst case                                 se Good region
                                60                                                 rs  t ca
                                                                           al   wo
                                                                       ctic                          2
                                50                                  Pra                        Fab
                                                                                    ny
                                                                                Pen
                           CT   40                                                                       1/rb
                                30

                           T0 20
                                                  Best case
                                10

                                  0
                                      0       2     4   6     8 10 12 14 16 18 20 22 24
                                                              W0    WIP




                                First, if we are operating a “good” line (i.e., throughput greater than the practical
                           worst case for any WIP level), then at typical WIP levels (e.g., between 5 and 10 times
                           W0 ) the cycle time will be very close to w/rb , where w is the WIP level. (This can be
                           observed in Figures 7.12 and 7.13.) Hence, increasing the bottleneck rate rb will reduce
                           cycle time for any given WIP level.
                                Unfortunately, there are times when it is physically or economically impractical to
                           speed up the bottleneck. For example, suppose the copper plater is the bottleneck in
                           a printed-circuit-board plant. The rate at which this machine runs is governed by the
                           chemistry of the process. Therefore, if it is already running for the maximum number of
                           hours per day (i.e., it does not suffer from stafﬁng or maintenance problems that could
                           be resolved to increase the effective capacity), then the only way to increase capacity
                           is to add another plater. This is an extremely expensive option that would probably be
                           overkill, since it would result in a 100 percent increase in capacity. In a situation like this,
                           it may make economic sense to consider increasing capacity of nonbottleneck resources.
                                To see this, consider a system with four single-machine stations. Each station takes
                           10 minutes to perform a job except the last station (the bottleneck) which takes 15
                           minutes. Thus, the bottleneck rate is four jobs per hour.


Figure 7.13                           0.5
Throughput time versus                                                                                    Best case
WIP in Penny Fab Two.           rb 0.4
                                                                                           2
                                                                          y Fab                           Good region
                                                                      Penn
                                      0.3
                           TH                                                                    rst case
                                                                                           cal wo
                                                                              P r a c ti
                                      0.2                                                                 Bad region

                                      0.1
                                                                                                          Worst case
                                1/ T0
                                          0
                                              0    2    4     6   8 10 12 14 16 18 20 22 24
                                                                  W0    WIP
250                        Part II       Factory Physics

Figure 7.14                     0.12
Change in throughput
curve due to increase in        0.10
bottleneck rate.
                                0.08


                           TH   0.06


                                0.04


                                0.02


                                     0
                                         0    2      4     6     8      10     12     14    16
                                                                WIP

                                                    TH(w): base case
                                                    TH(w): increased bottleneck rates
                                                    THbest(w): base case
                                                    THbest(w): increased bottleneck rates



                                Now, suppose we speed up the bottleneck to 10 minutes per job (6 jobs per hour),
                           thereby balancing the line. Figure 7.14 illustrates the impact on the throughput versus
                           WIP curve for the line. Notice that the improved line has a higher limiting production
                           rate (a new rb ), but the throughput curve stays further from it than the original system.
                           The reason is that a balanced line tends to starve its bottleneck more frequently than
                           an unbalanced line, and hence requires more WIP for throughput to approach capacity.
                           Nevertheless, speeding up the bottleneck causes throughput to increase for any WIP
                           level.
                                Alternatively, suppose we speed up all of the nonbottleneck processes so that they
                           require only 5 minutes, but keep bottleneck time at 15 minutes. Figure 7.15 shows
                           that this also increases throughput for any WIP level. Indeed, for small WIP levels,
                           the increase in throughput is actually greater than that achieved by speeding up the
                           bottleneck. However, for large WIP levels (six or above), increasing the bottleneck rate
                           achieves a greater increase in throughput than does the increase in nonbottleneck rates.
                           Also we note that we made a bigger change to the nonbottleneck stations than we did to
                           the bottleneck station (i.e., we cut the process time in half at three machines as opposed
                           to reducing the time at a single machine by 33 percent). If we had the freedom to reduce
                           any process time by 5 minutes, the best place to do it would be the bottleneck, always!
                           But since this is not always possible (economical), it is good to know that performance
                           gains can be achieved by improving nonbottleneck resources.


7.3.5    Internal Benchmarking
                           We now have the tools to evaluate the performance of a line. The basic idea is to compare
                           actual performance to that of the best, worst, and practical worst cases. The PWC serves
                           as the benchmark; performance worse than this indicates problems (opportunities), while
                           performance better than this suggests that the line is not vastly inefﬁcient. To show how
                           this works in practice, we introduce a real case.
                           Chapter 7       Basic Factory Dynamics                                                            251

Figure 7.15                     0.08
Change in throughput            0.07
curve due to increase in
rate of nonbottlenecks.         0.06

                                0.05

                           TH   0.04

                                0.03

                                0.02

                                0.01

                                  0
                                       0     2     4      6     8      10     12     14     16
                                                               WIP

                                                 TH(w): base case
                                                 TH(w): increased nonbottleneck rates
                                                 THbest(w): base case
                                                 THbest(w): increased nonbottleneck rates




                                 HAL Case:
                                 HAL, a computer company, manufactures printed-circuit boards (PCBs), which are sold to
                                 other plants, where the boards are populated with components (“stuffed”) and then sent to be
                                 used in the assembly of personal computers. The basic processes used to manufacture PCBs
                                 are as follows:
                                       1. Lamination. Layers of copper and prepreg (woven ﬁberglass cloth impregnated with
                                          epoxy) are pressed together to form cores (blank boards).
                                       2. Machining. The cores are trimmed to size.
                                       3. Circuitize. Through a photographic exposing and subsequent etching process,
                                          circuitry is produced in the copper layers of the blanks, giving the cores “personality”
                                          (i.e., a unique product character). They are now called panels.
                                       4. Optical test and repair. The circuitry is scanned optically for defects, which are
                                          repaired if not too severe.
                                       5. Drilling. Holes are drilled in the panels to connect circuitry on different planes of
                                          multilayer boards. Note that multilayer panels must return to lamination after being
                                          circuitized to build up the layers. Single-layer panels go through lamination only
                                          once and do not require drilling or copper plating.
                                       6. Copper plate. Multilayer panels are run through a copper plating bath, which deposits
                                          copper inside the drilled holes, thereby connecting the circuits on different planes.
                                       7. Procoat. A protective plastic coating is applied to the panels.
                                       8. Sizing. Panels are cut to ﬁnal size. In most cases, multiple PCBs are manufactured on
                                          a single panel and are cut into individual boards at the sizing step. Depending on the
                                          size of the board, there could be as few as two boards made from a panel, or as many
                                          as 20.
                                       9. End-of-line test. An electrical test of each board’s functionality is performed.
                                    HAL engineers monitor the capacity and performance of the PCB line. Their best estimates
                                 of capacity are summarized in Table 7.4, which gives the average process rate (number of
                                 panels per hour) and average process time (hours) at each station. (Note that because panels
252   Part II   Factory Physics


                   Table 7.4 Capacity Data for HAL Printed-Circuit-Board Line
                    Process                        Rate (parts per hour)       Time (hours)

                    Lamination                             191.5                     4.7
                    Machining                              186.2                     0.5
                    Internal circuitize                    114.0                     3.6
                    Optical test/repair—int.               150.5                     1.0
                    Lamination—composites                  158.7                     2.0
                    External circuitize                    159.9                     4.3
                    Optical test/repair—ext.               150.5                     1.0
                    Drilling                               185.9                    10.2
                    Copper plate                           136.4                     1.0
                    Procoat                                117.3                     4.1
                    Sizing                                 126.5                     1.1
                    EOL test                               169.5                     0.5

                    rb , T0                                114.0                    33.9




            are often processed in batches and because many processes have parallel machines, the rate
            of a process is not the inverse of the time.) These values are averages, which account for
            the different types of PCBs manufactured by HAL and also the different routings (e.g.,
            some panels may visit lamination twice). They also account for “detractors,” such as machine
            failures, setup times, and operator efﬁciency. As such, the process rate gives an approximation
            of how many panels each process could produce per hour if it had unlimited inputs. The process
            time represents the average time a typical panel spends being worked on at a process, which
            includes time waiting for detractors but does not include time waiting in queue to be worked on.
                The main performance measures emphasized by HAL are throughput (how many PCBs
            are produced), cycle time (the time it takes to produce a typical PCB), work in process
            (inventory in the line), and customer service (fraction of orders delivered to customers on
            time). Over the past several months, throughput has averaged about 1,400 panels per day, or
            about 71.8 panels per hour (HAL works three shifts per day, which results in 19.5 productive
            hours per day after considering breaks, lunches, shift changes, and meetings). WIP in the line
            has averaged about 47,000 panels, and manufacturing cycle time has been roughly 34 days,
            or 816 hours. Customer service has averaged about 75 percent.
                The question is, how is HAL doing?

          We can answer part of this question with no analysis at all. HAL management is not
      happy with 75 percent customer service because it has a corporate goal of 90 percent.
      So this aspect of performance is not good. However, perhaps the reason for this is that
      overzealous salespersons are promising unrealistic due dates to customers. It may not
      be an indication of anything wrong with the line.
          To evaluate performance along the other metrics—throughput, WIP, and cycle
      time—we make use of the internal benchmarking procedure. To do this, observe from
      Table 7.4 that the bottleneck rate is rb = 114 panels per hour and raw process time is
      T0 = 33.9 hours. Hence, the critical WIP for the line is

                               W0 = rb × T0 = 114 × 33.9 = 3,869 panels

           Before making the benchmark calculations we make a quick Little’s law check of
      the data:

                      TH × CT = 1,400 panels/day × 34 days = 47,600 panels
                           Chapter 7                  Basic Factory Dynamics                                                 253

Figure 7.16                                 140
                                                                                                        Best case
Throughput versus WIP in
HAL case.                                   120
                                                           Good region                             Practical worst case
                                            100




                           TH (panels/hr)
                                             80

                                             60

                                             40
                                                           Bad region
                                                                                             Actual performance
                                             20

                                              0
                                                                                                        Worst case
                                            –20
                                                  0   5,000 10,000 15,000 20,000 25,000 30,000 35,000 40,000 45,000 50,000
                                                                              WIP (panels)



                           which is very close to the actual value of 47,000 panels. Since Little’s law applies
                           precisely only to long-term averages, we would not expect it to hold exactly. However,
                           this is certainly well within the precision of the data and hence suggests no problems.
                                We now compare actual performance to that of the PWC with the same rb , T0 , and
                           WIP level as the HAL line:
                                                             w                 47,000
                                            THPWC =                 rb =                    (114) = 105.3 panels per hour
                                                         W0 + w − 1      3,869 + 47,000 − 1

                           Actual throughput is 71.8 panels per hour, which is signiﬁcantly smaller than 105.3 and
                           hence indicates that performance that is much worse than that of the practical worst case.
                                We can put these calculations in graphical terms by plotting the best, worst, and
                           practical worst throughput versus WIP curves and plotting the actual performance. This
                           results in the graph in Figure 7.16, which shows dramatically that the (WIP, TH) pair of
                           (47,000, 71.8) is well into the “bad” region between the worst and practical worst cases.
                           Clearly, lines that exhibit such behavior offer much more opportunity for improvement
                           than lines in the “good” region between the practical worst and best cases.
                                This example shows that the models presented in this chapter can help diagnose a
                           production line and determine whether it is operating efﬁciently or not. But they do not
                           tell us why a line is operating poorly and therefore do not help us determine how to
                           improve it. For this, we require a deeper investigation of what causes some lines to be
                           very efﬁcient at converting WIP to throughput and others to be very inefﬁcient. This is
                           the subject of the next two chapters.


7.4    Labor-Constrained Systems
                           Throughout this chapter, we have focused on lines in which machines are the constraint
                           (bottleneck). We have implicitly assumed that if there are human operators, they are
                           assigned to machines and can therefore be viewed as part of the workstations. However,
                           in some systems, workers perform multiple tasks or tend more than one workstation.
                           These types of systems exhibit more complex behavior than the simple lines considered
254                        Part II   Factory Physics

                           so far, since the ﬂow of work is affected by the number and characteristics of both
                           machines and operators.
                                Although the subject of ﬂexible labor is much too broad for us to treat comprehen-
                           sively here, we can make some observations about how labor-constrained lines relate to
                           the simple lines presented earlier. We do this by considering three situations below.


7.4.1   Ample Capacity Case
                           We begin with the case in which labor is the only constraint on output. That is, we as-
                           sume sufﬁcient equipment at each workstation to ensure that a worker is never blocked
                           for lack of a machine. While one might think that such a situation would never arise
                           in practice, there are realistic situations that approximate this behavior. An example the
                           authors encountered was that of a prepress graphical production facility of catalogs and
                           other marketing materials. This ﬁrm received content (text, photos, etc.) from its clients
                           and converted these materials into electronic engraving data via a series of steps (e.g.,
                           scanning, color correction, page ﬁnishing), which it then sent to a printer to be made
                           into paper products. Most of the prepress steps required a computer along with some pe-
                           ripheral equipment. Because computer equipment was inexpensive relative to the cost of
                           delays, the ﬁrm installed enough duplicates of each station to ensure that technicians vir-
                           tually never had to wait for equipment to perform the various tasks. The result was many
                           more machines than people, which meant that labor was the key constraint in the system.
                                A primary reason the graphics company installed ample capacity at its stations was
                           to facilitate its ﬂexible labor policy. Instead of having specialists for each operation,
                           the company had cross-trained the workforce so that almost everyone could do almost
                           every operation. This allowed the company to assign workers to jobs instead of stations.
                           A worker would follow a job through the system, performing each operation on the
                           appropriate workstation, as shown in Figure 7.17. The extra computers made it very
                           unlikely that someone would ever have to wait for equipment at a station. Having workers
                           stay with a job all the way through the system meant that customers had a single person
                           to contact and also made one person clearly responsible for quality.
                                In a system like this, capacity is deﬁned by labor rather than equipment. To char-
                           acterize capacity, we will continue to let T0 represent the average time for one job to
                           traverse the system, which we assume is independent of which worker is assigned to the
                           job. Furthermore, we suppose that once a worker starts a job, he or she continues with
                           it until it is done. Stopping work midway through a job cannot improve throughput and
                           will only increase cycle time, so unless some customers have higher priority than others,
                           there is no reason to do this. Under these assumptions, jobs are released into the system
                           only when a worker becomes available, and since there is no blocking due to equipment,


Figure 7.17                Worker
Ample capacity line with
fully cross-trained           1
workers.

                              2


                              3

                                            1               2                 3                  4           Station
                             Chapter 7   Basic Factory Dynamics                                                      255

                             cycle time is always T0 . If there are n workers in the line, all working at the same rate,
                             then each puts out a job every T0 time units, which means that throughput is n/T0 .
                                  Since the ample capacity case is an ideal situation, any changes to our assumptions
                             can only decrease throughput. Examples of such changes include less-than-ample equip-
                             ment so that blocking occurs, intermittent arrival of work that may cause starving, partial
                             cross-training so that jobs may have to wait for a “specialist” at some stations, or any
                             other change that prevents workers from being completely busy. Hence, we can deﬁne
                             the capacity of a labor-constrained system as follows.

                             Deﬁnition (Labor Capacity): The maximum capacity of a line staffed by n cross-
                             trained operators with identical work rates is
                                                                               n
                                                                    THmax =
                                                                               T0
                                  This deﬁnition provides a way to introduce labor into the capacity calculations. For
                             instance, in a line that has more stations than workers, the bottleneck rate of the equipment
                             rb may be a poor estimate of the capacity of the line. Where throughput is constrained
                             by labor, n/T0 may be a more realistic and useful upper bound on throughput. This
                             bound is applicable to a wide range of systems, including those with fully or partially
                             cross-trained workers.
                                  One class of systems to which it does not apply, however, is that in which a worker can
                             process more than one job simultaneously. For instance, a manufacturing cell where a sin-
                             gle operator can tend several automated machines at the same time may have throughput
                             exceeding n/T0 . Such systems are often appropriately viewed as equipment-constrained,
                             where operator unavailability acts as a capacity detractor and variability inﬂator. We will
                             examine detractors in Chapter 8.


7.4.2    Full Flexibility Case
                             To deepen our insight into how both equipment and labor affect capacity, we next consider
                             the case in which workers are completely cross-trained (i.e., can operate every station
                             in the line). Furthermore, we begin by assuming that workers are tied to jobs as in the
                             ample capacity case. However, unlike in the ample capacity case, equipment is limited
                             so workers may become blocked, as shown in Figure 7.18. Once a worker ﬁnishes a job
                             at the end of the line, she goes back to the beginning and starts a new one.
                                  If the workers in Figure 7.18 have identical work rates, then this line is logically
                             identical to the CONWIP lines we considered previously, except that the WIP level is
                             now the number of workers. Hence, the behavior of the line will lie somewhere between
                             the best and worst cases, with the practical worst case deﬁning the division between
                             good and bad lines. Furthermore, all the improvement strategies we listed earlier—
                             increasing capacity, reducing line balance, using parallel machine stations, and reducing
                             variability—still apply to this case.
                                  The assumption of fully cross-trained workers who walk jobs all the way through the
                             line may not be realistic in many situations. For instance, if the workstations require very
                             different skills, it may make sense to have workers pass jobs from one to another. One
                             mechanism is the bucket brigade (see Bartholdi and Eisenstein 1996). In this system,
Figure 7.18
Line with fully
cross-trained workers tied
to jobs.
256                       Part II   Factory Physics

                          whenever the worker farthest downstream in the line completes a job, he or she moves
                          up the line and takes the job from the next worker upstream. That worker in turn moves
                          upstream and takes the job from the next worker. And so on, until the worker farthest
                          upstream takes a new job. If all workers work at the same speed and there is no delay
                          due to the handing off of the jobs, then there is no logical difference in this system from
                          the one depicted in Figure 7.18. The line still operates as a CONWIP line with the WIP
                          level set by the number of workers. Only the identities of the workers assigned to each
                          job are changed.
                               While the bucket brigade system may not differ logically from the system with
                          workers tied to jobs, it does differ practically. Each worker will tend to operate stations
                          in a zone. Indeed, in the case where all process times are perfectly deterministic (i.e., the
                          best case), the line will settle into a repetitive cycle where each worker processes jobs
                          through the same sequence of stations. Cross-training and job transfers allow the line
                          to balance itself so that each worker spends the same amount of time with a job. This
                          type of system has been used effectively in automobile seat construction (see Chapter 10
                          for a discussion of this system at Toyota), warehouse picking, and fast-food sandwich
                          construction (Subway).
                               Notice that blocking is still possible in bucket brigades. Whenever an upstream
                          worker catches up with the next worker downstream, she or he will be blocked unless
                          the station has extra equipment. Hence, it makes sense to organize the workers so as
                          to minimize the frequency with which this happens, by placing the fastest workers
                          downstream and the slowest workers upstream. Bartholdi and Eisenstein (1996) showed
                          that this arrangement from slowest to fastest can signiﬁcantly improve throughput and
                          observed that this tends to be the practice in industry where such systems are used.


7.4.3   CONWIP Lines with Flexible Labor
                          If workers stay tied to jobs (or hand off jobs directly from one to another as in the
                          bucket brigade system), then the number of jobs in the system always equals the number
                          of workers and the system behaves logistically as a CONWIP line. But in many, if
                          not most, systems, the number of jobs will typically exceed the number of workers. If
                          workers can rove through the system and work at different stations, then the performance
                          of the system will depend on how effectively labor is allocated to promote ﬂow through
                          the system. This can get complex, since there are countless ways that labor can be
                          dynamically allocated in the system.
                               One approach, which is a natural extension of the bucket brigade system to the
                          case with more jobs than workers, is to have any worker who becomes free take the
                          next job upstream, either from the upstream worker or from a buffer (see Figure 7.19
                          for an illustration of the mechanics). Whenever a worker becomes blocked because a
                          downstream station is busy, the worker drops the job in the buffer in front of the station
                          and moves upstream to get another job. This continues as long as the total number of


Figure 7.19
CONWIP line using
bucket brigade with job          Released jobs
dropping.                       awaiting workers                       Dropped job
                        Chapter 7   Basic Factory Dynamics                                                      257

                        jobs in the system does not exceed some preset limit (without such a limit, a fast worker
                        at the front of the line would ﬂood the line with WIP).
                             If all stations consist of single machines, so that no passing is possible, then at any
                        time worker n (the last worker in the line) will be working on the job farthest downstream.
                        Worker n − 1 will be working on the next-farthest job downstream that is not blocked by
                        worker n. And so on. If passing on multimachine stations is possible, then the workers can
                        get out of order. But the basic intent is still to keep workers working whenever possible
                        on the jobs farthest downstream. Keeping workers busy tends to maximize throughput;
                        working on downstream jobs tends to minimize cycle times. Hence, we would expect
                        this policy to work reasonably well.
                             Systems where job processing requires both a machine and an operator are more
                        complex than those we discussed in earlier sections of this chapter, where only machines
                        were constraints. However, in some cases, the behavior of systems with labor can be
                        described in similar terms. For instance, if there is no difference in the speed of workers,
                        then the throughput of the system depends entirely on how often unblocked jobs are idle
                        for lack of a worker. If this never happens, then the system will operate like a regular
                        CONWIP line. If it happens so frequently that the workers might just as well be tied to
                        one job each, then the system will operate as a CONWIP line with only as many jobs as
                        workers. If jobs with an available machine occasionally wait for an operator, then perfor-
                        mance will be somewhere in between that of a regular CONWIP line (i.e., with WIP equal
                        to the number of jobs) and a CONWIP line with WIP equal to the number of workers.

7.4.4   Flexible Labor System Design
                        In practice, making use of ﬂexible labor to improve operational efﬁciency involves two
                        levels of management decisions:
                             1. Training: determining which operators will be trained to do which tasks within
                                the system.
                             2. Assignment: allocating operators to tasks in real time according to system needs
                                and operator capabilities.
                             Because training can be expensive and time-consuming, it is often impractical to
                        equip every operator with the necessary skills to do every job. So, assignment policies
                        that require operators to follow jobs through the entire line, or even a large segment
                        of it, may not be practical options. Fortunately, however, recent research suggests that
                        policies based on much more restrictive levels of cross-training can achieve most of
                        the performance beneﬁts achievable with full cross-training. One approach is the use of
                        chaining policies, in which operators are trained to cover limited zones of workstations,
                        but where the zones overlap. Figure 7.20 depicts a U-shaped line in which operators are

Figure 7.20                         Material flow
Example of production
line with chaining of
operator skills.
258                 Part II   Factory Physics

                    able to cover their base station and the next station in the sequence (with the operator
                    of the last station trained to cover the ﬁrst station, to complete the chain). In chaining
                    systems, capacity can be dynamically shifted from any station to any other by reassigning
                    operators within their zones (see Hopp, Tekin, and Van Oyen 2004 for details). This makes
                    them very robust to ﬂuctuations in workloads (e.g., due to temporary shifts in product
                    mix) or stafﬁng levels (e.g., due to absenteeism).
                         In addition to affecting operational efﬁciency, cross-training and dynamic assign-
                    ment of operators can affect quality, ergonomics, customer service, and other dimensions
                    of a production system. Because both strategic needs and environmental characteristics
                    vary greatly among systems, many different approaches have been used to develop and
                    use labor ﬂexibility. Determining the best approach for a given system involves evalu-
                    ating the strategic objectives that can be addressed through cross-training and matching
                    the policy to the environmental characteristics of the system (see Hopp and Van Oyen
                    2004 for a formal framework with which to make such evaluations).



7.5   Conclusions
                    In this chapter we examined the fundamental behavior of a single production line by
                    studying the relationships among cycle time, WIP, throughput, and capacity. We observed
                    the following:
                          1. A single line can be reasonably summarized by two independent parameters:
                             the bottleneck rate rb and the raw process time T0 . However, as we observed, a
                             wide range of behavior is possible for lines with the same rb and T0 . We will
                             investigate the causes of this disparity in the next two chapters.
                          2. Little’s law (WIP = TH × CT) provides a fundamental relationship between
                             three long-term average measures of the performance of any production station,
                             line, or system.
                          3. The best case deﬁnes the maximum throughput and minimum cycle time for a
                             given WIP level for any line with speciﬁed values of rb and T0 . The worst case
                             deﬁnes the minimum throughput and maximum cycle time for any line with
                             speciﬁed values of rb and T0 . The practical worst case provides an intermediate
                             scenario that serves as a useful demarcation between “good” and “bad” systems.
                          4. The critical WIP level, deﬁned as W0 = rb T0 , represents a realistic ideal WIP
                             level (as opposed to the unrealistic ideal of zero inventory, which would result
                             in zero throughput). At W0 , a best-case (i.e., zero-variability) line achieves both
                             maximum throughput (i.e., rb ) and minimum cycle time (i.e., T0 ).
                          5. Both the best case and the worst case occur in systems with zero randomness.
                             The worst case results from high variability caused by bad control rather than
                             randomness. The practical worst case represents the maximum randomness
                             situation.
                          6. When WIP levels are high, reducing raw process time T0 has little effect on
                             cycle times, while increasing rb can have a great impact.
                          7. Other things being equal (that is, rb and T0 are the same), unbalanced lines
                             exhibit less congestion than balanced lines.
                          8. Production lines can be constrained by a combination of equipment and labor.
                             Equipment capacity is bounded by the bottleneck rate rb , while labor capacity is
                             bounded by n/T0 , where n is the number of workers in the line.
                  Chapter 7   Basic Factory Dynamics                                                              259

                       9. Systems with high process variability and balanced stations are most amenable
                          to cross-training and ﬂexible labor policies. In addition, parallel machine
                          stations help facilitate ﬂexible work policies.
                       A thread that has emerged from this analysis of basic factory dynamics is that a line
                  can achieve the same throughput at a lower WIP level by either increasing capacity or
                  improving the efﬁciency of the line. As we hinted in our treatment of the practical worst
                  case, a primary way of increasing line efﬁciency is by reducing variability at individual
                  stations. To be able to evaluate the relative effectiveness of capacity increases versus
                  variability reduction, we must further develop the science of Factory Physics to describe
                  the behavior of production systems involving variability. We do this next in Chapters 8
                  and 9.



Study Questions
                  1. Suppose throughput TH is near capacity rb . Using Little’s law, relate
                     (a) WIP and cycle time in a production line.
                     (b) Finished goods inventory and time spent in ﬁnished goods inventory.
                     (c) The number of cars waiting at a toll booth and the average wait time.
                  2. Is it possible for a line to have the same throughput with both high WIP with high cycle time
                     and low WIP with low cycle time? Which would you rather have? Why?
                  3. For a given set of production line characteristics (i.e., raw process time T0 and bottleneck
                     rate rb ) and a given WIP level w, what is the best cycle time that can be achieved? What is
                     the “worst”? What is the corresponding throughput for these two cases?
                  4. What are the conditions for the practical worst-case throughput? What types of behavior can
                     lead to performance worse than that in this case? What would this do to throughput? To cycle
                     times?
                  5. Can the critical WIP level W0 ever exceed the number of machines in the line?
                  6. Suppose process times on a machine are exponentially distributed with a mean of 10 minutes.
                     A job has currently been running for 90 minutes. What is the expected time until completion?




Problems
                   1. Compute the capacity in parts per hour of the following:
                      (a) A station with three machines operating in parallel with 20-minute process times at each
                          station.
                      (b) A balanced line with single-machine stations, all with average processing times of 15
                          minutes.
                      (c) A four-station line with single-machine stations, where the average processing times are
                          15, 20, 10, 12 minutes, respectively for stations 1, 2, 3, 4.
                      (d) A four-station line with multimachine stations, where the number of (parallel) machines
                          at stations 1, 2, 3, 4 is 2, 6, 10, 3, respectively. The average processing times at stations
                          1, 2, 3, 4 are 10, 24, 40, 18 minutes, respectively.
                      (e) A three-station line with ample equipment (i.e., such that operators are never prevented
                          from processing a job by a lack of equipment) staffed by six operators who are identical
                          with regard to average processing times and require 10, 15, and 5 minutes, respectively,
                          on stations 1, 2, 3.
                      (f) The same line as in the above case except that station 2 consists of only two parallel
                          machines. All other stations still have ample capacity.
260   Part II   Factory Physics

       2. Consider a three-station line with single-machine stations. The average processing times on
          stations 1, 2, 3 are 15, 12, and 14 minutes, respectively. However, station 2 is subject to
          random failures, which cause its fraction of uptime (availability) to be only 75 percent.
          (a) Which station is the bottleneck of this line?
          (b) What are the bottleneck rate rb , raw process time T0 , and critical WIP W0 for the line?
          (c) If availability of station 2 is reduced to 50 percent, what happens to the critical WIP W0 ?
               Briefly describe the likely impacts of this change.
       3. A powder metal (PM) manufacturing line produces bushings in three steps, compaction,
          sinter-harden, and rough/finish turn, which are accomplished at three single-machine
          stations with average processing times of 12, 10, and 6 minutes, respectively. However,
          while compaction and sinter-harden are dedicated to the bushing line, the rough/finish turn
          station also processes bearings from another line; the average processing times for bearings
          are 14 minutes.
          (a) If the production volumes of bushings and bearings are the same, what is the bottleneck
               of the PM line?
          (b) If the volume of bearings is 1/2 that of bushings, what is the bottleneck of the PM line?
          (c) If the volume of bearings is 1/3 that of bushings, what is the bottleneck of the PM line?
          (d) If you had to pick one process for the bottleneck, which one would it be?
       4. A print shop runs a two-station binding line, in which the first station punches holes in the
          pages and the second station installs the binders. On average, the punch machine can
          process 15,000 pages per hour, while the binder can process 10,000 pages per hour. The
          shop receives work that requires both punching and binding at a rate of 8,000 pages per
          hour. It also receives work requiring only punching at a rate of 5,000 pages per hour. Which
          station is the bottleneck of this line and why?
       5. Consider a four-station line in which all stations consist of single machines. Station 2 has
          average processing times of 2 hours per job, while the remaining stations have average
          processing times of 1 hour per job. Answer the following, under the assumption that process
          times are deterministic (as in the best case).
          (a) What are rb and T0 for this line?
          (b) How do rb and T0 change if a second identical machine is added to station 2? What
               effects will this have on performance?
          (c) How do rb and T0 change if the machine at station 2 is speeded up to have average
               processing times of 1 hour? What effects will this have on performance?
          (d) How do rb and T0 change if a second, identical machine is added to station 1? What
               effects will this have on performance?
          (e) How do rb and T0 change if the machine at station 1 is speeded up to have average
               processing times of 12 hour? What effects will this have on performance? Do your
               results agree or disagree with the statement “An hour saved at a nonbottleneck is a
               mirage (i.e., of no value)”?
       6. Repeat Problem 4 under the assumption that all jobs are processed at a station before
          moving (as in the worst case).
       7. Repeat Problem 4 under the assumption that process times are exponentially distributed and
          the line is balanced at the bottleneck rate (as in the practical worst case).
       8. Consider the following three-station production line with a single product that must visit
          stations 1, 2, and 3 in sequence:
            Station 1 has five identical machines with average processing times of 15 minutes

             per job.
            Station 2 has 12 identical machines with average processing times of 30 minutes

             per job.
            Station 3 has one machine with average processing time of 3 minutes per job.

             (a) What are the bottleneck rate rb , the raw process time T0 , and the critical WIP w 0 ?
                        Chapter 7    Basic Factory Dynamics                                                             261

                                (b) Compute the average cycle time when the WIP level is set at 20 jobs, under the
                                      assumptions of:
                                       (i) The best case
                                      (ii) The worst case
                                     (iii) The practical worst case
                                (c) Suppose you desire the throughput of a line to be 90 percent of the bottleneck rate.
                                      Find the WIP level required to achieve this under the assumptions of:
                                       (i) The best case
                                      (ii) The worst case
                                     (iii) The practical worst case
                                (d) If the cycle time at the critical WIP is 100 minutes, where does performance fall
                                      relative to the three cases? Is there much room for improvement?
                          9. Positively Rivet Inc. is a small machine shop that produces sheet metal products. It had one
                             line dedicated to the manufacture of light-duty vent hood shells, but because of strong
                             demand it recently added a second line. The new line makes use of higher-capacity
                             automated equipment but consists of the same basic four processes as the old line. In
                             addition, the new line makes use of one machine per workstation, while the old line has
                             parallel machines at the workstations. The processes, along with their machine rates,
                             number of machines per station, and average times for a lone job to go through a station
                             (i.e., not including queue time), are given for each line in the following table:


                                Old Line                                                New Line
            Rate per Machine    Number Machines        Time        Rate per Machine      Number Machines        Time
Process       (parts/hour)        per Station         (minute)       (parts/hour)          per Station         (minute)

Punching          15                    4                4.0              120                    1               0.50
Braking           12                    4                5.0              120                    1               0.50
Assembly          20                    2                3.0              125                    1               0.48
Finishing         50                    1                1.2              125                    1               0.48



                             Over the past 3 months, the old line has averaged 315 parts per day, where one day consists
                             of one 8-hour shift, and has had an average WIP level of 400 parts. The new line has
                             averaged 680 parts per 8-hour day with an average WIP level of 350 parts. Management has
                             been dissatisﬁed with the performance of the old line because it is achieving lower
                             throughput with higher WIP than the new line. Your job is to evaluate these two lines to the
                             extent possible with the above data and identify potentially attractive improvement paths for
                             each line by addressing the following questions.
                             (a) Compute rb , T0 , and W0 for both lines. Which line has the larger critical WIP? Explain
                                 why.
                             (b) Compare the performance of the two lines to the practical worst case. What can you
                                 conclude about the relative performance of the two lines compared to their underlying
                                 capabilities? Is management correct in criticizing the old line for inefﬁciency?
                             (c) If you were the manager in charge of these lines, what option would you consider ﬁrst to
                                 improve throughput of the old line? Of the new line?
                         10. Floor-On, Ltd., operates a line that produces self-adhesive tiles. This line consists of
                             single-machine stations and is almost balanced (i.e., station rates are nearly equal). A
                             manufacturing engineer has estimated the bottleneck rate of the line to be 2,000 cases per
                             16-hour day and the raw process time to be 30 minutes. The line has averaged 1,700 cases
                             per day, and cycle time has averaged 3.5 hours.
                             (a) What would you estimate average WIP level to be?
                             (b) How does this performance compare to the practical worst case?
262              Part II   Factory Physics

                      (c) What would happen to the throughput of the line if we increased capacity at a
                           nonbottleneck station and held WIP constant at its current level?
                      (d) What would happen to the throughput of the line if we replaced a single-machine station
                           with four machines whose capacity equaled that of the single machine and held the WIP
                           constant at its current level?
                      (e) What would happen to the throughput of the line if we began moving cases of tiles
                           between stations in large batches instead of one at a time?
                  11. T&D Electric manufactures high-voltage switches and other equipment for electric utilities.
                      One line that is staffed by three workers assembles a particular type of switch. Currently the
                      three workers have ﬁxed assignments; each worker fastens a speciﬁc set of components onto
                      the switch and passes it downstream on a rolling conveyor. The conveyor has capacity to
                      allow a queue to build up in front of each worker. The bottleneck is the middle station with a
                      rate of 11 switches per hour. The raw process time is 15 minutes. To improve the efﬁciency
                      of the line, management is considering cross-training the workers and implementing some
                      sort of ﬂexible labor system.
                      (a) If current throughput is 10.5 switches per hour with an average WIP level of ﬁve jobs,
                           how much potential do you think there is for a ﬂexible work system?
                      (b) If current throughput is eight switches per hour with an average WIP level of seven jobs,
                           how much potential do you think there is for a ﬂexible work system?
                      (c) If all three workers were fully cross-trained and equipped to assemble the entire switch
                           in parallel (i.e., no passing of jobs to one another) and were able to maintain the current
                           work pace of each operation, what would the capacity of the system be? What
                           real-world problems might make such a policy unattractive?
                      (d) Suggest a ﬂexible work system that could improve the efﬁciency of a line like this with
                           less than full cross-training (i.e., with workers trained and equipped to assemble only
                           certain components).
                  12. Consider a balanced line consisting of ﬁve single-machine stations with exponential process
                      times. Suppose the utilization is 75 percent and the line runs under the CONWIP protocol
                      (i.e., a new job is started each time a job is completed).
                      (a) What is the WIP level in the line?
                      (b) What is the cycle time as a percentage of T0 ?
                      (c) What happens to WIP, CT, and TH relative to the original system if you make each of
                           the following changes (one at a time)?
                              (i) Increase the WIP level
                             (ii) Decrease the variability of one station
                           (iii) Decrease the capacity at one station
                            (iv) Increase the capacity of all stations




Intuition-Building Exercises
                  1. Simulate Penny Fab Two by taking a piece of paper and drawing a schematic of the line (see
                     Figure 7.21). Draw the squares large enough to contain a penny. To the right of each square,
                     write the time of the completion of the job occupying that square (as the simulation
                     progresses, you will cross out the old time and replace it with the next time). The simulation
                     progresses by setting the current “simulated time” to be the earliest completion time and
                     moving the pennies accordingly.
                     (a) Run your simulation for several simulated hours with seven pennies. Note how the
                         second station sometimes starves.
                     (b) Run your simulation for several simulated hours with eight pennies. Observe that station
                         2 never starves and there is never any queueing once the initial transient queue is
                         dissipated in front of the ﬁrst station.
                           Chapter 7      Basic Factory Dynamics                                                            263

Figure 7.21                                                              27
                                                                         17
Penny Fab Two with                   24
w = 9, 22 hours into the             22
                                     18
simulation.                          16                                  29
                                     14                                  19
                                     12
                                     10
                                                        27                              25
                                      8
                                                        22               32             20
                                      6
                                                        17               22
                                      4
                                                        12
                                      2
                                                         7

                                                                         24
                                                        24                              22
                           2 hours                      19
                                                        14
                                                         9
                                              5 hours                         3 hours




                                                              10 hours


                              (c) Run your simulation for several simulated hours with nine pennies (Figure 7.21 illustrates
                                  this scenario after 22 simulated hours). Note that after the initial transient, there is always
                                  a queue in front of the second station.
                           2. Simulate Penny Fab Two for 25 hours starting with an empty line and eight pennies in front.
                              Record the cycle time of each penny that ﬁnishes during this time (i.e., record its start time
                              and ﬁnish time and compute cycle time as the difference).
                              (a) What is the average cycle time CT?
                              (b) How many jobs ﬁnish during the 25 hours?
                              (c) What is the average throughput TH over 25 hours? Does average WIP equal CT times
                                  TH? Why or why not? (Hint: Did Little’s law hold for the ﬁrst 2 hours of our simulation
                                  of Penny Fab One?) What does this tell you about the use of Little’s law over short time
                                  intervals?
