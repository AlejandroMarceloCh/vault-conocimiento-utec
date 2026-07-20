---
curso: LIDSI
titulo: 05 - Semana 3/2024_0701_CemexScalingAI_WixomSomehBeath
slides: 4
fuente: 05 - Semana 3/2024_0701_CemexScalingAI_WixomSomehBeath.pdf
---

                                                                       RESEARCH BRIEFING | VOLUME XXIV, NUMBER 7, JULY 2024


                                        ACHIEVING AI AT SCALE:
                                        CEMEX'S LEARNING JOURNEY
                                        Barbara H. Wixom, Principal Research Scientist
                                        MIT Center for Information Systems Research (CISR)
                                        Ida A. Someh, Senior Lecturer in Business Information Systems
                                        UQ Business School at The University of Queensland, Australia
                                        Cynthia M. Beath, Professor Emerita
                                        University of Texas, Austin


Recently, large established organizations have been growing                   Ideally, organizations establish the three facilitating elements
business value by increasing the volume of AI models they                     as part of their scaling AI learning journey. Table 1 summariz-
have in production, an activity we call scaling AI.1 For the                  es how organizations can build data liquidity, develop work-
past five years, MIT CISR researchers have followed more                      force savviness, and leverage scarce resources as they learn
than fifty data monetization initiatives that have relied on                  how to deploy, proliferate, and industrialize AI models. Some
machine learning to recognize patterns, draw inferences, and                  organizations establish these elements sequentially, while in
predict outcomes and thereby inform the scaling AI process.2                  other cases they establish them concurrently. Regardless of
                                                                              the order of their learning journey, organizations must estab-
In our research, we observed that scaling AI is the result of
                                                                              lish all three facilitating elements to achieve AI at scale.
a learning journey during which organizations learn how to
generate value from AI models across the AI lifecycle. This                   In this briefing, we describe scaling AI at Cemex, one of our
lifecycle encompasses three phases: deploying AI models,                      research sites. We focus on key practices that helped leaders
proliferating AI models, and industrializing AI models.                       at Cemex establish the elements to facilitate scaling AI and
                                                                              advance the company’s learning journey, and we share Ce-
A key finding from the research is that scaling AI without
                                                                              mex’s rewards for achieving AI at scale.
breaking the bank requires three facilitating elements:
• Highly liquid enterprise data assets: data assets that have                 SCALING AI AT CEMEX
  been prepared and are widely available for easy reuse and
                                                                              Cemex SAB de CV (Cemex)3 is a $15.6 billion global construc-
  recombination in value creation using AI
                                                                              tion materials company headquartered near Monterrey,
• An AI-savvy workforce: employees who can effectively par-                   Mexico. A decade ago, CEO Fernando A. González introduced
  ticipate in the AI lifecycle and cultivate AI solutions                     a strategic emphasis on delivering superior customer service
• Prudent use of scarce and costly AI resources: the ability to               and directed investments to support a customer-focused dig-
  economize on data science capabilities, tools, and expertise                ital transformation. In 2017, the company launched Cemex
                                                                              Go, the first end-to-end digital platform enabling the custom-
Organizations must establish these elements to arrive at AI at
                                                                              er journey in the construction materials industry.
scale, which we define as the state at which an organization
cost effectively manages large volumes of interconnected
                                                                              Learning to Deploy AI Models
models in production. The rewards for operating in this state
are inspiring: maximized AI returns, AI-fueled business en-                   In 2017, Cemex established a global center of excellence
ablement, and AI-fueled competitive moves.                                    for data science called Global Data Science (GDS) to devel-
                                                                              op standard, scalable AI solutions for Cemex. Initially, GDS
                                                                              data scientists developed AI use cases as individual projects,
1 Scaling AI is described in B.H. Wixom and C.M. Beath, “Pega: Driving Cus-   collaborating in cross-functional teams with business domain
  tomer Engagement Using AI-Enabled Decision Making,” MIT CISR Working        experts to select data sources, prepare project data, choose
  Paper No. 449, June 2021, https://cisr.mit.edu/publication/MIT_CISR-        algorithms, engineer features, train models, and validate
  wp449_PegaAIDecisionMaking_WixomBeath.
                                                                              results. Once a model was on track for deployment, GDS
