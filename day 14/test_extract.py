import pytest
import xml.etree.ElementTree as ET
from med import extract  

def test_real_medicle_file():
  
    result = extract(r"e:/wipro automotive/day 14/medicle.xml")
    
  
    expected = ['Allergy', 'Arthritis', 'Asthma', 'Cancer', 
                'Depression', 'Diabetes', 'Headache', 'Hypertension']
    
    assert len(result) >= 8
    assert result == sorted(set(result))  
    print(" file file works!")
    print("Found issues:", result)


