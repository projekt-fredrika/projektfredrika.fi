---
title: "Ny hemsida med Hugo"
url: "/ny-hemsida-med-hugo/"
date: "2022-12-14"
images: ['/img/hugohemsida.png']
author: ['Robert','Kaj']
categories: ['hemsida']
tags: ['hemsida','hugo','python']
toc: false
draft: false
_build:
  list: true
  publishResources: true
  render: true
---


På goda grunder brukar nya hemsidor kvitteras med en gäspning av omvärlden. Men när vi nu i december har bytt tekniken bakom webbsajten projektfredrika.fi från dynamiska Wordpress till statiska Hugo är vi ivriga att berätta om det, för via Hugos fördelar kan vi enklare befrämja Fredrikas mål – tillgängligheten på öppen information. Läs mer här.


## Vad är Hugo? Statiska webbsidor!

Wordpress bygger webbsidor dynamiskt då de behövs, Hugo bygger dem färdigt på förhand – statiskt – i samband med att man ändrar deras innehåll.

För de tekniskt lagda: Wordpress påminner om ett tolkat, långsamt programmeringsspråk, medan Hugo påminner om ett översatt (kompilerat), snabbt programmeringsspråk.

Hugo behöver inget PHP och ingen MariaDB (eller MySQL), utan spyr direkt ut färdiga HTML-sidor.


## Vad har Hugo med Wikipedia att skaffa? Källmaterial!

Vi på Fredrika jobbar med Wikipedia, som är beroende av goda källor som är bekväma för Wikipedia att komma åt. Detta är grundorsaken varför vi är begeisrade av Hugo: Med Hugo kan vi göra källmaterial enkelt tillgängligt, enkelt att använda som källor och enkelt att söka sig fram i. Detta är väsentligt för att ge enkelt åtkomst till de basdata som kan matas in i  Wikipedia, Wikidata och Wikimedia Commons – alltså den allmänna, öppna kunskap som är tillgänglig för alla.


## Varför är Hugo bättre för oss? Snabbt, säkert, enkelt!

Nyttan med Hugo kan sammanfattas i tre goda egenskaper. Hugo är: 


1. **Mycket snabb** - nya Hugo-sajten leverar attans snabbt de färdiga (statiska) sidor som Hugo har genererat på förhand. Svarstiden på gamla sajten var över 10 sekunder, och trots försök samt hjälp av diverse kunniga Wordpressexperter kom vi inte underfund med var problemet låg: i Wordpress koden, dess pluginsar eller konfiguration? I databasen? Eller i webhotellet? 
2. **Mycket säker** - det finns inget att logga in i på hemsidan mera. Redigeringar sker på Github och data hämtas från Netlify. Dessa har mycket säkrare autentikeringssystem än en Wordpress-sajt. Vår gamla sajt blev kontinuerligt bombaderad av olovliga försök att logga in, sabotera och göra reklam för än det ena, än det andra. 
3. **Mycket enkel** - sidorna skapas utgående från text skriven i Markdown (likt Markup-koden i Wikipedia). Detta gör det enkelt att göra uppdateringar för den som (likt oss) känner sig bekväm i en texteditor och vilsen bland diverse fönster, menyer, undermenyer och underfönster. Gamla sajten krävde klickande och sökande här och där – och nämnde jag att gamla sajten överlag var långsam? 


## Hur hittade vi Hugo? Via kan.se!

Vi blev tipsade om Hugo av den rikssvenska webbyrån kan.se, när vi skulle bygga om en annan sajt som behövs som källa för Wikipedia. "Ska vi använda existerande Wordpress och existerande teman och existerande strukurer i Wordpress, eller ska vi börja från en färsk Wordpress-sajt?" – det frågade vi. Deras svar var tudelat. "Börja från början, det är enklare!" och "När ni en gång börjar från början, överväg Hugo!". 

Experterna på kan.se som hur artitekturen skulle fungera. Kort sagt lägger man Hugo-sajtens innehåll i kod-förrådet Github och kopplar den till webbhotellet Netlify. Varje gång man gör en ändring i Github, bygger Netlify om sajten utgående från att man kopplat ihop dem. 


## Hur vårt Hugo-bygge gick till 

### A) Början



