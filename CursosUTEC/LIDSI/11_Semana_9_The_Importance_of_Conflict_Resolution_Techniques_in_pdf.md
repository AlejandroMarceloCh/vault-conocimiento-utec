---
curso: LIDSI
titulo: 11 - Semana 9/The Importance of Conflict Resolution Techniques in
slides: 4
fuente: 11 - Semana 9/The Importance of Conflict Resolution Techniques in.pdf
---

                                                         The Importance of Conflict Resolution Techniques in
                                                                     Autonomous Agile Teams
                                                                                                              Lucas Gren and Per Lenberg
                                                                                  Chalmers University of Technology and The University of Gothenburg
                                                                                        The Department of Computer Science and Engineering
                                                                                                     Gothenburg, Sweden 412–92
                                                                                               lucas.gren@cse.gu.se|perle@chalmers.se

                                        ABSTRACT                                                                                        more and more shared over time, and many groups do not reach the
                                        Today, software companies usually organize their work in teams.                                 more mature stages but get instead stuck for a variety of reasons




arXiv:1904.06285v1 [cs.SE] 5 Apr 2019
                                        Social science research on team development has shown that for                                  [25]. The group developmental theories state that, when humans
                                        a team to reach a productive and autonomous stage, it has to be                                 organize in small groups to achieve a set of common goals, we go
                                        able to manage internal conflicts and disagreements efficiently.                                through a specific set of stages and the group members behave
                                        To better facilitate the team development process, we argue that                                differently across these stages [13].
                                        software engineers needs additional training in negotiation skills                                 Research on development of small groups agrees on that a pe-
                                        and conflict resolution. In this position paper, we outline ideas for                           riod of disagreement and conflict is necessary to reach the better
                                        what aspects to consider in such training. As an example, we argue                              functioning mature stages [13]. People in groups need to challenge
                                        that a majority of the conflicts originate from team-level factors and                          one another to figure out the group members’ real competences
                                        that they, therefore, should be managed on the team-level instead                               and, also, set the group norms, i.e., the rules of the game [24]. This
                                        of in relation to dyads.                                                                        implies that some conflict stage is needed for most teams in or-
                                                                                                                                        der to later be more effective, and teams need to create a practical
                                        CCS CONCEPTS                                                                                    conflict management approach specific for every single constella-
                                                                                                                                        tion of people. Having efficient conflict resolution techniques in
                                        •Software and its engineering → Programming teams; Soft-
                                                                                                                                        agile teams are thus a prerequisite for building a well functioning
                                        ware development process management;
                                                                                                                                        autonomous team. Therefore, conflict resolution needs to be con-
                                                                                                                                        ducted on team level, which has also been shown in the software
                                        KEYWORDS
                                                                                                                                        engineering context in a study by Ocker [18]. They showed that
                                        agile teams; interpersonal conflict resolution; autonomous teams                                the group development maturity was positively connected to the
                                        ACM Reference format:                                                                           quality of work output, and the degree of satisfaction.
                                        Lucas Gren and Per Lenberg. 2018. The Importance of Conflict Resolution                            In this short paper, we first outline research on work-related
                                        Techniques in Autonomous Agile Teams. In Proceedings of XP ’18 Companion,                       conflicts from the information systems and software engineering
                                        Porto, Portugal, May 21–25, 2018, 4 pages.                                                      domain. We then present guidelines taken from conflict resolution
                                        DOI: 10.1145/3234152.3234185                                                                    research and, finally, we discuss potential gains in the software
                                                                                                                                        engineering autonomous teams’ context and suggest future work.
                                        1     INTRODUCTION
                                        The introduction of the agile methods has shifted the focus from                                2    INTERPERSONAL CONFLICT AND
                                        the individual software developer and instead highlighted team,                                      SOFTWARE ENGINEERING RESEARCH
                                        collaboration, and communication [3]. In software engineering                                   Traditionally, psychology researchers divide conflicts into the three
                                        organizations today, well-functioning teams are considered a criti-                             types (relation, process, and task) based on their content. Still, these
                                        cal success factor [12]. A natural consequence, or a byproduct, of                              types are not well-defined and their link to performance not fully
                                        increased collaboration is interpersonal conflict [11].                                         understood [2]. As an example, relationship conflicts have been
                                           To obtain well-functioning and autonomous teams, a set of group                              shown to affect both task-based and social aspects of team perfor-
                                        psychological factors has to be in place. Self-organization of teams                            mance negatively [16]. Therefore, there seem to be indications of
                                        has been shown to surface naturally only in the more mature stages                              more complex relationships between conflict types than presented
                                        of group development, which also implies that the leadership gets                               by, for example, Domino et al. [5] within the software development
                                                                                                                                        domain.
                                        Permission to make digital or hard copies of all or part of this work for personal or
                                        classroom use is granted without fee provided that copies are not made or distributed               A conflict can, in its broader sense, be defined as “the process
                                        for profit or commercial advantage and that copies bear this notice and the full citation       which begins when one party perceives that another has frustrated,
                                        on the first page. Copyrights for components of this work owned by others than the              or is about to frustrate, some concern of hers or his” [22]. Therefore,
                                        author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
                                        republish, to post on servers or to redistribute to lists, requires prior specific permission   a conflict has nothing to do with raising one’s voice of fighting, even
                                        and/or a fee. Request permissions from permissions@acm.org.                                     if that is the practical interpretation of the word in some languages,
                                        XP ’18 Companion, Porto, Portugal                                                               like Swedish.
                                        © 2018 Copyright held by the owner/author(s). Publication rights licensed to ACM.
                                        978-1-4503-6422-5/18/05. . . $15.00                                                                 Information system (IS) researchers have also conducted stud-
                                        DOI: 10.1145/3234152.3234185                                                                    ies related to conflict. In a study from 2001, Barki and Hartwick
