import kajiki  
# "." mean files in current directory and his subdirectories
loader = kajiki.FileLoader(".")

c1 = loader.import_("child.html")
c1_str = c1().render()
print(c1_str)


p1 = loader.import_("parent.html")

print(p1(dict(content=c1_str)).render())

