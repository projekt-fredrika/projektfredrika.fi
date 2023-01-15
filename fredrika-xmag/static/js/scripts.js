function makeSPARQLQuery( endpointUrl, sparqlQuery, doneCallback ) {
	var settings = {
		headers: { Accept: 'application/sparql-results+json' },
		data: { query: sparqlQuery }
	};
	return $.ajax( endpointUrl, settings ).then( doneCallback );
}

var elem = document.getElementById('wikipedia');
var wikidata = elem.getAttribute('data-wikidata');

var endpointUrl = 'https://query.wikidata.org/sparql',
	sparqlQuery = "SELECT ?itemLabel ?wikipage_title ?l ?wikipageLabel WHERE {\n" +
        " #  hint:Query hint:optimizer \"None\".\n" +
        "   VALUES ?item {wd:"+ wikidata +"}\n" +
        "   ?wikipage schema:about ?item . \n" +
        "   ?wikipage schema:isPartOf/wikibase:wikiGroup \"wikipedia\" .\n" +
        "   ?wikipage schema:name ?wikipage_title.\n" +
        "   ?wikipage schema:isPartOf ?lang.\n" +
        "   BIND(REPLACE(STR(?lang),\"https://|\\\\.wikipedia\\\\.org/\",\"\") AS ?l)\n" +
        "  SERVICE wikibase:label { bd:serviceParam wikibase:language \"sv\". }\n" +
        "} ORDER BY ?l";

makeSPARQLQuery( endpointUrl, sparqlQuery, function( data ) {

text = JSON.stringify( data )
console.log('text:', text);
obj = JSON.parse( text )

title = obj.results.bindings[0].itemLabel.value
output =  "Wikipedia: "
for (var i = 0; i < obj.results.bindings.length; i++){
  output += "<a href='"+obj.results.bindings[i].wikipageLabel.value +"'>" + obj.results.bindings[i].l.value + "</a>; ";
}
output += " Wikidata: <a href='https://www.wikidata.org/wiki/"+wikidata+"'>"+wikidata+"</a>"
$('#wikipedia').append(output);

//$('#anchor2').append( $( '<p>' ).text( obj.results.bindings[0].itemLabel.value ) );  

} );