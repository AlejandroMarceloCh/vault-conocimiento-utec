---
curso: LIDSI
titulo: 18 - Semana 16/2024_0901_GenAI_VanderMeulenWixom
slides: 4
fuente: 18 - Semana 16/2024_0901_GenAI_VanderMeulenWixom.pdf
---

                                                                RESEARCH BRIEFING | VOLUME XXIV, NUMBER 9, SEPTEMBER 2024



                                              MANAGING THE TWO FACES
                                              OF GENERATIVE AI
                                              Nick van der Meulen, Research Scientist
                                              Barbara H. Wixom, Principal Research Scientist
                                              MIT Center for Information Systems Research (CISR)




Over the past eighteen months, generative artificial intelli-                      GENERATIVE AI TOOLS
gence (GenAI) has grabbed the attention of organizational
                                                                                   GenAI tools are broadly applicable by design. They include
leaders. The technology’s ability to quickly and autonomous-
                                                                                   conversational AI systems (e.g., OpenAI’s ChatGPT) and
ly generate media content such as text, images, and audio
                                                                                   digital assistants embedded in existing productivity software
has unlocked opportunities that were previously too costly or
                                                                                   (e.g. Adobe’s Acrobat AI Assistant). Versatile and multi-
complicated for organizations to pursue. For example, GenAI
                                                                                   purpose, their use is generally not predefined, but instead
can help legal teams check whether lengthy contracts meet
                                                                                   identified and refined by users. To date, these tools primarily
regulatory standards, support learning professionals in adapt-
                                                                                   enhance users’ personal productivity, aiding them in tasks
ing training materials to new languages, and assist marketers
                                                                                   such as summarizing documents, brainstorming ideas, and
by hyperpersonalizing customer engagement to vary timing,
                                                                                   writing first drafts of emails. One executive in our study aptly
channel, and message.
                                                                                   referred to the benefit of such uses as “productivity shaves,”
Unlike traditional AI, which focuses on making predictions or                      saving users a few minutes of effort with each task.
classifications based on specific datasets, GenAI uses neural net-
                                                                                   The use of GenAI tools, however, poses four key challenges
work architectures—such as large language models (LLMs)—to
                                                                                   to organizations:
identify patterns in extensive training data and generate outputs
that mirror those patterns. This allows GenAI to produce co-                       1. GenAI tools, based on LLMs trained to predict the most
herent and contextually relevant responses to user instructions.                      likely sequence of words in a given context, often produce
GenAI’s perceived ease of use, coupled with its widespread                            output that is common or “average.” As a result, the qual-
public availability, has caused a growing number of people—                           ity and relevance of the output depends heavily on the
from the front line to the boardroom—to embrace GenAI in                              specificity and ingenuity of the instructions the user enters
their personal and professional lives. The combination of this                        to produce the output, called prompts.
consumerization and GenAI’s potential use in novel applications                    2. GenAI tools tend to lack context, contain bias, occasionally
has motivated many organizations to experiment with GenAI.                            present false or misleading information as fact, and are
                                                                                      notoriously bad at basic arithmetic. Consequently, users
Our research examined data and technology executives’ expe-
                                                                                      must continuously evaluate a tools’ output critically to
riences with such early experiments.1 We found that effective
                                                                                      avoid accepting biased or inaccurate assertions.
GenAI management requires that leaders distinguish between
two types of GenAI implementations: (1) broadly applicable                         3. Unvetted publicly available GenAI tools can bear significant
GenAI tools for individual use across myriad purposes, and (2)                        risks, particularly when employees use them for work, a
GenAI solutions designed for use by specific groups of organi-                        practice known as Bring Your Own AI (BYOAI). The risks can
zational stakeholders to achieve strategic business objectives                        include data loss, intellectual property leakage, copyright
through integration with processes, systems, and offerings. In                        violation, and security breaches.
this briefing, we describe the unique challenges and manage-                       4. GenAI tools are costly. Providing users with licenses to
ment principles for each type of implementation.                                      tools from multiple vendors can quickly become expensive
                                                                                      once free trials and early adoption incentives expire.
1 This research briefing draws from a series of three consecutive virtual round-   Given these challenges, educating employees is critical for the
  table discussions the authors conducted between Q4 2023 and Q2 2024 on
  the topic of GenAI with seventy data and technology executives representing      successful implementation of GenAI tools. Users need to know
  fifty organizations on the MIT CISR Data Research Advisory Board and from        how to write instructions with precise problem statements,
  twenty-three semi-structured interviews, each with an executive from an          context-specific objectives, and detailed process descriptions.
  organization on the board, conducted between February and August 2024.