2 This research draws on a Q1 to Q2 2019 asynchronous discussion about
  AI-related challenges with fifty-three data executives from the MIT
  CISR Data Research Advisory Board; more than one hundred structured
  interviews with AI professionals regarding fifty-two AI projects from Q3    3 This briefing case draws from I. A. Someh, B. H. Wixom, C. M. Beath, and
  2019 to Q2 2020; an October 2021 survey of the fifty-two AI project           R. W. Gregory, “The Cemex Journey to AI at Scale,” MIT CISR Working
  teams; and eleven AI project narratives published by MIT CISR between         Paper No. 463, July 2024, https://cisr.mit.edu/publication/MIT_CISR-
  2017 and 2024.                                                                wp463_CemexAIatScale_SomehWixomBeathGregory.


© 2024 MIT Center for Information Systems Research, Wixom, Someh, and Beath. MIT CISR Research Briefings are published monthly
  to update the center’s members on current research projects.                                                                          Mir
                                                                                                                                        MANAGEMENT
                                                                                                                                            SLOAN SCHOOL
2 | MIT CISR Research Briefing, Vol. XXIV, No. 7, July 2024



worked with Cemex’s Information Technology (IT) function                areas cleaned and mastered data from core systems, establish-
to assemble a scrum team to ready the model for integration             ing a data catalog to help people search for data assets they
with existing process-enabling software and begin change                could trust. IT established a cloud-based central data lake;
management activities.                                                  an enterprise portal that authorized employees could use to
                                                                        access a data view, use a business intelligence tool, or tap into
As GDS’s development teams and end users interacted with
                                                                        an API; and temporary online experimentation spaces.
the AI solutions, they asked an ever-growing number of ques-
tions about how and why the AI model produced its results.              Cemex encouraged and captured data science use case ideas
To explain the AI model and help people trust it, GDS created           via the company’s formal employee innovation program
what became known as the Magic Tools: a suite of visualiza-             as well as from IT, GDS, and the Cemex data science com-
tions and what-if simulations that shed light on model me-              munity at large. When the number of data science ideas
chanics and outcomes. The Magic Tools analyzed data going               mushroomed, leaders introduced a portfolio management
into and coming out of an AI solution. The analyses allowed             framework they called the Speed to Value framework to
users, managers, deployment teams, and technical support                assess the potential of novel use cases and make efficient
people to identify for themselves the root causes of AI model           use of model development resources. A wide range of ideas
problems they encountered, track model usage, and make                  went into an innovation funnel, and when a use case proved
model change recommendations.                                           to have global potential, it was assigned to GDS for global
                                                                        deployment. In these cases, GDS had to adapt core models
During this phase of Cemex’s learning journey, GDS involved
                                                                        and retrain them using local data; different countries often
business domain collaborators in creating data assets for
                                                                        operated using different business rules, requiring changes to
model training and in the evaluation of AI models, providing
                                                                        the AI model itself, its software context, or how it was used.
critical feedback to the data scientists. The process of model
                                                                        GDS began developing “super models” with parameters that
building helped the business understand AI and trust AI
                                                                        could be turned on and off to accommodate the needs of
model results. Some of the helpful new trust-building and AI
                                                                        many local areas.
model deployment practices that emerged were baked into
the self-service Magic Tools. This period of learning led to a          When the Speed to Value framework identified good ideas
wave of enthusiasm at Cemex about AI model usage.                       with only local potential, those use cases were assigned to
                                                                        leaders of the responsible business area for further develop-
Learning to Proliferate AI Models                                       ment, with significant support from IT and GDS. For example,
To leverage rising employee interest in AI, IT offered the data,        GDS began hosting data science communities of practice and
platforms, standards, governance, and training needed for AI            offering advisory services, and an IT planning group helped
model development. IT and data owners in Cemex’s business               teams establish metrics for tracking model value.


 Table 1: Outcomes of Establishing Facilitating Elements During the AI Scaling Journey

                  Learning to deploy           Learning to proliferate       Learning to industrialize     AI at Scale
                  AI models                    AI models                     AI models

 Data Assets      Evolve from source data      Evolve to shared              Evolve to highly liquid       Enterprise data assets
                  to project data assets       enterprise data assets        data assets                   with high data liquidity

 Workforce        Evolve from data             Evolve to citizen data        Evolve to an empowered        An AI-savvy workforce
                  scientists with AI           scientists and AI             AI-savvy workforce that
                  expertise to project         communities of                deploys, uses, and
                  teams with AI expertise      practice                      sustains AI models

 AI Resources     Evolve from bespoke AI       Evolve to shared              Evolve to AI work that        Prudent use of scarce
                  techniques to practices      enterprise capabilities       leverages machines and        and costly AI resources
                  of repeatable routines                                     non-data scientists
                                                                              MIT CISR Research Briefing, Vol. XXIV, No. 7, July 2024 | 3