XP ’18 Companion, May 21–25, 2018, Porto, Portugal                                                                Lucas Gren and Per Lenberg


[1] showed that interpersonal conflict consisting of disagreement,       known to trigger aggressive or unwilling responses in conflict
interference, and negative emotion had less of an impact on the          situations [10, 23]:
project outcomes when the teams had well-functioning conflict                    • One perspective — To see the problem only from your
management [1]. Similar results were obtained in that same year                     perspective.
by Sawyer [20].                                                                  • Poor communication — To stop listening/understanding.
    The research on conflict in software engineering is scarce, which            • Only binary options — Think “right or wrong;” there’s only
might indicate the difficulty of such inquiries. Among the older                    one way, and that’s my way.
studies is the work by Gobeli et al. [9] where they show that dys-               • Correspondence bias — It’s not just the concrete issue that
functional conflict management approaches have adverse effects on                   is the problem, it’s the person.
results. In a study on requirements specification, interpersonal con-            • Add new information — Bringing up new information not
flicts were shown to link directly to requirements diversity, which                 know to the other party.
was negatively associated to project performance [15]. Furthermore,              • Manipulation — Withholding information, talk behind peo-
a study by Gren [11] showed that interpersonal conflict was ad-                     ple’s backs.
versely connected to the agile team practices Iterative Development              • Hurting purposefully — Finding personal weak spots and
and Customer Access.                                                                attacking.
    Together, these mentioned studies further motivate the need for              • Ignoring social rules — Stop saying hello, ignore, and ex-
proper conflict resolution in agile teams. Therefore, in the following              clude from mailing lists.
sections, we will present techniques for how software organizations      If successfully avoiding the above mentioned mistakes, and instead
can raise the knowledge of having to manage interpersonal conflict       recognizing other people’s perspectives and referring to one’s own
efficiently.                                                             role in the conflict, trigger much more willingness to find agreeable
                                                                         solutions:
3   INTRA- AND INTER-GROUP CONFLICT                                              • I-message (not iMessage) — Meaning that arguments are
Interpersonal conflict manifests itself often i dyadic relations. A                 more effective if they refer to the person talking instead
work- or relationship-related conflict needs to be verbally expressed               of the person referring to a set of people or groups not
by one person at the time and most often directed to another indi-                  present. Conflict should also be resolved, as a first step, in
vidual. However, this does not mean that the conflict is isolated to                private using face-to-face communication.
the individuals expressing it [23]. In fact conflicts are seen to be             • Speak about what you want yourself, not what the other
between two parties, be it in individuals, groups or nations [19].                  one “should” want. Describe your problem with the other
   Intra-team conflicts, we argue, need a structure to be managed                   person’s action/behavior and not personality. Listen to the
