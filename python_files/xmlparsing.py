
# Example file for parsing and processing XML
import xml.dom.minidom

def main():
    doc=xml.doc.minidom.parse("samplexml.xml")

    print(doc.nodeName)
    print(doc.firstChild.tagName)

    skills=doc.getElementsByTagName("skill")
    print("%d skills:"%skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))

    
    # create a new XML tag and add it into the document
    newSkill=doc.createElement("skill")
    newSkill.setAttribute("name","jQuery")
    doc.firstChild.appendChild(newSkill)

    skills=doc.getElementsByTagName("skill")
    print("%d skills:"%skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))