During this phase, employees across the enterprise partic-                 powered, AI-savvy workforce in AI model management and
ipated in AI model building. Cemex encouraged pervasive                    to highly efficient use of data science expertise.
participation by making shared resources available for global
and local teams. As a result, model reuse opportunities grew,              Managing AI at Scale at Cemex
and new AI models flourished. Many people participated in                  Today Cemex Go incorporates a collection of AI solutions,
project teams, innovation forums, and data science commu-                  some of which are interdependent—for example, a demand
nities of practice. This period of learning led to an explosion            forecasting model informs an overbooking model, the over-
at Cemex of AI models at various stages of deployment.                     booking model influences an order confirmation model, and
                                                                           a plant scheduling model relies on the order confirmation
Learning to Industrialize AI Models                                        model results. The company’s globally scaled AI solutions
Cemex leaders used the term “industrializing” to refer to the              account for an estimated value of $30 million from a variety
work involved in globally deploying AI models as well as that              of efficiencies, such as reduced truck distances traveled, im-
required for setting up processes for monitoring, supporting,              proved order availability, and lower energy consumption.
and managing these models. Managing hundreds of indus-
                                                                           Up to 2022, Cemex primarily used AI solutions to enable
trialized AI models over time, in the face of change, was not
                                                                           an outstanding customer experience and to streamline
simple. Initially, GDS manually monitored model health for
                                                                           operations. After making significant headway in this regard,
drift and degradation of performance, to determine when
                                                                           Cemex leaders saw tremendous opportunities in leverag-
models needed to be reparameterized or retrained using
                                                                           ing the company’s digital capabilities, particularly in data
new data. As the number of AI models grew, this proved to
                                                                           science, beyond enterprise boundaries. For example, in
be an overly resource-intensive task, and GDS leaders turned
                                                                           mid-2022, Cemex launched a company called Arkik to sell
to automating data science work.
                                                                           the proprietary IT solution Cemex created for use by its
In 2022, GDS kicked off an internal project to implement                   Ready Mix businesses to competing ready-mix businesses in
MLOps4 practices. Fully embracing the MLOps platform                       the form of software-as-a-service.
functionality allowed GDS to reduce the time to deploy
models from weeks or months to hours or days. Leveraging                   SCALING AI WITHOUT BREAKING THE BANK
the company’s prepared and accessible data, data scientists                Achieving AI at scale means your organization is using AI for
used MLOps tools to compare team-developed models to                       business enablement efficiently and that it is positioned to
models the platform suggested and to retrain models for                    pursue new competitive opportunities. The key is for leaders
new cities or markets.                                                     to establish data liquidity, workforce AI savviness, and the
IT installed and managed an MLOps platform as a part of                    ability to leverage scarce resources as their organization
its infrastructure management responsibilities. GDS had a                  masters the AI lifecycle.
separate team that took on the bulk of AI model produc-                    The Cemex story suggests ways to keep AI learning journeys
tion support, escalating problems to GDS’s data scientists                 on track. First, leaders can surface novel practices that AI
only when absolutely necessary. Using the MLOps tools for                  teams have invented to build trusted models, inventory
data scientists’ tasks freed up those experts for other, more              them, understand why they help teams, and promote those
valuable activities.                                                       that help move AI use cases from idea to solution faster,
During this phase, Cemex was exploiting a sophisticated ca-                cheaper, and better. Second, leaders can get ready for model
pability to deploy, scale, and sustain interconnected AI mod-              proliferation by investing in data literacy and making AI ex-
els across the globe. When possible, the company automated                 pertise, processes, and technologies accessible to employees
routine tasks, such as drift management, offered self-service              throughout the organization. Connecting people to shared
access to resources, and increasingly made use of MLOps                    resources empowers them to exploit AI. Finally, leaders can
tool functionality. Such activities improved data assets to                look for ways to make the best use of their available data
become more comprehensive and standardized, and they                       science expertise. As the number of AI models grows, models
increased shared enterprise data asset usage. This period of               become interconnected, and change happens too fast for
learning led both to broader participation by Cemex’s em-                  manual model management to keep up. At that point, orga-
                                                                           nizations must leverage automation and focus the attention
