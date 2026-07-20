---
curso: FUNDOPS
titulo: Matching supply with demand - Gérard Cachon and Christian Terwiesch. 4 ed., 2019-74-97
slides: 24
fuente: Matching supply with demand - Gérard Cachon and Christian Terwiesch. 4 ed., 2019-74-97.pdf
---

Chapter

            4
            Estimating and
            Reducing Labor Costs
            The objective of any process should be to create value (make profits), not to maximize the
            utilization of every resource involved in the process. In other words, we should not attempt
            to produce more than what is demanded from the market, or from the resource down-
            stream in the process, just to increase the utilization measure. Yet, the underutilization of
            a resource, human labor or capital equipment alike, provides opportunities to improve the
            process. This improvement can take several forms, including
            ∙ If we can reduce the excess capacity at some process step, the overall process becomes
              more efficient (lower cost for the same output).
            ∙ If we can use capacity from underutilized process steps to increase the capacity at
              the bottleneck step, the overall process capacity increases. If the process is capacity-­
              constrained, this leads to a higher flow rate.
               In this chapter, we discuss how to achieve such process improvements. Specifically,
            we discuss the concept of line balancing, which strives to avoid mismatches between
            what is supplied by one process step and what is demanded from the following process
            step (referred to as the process step downstream). In this sense, line balancing attempts to
            match supply and demand within the process itself.
               We use Novacruz Inc. to illustrate the concept of line balancing and to introduce a num-
            ber of more general terms of process analysis. Novacruz is the producer of a high-end kick
            scooter, known as the Xootr (pronounced “zooter”), displayed in Figure 4.1.


4.1 Analyzing an Assembly Operation
            With the increasing popularity of kick scooters in general, and the high-end market seg-
            ment for kick scooters in particular, Novacruz faced a challenging situation in terms of
            organizing their production process. While the demand for their product was not much
            higher than 100 scooters per week in early March, it grew dramatically, soon reaching
            1,200 units per week in the fall. This demand trajectory is illustrated in Figure 4.2.
                First consider March, during which Novacruz faced a demand of 125 units per week.
            At this time, the assembly process was divided between three workers (resources) as illus-
            trated by Figure 4.3.
                The three workers performed the following activities. In the first activity, the first 30 of
            the overall 80 parts are assembled, including the fork, the steer support, and the t-handle.
                                                                                                         57
58 Chapter 4


FIGURE 4.1
The Xootr by
Novacruz
©Karl Ulrich/Reprinted with
permission from Xootr LLC.
All rights reserved.




                              Given the complexity of this assembly operation, it takes about 13 minutes per scooter to
                              complete this activity. We refer to the 13 minutes/unit as the processing time. Depending
                              on the context, we will also refer to the processing time as the activity time or the service
                              time. Note that in the current process, each activity is staffed with exactly one worker.
                                  In the second activity, a worker assembles the wheel, the brake, and some other parts
                              related to the steering mechanism. The second worker also assembles the deck. This step
                              is somewhat faster and its processing time is 11 minutes per unit. The scooter is completed
                              by the third worker, who wipes off the product, applies the decals and grip tape, and con-
                              ducts the final functional test. The processing time is about 8 minutes per unit.

FIGURE 4.2                     Weekly 1,400
Lifecycle Demand               Demand
Trajectory for Xootrs
                                        1,200


                                        1,000


                                         800


                                         600


                                         400


                                         200


                                           0


                                                                                                         October
                                                                                             September
                                                March   April   May          July
                                                                                    August                                               January
                                                                      June
                                                                                                                   November   December
                                                                                             Estimating and Reducing Labor Costs 59


FIGURE 4.3
Current Process
Layout
Left: ©Nathan Ulrich/Reprinted
with permission from Xootr
LLC. All rights reserved.
Right: ©Reprinted with
permission from Xootr LLC.
All rights reserved.




                                      Components                                                                 Finished Xootrs

                                                      Activity 1              Activity 2            Activity 3




                                    To determine the capacity of an individual resource or a group of resources performing
                                 the same activity, we write
                                                                                 Number of resources
                                                                   ​Capacity = ​ _________________
                                                                                                   ​​
                                                                                   Processing time
                                 This is intuitive, as the capacity grows proportionally with the number of workers.
                                   For example, for the first activity, which is performed by one worker, we write
                                                                         1
                                                   ​Capacity = ​ ________________
                                                                    ​  = 0.0769 scooter / minute​
                                                                 13 minutes / scooter
                                 which we can rewrite as
                                               ​0.0769 scooter / minute × 60 minutes / hour = 4.6 scooters / hour​
                                    Similarly, we can compute capacities of the second worker to be 5.45 scooters/hour and
                                 of the third worker to be 7.5 scooters/hour.
                                    As we have done in the preceding chapter, we define the bottleneck as the resource with
                                 the lowest capacity. In this case, the bottleneck is the first resource, resulting in a process
                                 capacity of 4.6 scooters/hour.


4.2 Time to Process a Quantity X Starting with an Empty Process
                                 Imagine Novacruz received a very important rush order of 100 scooters, which would
                                 be assigned highest priority. Assume further that this order arrives early in the morn-
                                 ing and there are no scooters currently in inventory, neither between the resources
                                 (work-in-process, WIP) nor in the finished goods inventory (FGI). How long will it take to
                                 fulfill this order?
60 Chapter 4


                           As we are facing a large order of scooters, we will attempt to move as many scooters
                       through the system as possible. Therefore, we are capacity-constrained and the flow rate of
                       the process is determined by the capacity of the bottleneck (one scooter every 13 minutes).
                       The time between the completions of two subsequent flow units is called the cycle time of
                       a process and will be defined more formally in the next section.
                           We cannot simply compute the time to produce 100 units as 100 units/0.0769 unit/
                       minute = 1,300 minutes because that calculation assumes the system is producing at the
                       bottleneck rate, one unit every 13 minutes. However, that is only the case once the system
                       is “up and running.” In other words, the first scooter of the day, assuming the system starts
                       the day empty (with no work-in-process inventory), takes even longer than 13 minutes to
                       complete. How much longer depends on how the line is paced.
                           The current system is called a worker-paced line because each worker is free to work at
                       his or her own pace: if the first worker finishes before the next worker is ready to accept the
                       parts, then the first worker puts the completed work in the inventory between them. Even-
                       tually the workers need to conform to the bottleneck rate; otherwise, the inventory before
                       the bottleneck would grow too big for the available space. But that concern is not relevant
                       for the first unit moving through the system, so the time to get the first scooter through the
                       system is 13 + 11 + 8 = 32 minutes. More generally,
                             ​Time through an empty worker-paced process = Sum of the processing times​
                          An alternative to the worker-paced process is a machine-paced process as depicted in
                       Figure 4.4. In a machine-paced process, all of the steps must work at the same rate even
                       with the first unit through the system. Hence, if a machine-paced process were used, then
                       the first Xootr would be produced after 3 × 13 minutes, as the conveyor belt has the same
                       speed at all three process steps (there is just one conveyor belt, which has to be paced to the
                       slowest step). More generally,
                                           ​Time through an empty machine-paced process
                              = Number of resources in sequence × Processing time of the bottleneck step​
                           Now return to our worker-paced process. After waiting 32 minutes for the first scooter,
                       it only takes an additional 13 minutes until the second scooter is produced and from then
                       onwards, we obtain an additional scooter every 13 minutes. Thus, scooter 1 is produced
                       after 32 minutes, scooter 2 after 32 + 13 = 45 minutes, scooter 3 after 32 + (2 × 13) =
                       58 minutes, scooter 4 after 32 + (3 × 13) = 71 minutes, and so on.
                           More formally, we can write the following formula. The time it takes to finish X units
                       starting with an empty system is
                                          ​Time to finish X units starting with an empty system
                                                                                 X − 1 unit
                                             = Time through an empty process + ​ ________ ​​
                                                                                 Flow rate
                          You may wonder whether it is always necessary to be so careful about the difference
                       between the time to complete the first unit and all of the rest of the units. In this case, it
                       is because the number of scooters is relatively small, so each one matters. But imagine a