© 2024 MIT Center for Information Systems Research, Van der Meulen and Wixom. MIT CISR Research Briefings are published monthly
  to update the center’s members on current research projects.                                                                      Mir
                                                                                                                                    MANAGEMENT
                                                                                                                                        SLOAN SCHOOL
2 | MIT CISR Research Briefing, Vol. XXIV, No. 9, September 2024



For instance, a marketer looking to generate campaign ideas        GENERATIVE AI SOLUTIONS
should provide the basic topic of the campaign and examples
                                                                   GenAI solutions are based on business case-driven develop-
of successful past campaigns, and clarify the campaign’s target
                                                                   ment initiatives that address strategic business objectives
audience, desired tone, and intended outcomes. In addition,
                                                                   and create value for specific groups of organizational stake-
users need to be able to evaluate whether their use of a tool is
                                                                   holders—ideally at scale. For example, a GenAI solution for a
consistent with organizational policy and verify the accuracy of
                                                                   call center might use an LLM to process the content and tone
the tool’s outputs. They also need to know that even when de-
                                                                   of conversations and provide real-time coaching to agents.
picted as free, GenAI tools come with costs to the organization.
                                                                   Such solutions generate financial returns through increased
Succeeding with Generative AI Tools                                efficiencies or revenue growth, such as improved agent pro-
                                                                   ductivity and customer retention in the call center context.
Providing enterprise-sanctioned access to a select number of       Like other business case-driven initiatives, organizations
GenAI tools is step one in creating a safe space for employ-       fund GenAI solutions after they meet innovation criteria for
ees to experiment while reducing the allure of BYOAI. It’s a       end-user desirability, technical feasibility, and business viabil-
new cost of securing the business. To enable GenAI tool use        ity and show greater promise than competing opportunities.
effectively, we further recommend that leaders:
                                                                   While GenAI solutions share similarities with other AI initia-
• Develop clear usage guardrails and guidelines. A cross-func-
                                                                   tives, the solutions present three unique challenges:
  tional leadership team representing technological, legal,
  privacy, and governance interests should establish policies      1. As employees across all levels discover ways GenAI can
  on sanctioned and unsanctioned GenAI tool use. Guide-               improve processes, augment systems, and enhance offer-
  lines should specify which tools are permissible (and under         ings, suggestions for new GenAI solutions will proliferate.
  which conditions) and articulate associated risks and their         If this pent-up demand is not addressed, organizations
  potential consequences. For instance, one executive in our          risk the development of “shadow GenAI,” where groups of
  study noted that their organization’s GenAI policy centered         stakeholders independently pursue unsanctioned GenAI
  on data input and output risks, specifying “always okay”            solutions with the help of eager vendors.
  uses (anything involving publicly available information) and     2. A few large vendors own and control most of the foun-
  “never okay” uses (anything involving personally identifiable       dation models2 that underpin GenAI solutions, retaining
  information, strategic information, or proprietary data), with      rights over model mechanics, distribution, and usage. This
  a clear process for seeking approval from the team managing         opacity complicates organizations’ understanding of the
  AI governance when in doubt about a specific use.                   models and their ability to assess biases and predict model
• Invest in ubiquitous training. Organizations should prior-          behavior, introducing risks such as exploitation of GenAI
  itize establishing what we call AI direction and evaluation         model behavior, data leaks, and inaccurate outputs. Un-
  (AIDE) practices for employees to benefit from using GenAI          certainty regarding future usage, model performance, and
  tools. AIDE proficiency requires teaching employees to              complex pricing models also makes it difficult to estimate
  effectively instruct and interrogate GenAI tools, understand        long-term operating costs of GenAI solutions.
  the underlying models, and use the tools ethically and re-       3. The value that an organization can ultimately realize from
  sponsibly. It also includes training in evaluating model out-       GenAI solutions depends on its chosen development
  puts by, for example, improving employees’ domain-specif-           approach (see table 1). Each of three approaches—buy,
  ic knowledge or critical thinking skills.                           boost, and build—involves trade-offs in transparency,