at an early point in time, since conflicts are known to escalate,                   other person and show that you understand the content
and sometimes quite severely over time [19]. Therefore, teams                       of what the person is saying. One way of easily achieving
are helped by discussing early conflicts continuously before they                   this is to verbally interpret what the other person just said,
become infected and personal. However, if a conflict has escalated,                 e.g. “if I understand you correctly you mean that…”
there are expensive knowledge on how to behave in order to solve                 • Define the problem as a mutual, narrow and specific prob-
conflicts fast depending on personal stake, rhetoric, etc. Even is                  lem.
the section below focuses on individuals they techniques can be                  • Describe your feelings connected to the problem (sad, an-
extended to any two parties [19].                                                   gry, frustrated, disrespected etc.)
                                                                                 • Exchange motives to your positions, what’s behind your
4   ESCALATED INTERPERSONAL CONFLICT                                                different views? What needs to be fulfilled? Listen to each
                                                                                    others’ perspectives.
In this section, we summarize the content from a number of practi-
                                                                                 • Identify possibilities for mutual benefit by providing many
cal handbooks on conflict management, since we want to provide
                                                                                    possible solutions, and chose one wisely [23].
hands-on tips of how to reason around conflict. It is intended as an
introduction to conflict management in practice. For an extensive            A clearer step-by-step protocol might be the following:
review of conflict resolution research, we recommend Coleman                     • A: Now (What’s the present situation? This is what I/we/
et al. [4] that includes almost a thousand pages and hundreds of                    they do now)
references to academic papers. We would, again, like to highlight                • B: Desired end result (This is how I want it. I/we/they
that the conflict resolution needs to be on team-level since they are               should do like this).
a prerequisite for getting a team to mature over time.                           • C: Obstacles (Why A instead of B?).
   There is a diversity of situations that potentially can lead to               • C1: Do we know about the obstacles?
interpersonal team conflict. For example competing needs, fight-                 • C2: Are the obstacles possible to remove?
ing about scarce resources, misunderstandings, unclear situations,               • C3: Can we remove the obstacles?
different views on roles or divisions, different values, norms or                • C4: Do we want to remove the obstacles?
understandings, communication problems, competition/rivalry, or-                 • D: Actions (Suggestions/changes) [23].
ganizational change, and stress [4, 23].                                     It is important to recognize that different approaches are needed
   Having high emotional intelligence is a very useful for successful    depending on how infected the conflicts are. One significant inter-
conflict management. Below is a list of common mistakes that are         vention when conflicts are more complicated is to use a mediator
The Importance of Conflict Resolution Techniques in Autonomous Agile Teams               XP ’18 Companion, May 21–25, 2018, Porto, Portugal


[17]. In the agile software development context, the process facili-     human interaction efficient. A core aspect of such interactions is
tator (i.e., the Scrum Master in Scrum) would be ideal to take on        the ability to manage conflict well. In order to build efficient and
such a role when needed. Gren et al. [12] also showed that Scrum         autonomous teams in software organizations, having a formal struc-
Masters often do manage teams in such a way in practice. We rec-         ture for conflict resolution would undoubtedly be helpful. Research
ognize that such behavior is not considered to be “pure Scrum,” but      conducted in the information system (IS) domain has shown that
argue for the usefulness of having a formal protocol for how agile       making employees aware of how conflicts work has positive effects
teams should manage conflict step-by-step in software development        [1].
organizations.                                                              To increase awareness and to raise software organizations’ gen-
    It is also important to acknowledge that employees have dis-         eral understanding of interpersonal conflicts, we suggest that soft-
parate interests in different conflicts. A well-used model of such       ware engineering education should include negotiation and conflict
stance in conflicts was suggested by Thomas [22], and is shown           resolution training [21]. Since software engineers tend to con-
in Figure 1. Depending on the assertiveness and cooperativeness          duct their work in small groups, we suggest that such training
in each conflict a person will approach the conflict mainly in five      should emphasize the group aspects, i.e., interpersonal conflict in
different ways (although people tend to resort to some of them more      autonomous agile teams should be seen a group-level problem and
than others). With low assertiveness, i.e., focus on own needs, and      not as a dyadic problem. We believe a majority of conflicts are
low cooperativeness the person will avoid the conflict and maintain      not due to individual factors but instead team-related contextual
their neutrality in relation to the conflict. With high assertiveness    factors such as poor communication, unclear role, or undefined
and low cooperativeness the person participated by having a zero-        goals. These dissimilarities can, therefore, not be resolved through
sum orientation and assumes that one has to win and the other            addressing the individuals involved only, but should instead be
has to lose. With high cooperativeness but low assertiveness, the        managed on a team-level.
person maintain harmony and accede to the other party. With an              As mentioned in the previous section, organizations need to
intermediate level on both assertiveness and cooperativeness, the        provide agile teams with a well-defined process of how to manage
person will compromise and try to find solutions acceptable to all       team conflict in the organization, and the Scrum Master role might
parties, which also maintains the relationship undamaged. With           be appropriate for facilitating this process. If such guidelines are
high levels of both assertiveness and cooperativeness, the person        not in place, it will be cumbersome to trust team with the authority
will collaborate, meaning that the person will try to expand the         they need to set directions for new products.
range of possible outcomes and achieve win/win outcomes, which
also challenges the relationship more.                                   6    CONCLUSIONS AND FUTURE WORK
    There is also a range of cognitive biases that might create con-
                                                                         In this position paper, we emphasize the importance of consider-
