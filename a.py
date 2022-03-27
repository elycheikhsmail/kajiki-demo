import kajiki  
def render_template(path:str,d:dict):
    with open(path,"r") as f:
        templateText = f.read()
        Template = kajiki.XMLTemplate(templateText)
        print(Template(d).render())
render_template(
    "index.html",
    dict(title='Kajiki is teh awesome!', repetitions=3)
    )