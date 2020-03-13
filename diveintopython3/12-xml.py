# examples/feed.xml
<entry>
  <author>                                                                 
    <name>Mark</name>
    <uri>http://diveintomark.org/</uri>
  </author>
  <title>Dive into history, 2009 edition</title>                           
  <link rel='alternate' type='text/html'                                   
    href='http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'/>
  <id>tag:diveintomark.org,2009-03-27:/archives/20090327172042</id>        
  <updated>2009-03-27T21:56:07Z</updated>                                  
  <published>2009-03-27T17:20:42Z</published>        
  <category scheme='http://diveintomark.org' term='diveintopython'/>       
  <category scheme='http://diveintomark.org' term='docbook'/>
  <category scheme='http://diveintomark.org' term='html'/>
  <summary type='html'>Putting an entire chapter on one page sounds        
    bloated, but consider this &amp;mdash; my longest chapter so far
    would be 75 printed pages, and it loads in under 5 seconds&amp;hellip;
    On dialup.</summary>
</entry>                                                                   


>>> import xml.etree.ElementTree as etree 
>>> tree = etree.parse('examples/feed.xml') 
>>> root = tree.getroot() 
>>> root[4].attrib
>>> root.findall('{http://www.w3.org/2005/Atom}entry')
>>> all_links = tree.findall('//{http://www.w3.org/2005/Atom}link')


# For large xml documents, lxml is significantly faster than the built-in ElementTree library. If you’re only using the ElementTree api and want to use the fastest available implementation, you can try to import lxml and fall back to the built-in ElementTree.

try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree

# But lxml is more than just a faster ElementTree. Its findall() method includes support for more complicated expressions.

# To parse this broken xml document, despite its wellformedness error, you need to create a custom xml parser.

>>> parser = lxml.etree.XMLParser(recover=True) 
>>> tree = lxml.etree.parse('examples/feed-broken.xml', parser) 
>>> parser.error_log 
examples/feed-broken.xml:3:28:FATAL:PARSER:ERR_UNDECLARED_ENTITY: Entity 'hellip' not defined
>>> tree.findall('{http://www.w3.org/2005/Atom}title')
[<Element {http://www.w3.org/2005/Atom}title at ead510>]
>>> title = tree.findall('{http://www.w3.org/2005/Atom}title')[0]
>>> title.text 
'dive into '
>>> print(lxml.etree.tounicode(tree.getroot())) 