FIGURE 4.4                                             Conveyor Belt
A Machine-Paced
Process Layout           Components                                                     Finished Xootrs
(Note: conveyor belt
is only shown for                       Activity 1        Activity 2       Activity 3
illustration)
Exhibit 4.1
             TIME TO PROCESS A QUANTITY X STARTING WITH AN EMPTY PROCESS
             1. Find the time it takes the flow unit to go through the empty system:
                • In a worker-paced line, this is the sum of the processing times.
                • In a machine-paced line, this is the cycle time × the number of stations.
             2. Compute the capacity of the process (see previous methods). Since we are producing
                X units as fast as we can, we are capacity-constrained; thus,
                                             ​Flow rate = Process capacity​
             3. Time to finish X units
                                                                       X − 1 unit
                                     ​= Time through empty process + ​ ________ ​​
                                                                       Flow rate
             Note: If the process is a continuous process, we can use X instead.




             continuous-flow process such as a cranberry processing line. Suppose you want to know
             how long it takes to produce five tons of cranberries. Let’s say a cranberry weighs one
             gram, so five tons equals five million cranberries. Now how long does it take to produce
             five million cranberries? Strictly speaking, we would look at the time it takes the first
             berry to flow through the system and then add the time for the residual 4,999,999 berries.
             However, for all computational purposes, five million minus one is still five million, so we
             can make our life a little easier by just ignoring this first berry:
                                    Time to finish X units with a continuous-flow process
                                  ​​                                        X units  ​​​
                                      = Time through an empty process + ​ ________ ​
                                                                           Flow rate
               Exhibit 4.1 summarizes the calculations leading to the time it takes the process to pro-
             duce X units starting with an empty system.


4.3 Labor Content and Idle Time
             What is the role of labor cost in the production of the Xootr? Let’s look first at how much
             actual labor is involved in the assembly of the Xootr. Toward this end, we define the labor
             content as the sum of the processing times of the three workers. In this case, we compute
             a labor content of
                            Labor content = Sum of processing times with labor
                            ​​           ​  =​  13 minutes / unit
                                              
                                                                  + 11 minutes / unit ​+ 8 minutes/unit​​
                                           ​ = 32 minutes per unit
                 These 32 minutes per unit reflect how much labor is invested into the production of
             one scooter. We could visualize this measure as follows. Let’s say there would be a slip of
             paper attached to a Xootr and each worker would write the amount of time spent working
             on the Xootr on this slip. The sum of all numbers entered on the slip is the labor content.
                 Assume that the average hourly rate of the assembly employees is $12 per hour (and
             thus $0.20 per minute). Would the resulting cost of labor then be 32 minutes/unit × $0.20/
             minute = $6.40/unit? The answer is a clear no! The reason for this is that the labor content
             is a measure that takes the perspective of the flow unit but does not reflect any information
             about how the process is actually operated.
                                                                                                            61
62 Chapter 4


                  Assume—for illustrative purposes—that we would hire an additional worker for the
               second activity. As worker 2 is not a constraint on the overall output of the process,
               this would probably not be a wise thing to do (and that is why we call it an illustrative
               example). How would the labor content change? Not at all! It would still require the same
               32 minutes of labor to produce a scooter. However, we have just increased our daily wages
               by 33 percent, which should obviously be reflected in our cost of direct labor.
                  To correctly compute the cost of direct labor, we need to look at two measures:
               ∙ The number of scooters produced per unit of time (the flow rate).
               ∙ The amount of wages we pay for the same time period.
                  Above, we found that the process has a capacity of 4.6 scooters an hour, or 161 scooters
               per week (we assume the process operates 35 hours per week). Given that demand is currently
               125 scooters per week (we are demand-constrained), our flow rate is at 125 scooters per week.
                  Now, we can compute the cost of direct labor as
                                                                Total wages per unit of time
                               Cost of direct labor = _______________________
                                                             ​    ​
                                                                          Flow rate
                                                                      Wages per week
                                                   ​ = _______________________
                                                              ​   
                                                                    ​
                                                                Scooters produced per week
                               ​​                  ​  ​ ​ 
                                                                                        ​    ​ ​​
                                                                3 × $12 /h × 35h / week
                                                     ​ = ___________________
                                                           ​                          ​
                                                                  125 scooters / week
                                                                   $1,260 /  week
                                                     ​ = ________________
                                                            ​      ​ = $10.08 /scooter
                                                                125 scooters / week
                  Why is this number so much higher than the number we computed based on the direct
               labor content? Because the workers are not working 100% of the time. The fraction of the
               time they are working, which is the average labor utilization, is
                                                                   Labor content × Flow rate
                                                                 ______________________
                                Average labor utilization = ​                                        ​
                                                                         Number of workers
                                ​​                       ​ ​  ​ 
                                                                   ​(​​32 min / 60 min / hr​)​​  × 3.57​ units/ hr ​​
                                                             ​ = ______________________________
                                                                 ​                          ​
                                                                                         3
                                                          ​ = 63.5%
                  Note that we must be consistent with units in the above equation—if the flow rate is in units
               per hour then labor content must be in hours, not in minutes. To explain the equation, note that
               the numerator is the number of hours of labor that must be completed every hour: 3.57 units
               arrive every hour and they each need 32/60 hours of work. To make the numbers somewhat
               easier to work with, imagine a health clinic in which 4 patients arrive every hour and each
               needs 1/2 hour of attention from a physician. That would mean that the clinic needs to spend
               4 × 1/2 = 2 hours of time with patients every hour. The denominator is the maximum number
               of hours of labor that could be provided: 3 workers are able to each give 1 hour of effort every
               hour, so in total they could all give 3 hours of work. If the health clinic has 3 physicians, then
               they too can give a total of 3 hours of work every hour. The ratio of the work demanded to the
               maximum that can be provided therefore is the fraction of time labor is working, which is the
               average labor utilization. With scooters it is 63.5%, and with the health clinic it is 2/3 = 67%.
                  Another way to think about labor utilization is through the time that workers are not
               working, what we will refer to as idle time. In this case, there are two sources of idle time:
               ∙ The process is never able to produce more than its bottleneck. In this case, this means
                 one scooter every 13 minutes. However, if we consider worker 3, who only takes 8
                 minutes on a scooter, this translates into a 5-minute idle time for every scooter built.
                                                                                       Estimating and Reducing Labor Costs 63


                       ∙ If the process is demand-constrained, even the bottleneck is not operating at its full
                         capacity and, consequently also exhibits idle time. Given a demand rate of 125 scoot-
                         ers/week, that is, 3.57 scooters/hour or 1 scooter every 16.8 minutes, all three workers
                         get an extra 3.8 minutes of idle time for every scooter they make.
                       This reflects the utilization profile and the sources of underutilization that we discussed in
                       Chapter 3 with the Circored process.
                          Note that this calculation assumes the labor cost is fixed. If it were possible to shorten
                       the workday from the current 7 hours of operations to 5 hours and 25 minutes (25 scooters
                       a day × 1 scooter every 13 minutes), we would eliminate the second type of idle time.
                          More formally, define the following:
                                                                              1
                                                           ​Cycle time = ​ ________ ​​
                                                                           Flow rate
                         Cycle time provides an alternative measure of how fast the process is creating output. As
                       we are producing one scooter every 16.8 minutes, the cycle time is 16.8 minutes. Similar to
                       what we did intuitively above, we can now define the idle time for worker i as the following:
                           ​Idle time for a single worker = Cycle time − Processing time of the single worker​
                          Note that this formula assumes that every activity is staffed with exactly one worker.
                       The idle time measures how much unproductive time a worker has for every unit of output
                       produced. These calculations are summarized by Table 4.1.
                          If we add up the idle time across all workers, we obtain the total idle time that is incurred
                       for every scooter produced:
                                                        ​3.8 + 5.8 + 8.8 = 18.4 minutes / unit​
                          Now, apply the wage rate of $12 per hour ($0.20/minute × 18.4 minutes/unit) and,
                       voilà, we obtain exactly the difference between the labor cost we initially expected based
                       on the direct labor content alone ($6.40 per unit) and the actual cost of direct labor com-
                       puted above.
                          We can now use the information regarding idle time to evaluate
                                                                             Labor content
                          Average labor utilization = ________________________________________
                                                          ​    
                                                                 ​
                                                            Labor content + Sum of idle times across workers
                          ​​                       ​  ​ 
                                                       ​                                                     ​​
                                                                        32[minutes per unit ]
                                                           ____________________________________
                                                     ​ = ​    
                                                                 ​ = 63.5%
                                                            32[minutes per unit ]  + 18.4[minutes per unit ]

