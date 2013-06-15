<%inherit file="_sidebar.mako"/>

<%def name="title()">CoffeePI - Test</%def>

<%def name="body()">
test

    % for member in members:
        ${member.name}
    % endfor
    
</%def>