1. Kollade en 40-minuters introduktion om Hugo på Youtube: [Hugo actually explained](https://www.youtube.com/watch?v=ZFL09qhKi5I)
2. Installerade Hugo på datorn (`brew install hugo`) 
3. Skapade en Hugo-sajt på egna datorn med valt tema enligt Hugos [quickstart](https://gohugo.io/getting-started/quick-start/)
4. Körde kommandot `hugo server` för att kunna kolla lokalt på sajten via adressen [http://localhost:1313/](http://localhost:1313/)

**Mellanresultat:** lokalt åskådlig Hugo sajt

### B) Lägg upp sajten på Github och Netlify



5. Grundade konto och repo på [Github](https://github.com/) 
6. Syncade lokala datorn och repon (en "katalog", ett "lagringsutrymme") med git clone [https://github.com/projekt-fredrika/projektfredrika.fi](https://github.com/projekt-fredrika/projektfredrika.fi), (kopierade in hugo-filerna i mappen), git add ., git commit -m ‘kommentar’, git push -u origin main
7. Grundade konto på [Netlify](https://netlify.com/) - gratis, men kontot är avgiftsbelagd om man vill använda en privat Github repo, om man inte vill att alla ser hemsidornas innehåll
8. Gick igenom Netlifys guidade setup för att länka Netlify till Github. Stegn är beskrivna i: [A step by step Guide: deploying on Netlify](https://www.netlify.com/blog/2016/09/29/a-step-by-step-guide-deploying-on-netlify/)

**Mellanresultat:** sajten från egna datorn gick via Github till Netlify och syns på [projektfredrika.netlify.app ](https://projektfredrika.netlify.app/)

### C) Export från Wordpress, och import till Hugo



9. Skapade lokalt på egen dator markdown-filer av wordpress sajten och lade dem i lokala Hugo-mappen /content/posts. Jag provade ett par olika verktyg, och detta verktyg är verkligen bra som läser WordPress default export XML-fil: [github.com/lonekorean/wordpress-export-to-markdown](https://github.com/lonekorean/wordpress-export-to-markdown)
10. Laddade ner alla bilder från gamla sajten och satt dem i Hugo /static/img
11. Gjorde diverse korrigeringar till sajtens sidors innehåll, bilder, taggar, rubriker och annan formattering genom att
    1. göra “search & replace” med regex med python-kod
    2. skapa listor i excelfiler, editera i Google Sheets, och sedan skapa nya markdown filer, med python-kod
    3. markdown-filernas Front Matter-parametrar ("variabler i början av filen") läste  jag med python från /content/post och sparade till excel, gjorde ändringar och skapade nya md-filer i en temporär mapp innan jag kopierade dem tillbaka till /content/post. Ett bra verktyg för att läsa front matter är  [github.com/eyeseast/python-frontmatter](https://github.com/eyeseast/python-frontmatter) som också stöder skrivande till markdown filer, men den biten tycker jag kunde förbättras i verktyget
* Editerade lokalt på egna datorn, och pushade med jämna mellanrum till Github när jag var nöjd
* I något skede meddelande Netlify om fel som inte uppstod på egna datorn. Då ställde jag in Netlifys build till samma Hugo-version som min lokala (under Site Settings, Environment Variables, Add a variable HUGO_Version)

**Mellanresultat:** ny sajt med gamla inlägg på [https://projektfredrika.netlify.app/](https://projektfredrika.netlify.app/)

### D) Peka domänet på Netlify-sajten



12. Klicka i Netlify “Add a domain” och följde instruktionerna (under Site Settings, Domain management) 
13. Förde in Netlify DNS-inställningar på domän-tjänstens sajt (i vårt fall _websupport.se_) - Netlifys inställningar fungerar bra (en CNAME for www, en A-pekare för apex domänet), men det var lite klurigt att föra in dem i gamla leverantörens kontrollpanel . Det tog ett par justeringar i inställningarna innan mejlet började fungera inklusive SPF inställningar.  
14. När allt fungerade gjorde jag apex domänet (utan www) till Primary Domain (under  Site Settings, Domain management), så att sajten fungerar primärt utan www tillägget i början av projektfredrika.fi

**Slutresultat:** ny sajt på [projektfredrika.fi](https://projektfredrika.fi/)

## Observationer överlag om att överföra sajten till Hugo



* Man kan göra strukturer och lösningar på olika sätt med Hugo, och det kan ta en stund att klura ut vilken metod är optimal för egna sajten - utnyttjar man parametrar eller mappstrukturer? Hur fungerar begreppen single.html, list.html och partials? Det är bara att få ett hum genom dokumentationen och youtube videon, sedan modigt testa!  
* Hugo har utvecklats snabbt på några år, vilket man märker i att bloggar ofta har föråldrade lösningar. En diskussion på Hugo-forumet om en tuggummslösning slutar med “nuförtiden finns det en inbyggd lösning för detta, se Hugos dokumentation”
* Hugos forum är jätte aktivt, och man får snabbt svar på specifika frågor om Hugos teknik 