import kajiki  
Template = kajiki.XMLTemplate('''
                              <html>
     <head><title>$title</title></head>
     <body>
         <h1>$title</h1>
         <ul>
             <li py:for="x in range(repetitions)">$title</li>
         </ul>
     </body>
 </html>
 ''')

print(Template(dict(title='Kajiki is teh awesome!', repetitions=3)).render())