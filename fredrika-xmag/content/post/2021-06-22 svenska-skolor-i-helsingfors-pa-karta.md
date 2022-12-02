---
title: "Rundvandring bland svenska skolor i Helsingfors"
url: "/svenska-skolor-i-helsingfors-pa-karta/"
date: "2021-06-22"
images: ["/img/hfors-skolor-rutt-revan.png"]
author: ['Robert']
categories: ['Helsingfors']
tags: ['helsingfors']
toc: true
draft: false
_build:
  list: true
  publishResources: true
  render: true
---

Ta dig ut på stan och bonga skolor! Vi har skapat en rutt som tar dig till de historiska svenska skolorna i centrala Helsingfors, genom att vi utnyttjat all den öppna data vi under de senaste månaderna lagt in i Wikidata, Wikimedia Commons samt Wikipedia.

Rutten börjar från Järnvägstorget och går via Kronohagen och Ulrikasborg till Bortre Tölö. På rutten finns Lärkan, Bööks, Revan, Lavan, Norsen, Pontan, Broban, Banan, Bullan, Vilohemmet, Arken, Apollo/Minerva, Lönkan, Zillen och Toppan. Hela rutten runt är lite på 12 kilometer lång - en halv dags promenad, men man kan förstås också besöka en kortare bit eller utnyttja allmänna transportmedel.

Klicka på punkterna i kartan nedan så ser du grundfakta om skolan från Wikidata samt länk till wikipediaartikeln på de språk som finns tillgängliga. Det går att spara kartan till egna Google Maps profilen och använda kartan i telefonen under en promenad - klicka den gråa stjärnan för att spara kartan till din Google Maps app.