4 MLOps (Machine Learning Operations) refers to the overall process of     of their data science experts on the highest-priority work.
  building AI models using machine learning and managing those models in
  production environments over time.
MIT CENTER FOR INFORMATION SYSTEMS RESEARCH (CISR)
MIT CISR helps executives meet the challenge of leading increasingly digital and data-driven organizations. We provide
insights on how organizations effectively realize value from approaches such as digital business transformation, data
monetization, business ecosystems, and the digital workplace. Founded in 1974 and grounded in MIT’s tradition of
combining academic knowledge and practical purpose, we work directly with digital leaders, executives, and boards to
develop our insights. Our consortium forms a global community that comprises more than seventy-five organizations.




CISR RESEARCH PATRONS            Cemex (Mexico)                   Nomura Research Institute,        Uniting (Australia)




                                                                                                                                   Information as of July 2024
                                 Cencora                          Ltd. Systems Consulting           USAA
AlixPartners                                                      Division (Japan)
Avanade                          Cochlear Limited (Australia)                                       Webster Bank, N.A.
                                                                  Novo Nordisk A/S (Denmark)
Cognizant                        Commonwealth                                                       Westpac Banking Corporation
                                 Superannuation Corp.             OCP Group                         (Australia)
Collibra                         (Australia)                      Pacific Life Insurance            WestRock Company
IFS                              Cuscal Limited (Australia)       Company
                                                                                                    Wolters Kluwer
                                 CVS Health                       Posten Bring AS (Norway)
Pegasystems Inc.                                                                                    Xenco Medical
                                 Dawn Foods                       Principal Life Insurance
The Ogilvy Group                                                  Company                           Zoetis Services LLC
                                 DBS Bank Ltd. (Singapore)
CISR SPONSORS                                                     QBE
                                 Doosan Corporation (Korea)                                         CISR ASSOCIATE MEMBERS
                                                                  Ramsay Health Care
Alcon Vision                     Fidelity Investments             (Australia)                       MIT CISR wishes to thank all
Amcor                            Fomento Economico                                                  of our associate members
                                                                  Raytheon Technologies
ANZ Banking Group                Mexicano, S.A.B., de C.V.                                          for their support and
                                                                  Reserve Bank of Austrailia        contributions.
(Australia)                      Fortum (Finland)
                                                                  Scentre Group Limited
AustralianSuper                  Genentech                        (Australia)
Banco Bradesco S.A. (Brazil)     Gilbane Building Company         Schneider Electric Industries
Banco do Brasil S.A.             Johnson & Johnson (J&J)          SAS (France)
Bank of Queensland               Kaiser Permanente                Stockland (Australia)
(Australia)                                                       TabCorp Holdings (Australia)
                                 King & Wood Mallesons
Barclays (UK)                    (Australia)                      Telstra Limited (Australia)
BlueScope Steel (Australia)      Koç Holding (Turkey)             Terumo Corporation (Japan)
BNP Paribas (France)             Mercer                           Tetra Pak (Sweden)
Bupa (Australia)                 Nasdaq, Inc.                     Truist Financial Corporation
CarMax                           NN Insurance Eurasia NV          UniSuper Management Pty
Caterpillar, Inc.                Nomura Holdings, Inc. (Japan)    Ltd (Australia)




 MIT CISR is funded by our members, and we gratefully acknowledge their financial support and their many contributions
 to our work.
 Membership and benefits: cisr.mit.edu/content/member-benefits
 MIT CISR research publications: cisr.mit.edu/research-library


                     MIT Sloan School of Management               Team | Isobela Byerly-Chapman, Margherita Di Pinto,
                     Center for Information Systems Research      Christine G. Foglia Associate Director,
                                                                  Dorothea Gray-Papastathis, Cheryl A. Miller,
                     245 First Street, E94-15th Floor             Ina M. Sebastian, Alan Thorogood, Nick van der Meulen,
                     Cambridge, MA 02142                          Austin Van Groningen Engagement Director,
                     t 617-253-2348 | e cisr@mit.edu              Peter Weill Chairman, Barbara H. Wixom,
                                                                  Stephanie L. Woerner Director
                     cisr.mit.edu |   00