• Standardize on a select set of vendors. As several exec-            context-awareness, and cost, which development teams
  utives pointed out, tracking all alternatives and pricing           must navigate.
  structures in a growing GenAI tools market is daunting. We       Implementing GenAI solutions requires the involvement of
  recommend forming a cross-functional team of potential           stakeholders across the organization. In particular, it takes ex-
  GenAI tool users to help the IT organization determine           perts from the functions or domains that the GenAI solutions
  which tools hold the most potential for your organization.       are intended to enhance to ensure that the solutions create
  As a way to provide access to sanctioned GenAI tools, one        their intended value.
  organization we studied set up a GenAI “app store” where
  employees can apply for tool licenses. In exchange, employ-
                                                                   2 Foundation models are large, pre-trained machine learning models built
  ees are asked to share their “value stories”: narratives that      on extensive datasets, which serve as the basis for rapidly and cost-effec-
  describe how a tool has benefited them.                            tively developing a variety of GenAI solutions.
                                                                           MIT CISR Research Briefing, Vol. XXIV, No. 9, September 2024 | 3



Succeeding with Generative AI Solutions                                           and long-term collaboration. Vendors benefit from direct
                                                                                  feedback on organizations’ willingness to pay and insights into
Making GenAI a cross-functional effort is step one in realiz-
                                                                                  how they will use their offerings to create value, while organi-
ing value from GenAI solutions. In addition, we recommend
                                                                                  zations gain from vendors’ transparency, advice, and custom
that leaders:
                                                                                  support. Viewing GenAI vendor partnerships as ongoing rela-
• Establish a formal, transparent GenAI innovation process.                       tionships rather than one-time transactions fosters adaptabili-
  To avoid falling into what one executive called a “GenAI                        ty and continuous improvement, benefiting both parties.
  laundry list mentality,” organizations need clear governance
  structures, early and consistent stakeholder engagement,                      A HOLISTIC GENERATIVE AI STRATEGY
  and a focus on scalable solutions. For instance, the exec-                    TO SECURE TOMORROW’S SUCCESS
  utive’s organization created a senior-level working group                     GenAI offers leaders not one, but two distinct opportunities for
  to guide its GenAI initiatives, tapping diverse sources like                  implementation: enabling their workforce with GenAI tools to
  hackathons and external consultants to surface stakeholder                    enhance individual productivity, and developing GenAI solutions
  ideas for GenAI solutions. By prioritizing rapid prototyp-                    that generate financial returns by changing processes, systems,
  ing and strategic alignment, the organization ensured its                     and offerings at scale. Leaders in large organizations should pur-
  solutions were effectively vetted and scaled, minimizing                      sue both, creating a virtuous cycle where increased employee
  risks associated with shadow GenAI efforts and maximizing                     awareness and proficiency with GenAI tools drives new GenAI
  value across the organization.                                                capability building and inspires innovation with GenAI solutions.
• Formulate guidelines for GenAI development decisions.
                                                                                For those early in their GenAI journey, the best starting point
  Leaders need to differentiate GenAI development approach-
                                                                                is the targeted adoption of a few GenAI tools from trusted ven-
  es to help teams make informed decisions. Buying GenAI
                                                                                dors, accompanied by hands-on training to improve AIDE prac-
  solutions increases speed but with less context, and teams
                                                                                tices and close oversight to mitigate organizational risk and
  opting for this approach should closely scrutinize vendors’
                                                                                costs. Those further along in their journey should shift their fo-
  policies and capabilities. Boosting GenAI solutions is a better
                                                                                cus to developing those GenAI solutions that most contribute
  approach when there’s a pressing need for high contextual-
                                                                                to strategic business objectives. Buy or boost GenAI solutions
  ization. Building GenAI solutions permits competitive differ-
                                                                                when you need to move fast and gain competitive parity. Opt
  entiation through customization, allowing teams to leverage
                                                                                to build when you need a differentiated GenAI solution that is
  proprietary data to outperform commercial solutions on
                                                                                hard to imitate and provides a competitive advantage.
  specific use cases.
