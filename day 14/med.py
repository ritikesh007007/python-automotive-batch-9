import xml.etree.ElementTree as ET

def extract(file):
    tree = ET.parse(file)
    root = tree.getroot()
    
    data = []
    for med in root.findall('med'):
        data.append(med.text.strip())
    
    
    return sorted(set(data))


issues = extract(r"e:/wipro automotive/day 14/medicle.xml")
for issue in issues:
    print(issue)
    