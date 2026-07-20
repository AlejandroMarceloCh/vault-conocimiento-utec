---
curso: IO2
titulo: bbwh
slides: 22
fuente: bbwh.pdf
---

                   BUCKET BRIGADES
                A Self-Balancing Order-Picking
                   System for a Warehouse
           John J. Bartholdi, III  Donald D. Eisenstein y
                            August 1, 1996

                                        Abstract
          \Bucket brigades" are a new way of sharing work among pickers in a
      warehouse so that the statistics of the order stream elicit a spontaneous
      allocation of work to balance the e ort. The result is increased pick rates
      without conscious intention of the workers, without guidance from man-
      agement, without any model of work content, without any computation,
      indeed without any data-gathering at all.
          We implemented order-picking by bucket brigade in the warehouses of
      a major chain retailer, where, among other bene ts, pick rates increased
      more than 30%.
          We believe that bucket brigades can replace zone-picking as the stan-
      dard method of picking orders in high-volume retail trade.



      Key words: warehouse, order-picking, work-sharing, bucket brigade, zone-
      picking, self-organizing systems, dynamical systems



   School of Industrial and Systems Engineering, Georgia Institute of Technology, Atlanta,
Georgia 30332-0205 USA. E-mail: john.bartholdi@isye.gatech.edu
  y Graduate School of Business, The University of Chicago, Chicago, Illinois 60637 USA.
E-mail: don.eisenstein@gsb.uchicago.edu

                                            1
    \Bucket brigades" are a way of coordinating workers who are progressively
assembling product along a ow line. If the workers are stationed from slowest
to fastest along the line (with respect to the direction of product ow), then a
balanced allocation of work will spontaneously emerge.
    We analyzed this surprising phenomenon in the context of manufacturing
(Bartholdi and Eisenstein, 1996). Here we report on the translation of these
ideas to the warehouse, where we con rmed the e ectiveness of order-picking
by bucket brigade at the central distribution center of a major chain retailer, at
which we observed improvements that were immediate, substantial, and cost-
free.
    In the following we describe standard industry practice for order-picking,
how we replaced it at one site with bucket brigades, and what happened. Finally,
we explain the apparent superiority of bucket brigades.