flict that could be avoided (for more examples of such cognitive
                                                                         ing conflicts in software organizations. Social science research on
biases see, e.g., Evans [6]). The literature on cognitive and biases
                                                                         group dynamics and team development have repeatedly shown
is vast, and we will only mention one of them in this paper. The
                                                                         that for a team to reach a productive stage it has to, in an efficient
one we have chosen that we believe have a significant impact on
                                                                         way, be able to manage internal conflicts and disagreements. To
conflict resolution is the correspondence bias already mentioned in
                                                                         increase the software engineering general knowledge on how to
the list above about common mistakes in conflict situations. This
                                                                         handle disagreements within a team, we also suggest that software
bias is known by many names and was first called the fundamental
                                                                         engineering education should include negotiation and conflict res-
attribution error. This error is about people’s tendency to place an
                                                                         olution training. In this papers, we have provided initial ideas for
undue emphasis on internal characteristics to explain the behav-
                                                                         what aspects to consider in such training. As an example, we argue
ior of someone else in a given situation, rather than considering
                                                                         that a majority of the conflicts originate from group-related factors
external factors, i.e., the tendency to believe that peoplefis actions
                                                                         and that they, therefore, should be managed using a team-level
reflect who they are [8]. Therefore, when observing an inappropri-
                                                                         approach.
ate behavior, it is critical to take into account and recognize the
situational factors, i.e., not only resort to individual factors, such
as personality, to explain the behavior (see Coleman et al. [4] pp.      REFERENCES
502). This further motivates avoiding to turn team-level problems         [1] Henri Barki and Jon Hartwick. 2001. Interpersonal conflict and its management
                                                                              in information system development. MIS Quarterly (2001), 195–228.
into personal ones.                                                       [2] Kristin J Behfar, Randall S Peterson, Elizabeth A Mannix, and William MK
                                                                              Trochim. 2008. The critical role of conflict resolution in teams: A close look
                                                                              at the links between conflict type, conflict management strategies, and team
                                                                              outcomes. Journal of applied psychology 93, 1 (2008), 170.
5   DISCUSSION                                                            [3] Alistair Cockburn and Jim Highsmith. 2001. Agile software development: The
The human factors are increasingly being recognized by software               people factor. IEEE Computer 11 (2001), 131–133.
                                                                          [4] Peter T. Coleman, Morton Deutsch, and Eric C. Marcus. 2014. The Handbook
engineering researchers and practitioners alike [14]. The psycho-             of Conflict Resolution: Theory and Practice (3rd ed.). John Wiley & Sons, San
logical and sociological aspects have been presented as the missing           Francisco, California.
                                                                          [5] Madeline Ann Domino, Rosann Webb Collins, Alan R Hevner, and Cynthia F
piece in software engineering education [26]. Such approaches to              Cohen. 2003. Conflict in collaborative software development. In Proceedings of
training already exist in other fields and can directly be applied to         the 2003 SIGMIS conference on Computer personnel research. ACM, 44–51.
the software engineering context (see e.g., Shell [21]).                  [6] Jonathan St. B. T. Evans. 1989. Bias in human reasoning: Causes and consequences.
                                                                              Erlbaum, London.
   In the agile manifesto [7], the value “Individuals and interactions    [7] M. Fowler and J. Highsmith. 2001. The Agile Manifesto. In Software Development,
over processes and tools” emphasizes the importance of making                 Issue on Agile Methodologies, last accessed on December 29th, 2006. (Aug. 2001).
           AGILEITYCORRGDQ                                                                                                                                                                Lucas Gren




