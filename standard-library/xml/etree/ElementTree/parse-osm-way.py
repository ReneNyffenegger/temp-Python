import xml.etree.ElementTree as ET

xml = ET.fromstring('''<?xml version="1.0" encoding="UTF-8"?>
<osm version="0.6" generator="CGImap 0.8.8 (3313918 spike-07.openstreetmap.org)" copyright="OpenStreetMap and contributors" attribution="http://www.openstreetmap.org/copyright" license="http://opendatacommons.org/licenses/odbl/1-0/">
 <node id="581359396" visible="true" version="5" changeset="92639725" timestamp="2020-10-17T19:15:24Z" user="Geonick" uid="6087" lat="47.5338731" lon="8.5871862"/>
 <node id="581359397" visible="true" version="5" changeset="92639725" timestamp="2020-10-17T19:15:24Z" user="Geonick" uid="6087" lat="47.5339712" lon="8.5871983"/>
 <node id="581359399" visible="true" version="5" changeset="92639725" timestamp="2020-10-17T19:15:24Z" user="Geonick" uid="6087" lat="47.5338817" lon="8.5870351"/>
 <node id="581359400" visible="true" version="5" changeset="92639725" timestamp="2020-10-17T19:15:24Z" user="Geonick" uid="6087" lat="47.5339797" lon="8.5870473"/>
 <node id="2293870143" visible="true" version="4" changeset="92639725" timestamp="2020-10-17T19:15:24Z" user="Geonick" uid="6087" lat="47.5338775" lon="8.5871078"/>
 <node id="10700033845" visible="true" version="1" changeset="133139768" timestamp="2023-02-28T17:51:09Z" user="Heloks" uid="11582591" lat="47.5339318" lon="8.5870412"/>
 <way id="45593112" visible="true" version="8" changeset="133139768" timestamp="2023-02-28T17:51:09Z" user="Heloks" uid="11582591">
  <nd ref="581359400"/>
  <nd ref="581359397"/>
  <nd ref="581359396"/>
  <nd ref="2293870143"/>
  <nd ref="581359399"/>
  <nd ref="10700033845"/>
  <nd ref="581359400"/>
  <tag k="access" v="yes"/>
  <tag k="addr:city" v="Freienstein"/>
  <tag k="addr:country" v="CH"/>
  <tag k="addr:housenumber" v="1"/>
  <tag k="addr:postcode" v="8427"/>
  <tag k="addr:street" v="Zur Burg"/>
  <tag k="alt_name" v="Burg Alten-Teufen"/>
  <tag k="building" v="yes"/>
  <tag k="castle_type" v="defensive"/>
  <tag k="historic" v="castle"/>
  <tag k="historic:civilization" v="medieval"/>
  <tag k="name" v="Ruine Freienstein"/>
  <tag k="ruins" v="yes"/>
  <tag k="wikidata" v="Q2175266"/>
  <tag k="wikipedia" v="de:Ruine Freienstein"/>
 </way>
</osm>
''')

# print(type(xml))

way=xml.find('way')
# print(type(way))

for nd in way.findall('nd'):
    node_id = nd.get('ref')
    node = xml.find(f"node[@id='{node_id}']")
    lat = float(node.get("lat"))
    lon = float(node.get("lon"))
    print(f'{node_id}: {lat} {lon}')


for tag in way.findall('tag'):
    print(f'{tag.get("k")}: {tag.get("v")}')
