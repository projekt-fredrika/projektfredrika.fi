---
title: "Suggestion: make Wikidata’s links to external data multilingual"
url: "/make-wikidatas-links-to-external-data-multilingual/"
date: "2021-05-18"
images: ["/img/Welcome_multilingual_Guernsey_tourism.jpg"]
author: ['Robert']
categories: ['Wikidata']
tags: ['wikidata']
toc: true
draft: false
_build:
  list: true
  publishResources: true
  render: true
---

![Multilingual Guernsey tourism](/img/Welcome_multilingual_Guernsey_tourism.jpg)


_Note 21.5.2021: Since publishing this blog, we have added a task to [Wikimedia Phabricator](https://phabricator.wikimedia.org/) that was merged with an earlier bug report: [T259801](https://phabricator.wikimedia.org/T259801). We hope this will contribute to the issue being resolved._

This is a suggestion for improving how links to external sources are forwarded at [wikidata.org](https://www.wikidata.org/), by honouring the language settings in the **Identifiers** section of individual Wikidata objects, and, over time, by automatically showing all existing language formatter versions for each Wikidata object, without edits required on a Wikidata object level. 

Note: This blog is more technical than our usual blogs at Projekt Fredrika. It is also in English to be comprehensible for international readers.

## A good property exists: P407 '_language of work or name_'

One of Wikidata’s strengths is for objects to be linked through IDs to external data sources. The links are automatically generated when a URL-syntax is has been entered for the property P1630 **_'formatter URL_**'.

The external data sources may exist in several language versions. The Wikidata user interface even allows separate entries for each P407 "**_language of work or name_**", but the onward pointers lead to one language only. In other words: all the language versions in wikidata.org point at only one of the available language versions, even though several languages have been entered into the **Identifiers** section of the Wikidata object and even though the underlying identifier (eg. P8309 '**_Yle topic ID_**') has well-defined language specific P1630 **_'formatter URL_**' properties, for each P407 '**_language of work or name_**'.

![](/img/2021/05/Yle_topic_ID-1024x608.jpeg)

Both of Q6348774 [Kaj Arnö](https://www.wikidata.org/wiki/Q6348774)'s ID-links go the the Finnish language URL, even though both Swedish and Finnish URL formats are available in the Yle Topic ID ([P8309](https://www.wikidata.org/wiki/Property:P8309))

This does not only affect official multi-lingual countries such as Finland, Switzerland, Canada, etc. This affects all data sources that have information in a lingua franca such as English in addition to the data sources’ single language in USA, Brazil, The Netherlands, Estonia, Taiwan, South Korea, China, Australia and more. 

In Wikidata there are more than 442 properties that have a link URL-format in more than one language. See [this query](https://query.wikidata.org/#SELECT%20DISTINCT%20%3Fitem%20%3FitemLabel%20%3Flang%20%3FlangLabel%20%3Frank%20%3FcountryLabel%20%0AWHERE%20%0A%7B%0A%20%20%3Fitem%20p%3AP1630%20%3Fstat.%0A%20%20%3Fstat%20ps%3AP1630%20%3Ff_url.%0A%20%20%3Fstat%20pq%3AP407%20%3Flang.%0A%20%20optional%20%7B%3Fitem%20wdt%3AP17%20%3Fcountry.%7D%0A%20%20%3Fstat%20wikibase%3Arank%20%3Frank.%0A%20%20%0A%20%20%3Fitem%20p%3AP1630%20%3Fstat2.%0A%20%20filter%28str%28%3Fstat%29%20%21%3D%20str%28%3Fstat2%29%29%0A%20%20%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%0A%7D%20ORDER%20BY%20%3FitemLabel%20%3Frank%20%3FlangLabel), thanks to [Wikidata:request a query](https://www.wikidata.org/wiki/Wikidata:Request_a_query#All_properties_with_property_P1630_%28URL_format%29_and_P407_%28language%29_for_that_entry). 

## An example: P902 Historical Dictionary of Switzerland

One example: One of the many external sources that has an entry about the country Finland is the Historical Dictionary of Switzerland (HDS). The Swiss encyclopedia has an article about Finland in German, French and Italian, all identified by the same ID 003353. 

However, when you scroll down on Finland’s Wikidata object, [Q33](https://www.wikidata.org/wiki/Q33) at [wikidata.org](http://wikidata.org/) to the entry for HDS-ID, you will only find one ID entry 003353 which will have a link to the article solely in German. 

![](/img/2021/05/HDS-ID.jpeg)

Finland ([Q33](https://www.wikidata.org/wiki/Q33)) has the HDS ID 007396 shown as one link to the German page with no direct link to the French nor Italian page.

This is not because the URL formats are missing for French and Italian. The property HDS-ID ([P902](https://www.wikidata.org/wiki/Property:P902)) has URL format ([P1630](https://www.wikidata.org/wiki/Property:P1630)) for three languages of which German has been set to preferred. The entered URL formats look like this:

German: [https://hls-dhs-dss.ch/de/articles/$1](https://hls-dhs-dss.ch/de/articles/$1)  
Italian: [https://hls-dhs-dss.ch/it/articles/$1](https://hls-dhs-dss.ch/it/articles/$1)  
French: [https://hls-dhs-dss.ch/fr/articles/$1](https://hls-dhs-dss.ch/fr/articles/$1)  
There are also three URLs with rank marked as deprecated, i.e. old URLs not in use. 

On Finland [Q33](https://www.wikidata.org/wiki/Q33), clicking [003353](https://hls-dhs-dss.ch/de/articles/003353) will lead to a page in German. In this case, the target page (outside Wikidata) has a clear way to switch language to Italian or French - but for other equivalent outside links, this is not always the case. 

## The right solution: Automatically list all language versions

In the above Swiss HDS-ID case, it is still somewhat understandable that there are no links to other languages than German: There is only one line entered for Finland, without an entry for P407 '**_language of work or name_**' – which makes it acceptable to default to German for HDS [003353](https://hls-dhs-dss.ch/de/articles/003353), but somewhat strange for Q834 known in English as **_Canton of Valais_**, which is reasonable considering its French speaking majority. But the HDS link points to [007396](https://hls-dhs-dss.ch/de/articles/007396), **_Wallis_**, which is the name used by the (sizeable) German minority. An **ideal solution** would thus 'automatically' improve upon the UI within the **_Identifiers_** section of Wikidata objects with properties having several P1630 **_'formatter URL_**' properties, one for each P407 '**_language of work or name_**'. 

![](/img/2021/05/HDS-Wallis-1024x397.jpeg)

The article about Wallis on HDS is available in German, French and Italian, but the Wikidata user interface only shows a link to the German page.

## Minimal solution (bug fix): Honour the language setting in the pointer

However, there is also a **minimal solution**, not requiring any changes in the user interface. This solution could even be likened to "fixing a bug".

Case in point: [P8309](https://www.wikidata.org/wiki/Property:P8309) '**_Yle topic ID_**'. For Yle topic ID, it is often the case that topics will only exist in one language. So when clicking through from Q6348774 [Kaj Arnö](https://www.wikidata.org/wiki/Q6348774) to his Yle topic ID [18-284310](https://yle.fi/aihe/t/18-284310) on the line with P407 '**_language of work or name_**' being Q9027 **_Swedish_**, the user will land on the Q1412 Finnish language page [https://yle.fi/aihe/t/18-284310](https://yle.fi/aihe/t/18-284310) instead of the correct Q9027 Swedish language page [https://svenska.yle.fi/t/18-284310](https://svenska.yle.fi/t/18-284310), even though P1630 **_'formatter URL_**' has been properly entered for Swedish for [P8309](https://www.wikidata.org/wiki/Property:P8309) '**_Yle topic ID_**'.

![](/img/2021/05/Yle_topic_ID-URL-format-1024x577.jpeg)

Yle Topic ID ([P8309](https://www.wikidata.org/wiki/Property:P8309)) has the URL-format entered for Finnish and Swedish

## Why honouring language settings matters for the end user  

This not just misleading but highly confusing for the end user. Kaj Arnö has only written articles in Swedish. The Finnish page gives the impression of being empty. Should you notice and click the link “Ruotsiksi: Kaj Arnö” (which is unlikely for non-Finnish speakers, as the text is in Finnish only, and translates to "In Swedish: Kaj Arnö") will switch to show Kaj Arnö's articles in Swedish (of which there are quite a few). This is the page to which there should be a direct link from inside Wikidata. 

The same disability exists in many places. For example, it affects Heritage Sites in Finland [P4009](https://www.wikidata.org/wiki/Property:P4009), but in this case switching language by clicking "på svenska" at [rky.fi](http://rky.fi/) on e.g. [Porvoon saaristokylät](http://www.rky.fi/read/asp/r_kohde_det.aspx?KOHDE_ID=4661) will throw the user to the rky.fi-main home page instead of the Swedish version of the same page, [Skärgårdsbyar i Borgå](http://www.kulturmiljo.fi/read/asp/rsv_kohde_det.aspx?KOHDE_ID=4661). 

## Conclusion: This confusion needs to stop

It is highly confusing for the user to have to go through this extra step to find the source in the preferred language. Not showing the language options for the user hides their existence, and makes the entry of the language specific formatter URLs rather pointless, as they are not in use.

Our suggestion is that the UI on [wikidata.org](http://wikidata.org/) would over time be improved to automatically show IDs with links in multiple languages (all non-deprecated URL formats that have a defined language), and urgently for the bug to be fixed, that language specific settings in the Identifier section of individual Wikidata Q objects are currently not honoured at all.

**Projekt Fredrika** improves the coverage of Swedish Finland and Swedish in Finland on Wikipedia, in Swedish and other languages. Read more about us on _Wikipedia (_[Projektsidan](https://sv.wikipedia.org/wiki/Wikipedia:Projekt_Fredrika), [Project page](https://en.wikipedia.org/wiki/Wikipedia:Projekt_Fredrika), [Projektisivut](https://fi.wikipedia.org/wiki/Wikipedia:Projekt_Fredrika), [Projektseite](https://de.wikipedia.org/wiki/Wikipedia:Projekt_Fredrika), [Page du projet](https://fr.wikipedia.org/wiki/Wikipedia:Projekt_Fredrika), [страница проекта](https://ru.wikipedia.org/wiki/Wikipedia:Projekt_Fredrika)) _or follow us on [Twitter](https://twitter.com/projektfredrika), [Facebook](https://www.facebook.com/projektfredrika/), or [Instagram](http://instagram.com/projektfredrika)._