_Du kan öppna rutten [i Google Maps med denna länk](https://www.google.com/maps/d/u/0/edit?mid=1Wx9eRoaVYWwcBkvgp7t9qVTum6wrV0r-&usp=sharing)._

Du får gärna fotografera skolorna och bidra med flera bilder till Commons-bildbanken [Swedish schools in Helsinki](https://commons.wikimedia.org/wiki/Category:Swedish_schools_in_Helsinki), så kan skolorna prydas med ännu flera bilder på Wikipedia.

## Hur gjorde vi Google Maps-kartan?

Kartans punkter är hämtade från Wikidata - den strukturerade relationsdatabasen bakom Wikipedia. Vi har satt in data om skolorna som vem som helst kan söka och förbättra. [Här kan du prova sökningen som hämtar namn, adresser, årtal, med mera](https://query.wikidata.org/#%23%20svenska%20folkskolor%20%28Q513984%29%20och%20l%C3%A4roverk%20%28Q10572388%29%20i%20Helsingfors%0ASELECT%20%20%20%0A%20%20%20%3FitemLabel%20%0A%20%20%20%3Fsmeknamn%20%0A%20%20%20%3F%C3%A5rtal%20%0A%20%20%20%3FtypeLabel%0A%20%20%20%3Fgatuadress%20%0A%20%20%20%28GROUP_CONCAT%28DISTINCT%20%3Fp112label%3BSEPARATOR%3D%22%2C%20%22%29%20AS%20%3Fgrundare%29%20%0A%20%20%20%28GROUP_CONCAT%28DISTINCT%20%3Fp1366label%3BSEPARATOR%3D%22%2C%20%22%29%20AS%20%3Fersattav%29%20%0A%20%20%20%28GROUP_CONCAT%28DISTINCT%20%3Fwpsv%3BSEPARATOR%3D%22%2C%20%22%29%20AS%20%3Fwp_sv%29%20%0A%20%20%20%28GROUP_CONCAT%28DISTINCT%20%3Fwpfi%3BSEPARATOR%3D%22%2C%20%22%29%20AS%20%3Fwp_fi%29%20%0A%20%20%20%28GROUP_CONCAT%28DISTINCT%20%3Fwpen%3BSEPARATOR%3D%22%2C%20%22%29%20AS%20%3Fwp_en%29%20%0A%20%20%20%3Fitem%20%0A%20%20%20%3FitemDescription%20%0A%20%20%20%3Fkoordinater%20%0A%20%20%20%3Fbild%20%0A%20%20%20%3Flat%0A%20%20%20%3Flon%0A%23%20%20%20%3Frgb%20%0A%0AWHERE%20%7B%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Csv%22.%20%7D%0A%20%20VALUES%20%3Ftype%20%7Bwd%3AQ513984%20wd%3AQ10572388%20wd%3AQ55043%20wd%3AQ101244523%7D%0A%20%20%3Fitem%20wdt%3AP31%20%3Ftype.%0A%20%20%3Fitem%20wdt%3AP131%20wd%3AQ1757.%0A%20%20%3Fitem%20wdt%3AP37%20wd%3AQ9027.%0A%20%20OPTIONAL%7B%3Fitem%20wdt%3AP18%20%3Fbild.%7D%0A%20%20OPTIONAL%7B%3Fitem%20wdt%3AP571%20%3Fp571.%7D%0A%20%20OPTIONAL%7B%3Fitem%20wdt%3AP576%20%3Fp576.%7D%0A%20%20BIND%28CONCAT%28SUBSTR%28STR%28COALESCE%28%3Fp571%2C%22%22%29%29%2C1%2C4%29%2C%22-%22%2CSUBSTR%28STR%28COALESCE%28%3Fp576%2C%22%22%29%29%2C1%2C4%29%29%20AS%20%3F%C3%A5rtal%29%0A%20%20OPTIONAL%20%7B%3Fitem%20wdt%3AP1449%20%3Fsmeknamn.%7D%0A%20%20OPTIONAL%20%7B%3Fitem%20wdt%3AP6375%20%3Fgatuadress%7D%0A%20%20OPTIONAL%20%7B%3Fitem%20wdt%3AP625%20%3Fkoordinater%7D%0A%20%20OPTIONAL%20%7B%3Fitem%20wdt%3AP112%20%3Fp112.%20%3Fp112%20rdfs%3Alabel%20%3Fp112label%20.%20FILTER%28lang%28%3Fp112label%29%3D%27sv%27%29%20%7D%0A%20%20OPTIONAL%20%7B%3Fitem%20wdt%3AP1366%20%3Fp1366.%20%3Fp1366%20rdfs%3Alabel%20%3Fp1366label%20.%20FILTER%28lang%28%3Fp1366label%29%3D%27sv%27%29%20%7D%0A%20%20OPTIONAL%20%7B%3Fwpsv%20schema%3Aabout%20%3Fitem%20.%20%3Fwpsv%20schema%3AisPartOf%20%3Chttps%3A%2F%2Fsv.wikipedia.org%2F%3E.%7D%0A%20%20OPTIONAL%20%7B%3Fwpfi%20schema%3Aabout%20%3Fitem%20.%20%3Fwpfi%20schema%3AisPartOf%20%3Chttps%3A%2F%2Ffi.wikipedia.org%2F%3E.%7D%0A%20%20OPTIONAL%20%7B%3Fwpen%20schema%3Aabout%20%3Fitem%20.%20%3Fwpen%20schema%3AisPartOf%20%3Chttps%3A%2F%2Fen.wikipedia.org%2F%3E.%7D%0A%20%20BIND%28geof%3Alatitude%28%3Fkoordinater%29%20as%20%3Flat%29%0A%20%20BIND%28geof%3Alongitude%28%3Fkoordinater%29%20as%20%3Flon%29%20%20%0A%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22sv%2C%5BAUTO_LANGUAGE%5D%22.%20%7D%0A%7D%20%20%0AGROUP%20BY%20%3Fitem%20%3FitemLabel%20%3F%C3%A5rtal%20%3Fsmeknamn%20%3FitemDescription%20%3Fkoordinater%20%3FgrundareLabel%20%3Fbild%20%3FtypeLabel%20%3Frgb%20%3Fgatuadress%20%3Flat%20%3Flon%0AORDER%20BY%20DESC%28%3FtypeLabel%29%20%3F%C3%A5rtal%20%0ALIMIT%202500). Vi har sedan laddat ner datan som CSV och importerat den i Google My Maps-tjänsten.

## OpenStreetMap

Öppna alternativet till Google Maps är OpenStreetMap. Det går att visa punkterna på OSM med t.ex. franska gratistjänsten uMap (se exemplet nedan), men vi valda att utnyttja Google Maps denna gång.

![](/2022/10/Screenshot-2022-10-24-at-22.37.25-1024x300.png)

OSM karta av skolor och vandringsrutt i uMap

OSM-kartan ovan har Helsingfors namn på finska. En utmaning för det svenska Finland är att OSM har som kutym att i Finland att visa namn på kommunens majoritetsspråk - trots att både finska och svenska namnen finns inmatade i OSM. Till exempel i Helsingfors är gatunamnen på finska, medan de i Ekenäs är på svenska. Ibland är det möjligt att uttryckligen köra över kutymen och välja svenska varianten av kartan i en tjänst. Ofta är det inte så, som i detta fall med uMap. T.ex. OSM i Belgien valt att vara äkta tvåspråkig - standarden i Belgien är att visa namn på båda språken.
