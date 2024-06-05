pop_REST_reref();
% Press Run Button on Graphical Interface
h3 = findobj(pop_REST_reref,'tag','Run_pushbutton3'); %get handle of the push button
feval(get(h3,'Callback'),h3,[]);

% clase graphical interface for REST
close(pop_REST_reref);