TABLE 4.1                                    Worker 1                          Worker 2                      Worker 3
Basic Calculations
Related to Idle Time    Processing time      13 minutes/unit                   11 minutes/unit               8 minutes/unit
                                                    1                                1
                        Capacity                ​  13
                                                __     ​ unit / minute            __ ​ unit / minute
                                                                                  ​  11                         ​  1__8 ​ unit / minute
                                             ​​                       ​   ​​   ​​                   ​   ​​   ​​                        ​ ​​
                                             = 4.61 units/hour                 = 5.45 units/hour             = 7.5 units/hour
                        Process capacity     Minimum {4.61 units/h, 5.45 units/h, 7.5 units/h}
                                             = 4.61 units/hour
                        Flow rate            Demand = 125 units/week = 3.57 units/hour
                                             Flow rate = Minimum {demand, process capacity} = 3.57 units/hour
                        Cycle time           1/3.57 hours/unit = 16.8 minutes/unit
                        Idle time            16.8 minutes/unit                 16.8 minutes/unit             16.8 minutes/unit
                                             − 13 minutes/unit                 − 11 minutes/unit             − 8 minutes/unit
                                             = 3.8 minutes/unit                = 5.8 minutes/unit            = 8.8 minutes/unit
                        Utilization          3.57/4.61 = 77%                   3.57/5.45 = 65.5%             3.57/7.5 = 47.6%
Exhibit 4.2
             SUMMARY OF LABOR COST CALCULATIONS
             1. Compute the capacity of all resources; the resource with the lowest capacity is the bot-
                tleneck (see previous methods) and determines the process capacity.
             2. Compute Flow rate = Min{Available input, Demand, Process capacity}; then compute
                                                                             1
                                                         ​Cycle time = ​ ________ ​​
                                                                         Flow rate
             3. Evaluate Total wages, which is the total wages (across all workers) that are paid per unit
                of time.
             4. Cost of direct labor is
                                                                   Total wages
                                         ​Cost of direct labor = ​ __________
                                                                              ​​
                                                                    Flow rate
             5. Average labor utilization is
                                                                     Labor content × Flow rate
                                      ​Average labor utilization = ​ ______________________
                                                                                            ​​
                                                                        Number of workers
             6. Idle time across all workers at resource i
              Idle time across all workers at resource i = Cycle time × (Number of workers
              ​​​                     ​​​   ​
                                                                                                                    ​
                                     ​                     ​at resource i ​)​​  − Processing time at resource i​​ ​​
             7. Average labor utilization is also
                                                                        Labor content
                                                                _________________________
                                 ​Average labor utilization = ​   
                                                                    ​​
                                                                Labor content + Total idle time




                An alternative way to compute the same number is by averaging the utilization level
             across the three workers:

                ​Average labor utilization = ​ _13 ​  × (​Utilization​  1​​  + ​Utilization​  2​​  + ​Utilization​  3​​) = 63.4%​

             where Utilizationi denotes the utilization of the ith worker.
                Exhibit 4.2 summarizes the calculations related to our analysis of labor costs. It includes
             the possibility that there are multiple workers performing the same activity.


4.4 Increasing Capacity by Line Balancing
             Comparing the utilization levels in Table 4.1 reveals a strong imbalance between work-
             ers: while worker 1 is working 77 percent of the time, worker 3 is only active about half
             of the time (47.6 percent to be exact). Imbalances within a process provide micro-level
             mismatches between what could be supplied by one step and what is demanded by the fol-
             lowing steps. Line balancing is the act of reducing such imbalances. It thereby provides
             the opportunity to
             ∙ Increase the efficiency of the process by better utilizing the various resources, in this
               case labor.
             ∙ Increase the capacity of the process (without adding more resources to it) by reallo-
               cating either workers from underutilized resources to the bottleneck or work from the
               bottleneck to underutilized resources.
64
                                                                            Estimating and Reducing Labor Costs 65


   While based on the present demand rate of 125 units per week and the assumption
that all three workers are a fixed cost for 35 hours per week, line balancing would change
neither the flow rate (process is demand-constrained) nor the cost of direct labor (assum-
ing the 35 hours per week are fixed); this situation changes with the rapid demand growth
experienced by Novacruz.
   Consider now a week in May, by which, as indicated by Figure 4.2, the demand for
the Xootr had reached a level of 200 units per week. Thus, instead of being demand-­
constrained, the process now is capacity-constrained, specifically, the process now is con-
strained by worker 1, who can produce one scooter every 13 minutes, while the market
demands scooters at a rate of one scooter every 10.5 minutes (200 units/week/35 hours/
week = 5.714 units/hour).
   Given that worker 1 is the constraint on the system, all her idle time is now eliminated
and her utilization has increased to 100 percent. Yet, workers 2 and 3 still have idle time:
                                                                                                           1
∙ The flow rate by now has increased to one scooter every 13 minutes or ​​ __                             13
                                                                                                              ​​unit per min-
                              1
  ute (equals ​​ __          13
                                 ​ × 60 × 35 = 161.5​ scooters per   week)          based on  worker   1.
∙ Worker 2 has a capacity of one scooter every 11 minutes, that is, ​​ 111                      __ ​​unit per minute. Her
                                                               1    1         11
  utilization is thus ​Flow rate / ​Capacity​  2​​  = ​  13 ​  ╱​  11 ​  = ​  13 ​  = 84.6%​.
                                                              __  __         __

∙ Worker 3 has a capacity of one scooter every 8 minutes. Her utilization is thus
  __ ​ ​  1
  ​  131          ​  138  ​ = 61.5%​.
         ╱__8 ​ = __
   Note that the increase in demand not only has increased the utilization levels across
workers (the average utilization is now ​​ 1__3 ​ × (100% + 84.6% + 61.5%) = 82%​), but also has
reduced the cost of direct labor to
                                             Total wages per unit of time
                    Cost of direct labor = _______________________
                                           ​    
                                                                         ​
                                              Flow rate per unit of time
                                                         Wages per week
                                  ​        = _______________________
                                                 ​   
                                                       ​
                                                   Scooters produced per week
                    ​​            ​ ​ 
                                         ​  ​ ​ 
                                                                               ​ ​ ​​
                                                   3 × $12 / hour × 35 hours/week
                                       ​   = _________________________
                                                  ​                           ​
                                                        161.5 scooters/  week
                                                      $1,260 /  week
                                  ​             = _________________
                                                  ​  
                                                      ​  = $7.80 / scooter
                                                   161.5 scooters/ week
   Now, back to the idea of line balancing. Line balancing attempts to evenly (fairly!)
allocate the amount of work that is required to build a scooter across the three process
steps.
   In an ideal scenario, we could just take the amount of work that goes into building a
scooter, which we referred to as the labor content (32 minutes/unit), and split it up evenly
between the three workers. Thus, we would achieve a perfect line balance if each worker
could take 32/3 minutes/unit; that is, each would have an identical processing time of 10.66
minutes/unit.
   Unfortunately, in most processes, it is not possible to divide up the work that evenly.
Specifically, the activities underlying a process typically consist of a collection of tasks
that cannot easily be broken up. A closer analysis of the three activities in our case reveals
the task structure shown in Table 4.2.
   For example, consider the last task of worker 1 (assemble handle cap), which takes
118 seconds per unit. These 118 seconds per unit of work can only be moved to another
worker in their entirety. Moreover, we cannot move this task around freely, as it obvi-
ously would not be feasible to move the “assemble handle cap” task to after the “seal
carton” task.
66 Chapter 4


