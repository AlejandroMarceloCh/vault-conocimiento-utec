---
curso: MKT
titulo: Bazaar Caso
slides: 6
fuente: Bazaar Caso.pdf
---

 Measuring ROI on Sponsored Search Ads
 BY KINSHUK JERATH *


Online Marketing at Bazaar.com
Bob and Myra are senior members of the marketing analytics team at Bazaar (Bazaar.com), theleading online retailer in the United States. Bazaar
uses both display advertising and search engine advertising, running paid search ads on the two major search engines, Google and Bing.Bazaar
releases its ads in response to keywords used by online consumers; the marketing teamclassifies these keywords into two broad categories:
branded and nonbranded. Branded keywords include keywords such as “Bazaar,” “Bazaar shoes,” and “Bazaar guitar” that contain the Bazaar
brand name. (See Exhibit 1 to view a typical page of results on Google aftera branded keyword search.) Nonbranded keywords include
keywords such as “shoes” and “guitar” that do not contain the Bazaar brand name. The firm employs the same strategies for both Google and
Bing for targeting ads, choosing keywords to advertise on, and ad copies used, and the mix of potential customers visiting the company’s
website from both search engines is virtually identical; the only difference is that their Bing campaign is much smaller than their Google
campaign.
Bob and Myra have agreed to meet to discuss the recent advertising reports relating to paid search efforts. Specifically, they want to take a
deeper dive into ROI calculations on the sponsored search ads for branded keywords on Google. Also joining this meeting is Sunil, a newly
hired data scientist.


The ROI Discussion
Bob (smiling broadly): Myra, I am very pleased with these numbers for sponsored search advertising for branded keywords on Google. (See
Exhibit 2, Table 1.) As you know, we were planning to run our sponsored ad campaign for 12 weeks, but there was a technical glitch in our
systems starting week 10, at which point we suspended our Google campaign. However, as you know, our Bing campaign was unaffected by
this glitch. Taking this into account, my analysis ignored the Google numbers for weeks 10, 11, and 12, since no sponsored search advertising
was going on at that time. So let’s focus on the data from weeks 1 to 9. Sunil, you might recall that this data reflects weekly ad traffic numbers
to Bazaar.com from consumers clicking on sponsored ad links as well as on organic links that appear on Google after a branded keyword is
searched. This data reveals that we obtain about 20% of our traffic for these branded keywords through the sponsored ads that we show on
Google.
Myra: So, just to clarify, if the consumer searches a keyword with our brand name in it, then they are shown a sponsored ad from us. Of
course, since the search term includes our brand name, Google displays a link, or even multiple links, to our website in the organic results as
well. The click-through numbers are for users who visit Bazaar.com by clicking on those two types of links, right?
Bob: Yes, that’s exactly right. I just did an ROI analysis, and we are getting amazing ROI on this ad spend. Here is how it goes. (Drawing on
whiteboard.) We know that the average cost per click for a sponsored click is $0.60. Once consumers land on Bazaar.com, their average
probability of making a purchase from our website is 12% and our average margin per conversion is $21. So that leads to an average revenue
per click of 0.12 x $21, or $2.52, which implies an ROI of ($2.52–$0.60)/($0.60), or 320.0%.
Myra: Wow, Bob! That’s a really high ROI number. I don’t think any of our other advertising channels have ROI numbers anything close to
that. That actually makes me suspicious.
Bob: Come on, Myra! I just did the calculation in front of you. Numbers don’t lie, do they?
Myra: Of course not, Bob. Our team is all about the analytics. But I think we need to be more careful in doing the analysis. My main concern
is that these keyword searches include the name of our company. These people seem to be already aware of our website and actively looking
for it. I wonder if we even need to show the sponsored ads to them.
Bob: What do you mean by that?
Myra: Suppose a consumer used the search term “Bazaar shoes” and clicked on our sponsoredad that came up in the results. If the ad weren’t
there, my guess is that this consumer would be very likely to simply click on our link in the organic list, and so we would get the same
consumer for free. And we know that the conversion probability and margin per conversion numbers are the same for all consumers,
irrespective of how they landed up at our website.
Bob: That’s a good point, Myra. You always make me think! But if we don’t put our own sponsored ad out there and competitors put theirs
up, maybe we’ll end up losing potential customers.
Myra: That’s definitely possible. But someone who is looking for us specifically is quite likely to ignore the competitor’s ad and simply go to
the organic link for our website. After all, if people use “Bazaar” as a search term, that indicates that they want to come to our website.
Plus, quite often competitors do not even advertise on keywords that explicitly include the name of our website. That said, we run the risk of
leakage to competitors if we stop doing sponsored search advertising.
Bob: These arguments certainly make sense. But ultimately, it is an empirical question.
Myra: I agree with that. You know what, I think we might be able to answer this question. What if we compare the data from the first nine
weeks to the data from the last three weeks, when there was no sponsored advertising going on?
Bob: So that would help us understand what the impact of stopping sponsored search advertising for these keywords would be. That’s brilliant!
And since this interruption was caused by a technical glitch and not by any strategic decisions on our side, it would be safe to call this a natural
experiment.
Myra: Yes, exactly, Bob! But there still may be one problem with this analysis. What if the firstnine weeks were systematically different from
the last three weeks? I wonder if we can detect that and control for it if needed.
Just then, Chung, the team’s marketing intern, walks in.
Chung: Hi, Bob and Myra! The traffic data for our sponsored and organic traffic for branded keywords on Bing for weeks 1 to 12 just came in.
Here it is. (See Exhibit 2, Table 2.) But beforeyou take a look, the rep from our advertising agency just arrived and is waiting for you in the
lobby.
Bob (getting up to meet the rep): Sunil, Myra and I need to step out for a bit. Myra made somegood points about measuring ad spend ROI on
Google. We’ll be back in about 30 minutes. Please run this analysis in the meantime, and we’ll discuss the results when we have finished up
with the agency meeting.
Sunil: Certainly, Bob. This sounds very exciting!


The ROI Analysis
Sunil was on board with Bob and Myra’s thinking but knew that he had to run the ROI analysiscarefully. He was eager to impress his new
colleagues. What analysis should he run?
Exhibit 1
Screenshots of Results for Some Typical Branded Keyword Searches on Google
Exhibit 2
Weekly Traffic from Bing and Google
Table 1: Weekly traffic from Google by origin of click (for branded keywords searches only)
 Week                                                                                                           10           11           12
 Sponsored   32,269    31,951    32,143    31,417    31,194    31,576    30,951    30,611     30,401             0            0            0
 Organic     127,876   128,169   125,717   126,264   123,871   124,053   126,105   123,064    121,637   150,188      148,658      146,584


Table 2: Weekly traffic from Bing by origin of click (for branded keywords searches only)
 Week                                                                                                           10           11           12
 Sponsored   3,965     3,984     3,960     3,952     3,874     3,932     3,890     3,883      3,843     3,815        3,754        3,754
 Organic     15,805    15,964    15,815    15,810    15,633    15,797    15,462    15,309     15,499    15,185       15,159       15,036
