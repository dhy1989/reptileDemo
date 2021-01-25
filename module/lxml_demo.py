from lxml import etree

text = '''
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book>
    <title lang="en">Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
  <book>
    <title lang="cn">哈利波特</title>
    <author>罗琳</author>
    <year>1989</year>
    <price>29.99</price>
  </book>
</bookstore>
'''

root = etree.HTML(text)
# 从根节点出发获取bookstore
root.xpath('/html/body/bookstore')
# 从bookstore节点出发
print(root.xpath('//bookstore'))
# 获取标签属性
print(root.xpath('//bookstore/book/title/@lang'))
print(root.xpath('//title/@lang'))
# 获取book的文本信息
print(root.xpath('//book/title/text()'))
# 获取第一个book的文本信息
print(root.xpath('//book[1]/title/text()'))
# 获取指定属性的title
print(root.xpath('//title[@lang="cn"]/text()'))