TABLE 4.2         Worker           Tasks                                        Task Duration [seconds/unit]
Task Durations
                  Worker 1         Prepare cable                                                 30
                                   Move cable                                                    25
                                   Assemble washer                                              100
                                   Apply fork, threading cable end                               66
                                   Assemble socket head screws                                  114
                                   Steer pin nut                                                 49
                                   Brake shoe, spring, pivot bolt                                66
                                   Insert front wheel                                           100
                                   Insert axle bolt                                              30
                                   Tighten axle bolt                                             43
                                   Tighten brake pivot bolt                                      51
                                   Assemble handle cap                                          118
                                                                                         Total: 792
                  Worker 2         Assemble brake lever and cable                               110
                                   Trim and cap cable                                            59
                                   Place first rib                                               33
                                   Insert axles and cleats                                       96
                                   Insert rear wheel                                            135
                                   Place second rib and deck                                     84
                                   Apply grip tape                                               56
                                   Insert deck fasteners                                         75
                                                                                         Total: 648
                  Worker 3         Inspect and wipe off                                          95
                                   Apply decal and sticker                                       20
                                   Insert in bag                                                 43
                                   Assemble carton                                              114
                                   Insert Xootr and manual                                       94
                                   Seal carton                                                   84
                                                                                         Total: 450



                     However, we could move the 118 seconds per unit from worker 1 to worker 2. In this
                 case, worker 1 would now have a processing time of 674 seconds per unit and worker
                 2 (who would become the new bottleneck) would have a processing time of 766 seconds
                 per unit. The overall process capacity is increased, we would produce more scooters, and
                 the average labor utilization would move closer to 100 percent.
                     But can we do better? Within the scope of this book, we only consider cases where
                 the sequence of tasks is given. Line balancing becomes more complicated if we can rese-
                 quence some of the tasks. For example, there exists no technical reason why the second
                 to last task of worker 2 (apply grip tape) could not be switched with the subsequent task
                 (insert deck fasteners). There exist simple algorithms and heuristics that support line bal-
                 ancing in such more complex settings. Yet, their discussion would derail us from our focus
                 on managerial issues.
                     But even if we restrict ourselves to line balancing solutions that keep the sequence of
                 tasks unchanged, we can further improve upon the 766-second cycle time we outlined
                 above. Remember that the “gold standard” of line balancing, the even distribution of the
                 labor content across all resources, suggested a processing time of 10.66 minutes per unit,
                 or 640 seconds per unit.
                     Moving the “assemble handle cap” task from worker 1 to worker 2 was clearly a substan-
                 tial step in that direction. However, worker 2 has now 126 seconds per unit (766 seconds/
                 unit − 640 seconds/unit) more than what would be a balanced workload. This situation can
                                                                         Estimating and Reducing Labor Costs 67


            be improved if we take the worker’s last two tasks (apply grip tape, insert deck fasteners)
            and move the corresponding 56 + 75 seconds/unit = 131 seconds/unit to worker 3.
               The new processing times would be as follows:
            ∙ Worker 1: 674 seconds per unit (792 − 118 seconds/unit).
            ∙ Worker 2: 635 seconds per unit (648 + 118 − 56 − 75 seconds/unit).
            ∙ Worker 3: 581 seconds per unit (450 + 56 + 75 seconds/unit).
               Are they optimal? No! We can repeat similar calculations and further move work from
            worker 1 to worker 2 (tighten brake pivot bolt, 51 seconds per unit) and from worker 2 to
            worker 3 (place second rib and deck, 84 seconds per unit). The resulting (final) processing
            times are now
            ∙ Worker 1: 623 seconds per unit (674 − 51 seconds/unit).
            ∙ Worker 2: 602 seconds per unit (635 + 51 − 84 seconds/unit).
            ∙ Worker 3: 665 seconds per unit (581 + 84 seconds/unit).
               To make sure we have not “lost” any work on the way, we can add up the three new
            processing times and obtain the same labor content (1,890 seconds per unit) as before. The
            resulting labor utilization would be improved to
                   ​Average labor utilization = Labor content  /  ​(​​Labor content + Total idle time​)​​​
                    ​​                                                                           ​​​
                              ​                 = 1,890 / ​(​​1,890 + 42 + 63 + 0​)​​  = 94.7%​
               The process improvement we have implemented based on line balancing is sizeable
            in its economic impact. Based on the new bottleneck (worker 3), we see that we can pro-
                                                                                          1
            duce one Xootr every 665 seconds, thereby having a process capacity of ___​​ 665  ​​ units/second ×
            3,600 seconds/hour × 35 hours/week = 189.5 units per week. Thus, compared to the unbal-
            anced line (161.5 units per week), we have increased process capacity (and flow rate) by
            17 percent (28 units) without having increased our weekly spending rate on labor. More-
            over, we have reduced the cost of direct labor to $6.65/unit.
               Figure 4.5 summarizes the idea of line balancing by contrasting cycle time and task
            allocation of the unbalanced line (before) and the balanced line (after).



4.5 Scale Up to Higher Volume
            As indicated by Figure 4.2, demand for the Xootr increased dramatically within the next
            six months and, by July, had reached a level of 700 units per week. Thus, in order to main-
            tain a reasonable match between supply and demand, Novacruz had to increase its process
            capacity (supply) further.
               To increase process capacity for a worker-paced line, in this case from 189.5 units
            per week (see balanced line with three workers above) to 700 units per week, additional
            workers are needed. While the fundamental steps involved in building a Xootr remain
            unchanged, we have several options to lay out the new, high-volume process:
            ∙ Using the exact same layout and staffing plan, we could replicate the—now balanced—
              process and add another (and another, . . .) worker-paced line with three workers each.
            ∙ We could assign additional workers to the three process steps, which would increase the
              capacity of the steps and hence lead to a higher overall process capacity.
            ∙ We could divide up the work currently performed by three workers, thereby increasing
              the specialization of each step (and thus reducing processing times and hence increas-
              ing capacity).
68 Chapter 4


FIGURE 4.5                                                           Cycle Time before Line Balancing
Graphical                                           900                                                            1. Prepare Cable
Illustration of Line                                800                                                            2. Move Cable




                        Processing Time [Seconds]
