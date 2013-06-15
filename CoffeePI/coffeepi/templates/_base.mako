<html>
    <head>
        <%def name="title()">Coffee PI</%def>
        <title>${self.title()}</title>
    </head>
    
    <body>
        <h1>this is a test ${a}</h1>
        
        ${next.body()}
    </body>
</html>