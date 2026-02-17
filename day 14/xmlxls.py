#parsin/paerser :
#xml : extensible markup language
#rss : rich site summary

import xml.etree.ElementTree as ET

ddef extract(file):
    tree=parse(ile)
    root=tree.getroot()

data=[]
    for note in root.findall('med'):