XP ’18 Companion, May 21–25, 2018, Porto, Portugal                                                                                                Lucas Gren and Per Lenberg


                                 Assertiveness                       Competing                                               Collaborating
                             Focus on my needs, desired
                                                               - Zero-sum orientation                              - Expand range of possible outcomes
                               outcomes and agenda
                                                               - Win/lose power struggle                           - Achieve win/win outcomes




                                                                                               Compromising
                                                                                          - Minimally acceptable to all
                                                                                          - Relationships undamaged




                                                                         Avoiding                                         Accomodating
                                                               - Withdraw from the situation                       - Accede to the other party
                                                               - Maintain neutrality                               - Maintain harmony


                                                                                                                               Cooperativeness
                                                                                                                             Focus on others' needs and
                                                                                                                                mutual relationships



                                         Figure 1: The Thomas-Kilmann Conflict Modes (adopted from [22]).


 [8] Bertram Gawronski. 2004. Theory-based bias correction in dispositional infer-                [26] L. Yu. 2014. Overcoming Challenges in Software Engineering Education: Delivering
     ence: The fundamental attribution error is dead, long live the correspondence                     Non-Technical Knowledge and Skills. IGI Global, Hershey, Pennsylvania.
     bias. European review of social psychology 15, 1 (2004), 183–217.
 [9] David H Gobeli, Harold F Koenig, and Iris Bechinger. 1998. Managing conflict in
     software development teams: A multilevel analysis. Journal of Product Innovation
     Management 15, 5 (1998), 423–435.
[10] Daniel Goleman. 1998. Working with emotional intelligence. Bantam Books, New
     York.
[11] Lucas Gren. 2017. The Links Between Agile Practices, Interpersonal Conflict,
     and Perceived Productivity. In Proceedings of the 21st International Conference on
     Evaluation and Assessment in Software Engineering. ACM, 292–297.
[12] L Gren, R Torkar, and R Feldt. 2017. Group development and group maturity
     when building agile teams: A qualitative and quantitative investigation at eight
     large companies. The Journal of Systems and Software 124 (2017), 104fi!?–119.
     DOI:http://dx.doi.org/10.1016/j.jss.2016.11.024
[13] Steve WJ Kozlowski and Daniel R Ilgen. 2006. Enhancing the effectiveness of
     work groups and teams. Psychological science in the public interest 7, 3 (2006),
     77–124.
[14] Per Lenberg, Robert Feldt, and Lars Göran Wallgren. 2015. Behavioral software
     engineering: A definition and systematic literature review. Journal of Systems
     and software 107 (2015), 15–37.
[15] Julie Yu-Chih Liu, Hun-Gee Chen, Charlie C Chen, and Tsong Shin Sheu. 2011.
     Relationships among interpersonal conflict, requirements uncertainty, and soft-
     ware project performance. International Journal of Project Management 29, 5
     (2011), 547–556.
[16] Brian Manata. 2016. Exploring the association between relationship conflict and
     group performance. Group Dynamics: Theory, Research, and Practice 20, 2 (2016),
     93–104.
[17] Christopher W. Moore. 2003. The mediation process: Practical strategies for
     resolving conflict (3rd ed.). Jossey-Bass, San Francisco, California.
[18] Rosalie J Ocker. 2001. The relationship between interaction, group development,
     and outcome: A study of virtual communication. In Proceedings of the 34th Annual
     Hawaii International Conference on System Sciences. IEEE, 1–10.
[19] Dean G Pruitt. 1969. Stability and sudden change in interpersonal and interna-
     tional affairs. Journal of Conflict Resolution 13, 1 (1969), 18–38.
[20] Steve Sawyer. 2001. Effects of intra-group conflict on packaged software devel-
     opment team performance. Information Systems Journal 11, 2 (2001), 155–178.
[21] G Richard Shell. 2001. Teaching Ideas: Bargaining Styles and Negotiation: The
     Thomas-Kilmann Conflict Mode Instrument in Negotiation Training. Negotiation
     Journal 17, 2 (2001), 155–174.
[22] Kenneth W Thomas. 1992. Conflict and conflict management: Reflections and
     update. Journal of organizational behavior 13, 3 (1992), 265–274.
[23] James A Wall Jr and Ronda Roberts Callister. 1995. Conflict and its management.
     Journal of management 21, 3 (1995), 515–558.
[24] S Wheelan. 2005. Group processes: A developmental perspective (2 ed.). Allyn and
     Bacon, Boston.
[25] Susan Wheelan, Barbara Davidson, and Felice Tilin. 2003. Group Development
     Across Time: Reality or Illusion? Small group research 34, 2 (2003), 223–245.