Balance                                                         12       11                                        3. Assemble Washer
                                                    700
                                                          10                                                       4. Apply Fork, Threading Cable End
                                                    600                   9            20
                                                                                       19                          5. Assemble Socket Head Screws
                                                    500          8                     18                          6. Steer Pin Nut
                                                                 7                                   26            7. Brake Shoe, Spring, Pivot Bolt
                                                    400                                17
                                                                 6                                                 8. Insert Front Wheel
                                                    300                                              25
                                                                 5               15                                9. Insert Axle Bolt
                                                                                       16
                                                    200          4                             23    24           10. Tighten Axle Bolt
                                                                                       14                    22
                                                          2      3                                                11. Tighten Brake Pivot Bolt
                                                    100
                                                                             1         13            21           12. Assemble Handle and Cap
                                                      0                                                           13. Assemble Brake Lever and Cable
                                                               Step 1                 Step 2        Step 3        14. Trim and Cap Cable
                                                                                                                  15. Place First Rib
                                                                     Cycle Time after Line Balancing
                                                                                                                  16. Insert Axles and Cleats
                                                    900
                                                                                                                  17. Insert Rear Wheel
                                                    800                                                           18. Place Second Rib and Deck




                        Processing Time [Seconds]
                                                    700                                                           19. Apply Grip Tape
                                                          10
                                                                         9                           26           20. Insert Deck Fasteners
                                                    600
                                                                                       17            25           21. Inspect and Wipe Off
                                                    500          8                                                22. Apply Decal and Sticker
                                                                 7           15        16      23    24
                                                    400                                                      22   23. Insert in Bag
                                                           6
                                                                                       14                         24. Assemble Carton
                                                    300          5                                   21
                                                                                       13                         25. Insert Xootr and Manual
                                                    200          4                                   20           26. Seal Carton
                                                          2                            12            19
                                                    100          3
                                                                         1                           18
                                                                                       11
                                                      0
                                                               Step 1                 Step 2        Step 3


                          We will quickly go through the computations for all three approaches. The correspond-
                       ing process flow diagrams are summarized in Figure 4.6.

                       Increasing Capacity by Replicating the Line
                       As the capacity of the entire operation grows linearly with the number of replications,
                       we could simply add three replications of the process to obtain a new total capacity of
                       4 × 189.5 units/week = 758 units per week.
                          The advantage of this approach is that it would allow the organization to benefit from
                       the knowledge it has gathered from their initial process layout. The downside of this
                       approach is that it keeps the ratio of workers across the three process steps constant (in
                       total, four people do step 1, four at step 2, and four at step 3), while this might not neces-
                       sarily be the most efficient way of allocating workers to assembly tasks (it keeps the ratio
                       between workers at each step fixed).
                          Alternatively, we could just add two replications and obtain a process capacity of
                       568.5 units per week and make up for the remaining 131.5 units (700 − 568.5 units/week)
                       by adding overtime. Given that the 131.5 units to be produced in overtime would be spread
                       over three lines, each line would have to produce 131.53/3 = 43.84 units per week corre-
                       sponding to 8.1 hours of overtime per week (43.83 units/week/5.41 units/hour).
                          Under the assumption that we could use overtime, the average labor utilization would
                       remain unchanged at 94.7 percent.

                       Increasing Capacity by Selectively Adding Workers
                       While the first approach assumed the number of workers at each process step to be the same,
                       such a staffing might not necessarily be optimal. Specifically, we observe that (after the
                                                                                            Estimating and Reducing Labor Costs 69


FIGURE 4.6 Three Process Layouts for High-Volume Production

                                  Step 1                     Step 2                Step 3


         Components               Step 1                     Step 2                Step 3               Finished Xootrs


                                  Step 1                     Step 2                Step 3


                                  Step 1                     Step 2                Step 3


                        Four Identical Lines Using the Initial Process Layout, One Worker per Step

         Components              4 workers               4 workers              4 workers              Finished Xootrs

                                  Step 1                     Step 2                Step 3



      Components                                                                                            Finished Xootrs

                   1     2        3        4     5       6            7   8    9       10        11    12


                             One Line, One Worker per Step; Inventory between Steps Not Shown


                       rebalancing) the third step is the bottleneck (processing time of 665 seconds per unit). Thus,
                       we feel tempted to add over-proportionally more workers to this step than to the first two.
                          Given that we defined the capacity at each resource as the number of workers divided
                       by the corresponding processing time, we can write the following:
                                                                             Number of workers
                                                     ​Requested capacity = ​ ________________
                                                                                              ​​
                                                                                Activity time
                          For step 1, this calculation yields (700 units per week at 35 hours per week is 0.00555
                       unit per second):
                                                                           Number of workers
                                               ​0.00555 unit / second = ​ _________________
                                                                             ​​
                                                                           
                                                                          623 seconds per unit
                          Thus, the number of workers required to meet the current demand is 0.00555 × 623 =
                       3.46 workers. Given that we cannot hire half a worker (and ignoring overtime for the
                       moment), this means we have to hire four workers at step 1. In the same way, we find that
                       we need to hire 3.34 workers at step 2 and 3.69 workers at step 3.
                          The fact that we need to hire a total of four workers for each of the three steps reflects
                       the good balance that we have achieved above. If we would do a similar computation based
                       on the initial numbers (792,648,450 seconds /unit for workers 1, 2, and 3, respectively; see
                       Table 4.2), we would obtain the following:
                       ∙ At step 1, we would hire 0.00555 unit /second = Number of workers /792 seconds /unit;
                         therefore, Number of workers = 4.4.
                       ∙ At step 2, we would hire 0.00555 unit /second = Number of workers /648 seconds /unit;
                         therefore, Number of workers = 3.6.
                       ∙ At step 3, we would hire 0.00555 unit /second = Number of workers /450 seconds /unit;
                         therefore, Number of workers = 2.5.
70 Chapter 4


                  Thus, we observe that a staffing that allocates extra resources to activities with longer
               processing times (five workers for step 1 versus four for step 2 and three for step 3) pro-
               vides an alternative way of line balancing.
                  Note also that if we had just replicated the unbalanced line, we would have had to add
               four replications as opposed to the three replications of the balanced line (we need five
               times step 1). Thus, line balancing, which at the level of the individual worker might look
               like “hair-splitting,” debating about every second of worker time, at the aggregate level can
               achieve very substantial savings in direct labor cost.
                  At several places throughout the book, we will discuss the fundamental ideas of the
               Toyota Production System, of which line balancing is an important element. In the spirit
               of the Toyota Production System, idle time is considered as waste (muda) and therefore
               should be eliminated from the process to the extent possible.

               Increasing Capacity by Further Specializing Tasks
               Unlike the previous two approaches to increase capacity, the third approach fundamen-
               tally alters the way the individual tasks are assigned to workers. As we noted in our dis-
               cussion of line balancing, we can think of each activity as a set of individual tasks. Thus,
               if we increase the level of specialization of workers and now have each worker only be
               responsible for one or two tasks (as opposed to previously an activity consisting of 5 to
               10 tasks), we would be able to reduce processing time and thereby increase the capacity
               of the line.
                   Specifically, we begin our analysis by determining a targeted cycle time based on
               demand: in this case, we want to produce 700 units per week, which means 20 scooters per
               hour or 1 scooter every three minutes. How many workers does it take to produce 1 Xootr
               every three minutes?
                   The answer to this question is actually rather complicated. The reason for this complica-
               tion is as follows. We cannot compute the capacity of an individual worker without know-
               ing which tasks this worker will be in charge of. At the same time, we cannot assign tasks
               to workers, as we do not know how many workers we have.
                   To break this circularity, we start our analysis with the staffing we have obtained under
               the previous approaches, that is, 12 workers for the entire line. Table 4.3 shows how we can
               assign the tasks required to build a Xootr across these 12 workers.
                   Following this approach, the amount of work an individual worker needs to master
               is reduced to a maximum of 180 seconds. We refer to this number as the span of con-
               trol. Given that this span of control is much smaller than under the previous approaches
               (665 seconds), workers will be able to perform their tasks with significantly less training.
               Workers are also likely to improve upon their processing times more quickly as specializa-
               tion can increase the rate of learning.
                   The downside of this approach is its negative effect on labor utilization. Consider what
               has happened to labor utilization:
                                                                      Labor content
                               Average labor utilization = ​ ___________________________
                                                                ​
                                                              
                                                             Labor content + Sum of idle time
                       ​​                                                                     ​ ​     ​​​
                                                          1890
                            ___________________________________________
                         = ​   
                                  ​ = 87.5%
                            1,890 + 25 + 0 + 65 + 7 + 11 + 11 + 51 + 45 + 40 + 10 + 3 + 2
                  Note that average labor utilization was 94.7 percent (after balancing) with three work-
               ers. Thus, specialization (smaller spans of control) makes line balancing substantially more
               complicated. This is illustrated by Figure 4.7.
                  The reason for this decrease in labor utilization, and thus the poorer line balance, can be
               found in the granularity of the tasks. Since it is not possible to break up the individual tasks
               further, moving a task from one worker to the next becomes relatively more significant.
                                                                                Estimating and Reducing Labor Costs 71


TABLE 4.3              Worker               Tasks                                      Task Duration [seconds/unit]
Processing Times
                       Worker 1             Prepare cable                                               30
and Task Allocation
                                            Move cable                                                  25
under Increased
                                            Assemble washer                                            100
Specialization
                                                                                                Total: 155
                       Worker 2             Apply fork, threading cable end                             66
                                            Assemble socket head screws                                114
                                                                                                Total: 180
                       Worker 3             Steer pin nut                                               49
                                            Brake shoe, spring, pivot bolt                              66
                                                                                                Total: 115
                       Worker 4             Insert front wheel                                         100
                                            Insert axle bolt                                            30
                                            Tighten axle bolt                                           43
                                                                                                Total: 173
                       Worker 5             Tighten brake pivot bolt                                    51
                                            Assemble handle cap                                        118
                                                                                                Total: 169
                       Worker 6             Assemble brake lever and cable                             110
                                            Trim and cap cable                                          59
                                                                                                Total: 169
                       Worker 7             Place first rib                                             33
                                            Insert axles and cleats                                     96
                                                                                                Total: 129
                       Worker 8             Insert rear wheel                                          135
                                                                                                Total: 135
                       Worker 9             Place second rib and deck                                   84
                                            Apply grip tape                                             56
                                                                                                Total: 140
                       Worker 10            Insert deck fasteners                                       75
                                            Inspect and wipe off                                        95
                                                                                                Total: 170
                       Worker 11            Apply decal and sticker                                     20
                                            Insert in bag                                               43
                                            Assemble carton                                            114
                                                                                                Total: 177
                       Worker 12            Insert Xootr and manual                                     94
                                            Seal carton                                                 84
                                                                                                Total: 178
                                            Total labor content                                     1,890




                      For example, when we balanced the three-worker process, moving a 51-second-per-unit
                      task to another step accounted for just 8 percent of the step’s work (674 seconds per unit).
                      In a 12-step process, however, moving the same 51-second-per-unit task is now relative to
                      a 169-second-per-unit workload for the step, thereby accounting for 30 percent of work.
                      For this reason, it is difficult to further improve the allocation of tasks to workers relative
                      to what is shown in Figure 4.7.
                         The observation that line balancing becomes harder with an increase in specialization
                      can best be understood if we “turn this reasoning on its head”: line balancing becomes
                      easier with a decrease in specialization. To see this, consider the case of having one
