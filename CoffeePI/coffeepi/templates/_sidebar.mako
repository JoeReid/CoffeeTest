<%inherit file="_base.mako"/>

<%def name="body()">
    <ul>
        <li><a href="#">Option 1</a>
        <li><a href="#">Option 2</a>
        <li><a href="#">Option 3</a>
    </ul>
    
    <div>
        ${next.body()}
    </div>
        
</%def>