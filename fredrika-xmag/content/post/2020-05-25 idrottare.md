---
title: "Kategorin “Finlandssvenska idrottare” städad!"
url: "/idrottare/"
date: "2020-05-25"
images: ["/img/Stafettkarnevalen.jpeg"]
author: ['Robert']
categories: ['Idrott']
tags: ['personer']
toc: true
draft: false
_build:
  list: true
  publishResources: true
  render: true
---

Nu är det ordentligt städat i kategorin [Finlandssvenska idrottare](https://sv.wikipedia.org/wiki/Kategori:Finlandssvenska_idrottare) på svenska Wikipedia.

Förutom att markera existerande Wikipedia artiklar i rätta kategorier, så jämförde jag också idrottarna med Yles artikel [Svenskfinlands 50 största idrottshjältar genom tiderna](https://svenska.yle.fi/artikel/2020/04/20/rankning-svenskfinlands-50-storsta-idrottshjaltar-genom-tiderna) för att se hur Wikipedia återspeglar en genomtänkt lista på idrottare. Mera om det nedan! 

Fördelarna med att sätta en kategori i skick är flera. Dels förbättras överblicken av ett ämne och dels blir det svenska Finland mer synligt då kategorin nämns på relevanta artiklar. Dessutom blir Projekt Fredrikas lupps analys mera helhetstäckande med fullständiga kategorier, och mer lättläst med genomtänkta underkategorier.  

Utgångsläget
------------

Före jag började fanns det bara 33 artiklar i kategorin Finlandssvenska idrottare. Jag visste dock att det fanns mycket flera finlandssvenska idrottare - exakt 98 på svenskspråkiga Wikipedia och 48 till på finska och engelska Wikipedia. Detta visste jag tack vare [en Wikidata-sökning (etnisk grupp finlandssvenskar kombinerat med sysselsättning idrott eller någon av dess underkategorier](https://query.wikidata.org/#%23Finlandssvenska%20idrottare%0ASELECT%20%3Fperson%20%3FpersonLabel%20%3FpersonDescription%20%3Fwpsv%20%3Fwpfi%20%3Fwpen%0AWHERE%20%0A%7B%0A%20%20%3Fperson%20wdt%3AP172%20wd%3AQ726673.%0A%20%20%3Fperson%20wdt%3AP106%2Fwdt%3AP279%2a%20wd%3AQ2066131.%0A%20%20OPTIONAL%20%7B%3Fwpsv%20schema%3Aabout%20%3Fperson%20.%20%3Fwpsv%20schema%3AisPartOf%20%3Chttps%3A%2F%2Fsv.wikipedia.org%2F%3E.%7D%0A%20%20OPTIONAL%20%7B%3Fwpfi%20schema%3Aabout%20%3Fperson%20.%20%3Fwpfi%20schema%3AisPartOf%20%3Chttps%3A%2F%2Ffi.wikipedia.org%2F%3E.%7D%0A%20%20OPTIONAL%20%7B%3Fwpen%20schema%3Aabout%20%3Fperson%20.%20%3Fwpen%20schema%3AisPartOf%20%3Chttps%3A%2F%2Fen.wikipedia.org%2F%3E.%7D%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22sv%2Cfi%2Cen%22.%20%7D%0A%7D)).

Massuppdatering och observationer
---------------------------------

Vill man massuppdatera Wikipedia-kategorin för många artiklar på en gång kan man använda verktyget [QuickCategories](https://quickcategories.toolforge.org/). Massuppdatering kräver ansvar: hellre minskar man på skräp än kopierar det blint vidare, så till min process hörde att jag dubbelkollade listan från Wikidata genom att öppna en artikel åt gången från min lista i Google Spreadsheet, ögnade igenom att det faktiskt var frågan om en finlandssvensk idrottare, och markerade så i min lista. 

Wikidata-listan var pålitlig. Då jag var osäker om det verkligen fanns en koppling till det svenska Finland var det till min överraskning ofta engelska Wikipedia som visste besked om ishockey- och fotbollsspelares finlandssvenskhet. Största frågetecken orsakade finlandssvenskar som flyttat till Sverige som unga och idrottat i Sverige - jag gjorde dem till finlandssvenska idrottare, men såg till att de också är i kategorin [Sverigefinlandssvenskar](https://sv.wikipedia.org/wiki/Sverigefinlandssvenskar). 

I Google Spreadsheet var det sen lätt att skapa de QuickCategories-kommandon jag behövde för att lägga artiklar till kategorier:

```
Förnamn Efternamn | +Category:Finlandssvenska idrottare | -Category Finlandssvenskar
```

Jag lade till personer till Finlandssvenska idrottare och tog bort dem från Finlandssvenskar så att personen inte blir “överkategoriserad” - ett tips jag fick på [min diskussionssida](https://sv.wikipedia.org/wiki/Anv%C3%A4ndardiskussion:Robertsilen#Kategorier) av en Wikipedia-veteran som märkt att jag kommit igång med mitt projekt. 

Då en del idrottsgrenar hade tillräckligt med representanter för en underkategori (långt över 5 stycken var), så skapade jag [finlandssvenska fotbollsspelare](https://sv.wikipedia.org/wiki/Kategori:Finlandssvenska_fotbollsspelare), [ishockeyspelare](https://sv.wikipedia.org/wiki/Kategori:Finlandssvenska_ishockeyspelare) och [friidrottare](https://sv.wikipedia.org/wiki/Kategori:Finlandssvenska_friidrottare). Dessa personer raderade jag med det samma från kategorin idrottare. 

Hur fullständig är svenska Wikipedias kategori finlandssvenska idrottare? 
--------------------------------------------------------------------------

Efter hårt städande var det sedan dags att jämföra resultatet med en genomtänkt redigerad lista från en pålitlig källa: Svenska Yles [Svenskfinlands 50 största idrottshjältar genom tiderna](https://svenska.yle.fi/artikel/2020/04/20/rankning-svenskfinlands-50-storsta-idrottshjaltar-genom-tiderna). Visserligen innehåller listan idag (21.5.2020) bara 40 personer då alla inte ännu publicerats - men det räcker bra för en jämförelse. Hur många av dessa högt ansedda idrottare finns med på svenskspråkiga Wikipedia - och är de faktiskt kategoriserade som finlandssvenskar?

Av 40 hade 24 en svenskspråkig Wikipedia sida och var rätt kategoriserade. Mera än hälften, men nog en bit ifrån berömligt! Skillnaden på 16 personer förklarades av: 

1) En idrottshjälte hade ingen Wikipedia-sida alls: Catarina Svenlin.

2) Sex idrottshjältar hade en svenskspråkig Wikipedia sida, men var inte kategoriserade som finlandssvenskar på Wikipedia eller Wikidata och hade blivit utanför vår uppdatering. Jag korrigerade detta för: 

*   [Mårten Boström](https://sv.wikipedia.org/wiki/M%C3%A5rten_Bostr%C3%B6m) - orienterare
*   [Walter Jakobsson](https://sv.wikipedia.org/wiki/Walter_Jakobsson) - konståkare
*   [Elias Katz](https://sv.wikipedia.org/wiki/Elias_Katz) - friidrottare
*   [Petri Kokko](https://sv.wikipedia.org/wiki/Petri_Kokko) - ishockeyspelare
*   [Curt Lincoln](https://sv.wikipedia.org/wiki/Curt_Lincoln) - tennisspelare och formulaförare
*   [Adolf Lindfors](https://sv.wikipedia.org/wiki/Adolf_Lindfors_(brottare)) - brottare

3) De resterande nio idrottshjältarna hade ingen svenskspråkig Wikipedia sida, men nog en artikel på finska och/eller engelska. Jag korrigerade dem så att de är kategoriserade på minst ett språk: på engelska som [Swedish-speaking Finns](https://en.wikipedia.org/wiki/Category:Swedish-speaking_Finns) eller finska som [Suomenruotsalaiset henkilöt](https://fi.wikipedia.org/wiki/Luokka:Suomenruotsalaiset_henkil%C3%B6t), samt har som etnisk grupp Finlandssvenskar i Wikidata. På så vis hänger de med i framtida analyser och körningar. De 9 som saknar svenskspråkig artikel är: 

*   [Harry Hannus](https://en.wikipedia.org/wiki/Harry_Hannus) - cyklist
*   [Krister Holmberg](https://en.wikipedia.org/wiki/Krister_Holmberg_(sport_shooter)) - sportskytte
*   [Kevin Lankinen](https://en.wikipedia.org/wiki/Kevin_Lankinen) - ishockeyspelare
*   [Mona-Lisa Pursiainen](https://en.wikipedia.org/wiki/Mona-Lisa_Pursiainen) - sprintlöpare
*   [Jan Rönnberg](https://fi.wikipedia.org/wiki/Jan_R%C3%B6nnberg) - handbollspelare
*   [Ronja Savolainen](https://en.wikipedia.org/wiki/Ronja_Savolainen) - ishockeyspelare
*   [Fredrik Smulter](https://fi.wikipedia.org/wiki/Fredrik_Smulter) - styrkelyft
*   [Pia Sundstedt](https://en.wikipedia.org/wiki/Pia_Sundstedt) - cyklist
*   [Peter Tallberg](https://en.wikipedia.org/wiki/Peter_Tallberg) - seglare

Så slutresultat var att 30 av Yles 40 idrottshjältar har det bra ställt: de har en svenskspråkig sida och är rätt kategoriserad på Wikipedia. Jag ger vitsordet 7+ för den uppdaterade kategorin [Finlandssvenska idrottare](https://sv.wikipedia.org/wiki/Kategori:Finlandssvenska_idrottare) och uppmanar alla skrivkunniga idrottsintresserade att skriva om våra svenskspråkiga idrottshjältar :) 

Kommentarer eller frågor om finlandssvenska idrottare, kategorisering på Wikipedia, eller massuppdatering med Wikidata och QuickCategories? Fråga gärna!