72 Chapter 4


FIGURE 4.7                                            200
Line Balance in a
Highly Specialized                                    180
Line
(Different shades                                     160
represent different                                   140




                          Processing Time [Seconds]
tasks)
                                                      120

                                                      100

                                                       80

                                                       60

                                                       40

                                                       20

                                                        0
                                                            1   2   3    4   5   6     7      8      9     10   11   12
                                                                                 Worker




                         single worker do all the tasks in the process. The corresponding labor utilization would be
                         100 percent (assuming there is enough demand to keep at least one worker busy), as, by
                         definition, this one person also would be the bottleneck.
                            The idea of having one resource perform all activities of the process is referred to as
                         a work cell. The process flow diagram of a work cell is illustrated by Figure 4.8. Since
                         the processing time at a work cell with one worker is the same as the labor content, we
                                                                       1
                         would have a capacity per work cell of ​​ _____
                                                                     1,890
                                                                           ​​unit per second = 1.9048 units per hour,
                         or 66.67 units per week. Already 11 work cells would be able to fulfill the demand of
                         700 Xootrs per week. In other words, the improved balance that comes with a work cell
                         would allow us to further improve efficiency.
                            Again, the downside of this approach is that it requires one worker to master a span of
                         control of over 30 minutes, which requires a highly trained operator. Moreover, Novacruz
                         found that working with the 12-person line and the corresponding increase in specializa-
                         tion led to a substantial reduction in processing times.


FIGURE 4.8
Parallel Work Cells
                                                                    Step 1           Step 2                 Step 3
(Only three work cells
are shown)
                                  Components                                                                              Finished Xootrs
                                                                    Step 1           Step 2                 Step 3




                                                                    Step 1           Step 2                 Step 3


                                                                                                  Same Person
                                                                                           Estimating and Reducing Labor Costs 73



4.6                      In this chapter, we introduced the concept of line balancing. Line balancing attempts to
                         eliminate idle time from the process and thereby increase labor utilization. At first sight,
Summary                  line balancing seems to belong in the same category as “hair-splitting” and “penny-­
                         counting.” However, it is important to understand the managerial role that line balancing
                         plays in operations. Specifically, it is important to understand the following three manage-
                         rial benefits:
                         ∙ First of all, while it is always more tempting to talk about dollars rather than pennies,
                           pennies do matter in many industries. Consider, for example, the computer industry. All
                           PC manufacturers purchase from the same pool of suppliers of processors, disk drives,
                           optical devices, and so forth. Thus, while the $10 of labor cost in a computer might
                           seem small relative to the purchase price of the computer, those $10 are under our man-
                           agerial control, while most of the other costs are dictated by the market environment.
                         ∙ Second, in the spirit of the Toyota Production System (TPS), idle time is waste and
                           thereby constitutes what in TPS is known as muda. The problem with muda/idle time
                           is that it not only adds to the production costs, but has the potential to hide many other
                           problems. For example, a worker might use idle time to finish or rework a task that she
                           could not complete during the allocated processing time. While this does not lead to a
                           direct, out-of-pocket cost, it avoids the root cause of the problem, which, when it sur-
                           faces, can be fixed.
                         ∙ Third, while the $10 labor cost in the assembly operation of a PC manufacturer dis-
                           cussed above might seem like a low number, there is much more labor cost involved in
                           the PC than $10. What appears as procurement cost for the PC maker is to some extent
                           labor cost for the suppliers of the PC maker. If we “roll up” all operations throughout
                           the value chain leading to a PC, we find that the cost of labor is rather substantial.
                           This idea is illustrated in Figure 4.9 for the case of the automotive industry: while for
                           a company like an automotive company assembly labor costs seem to be only a small
                           element of costs, the 70 percent of costs that are procurement costs themselves include
                           assembly labor costs from suppliers, subsuppliers, and so forth. If we look at all costs
                           in the value chain (from an automotive company to their fifth-tier supplier), we see that
                           about a quarter of costs in the automotive supply chain are a result of labor costs. A
                           consequence of this observation is that it is not enough to improve our own operations


FIGURE 4.9                100%                                                                                     Other
Sources of Cost in the
                           90%                                                                                     Overhead
Supply Chain                                                                                                       Warranty
                           80%                                                                                     Quality
Source: Whitney 2004.
                           70%
                                                                                                                   Assembly
                           60%                                                                                     and Other
                           50%                                                                                     Labor Costs
                                               Purchased                Parts and
                           40%                 Parts and                Material
                                               Assemblies               Costs                                      Logistics Costs
                           30%
                           20%
                           10%                                                                                     Material Costs

                            0%
                                     Final                  Including               Including         Rolled-up
                                     Assembler's            Tier 1                  Tier 2            Costs Over
                                     Cost                   Costs                   Costs             ~ 5 Tiers
74 Chapter 4


                        internally, but to spread such improvements throughout the supplier network, as this
                        is where the biggest improvement opportunities are hidden. This concept of supplier
                        development is another fundamental concept of the Toyota Production System.
                         In addition to these three factors, line balancing also illustrates an important—and
                     from a managerial perspective very attractive—property of operations management. Line
                     balancing improves per-unit labor cost (productivity) and does not require any financial
                     investments in assets! To improve labor productivity, we would typically attempt to auto-
                     mate parts of the assembly, which would lower the per-unit labor cost, but at the same
                     time require a higher investment of capital. Such an approach would be most likely if we
                     operated in a high-wage location such as Germany or France. In contrast, we could try to
                     operate the process with little or no automation but have a lot of labor time invested in the
                     process. Such an approach would be more likely if we moved the process to a low-wage
                     location such as China, Indonesia, or Taiwan.
                         This tension is illustrated by Figure 4.10. The horizontal axis of Figure 4.10 shows the
                     return on the assets tied up in the manufacturing process. High returns are desirable, which
                     could be achieved by using little automation and a lot of labor. The vertical axis shows the
                     productivity of labor, which would be maximized if the process were highly automated. As
                     can be seen in Figure 4.10, there exists a tension (trade-off) between the dimensions, visi-
                     ble in the form of an efficient frontier. Thus, changes with respect to the level of automation
                     would move the process up or down the frontier. One dimension is traded against the other.
                         In contrast, the effect of line balancing in the context of Figure 4.10 is very different. Line
                     balancing improves labor productivity without any additional investment. To the extent that
                     line balancing allows the firm to eliminate some currently underutilized resources using
                     production equipment, line balancing also reduces the required assets. Thus, what from a
                     strategic perspective seems like a simple, one-dimensional positioning problem along the
                     technology frontier now has an additional dimension. Rather than simply taking the current
                     process as given and finding a good strategic position, the firm should attempt to improve
                     its process capability and improve along both performance dimensions simultaneously.

FIGURE 4.10
Trade-off between     Labor Productivity
                                                    Largely Automated Process
Labor Productivity                                  Likely to Be Operated in
                      (Xootrs per
and Capital                                         High-Wage Region
                      Employee)
Investment
                              High Labor                                             Improvement Because
                              Productivity                                           of Line Balancing



                                                                                              High-Capability
                                                                                  Trade-off   Frontier



                              Low Labor                                                       Largely Manual Process
                              Productivity                                                    Likely to Be Operated in
                                                                                              Low-Wage Region
                                                                 Low-Capability
                                                                 Frontier

                                                           Low                            High     Return on Assets
                                                                                                   (Sales per $ of
                                                                                                   Equipment)
                                                                           Estimating and Reducing Labor Costs 75


