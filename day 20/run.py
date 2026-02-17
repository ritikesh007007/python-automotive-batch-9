import xml.etree.ElementTree as ET
import os

if not os.path.exists('data.txt'):
    print("Create data.txt first!")
    exit()

vehicles = []
with open('data.txt') as f:
    for line in f:
        if line.strip():
            name, mpg, fuel = line.strip().split(',')
            vehicles.append([name, float(mpg), float(fuel)])

print(f"Loaded {len(vehicles)} cars")

root = ET.Element('vehicles')
for v in vehicles:
    car = ET.SubElement(root, 'car')
    car.set('model', v[0])
    ET.SubElement(car, 'mileage').text = str(v[1])
    ET.SubElement(car, 'fuel').text = str(v[2])

tree = ET.ElementTree(root)
ET.indent(tree, space="  ", level=0)  
tree.write('output.xml', encoding='utf-8', xml_declaration=True)

print(" output.xml created ")