• Create a GenAI vendor partnership strategy. Effective part-                   By approaching the two faces of GenAI in this manner, you
  nerships with GenAI vendors rely on mutual understanding                      will ensure that today’s experimentation lays a solid founda-
                                                                                tion for future value realization.

  Table 1: Generative AI Solution Development Approaches

 Buy        The vendor provides, runs, and maintains the solution and its model, allowing quick GenAI adoption without having to invest in
            model development or fine-tuning. Pricing is typically usage-based (e.g., per user, per token). Off-the-shelf GenAI solutions are
            often opaque and geared to a narrow context (e.g., a function, an industry).

 Boost      The vendor provides, runs, and maintains the model, but the organization enhances it to create a solution—often using proprietary
            data. Common boosting approaches include fine-tuning the model to perform better in specific contexts; and employing Retriev-
            al Augmented Generation (RAG), which appends relevant contextual data to user prompts. RAG requires that data scientists and
            domain experts prepare domain-specific data, convert it into numerical representations (called “vectors”), refine retrieval algorithms,
            and provide feedback on the accuracy and relevance of generated output. While RAG provides more context to otherwise opaque
            models, it increases prompt length and thus usage costs.

 Build      The organization fully assumes responsibility for developing, running, and maintaining the solution and its model. Fully training a
            GenAI model from the ground up is expensive, so most organizations instead opt to fine-tune an open-source foundation model.
            This approach lowers usage costs but requires significant up-front computational investment and advanced data monetization
            capabilities: data management, data platform, data science, acceptable data use, customer understanding, and AI explanation.31


3 For more on advanced data monetization capabilities, see B. H. Wixom, I. A. Someh, and C. M. Beath, “Building Advanced Data Monetization Capabilities for
  the AI-Powered Organization,” MIT CISR Research Briefing, Vol. XXII, No. 6, June 2022.
MIT CENTER FOR INFORMATION SYSTEMS RESEARCH (CISR)
MIT CISR helps executives meet the challenge of leading increasingly digital and data-driven organizations. We provide
insights on how organizations effectively realize value from approaches such as digital business transformation, data
monetization, business ecosystems, and the digital workplace. Founded in 1974 and grounded in MIT’s tradition of
combining academic knowledge and practical purpose, we work directly with digital leaders, executives, and boards to
develop our insights. Our consortium forms a global community that comprises more than seventy-five organizations.




CISR RESEARCH PATRONS            Cencora                          Novo Nordisk A/S (Denmark)        Westpac Banking Corporation




                                                                                                                                   Information as of September 2024
                                 Cochlear Limited (Australia)     OCP Group                         (Australia)
AlixPartners
                                 Commonwealth                     Pacific Life Insurance            WestRock Company
Avanade
                                 Superannuation Corp.             Company                           Xenco Medical
Cognizant                        (Australia)                      Posten Bring AS (Norway)          Zoetis Services LLC
Collibra                         Cuscal Limited (Australia)       Principal Life Insurance
IFS                              CVS Health                       Company                           CISR ASSOCIATE MEMBERS
Pegasystems Inc.                 Dawn Foods                       QBE                               MIT CISR wishes to thank all
                                 DBS Bank Ltd. (Singapore)        Ramsay Health Care                of our associate members
The Ogilvy Group                                                                                    for their support and
                                 Doosan Corporation (Korea)       (Australia)
                                                                                                    contributions.
CISR SPONSORS                    Fidelity Investments             Raytheon Technologies
Alcon Vision                     Fomento Economico                Reserve Bank of Austrailia
Amcor                            Mexicano, S.A.B., de C.V.        Scentre Group Limited
                                 Fortum (Finland)                 (Australia)
ANZ Banking Group
(Australia)                      Genentech                        Schneider Electric Industries
                                                                  SAS (France)
AustralianSuper                  Gilbane Building Company
                                                                  Stockland (Australia)
Banco Bradesco S.A. (Brazil)     Johnson & Johnson (J&J)
                                                                  TabCorp Holdings (Australia)
Banco do Brasil S.A.             Kaiser Permanente
                                                                  Telstra Limited (Australia)
Bank of Queensland               King & Wood Mallesons
(Australia)                      (Australia)                      Terumo Corporation (Japan)
Barclays (UK)                    Mercer                           Tetra Pak (Sweden)
BlueScope Steel (Australia)      Nasdaq, Inc.                     Truist Financial Corporation
BNP Paribas (France)             NN Insurance Eurasia NV          UniSuper Management Pty
                                                                  Ltd (Australia)
Bupa (Australia)                 Nomura Holdings, Inc. (Japan)
                                                                  Uniting (Australia)
CarMax                           Nomura Research Institute,
                                 Ltd. Systems Consulting          USAA
Caterpillar, Inc.
                                 Division (Japan)                 Webster Bank, N.A.
Cemex (Mexico)




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