4.7        Bartholdi and Eisenstein (1996) develop the concept of a bucket brigade, which corresponds to a line
           operation that is self-balancing. In this concept, workers move between stations and follow relatively
Further    simple decision rules that determine which task should be performed next.
Reading        Whitney (2004) presents a systematic approach to design and production of mechanical assemblies.
           This book introduces mechanical and economic models of assemblies and assembly automation. The
           book takes a system view of assembly, including the notion of product architecture, feature-based
           design, computer models of assemblies, analysis of mechanical constraint, assembly sequence analysis,
           tolerances, system-level design for assembly and JIT methods, and economics of assembly automation.

4.8        The following questions will help in testing your understanding of this chapter. After each question,
           we show the relevant section in parentheses [Section x].
Practice      Solutions to problems marked with an “*” are available in Appendix E. Video solutions to select
Problems   problems are available in Connect.
           Q4.1*     (Empty System, Labor Utilization) Consider a process consisting of three resources in a
                     worker-paced line and a wage rate of $10 per hour. Assume there is unlimited demand for
                     the product.

                     Resource                  Processing time (minutes)                    Number of Workers

                        1                                  10                                        2
                        2                                    6                                       1
                        3                                  16                                        3

                     a. How long does it take the process to produce 100 units starting with an empty system? [4.2]
                     b. What is the average labor content? [4.3]
                     c. What is the average labor utilization? [4.3]
                     d. What is the cost of direct labor? [4.4]
           Q4.2      (Assign Tasks to Workers) Consider the following six tasks that must be assigned to four
                     workers on a conveyor-paced assembly line (i.e., a machine-paced line flow). Each worker
                     must perform at least one task.

                                                            Time to Complete Task (seconds)

                                      Task 1                             30
                                      Task 2                             25
                                      Task 3                             35
                                      Task 4                             40
                                      Task 5                             15
                                      Task 6                             30

                The current conveyor-paced assembly line configuration assigns the workers in the following way:
                   ∙ Worker 1: Task 1
                   ∙ Worker 2: Task 2
                   ∙ Worker 3: Tasks 3, 4
                   ∙ Worker 4: Tasks 5, 6
                   a. What is the capacity of the current line? [4.1]
                   b. Now assume that tasks are allocated to maximize capacity of the line, subject to the
                      conditions that (1) a worker can only perform two adjacent operations and (2) all tasks
                      need to be done in their numerical order. What is the capacity of this line now? [4.4]
                   c. Now assume that tasks are allocated to maximize capacity of the line and that tasks can
                      be performed in any order. What is the maximum capacity that can be achieved? [4.4]
           Q4.3    (PowerToys) PowerToys Inc. produces a small remote-controlled toy truck on a conveyor
                   belt with nine stations. Each station has, under the current process layout, one worker
                   assigned to it. Stations and processing times are summarized in the following table:
76 Chapter 4


                      Station           Task                                           Processing Times (seconds)
                         1              Mount battery units                                         75
                         2              Insert remote control receiver                              85
                         3              Insert chip                                                 90
                         4              Mount front axle                                            65
                         5              Mount back axle                                             70
                         6              Install electric motor                                      55
                         7              Connect motor to battery unit                               80
                         8              Connect motor to rear axle                                  65
                         9              Mount plastic body                                          80

                      a. What is the bottleneck in this process? [4.1]
                      b. What is the capacity, in toy trucks per hour, of the assembly line? [4.1]
                      c. What is the direct labor cost for the toy truck with the current process if each worker
                          receives $15/hour, expressed in dollars per toy truck? [4.4]
                      d. What would be the direct labor cost for the toy truck if work would be organized in
                          a work cell; that is, one worker performs all tasks? Assume that the processing times
                          would remain unchanged (i.e., there are no specialization gains). [4.5]
                      e. What is the utilization of the worker in station 2? [4.1]
                          Because of a drastically reduced forecast, the plant management has decided to cut
                      staffing from nine to six workers per shift. Assume that (i) the nine tasks in the preced-
                      ing table cannot be divided; (ii) the nine tasks are assigned to the six workers in the most
                      efficient way possible; and (iii) if one worker is in charge of two tasks, the tasks have to be
                      adjacent (i.e., one worker cannot work on tasks 1 and 3, unless the worker also does task 2).
                       f. How would you assign the nine tasks to the six workers? [4.4]
                      g. What is the new capacity of the line (in toy trucks per hour)? [4.4]
               Q4.4   (12 Tasks to 4 Workers) Consider the following tasks that must be assigned to four work-
                      ers on a conveyor-paced assembly line (i.e., a machine-paced line flow). Each worker must
                      perform at least one task. There is unlimited demand.

                                                                     Time to Complete
                                                                       Task (seconds)
                                                  Task 1                    30
                                                  Task 2                    25
                                                  Task 3                    15
                                                  Task 4                    20
                                                  Task 5                    15
                                                  Task 6                    20
                                                  Task 7                    50
                                                  Task 8                    15
                                                  Task 9                    20
                                                  Task 10                   25
                                                  Task 11                   15
                                                  Task 12                   20

                         The current conveyor-paced assembly-line configuration assigns the workers in the fol-
                      lowing way:
                      ∙ Worker 1: Tasks 1, 2, 3
                      ∙ Worker 2: Tasks 4, 5, 6
                      ∙ Worker 3: Tasks 7, 8, 9
                      ∙ Worker 4: Tasks 10, 11, 12

                                                                Estimating and Reducing Labor Costs 77


       a. What is the capacity of the current line? [4.1]
       b. What is the direct labor content? [4.3]
       c. What is the average labor utilization (do not consider any transient effects such as the
           line being emptied before breaks or shift changes)? [4.3]
       d. How long would it take to produce 100 units, starting with an empty system? [4.2]
           The firm is hiring a fifth worker. Assume that tasks are allocated to the five workers to
       maximize capacity of the line, subject to the conditions that (i) a worker can only perform
       adjacent operations and (ii) all tasks need to be done in their numerical order.
       e. What is the capacity of this line now? [4.4]
           Again, assume the firm has hired a fifth worker. Assume further that tasks are allocated
       to maximize capacity of the line and that tasks can be performed in any order.
        f. What is the maximum capacity that can be achieved? [4.4]
       g. What is the minimum number of workers that could produce at an hourly rate of
           72 units? Assume the tasks can be allocated to workers as described in the beginning
           (i.e., tasks cannot be done in any order). [4.4]
Q4.5   (Geneva Watch) The Geneva Watch Corporation manufactures watches on a conveyor
       belt with six stations. One worker stands at each station and performs the following tasks:

       Station                    Tasks                                   Processing Time (seconds)

       A: Preparation 1           Heat-stake lens to bezel                            14
                                  Inspect bezel                                       26
                                  Clean switch holes                                  10
                                  Install set switch in bezel                         18
                                    Total time for A                                  68
       B: Preparation 2           Check switch travel                                 23
                                  Clean inside bezel                                  12
                                  Install module in bezel                             25
                                    Total time for B                                  60
       C: Battery installation    Install battery clip on module                      20
                                  Heat-stake battery clip on module                   15
                                  Install 2 batteries in module                       22
                                  Check switch                                        13
                                    Total time for C                                  70
       D: Band installation       Install band                                        45
                                  Inspect band                                        13
                                    Total time for D                                  58
       E: Packaging preparation Cosmetic inspection                                   20
                                Final test                                            55
                                  Total time for E                                    75
       F: Watch packaging         Place watch and cuff in display box                 20
                                  Place cover in display box base                     14
                                  Place owner’s manual, box into tub                  30
                                    Total time for F                                  64


          These six workers begin their workday at 8:00 a.m. and work steadily until 4:00 p.m.
       At 4:00, no new watch parts are introduced into station A and the conveyor belt continues
       until all of the work-in-process inventory has been processed and leaves station F. Thus,
       each morning the workers begin with an empty system.
       a. What is the bottleneck in this process? [4.1]
       b. What is the capacity, in watches per hour, of the assembly line (ignore the time it takes
          for the first watch to come off the line)? [4.1]
