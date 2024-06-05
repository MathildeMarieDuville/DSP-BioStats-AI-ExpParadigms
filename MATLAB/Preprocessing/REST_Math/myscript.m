h1 = findobj(gcf,'tag','edit1') %get handle of "Edit Text" uicontrol
h2 = findobj(gcf,'tag','edit2') %get handle of "Edit Text" uicontrol
h3 = findobj(gcf,'tag','pushbutton1') %get handle of the push button
feval(get(h3,'Callback'),h3,[]);

A = rand(100,2);

for ii=1:100
    %manually set the 'String' property for the two text fields
    set([h1 h2],{'String'},{A(ii,1);A(ii,2)}); 
    %manually invoke pushbutton callback
    feval(get(h3,'Callback'),h3,[]);
end