1 Order-picking
In the stores of chain retailers, sales space for inventory is severely limited,
and so the warehouses supporting them replenish stock-keeping units (sku's )
frequently and in small, less-than-caseload amounts. This means that a typical
store orders many sku's, but small numbers of each. Picking these many sku's
in small amounts is very labor intensive.
    Under these circumstances, the preferred mode of storage in the warehouse
is generally ow rack, illustrated in Figure 1. Flow rack is arranged in aisles,
through which runs a unidirectional conveyor system. The racks are divided
into bays. Within each bay are shelves with rollers and the shelves are tilted to
bring the cases forward. Each sku in the ow rack is stored as a lane of cases
and individual items of each sku are picked from the forward-most case.
    An order is a list of sku's for a single customer together with quantities to
be picked. Paperwork describing orders to be picked waits at the start of the
aisle. Each order sheet lists the sku's (and amounts to pick) in the sequence in
which they will be encountered along the aisle.

                                        2
Figure 1: A team picking from an aisle of ow rack to a conveyor (from \Ware-
house Modernization and Layout Planning Guide", Department of the Navy,
Naval Supply Systems Command, NAVSUP Publication 529, March 1985, p
8-17). The \passive" conveyor (closer to the pickers) holds partially completed
orders. The powered \take-away" conveyor transports completed orders to the
shipping department.




                                      3
    Workers assemble each order progressively along the aisle, putting the sku's
into totes (cartons), which travel together. Workers keep the orders in sequence,
to avoid sorting at the shipping dock, where trucks are loaded in reverse order
of delivery.
    The aisles work in parallel to pick the orders of a common set of customers.
This means the aisles must periodically synchronize their completions to corre-
spond to the timed departure of a set of trucks. Otherwise the aisles operate
independently of each other.

2 Sequential Zone-picking
Because broken-case order-picking is so labor-intensive, managers naturally want
to keep all pickers busy. Standard practice is to attempt to balance the work
by partitioning the bays into contiguous sections called zones and then restrict-
ing each picker to work within her1 zone. The picker in the rst zone takes a
new order, opens a tote (box) and slides it along the passive lane of the con-
veyor as she moves down the aisle picking the sku's for that order. On reaching
the end of her zone, she leaves the order on the passive conveyor for the next
worker and returns to the beginning of her zone for more work. Each worker
remains in her zone, moving totes forward while picking, and is idle if there
are no orders waiting when she returns to the beginning of her zone. The last
picker pushes the totes of a completed order onto the take-away conveyor, which
takes them to the shipping department. The idea is that all workers will pre-
sumably remain busy if their zones have approximately the same total work.
This style of order-picking is called sequential zone-picking. (For more about
order-picking protocols, see \The warehouse manager's guide to e ective order
picking", Monograph M-8, Tompkins Associates, Inc., Raleigh, NC.)
    Zones are xed in advance of picking, based on some model of work content,
but in practice require constant readjustment to maintain balance. There are
three reasons for this.
  1   In our experience most pickers are female.

                                               4
    Zones usually span integral numbers of bays so that zone boundaries are
      easy for the pickers to recognize; but the work might be distributed in
      such a way that no division by bay produces a good balance.
    The model of work content is unavoidably inaccurate. There are more
      factors that determine work content than can be economically modeled:
      In addition to the number and locations of the sku's to be picked, work
      content is also determined by heights of the locations (at waist level or
      inconveniently high?), weight and shape of the sku's (heavy? hard to
      handle?), and so on. Moreover, such models cannot account for inevitable
      disruptions such as disposing of an empty case, opening a new case, sealing
      a full tote, pulling stalled cases to the front of the ow rack, and so on.
      Even more importantly, such models never, in our experience, account
      for the inherent di erences in the pick rates of individual workers, which
      typically range from 50% to 200% of work standard. It is not surprising
      that zones tend to underutilize the fastest workers, while frustrating the
      slower workers, who, under pressure to keep up, can introduce errors.
    Zones are static: They attempt to balance only the total work over, say,
      one day, but fail to maintain balance from order to order. The result is
      that every picker might accomplish the same total work at the end of the
      day; and yet no one have been fully utilized.
    Some facilities have tried to improve balance by recomputing zones several
times a day, and others have invested heavily to build more sophisticated models
of work content. Many more rms try to ignore the problem by assigning each
picker an identical number of contiguous bays of ow rack from which to pick,
which implicitly assumes that all pickers are identical and all bays will be picked
equally often (O'Brian, 1986, for example). None of these strategies overcome
the inherent ineciencies of zone-picking.
    In summary, zone-picking requires constant supervision to ameliorate un-
avoidable imbalance | and is imbalanced nonetheless. The cost of imbalance

                                        5
is reduced pick rates due to incompletely utilized pickers and due to work-in-
process, which interferes with picking.

3 Bucket brigade order-picking
We suggest that the pickers work as a bucket brigade : Each picker follows the
rule \Pick forward until someone takes over your work; then go back for more".
When the last picker completes an order, she pushes it onto the take-away
conveyor and then walks back to take over the order of her predecessor, who
in turn takes over the order of her predecessor, and so on until the rst picker
begins a new order.
    Workers are not restricted to zones, and so any worker can in principle pick
from any location. There are no bu ers, so the only work-in-process inventory
is that in the hands of the pickers.
    Pickers must maintain their sequence: No passing is allowed and so it can
happen that a picker is blocked by her successor, in which case we require that
she simply wait until she can resume picking, after her successor has moved out
of the way. (Thus there is at least the possibility of wasted pick capacity due
to blocking; later we shall show how to minimize this waste.)
    We further require that the pickers be sequenced from slowest-to-fastest, so
that the slowest picker is starting new orders and the fastest is nishing them.
Then, as we shall show, pickers will spontaneously migrate to where the work is.
The results will be increased pick rates, due to more e ective work-sharing, and
reduced management because the balanced allocation of work is spontaneous.
    The idea of spontaneous reallocation of work in a manufacturing environ-
ment has been explored by Bartholdi and Eisenstein (1996) and by Bartholdi,
Bunimovich, and Eisenstein (1995). Here we apply the essential ideas to ware-
housing, where we believe it has even greater potential. Some translation is
necessary, however, for the issues in warehousing are somewhat di erent than
in manufacturing. For example, a deterministic model of work was appropriate
for apparel manufacturing, where successive units of work are identical, while

                                       6
here the location and amount of work vary from order to order. Neverthe-
less, the general conclusions are similar: When properly con gured | that is,
when workers are sequenced from slowest-to-fastest and are carrying appropriate
amounts of work | a bucket brigade line will continuously and spontaneously
balance the work to improve throughput.
    We implemented order-picking by bucket brigade at a distribution center
that supports over two thousand stores of a major US chain retailer2. This has
subsequently been extended to additional, regional warehouses and now involves
several hundred pickers. Previously, all sites had used sequential zone-picking.
    One of the advantages of bucket brigades is that to implement them requires
no special equipment and no changes to a typical warehouse management sys-
tem. This made it easy to try one morning on a single pick-line. We described
the idea to the workers in fteen minutes, management sequenced the workers
from slowest-to-fastest, and within a half-hour they were picking comfortably.
    Another advantage of bucket brigades is that they are easy to adjust. This
made it easy to experiment with settings, such as \bucket size" (the number of
orders to be carried by each picker).

3.1 Bucket size
There are two opportunities for waste under bucket brigades: time lost when
one worker is blocked by, but forbidden to pass, her successor; and time spent
walking back to get more work. (There are similar opportunities for waste under
zone-picking: time lost when a picker is starved for work; and time spent walking
back to get more work at the beginning of a zone.) Our biggest design challenge
was to reduce this waste; and the natural way to do this is to increase the size
of the \bucket" (the number of orders carried by each worker). Larger buckets
mean fewer walk-backs to get work. Larger buckets also mean reduced variance
in the amount and location of work; and so there will be less opportunity for a
  2 Our client has requested anonymity to protect the competitive advantage a orded by
bucket brigades; in deference to their wishes we refer to them herein as X, Inc.


                                          7
faster but busy worker to block a slower one.
    However, if the bucket is too large, the conveyor can become congested with
totes. Then workers may nd their totes pushed downstream by those of their
predecessors and so they must walk to put sku's in the appropriate totes. This
walking reduces the e ective pick rate, and so throughput.
    We had, in advance, estimated by simulation an adequate bucket size, which
we then adjusted by experiment on the line. This was an easy adjustment
that required merely that the rst worker change the number of new orders
she introduced into the line. The most e ective bucket size depends on the
statistics of the order stream and will di er from site to site, but was in this
case four orders per worker.
    We brie y considered releasing a variable number of orders to better smooth
the work content per bucket; but this seemed unattractively complicated. For-
tunately, it proved unnecessary because we found a bucket size that eliminated
blocking without causing congestion.
    Under zone-picking, congestion had been a frequent problem due to spot im-
balances between zones; and this had been exacerbated by a policy of stationing
the fastest worker rst on the line, where she started as many new orders at one
time as she wished (sometimes up to fteen). In contrast, the bucket brigade
protocol strictly controls work-in-process, and so congestion, by linking the start
of new orders to the completion of previous orders. Furthermore, sequencing
the workers from slowest-to-fastest still allows the fastest worker to pace the
system, but by pulling work rather than by pushing it.

3.2 Results
The most striking bene t of order-picking by bucket brigade was the increase
in pick rates, which reached sustained levels over 30% greater than the previous
historical averages, while reducing management intervention (Figure 2). This
was achieved at essentially no cost, and in particular, with no change to the
product layout, equipment, or control system (except to render parts of the


                                        8
       pick rate
         1.3

         1.2

         1.1

                                                                     week
                     5       10      15       20       25       30

         0.9




Figure 2: Average pick rate as a fraction of the work-standard. Zone-picking
was replaced by bucket brigade in week 12. (The solid lines represent best ts
to weekly average pick rates before and after introduction of the bucket brigade
protocol.)

latter unnecessary).
    To determine whether the increased throughput is an artifact of our tin-
kering or represents a genuine improvement in technology, we simulated both
zone-picking and bucket brigade on the order stream of one aisle for a day and
compared their relative performances (Figure 3). Bucket brigade was clearly
superior, even though our simulation showed zone-picking at its most advanta-
geous. In real life, the greater work-in-process of zone-picking means congestion
and therefore both decreased pick rates and more opportunities to put sku's in
the wrong tote. This suggests that the observed increase in pick rates under
bucket brigade is real.
    Picking by bucket brigade produced additional bene ts, including the fol-
lowing.
    Spontaneous (re)balance of the work has freed management time. Previ-
     ously each aisle was monitored by a manager who adjusted zones within
     the aisle to correct the inevitable spot imbalances and the resulting conges-
     tion or starvation. This level of supervision is no longer necessary because

                                       9
         wip
         1
                          zone-picking

      0.8

      0.6
                          bucket brigade
      0.4

      0.2

         0                                                          time
                    0.2       0.4          0.6      0.8         1

Figure 3: The (normalized) work-in-process under simulated zone-picking and
under bucket brigade. Bucket brigade nished in 85% of the time required by
zone-picking and had only half the peak work-in-process.

     adjustments are spontaneous and continual.
     Furthermore, di erences in work rates are now visible and so it has be-
     come easier to recognize problems. For example, at X, Inc. each bay con-
     tains comparable amounts of work of each order and so, under the bucket
     brigade protocol, each worker tends to visit a length of aisle proportional
     to her pick rate. In one case, an unusually slow worker at the rst position
     was repeatedly \pushed back" by her faster teammates: She was unable
     to pick quickly enough ever to leave the rst bay of ow rack and so her
     teammates asked that she be removed. It was apparent to all that they
     could pick as fast without her and they preferred to split the incentive pay
     n , 1 ways. Under zone-picking such imbalances were harder to recognize
     because they could be hidden by work-in-process.
    The synchronization of multiple aisles has become easier. A manager can
     now monitor the progress of an aisle by simply checking what order any
     worker is picking. Under zone-picking it was dicult to know the status
     of an aisle because of the considerable and variable work-in-process.


                                      10
  It has also become easier to move workers to maintain the balance among
  aisles. Under zone-picking, when one picker was moved, work was inter-
  rupted while management rede ned the zones in each aisle; but under
  bucket brigades, the pickers in each aisle spontaneously adjust to account
  for the new con guration.
 A bucket brigade is extensible. For example, at X, Inc. there was a worker
  picking from carousels immediately upstream from one aisle; and she oc-
  casionally got ahead of the workers in that aisle. Under zone-picking she
  had to cease working until the congestion was cleared. Now she simply
  joins the bucket brigade to help them pick. After they have caught up,
  she returns to the carousels at the next walk-back.
 Reduced levels of work-in-process increased the accuracy of order-picking.
  Because the number of totes on the conveyor is strictly controlled, workers
  put sku's in the wrong totes less frequently.
 The pickers claim to be more satis ed because they prefer working in
  teams, with clear instructions about where to go and when. Furthermore,
  the simpli ed and regularized movements mean that temporary workers
  can become productive more quickly.
 The expense and inaccuracy of work content models is avoided. X, Inc. had
  calculated zones several times a day based on a sophisticated, computer-
  hosted model of work content. With bucket brigades, X, Inc. is able
  to forego this expense and still increase pick rates. Other sites in our
  experience use less sophisticated work-content models to determine zones
  and so we expect such sites to bene t still more from conversion to order-
  picking by bucket brigade.




                                   11
4 Special conditions
Warehouses vary enormously in their details, even within the same company.
Here we discuss some interesting special issues that arose at various sites.

4.1 Dynamic adjustment of bucket size
Under zone-picking pickers started and ended their day at staggered times be-
cause work was not simultaneously available for all. This complicated and ex-
tended the day for management. We found we could reduce the problem under
the bucket brigade protocol: At the start of the day the fastest worker begins
picking a single order from the very start of the aisle, followed by the next
worker picking a single order, and so on, until every worker is picking a single
order. Then, at each subsequent walk-back, the rst picker increases the number
of orders introduced, until reaching the standard bucket size.
    Similarly, workers changed the bucket size at the end of the day. For example,
in one aisle we had directed each worker to carry four orders. Initially this
caused a problem at the end of the day because the rst worker nished almost
an hour before the last worker. To simplify employee scheduling, management
introduced the following modi cation: When the rst worker begins picking
the nal four orders of the day, she signals the last worker; then at the next
walk-back the last worker takes over only two of the orders of her predecessor.
At each subsequent walk-back, any worker with only two orders takes only two
from her predecessor, until eventually everyone has exactly two orders. Then the
  rst and last pickers are separated by half the work content as when everyone
carried four orders, and so they will nish work within 30 minutes or so of each
other. The extra time for the rst workers is used to clean the work area and
prepare for the next day.




                                       12
4.2 Pick-to-light
X, Inc. had instrumented the ow rack in some aisles with a pick-to-light system,
by which a central computer turns on a lighted display at each storage location
to show exactly what and how many to pick from the next bay for a particular
order. This is intended to reduce search time and paper-handling; but it also
allows the bucket brigade protocol to work even more eciently: Because all the
locations to be picked within a bay are lighted at the same time, two workers
can pick simultaneously, side-by-side, on the same order. This helps the bucket
brigade protocol in two ways.
    It reduces time lost during hand-o s: During a walk-back each picker
     must take over the work of her predecessor; and because all the remaining
     picks in a bay are lighted simultaneously, both pickers can work side-by-
     side until the preempted picker reaches a convenient stopping point. Thus
     there is almost no time wasted in handing o work.
    It reduces time lost due to blocking. Because of variations in the amount
     and location of work among pickers there will occasionally be some block-
     ing. We reduced consequent waste by requiring that, whenever a worker
     is blocked, she temporarily abandon her own work to help the picker who
     is blocking her. (\If blocked, help your teammate get out of your way.")

4.3 Any picker can start a walk-back
Bucket brigades may be even more productive if the protocol is amended to
allow any picker who completes an order | not exclusively the last picker | to
push her order onto the take-away conveyor and go back to take over the work
of her predecessor. This avoids waste because no picker who has completed her
order will ever be forced to wait.
    Such a modi cation is useful at sites in which orders need not remain in
sequence and where picks for each order are not typically required along the
entire length of the pick ailse.

                                      13
    For instance, such a modi ed protocol is helpful at the national distribution
center of Blockbuster Music, where part of their picking operation is organized
so that workers push carts through one-way aisles of static shelving, which
contain sku's with a wide range of pick activity. The most active of these
sku's are concentrated in the rst ve of 23 aisles, so that many orders are
completed within the rst few aisles and are sent directly to shipping whenever
they have been lled. The operations manager reported an increase in pick rate
of over 50% within a day of changing from zone-picking to bucket brigade. An
additional bene t from bucket brigades at this site is that, because pickers are
not allowed to pass one another anyway, the aisles could be narrowed to the
width of a single cart. This reduced space requirements by almost half, which
reduced walking time and so further contributed to increased pick rates.

5 The e ectiveness of bucket brigades
To better understand where bucket brigades will be e ective, let us consider a
simple model in which the amount and location of work varies. This model is in-
tended to be tractable as well as representative, and so some of the assumptions,
especially one on the distribution of work, are more strict than is necessary for
bucket brigades to be e ective in real life.
    Let there be m discrete positions at which a worker may stand while picking.
These positions partition the sku's into m disjoint sets. For example, the posi-
tions might correspond to the bays of ow rack; or possibly, in a more detailed
representation, one foot intervals along the aisle.
Assumption 1 (Total ordering of positions) Positions can be numbered ac-
cording to their appearance in an a priori sequence j = 1; : : : ; m, so that, for
any given order, any picks from position j will be completed before any picks
from subsequent positions beyond j .

    Such an ordering is generally implicit in the layout (geometry) of storage and
direction of material ow. For example, when sku's are stored along an aisle

                                       14
that must be traversed, it is natural to pick them in the order in which they are
encountered. On the other hand, storage need not be restricted to a single aisle;
for example, our model applies (and bucket brigades are being used) where the
pickers walk through parallel aisles of shelves like shoppers in a grocery store.
    An order is a m-tuple, the j -th entry of which represents the amount of
standard work to pick from location j :
Assumption 2 (iid orders, exponentially distributed work) Orders are
independent and identically distributed random vectors, the components of which
are independent; and the j -th component, representing the standard work at
location j , follows an exponential distribution with common mean 1=.

    This assumption holds only approximately at X, Inc. Orders tend to be iden-
tically distributed because chain retail outlets experience the same seasonalities
and are served by a common marketing plan. Also, all the orders within a day
are generally destined for the same geographical region and therefore likely to
re ect common regional tastes. Orders tend to be independent because they
re ect the purchasing decisions of local customers, who presumably act inde-
pendently.
    Orders are to be picked by n pickers who can be ranked according to the
speed at which they work:
Assumption 3 (Total ordering of the workers by velocity) Each picker
i is characterized by a work velocity v , and so the time for picker i to complete
                                      i

a pick is exponentially distributed with mean 1=(v ).
                                                     i



    This assumption is uncontroversial for order-picking, where the pertinent
skills are simply dexterity and motivation. All the managers and workers we
interviewed agreed that such a ranking could be quickly agreed upon by any
pickers who had worked together. Indeed, it is typical in the industry that
order-pickers are evaluated in terms of their \pick rate".
    Finally, we assume that time spent walking is relatively small:


                                          15
Assumption 4 (Insigni cant walking time) The time to pick a typical or-
der is signi cantly greater than the time to walk the length of the aisle.

5.1 Spontaneous emergence of teamwork
Based on our model of work, we can describe the behavior of a bucket brigade
as a continuous-time Markov chain in which the state of the system is given by
a vector fx1; x2 ; : : : ; xn g, where xi 2 f1; 2; : : : ; mg gives the position of worker
i. This Markov chain is nite and all states communicate, so there is a unique
limiting distribution to which the system converges (Ross, 1989, for example).
Therefore, statistically predictable behavior will assert itself; and so we can
evaluate the e ectiveness of a bucket brigade line by measuring its production
rate.
    We claim that, under our model of work, a bucket brigade line will perform
at its best (that is, at its highest production rate) if the pickers are sequenced
from slowest-to-fastest along the direction of material ow. This makes intu-
itive sense, at least locally, because it reduces the probability of blocking. This,
however, is a local argument and says nothing about the evolution of the system
over time. Nevertheless, we have veri ed this claim for small lines, for which
the Markov equations for the limiting distribution can be solved easily. We
observed that the randomness of the orders does not qualitatively change the
dynamics of the bucket brigade from those of the deterministic model analyzed
by Bartholdi and Eisenstein (1996) and Bartholdi, Bunimovich, and Eisenstein
(1995). Asymptotic behavior remains recognizably the same, except that the
faithfulness of the reproduction depends on the variance of work among orders.
For example, in Figures 4 and 5 the limiting distributions are concentrated over
the stable (asymptotic) sets of the deterministic model (cf. Bartholdi, Buni-
movich, and Eisenstein, 1995). In Figure 4 the pickers are sequenced from
faster-to-slower. Here, the faster worker tends to stay close on the heels of the
slower worker, and thus hand-o s alternate between the start and end of the
line. In Figure 5 the pickers are sequenced from slower-to-faster, and hand-o s


                                           16
      frequency




                  1                                                     m
                         position after resetting

Figure 4: Faster-to-slower: Position of the second, slower, of two pickers imme-
diately after walk-back. In the deterministic model of work, the second picker
alternates between the rst and last positions (dashed vertical lines).

are concentrated where the pickers will be pre-positioned to share e ectively the
work of the next order.
    Now we can ask a theoretical question: How good is the production rate of
bucket brigades in an absolute sense? In other words, can we guarantee that
all pickers will always be busy? When work is probabilistic the answer is, of
course, no; but we can recognize what factors reduce blocking and so improve
the production rate.
    For example, the chance of blocking is reduced when there is a large di erence
in the velocities of adjacent pickers. Figure 6 shows the limiting behavior of a
two-picker line as the relative contribution of the last picker increases. More
precisely, the production capacity remains constant: v1 + v2 = 1 and  = m;
so the maximum production rate is 1 (the horizontal dashed line) while the
relative contribution v2 of the second picker changes. When the pickers are
sequenced from faster-to-slower (the leftmost region), the production rate falls
o rapidly as the relative contribution of the second picker decreases. However,

                                       17
                       frequency




                                   1
                                                 position after resetting

Figure 5: Slower-to-faster: Position of the second, faster, of two pickers imme-
diately after walk-back. In the deterministic model of work, the second picker
repeatedly returns to the position marked by the dashed vertical line.

                          1

                      0.8




    production rate
                      0.6

                      0.4

                      0.2

                                       faster-to-slower         slower-to-faster
                          0
                                   0       0.2       0.4        0.6     0.8
                                            velocity of second worker


Figure 6: The production rate increases with the contribution of the second
picker. Here, the velocity of the team remains constant, but the velocity of the
second picker increases from 0 to 100 percent of the total work velocity of the
team. Slowest-to-fastest is nearly optimal, despite variance in the work.

                                                           18
when the pickers are sequenced from slower-to-faster (the rightmost region), the
production rate is nearly unbeatable (no blocking), even when the second picker
is only a little faster than the rst picker. This suggests that a workforce should
be partitioned into bucket brigades so that each brigade contains a wide range
of work velocities. This is consistent with analysis of the deterministic model in
Bartholdi, Bunimovich, and Eisenstein (1995).
    Another way to reduce the chance of blocking and improve the production
rate is to reduce the variance of the work. As variance decreases, the behavior of
the bucket brigade approaches that of the deterministic model analyzed in The-
orem 3 of Bartholdi and Eisenstein (1996), in which the work is the same from
order to order and is distributed uniformly and continuously through space. For
this deterministic model the production rate converges to the highest possible
because all blocking eventually ceases. In practice one can reduce the variance,
as we did at X, Inc. , by increasing the bucket size (aggregating groups of four
orders for batch picking). The chance of blocking can also be reduced by re-
ducing the number of pickers, after which the team members will tend to be
separated by larger and so less variable amounts of work.
    The issues are more complicated when the intensity of work is allowed to vary
among locations, so that work is no longer uniform. Bartholdi and Eisenstein
(1996) show that when work is pathologically concentrated it can happen that
blocking is endemic to bucket brigades. However, this is highly unlikely in
practice because any extraordinarily busy items are generally picked separately,
such as from oor storage on the shipping dock. In fact, our experience suggests
that bucket brigades are e ective even in the presence of rather severe variations
in work intensity among locations.

6 Conclusions
We believe that bucket brigades are more productive than zone-picking for two
reasons: First, bucket brigades constantly and spontaneously seek balance; and
second, balance is based on actual, realized work content and not mere estimates

                                       19
of work content. Furthermore, the bucket brigades can achieve high production
rate without resorting to high work-in-process because they absorb variance
in the work by allowing the pickers to move to where the work is. Of course
the strongest | and incontrovertible | evidence for the e ectiveness of bucket
brigades is experience in a commercial warehouse, such as we have reported.
    The main bene ts of order-picking by bucket brigade are increased pick
rates and simpli ed management, including freedom from work-content models.
These bene ts were so substantial at X, Inc. that other, initial concerns, such
as whether brigade members might shirk or free-ride, were dismissed as second
order e ects at best. There are thousands of warehouses, particularly those
supporting high-volume retail sales, that could enjoy the same bene ts we report
here.
    Our work may be seen to lie within two current streams of thought. Most
immediately, it is a special case of dynamic line-balancing, wherein an intelli-
gent controller adjusts the allocation of work in real time (for example, Ostolaza,
Thomas, and McClain, 1990). For bucket brigades the allocation occurs spon-
taneously, which has the considerable advantage of requiring no controller at
all! (In fact, our biggest problem in implementing bucket brigades has been
to persuade workers that their ad hoc local \improvements" are generally not
improvements at all and only interrupt the emergence of balance. We learned
to insist on strict observance of the bucket brigade protocol3.)
    The second stream of thought into which our work ts is the hosting of
computational processes on analogue devices. In our case the order-picking
system is the computer of its own allocation of work. It might be said that we
program this computer by sequencing the workers from slowest-to-fastest. There
is no need to measure and input data because it is already encoded directly in
the \hardware". The output is the balance.
   3For which, incidentally, the metaphor of \bucket brigade", with its vivid sense of urgency,
provides an e ective training aid.




                                              20

Acknowledgments
We thank the many people who contributed to the success of this project, in-
cluding Dave Cole, Jim Rollins, Joe Jernigan, Ron Kelly, and especially Victor
Lee and Pam Hinkle. We also thank Dave Wolfe of TransTech Consulting, Inc.
for sharing his considerable experience and insights in order-picking; and we
thank Leonid Bunimovich and Bob Foley for helpful technical discussions.
    We are grateful for the hospitality of Big B, Blockbuster Music, Eckerd's
Drugs, Fel-Pro, McMaster-Carr, Rank Video Services America, Revco Drug
Stores, Inc., and Superclub Music.
    We appreciate the support of the National Science Foundation through
grants #DDM-9215564 (Bartholdi and Eisenstein); the Air Force Oce of Sci-
enti c Research through grant #F49620-94-1-0232 (Bartholdi); the Oce of
Naval Research through grant #N00014-89-J-1571 (Bartholdi); and the Gradu-
ate School of Business at the University of Chicago (Eisenstein).
    Portions of this paper have been presented at Cornell University (October
1993); Northwestern University (February 1994); the University of Michigan
(March 1994); the Wharton School of the University of Pennsylvania (March
1995); MIT (March 1996); the University of Chicago (May 1996); and the na-
tional meeting of the Warehousing Educational and Research Council (May
1996). We thank the audiences for many stimulating questions.

References
[1] J. J. Bartholdi, III, L. A. Bunimovich, and D. D. Eisenstein. \Dy-
    namics of 2- and 3-worker `bucket brigade' production lines", submitted
    (1995).
[2] J. J. Bartholdi, III and D. D. Eisenstein. \A production line that
    balances itself", Operations Research 44(1) (1996).



                                     21
[3] J. W. O'Brian. \Pharmaceutical distribution improved order picking",
    Proceedings of the 1986 Fall Industrial Engineering Conference, Institute
    of Industrial Engineers, pp 476{480.
[4] S. M. Ross. Introduction to Probability Models, Academic Press (1989).
[5] J. Ostolaza, J. O. McClain, and L. J. Thomas. \The use of dynamic
    (state-dependent) assembly-line balancing to improve throughput", Journal
    of Manufacturing and Operations Management 3:105{133 (1990).




                                     22