78 Chapter 4


                      c. What is the direct labor content for the processes on this conveyor belt? [4.3]
                      d. What is the utilization of the worker in station B (ignore the time it takes for the first
                          watch to come off the line)? [4.1]
                      e. How many minutes of idle time will the worker in station C have in one hour (ignore
                          the time it takes for the first watch to come off the line)? [4.3]
                       f. What time will it be (within one minute) when the assembly line has processed
                          193 watches on any given day? [4.2]
               Q4.6   (Yoggo Soft Drink) A small, privately owned Asian company is producing a private-label
                      soft drink, Yoggo. A machine-paced line puts the soft drinks into plastic bottles and then
                      packages the bottles into boxes holding 10 bottles each. The machine-paced line is com-
                      prised of the following four steps: (1) the bottling machine takes 1 second to fill a bottle,
                      (2) the lid machine takes 3 seconds to cover the bottle with a lid, (3) a labeling machine
                      takes 5 seconds to apply a label to a bottle, and (4) the packaging machine takes 4 seconds
                      to place a bottle into a box. When a box has been filled with 10 bottles, a worker tending
                      the packaging machine removes the filled box and replaces it with an empty box. Assume
                      that the time for the worker to remove a filled box and replace it with an empty box is neg-
                      ligible and hence does not affect the capacity of the line. At step 3 there are two labeling
                      machines that each process alternating bottles; that is, the first machine processes bottles
                      1, 3, 5, . . . and the second machine processes bottles 2, 4, 6, . . . . Problem data are sum-
                      marized in the table following.



                      Process Step                      Number of Machines                    Seconds per Bottle

                      Bottling                                     1                                    1
                      Applying a lid                               1                                    3
                      Labeling                                     2                                    5
                      Packaging                                    1                                    4



                      a. What is the process capacity (bottles/hour) for the machine-paced line? [4.1]
                      b. What is the bottleneck in the process? [4.1]
                      c. If one more identical labeling machine is added to the process, how much is the increase
                          in the process capacity going to be (in terms of bottles/hour)? [4.1]
                      d. What is the implied utilization of the packaging machine if the demand rate is 60 boxes/
                          hour? Recall that a box consists of 10 bottles. [4.1]
               Q4.7   (Atlas Inc.) Atlas Inc. is a toy bicycle manufacturing company producing a five-inch small
                      version of the bike that Lance Armstrong rode to win his first Tour de France. The assem-
                      bly line at Atlas Inc. consists of seven work stations, each performing a single step. Sta-
                      tions and processing times are summarized here:
                      ∙ Step 1 (30 sec.): The plastic tube for the frame is cut to size.
                      ∙ Step 2 (20 sec.): The tube is put together.
                      ∙ Step 3 (35 sec.): The frame is glued together.
                      ∙ Step 4 (25 sec.): The frame is cleaned.
                      ∙ Step 5 (30 sec.): Paint is sprayed onto the frame.
                      ∙ Step 6 (45 sec.): Wheels are assembled.
                      ∙ Step 7 (40 sec.): All other parts are assembled to the frame.
                      Under the current process layout, workers are allocated to the stations as shown here:
                      ∙ Worker 1: Steps 1, 2
                      ∙ Worker 2: Steps 3, 4
                      ∙ Worker 3: Step 5
                                                              Estimating and Reducing Labor Costs 79


       ∙ Worker 4: Step 6
       ∙ Worker 5: Step 7
       a. What is the bottleneck in this process? [4.1]
       b. What is the capacity of this assembly line, in finished units/hour? [4.1]
       c. What is the utilization of Worker 4, ignoring the production of the first and last units? [4.1]
       d. How long does it take to finish production of 100 units, starting with an empty process? [4.2]
       e. What is the average labor utilization of the workers, ignoring the production of the first
           and last units? [4.3]
        f. Assume the workers are paid $15 per hour. What is the cost of direct labor for the
           bicycle? [4.4]
       g. Based on recommendations of a consultant, Atlas Inc. decides to reallocate the tasks
           among the workers to achieve maximum process capacity. Assume that if a worker is in
           charge of two tasks, then the tasks have to be adjacent to each other. Also, assume that
           the sequence of steps cannot be changed. What is the maximum possible capacity, in
           units per hour, that can be achieved by this reallocation? [4.4]
       h. Again, assume a wage rate of $15 per hour. What would be the cost of direct labor if
           one single worker would perform all seven steps? You can ignore benefits of specializa-
           tion, set-up times, or quality problems. [4.5]
        i. On account of a reduced demand forecast, management has decided to let go of one
           worker. If work is to be allocated among the four workers such that (i) the tasks can’t
           be divided, (ii) if one worker is in charge of two tasks, the tasks have to be adjacent,
           (iii) the tasks are assigned in the most efficient way and (iv) each step can only be
           carried out by one worker, what is the new capacity of the line (in finished units/
           hour)? [4.5]
Q4.8   (Glove Design Challenge) A manufacturer of women’s designer gloves has employed a
       team of students to redesign her manufacturing unit. They gathered the following informa-
       tion. The manufacturing process consists of four activities: (1) fabric cutting; (2) dyeing;
       (3) stitching, done by specially designed machines; and (4) packaging. Processing times
       are shown below. Gloves are moved between activities by a conveyor belt that paces the
       flow of work (machine-paced line).



       Process Step                     Number of Machines                         Minutes per Glove

       Cutting                                    1                                         2
       Dyeing                                     1                                         4
       Stitching                                  1                                         3
       Packaging                                  1                                         5




       a. What is the process capacity in gloves/hour? [4.1]
       b. Which one of the following statements is true? [4.1]
            i. The capacity of the process increases by reducing the dyeing time.
           ii. If stitching time increases to 5 minutes/glove, the capacity of the process remains
               unchanged, but “time through an empty machine-paced process” increases.
          iii. By reducing packaging time, the process capacity increases.
          iv. By reducing cutting time, the capacity of the process increases.
       c. What is the implied utilization of the packaging machine if the demand rate is 10
          gloves/hour? [4.1]
       d. What is the flow time for a glove? [4.1]
80 Chapter 4


               Q4.9     (Worker-Paced Line)



                        Process             Process              Process              Process              Process
                        Step 1              Step 2               Step 3               Step 4               Step 5

                          U1                  U2                   U3                   U4                   U5


                        The accompanying diagram depicts a five-step, worker-paced headphone manufacturing
                        plant. The headphones are meant to be used with iPods and DVD players. Step 1 involves
                        a worker bending a metal strip into an arc shape. In step 2, the metal arc is fitted with a
                        plastic sleeve. In step 3, the headphones are fitted at the end of the metal and plastic strips.
                        In step 4, the wires are soldered into the headphones. Step 5 involves a specially designed
                        packaging unit. After the plant has been operational for a couple of hours, the manager
                        inspects the plant. He is particularly interested in cutting labor costs. He observes the fol-
                        lowing. The process is capacity-constrained and the entire process produces 36 units in
                        one hour. U1 through U5 denote the utilization at steps 1 through 5 respectively. Currently,
                        there is a single worker at each step and the utilizations are as follows: U1 = 4/30, U2 =
                        4/15, U3 = 4/5, U4 = 1, U5 = 2/5.
                            Answer the following questions based on the given data and information.
                        a. What is the capacity of step 5? [4.1]
                        b. Which step is the bottleneck? [4.1]
                        c. Which process step has the highest capacity? [4.1]
                        d. If the wage rate is $36 per hour per person, what is the direct labor cost per unit? [4.4]

               If you would like to test your understanding of a specific section, here are the questions organized
               by section:
               Section 4.1: Q4.2a, Q4.3abe, Q4.4a, Q4.5abd, Q4.6, Q4.7abc, Q4.8, Q4.9abc
               Section 4.2: Q4.1a, Q4.4d, Q4.5f, Q4.7d
               Section 4.3: Q4.1bc, Q4.4bc, Q4.5ce, Q4.7e
               Section 4.4: Q4.1d, Q4.2bc, Q4.3cfg, Q4.4efg, Q4.7f, Q4.9d
               Section 4.5: Q4.3d, Q4.7hi
