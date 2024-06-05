function marimekkoh(A, class, groups)
%marimekko chart that takes A: matrix of numbers and y the names to each
%index
cmap = colormap(parula(length(A(:,1))));
pxold = 0;
tot = sum(sum(A));
for i = 1:length(A(1,:))
    a_1(i) = sum(A(:,i));
    pxold(i+1) = a_1(i)/tot+pxold(i); pyold(1) = 0;
    for k = 1:length(A(:,1))
        if A(k,i) == 0
        else
            p1 = [pxold(i)             pyold(k)];
            p2 = [a_1(i)/tot+pxold(i)  pyold(k)];
            p3 = [a_1(i)/tot+pxold(i)  A(k,i)/a_1(i)+pyold(k)];
            p4 = [pxold(i)             A(k,i)/a_1(i)+pyold(k)];
            pyold(k+1) = p3(2);       
            x = [p1(1) p2(1) p3(1) p4(1)];
            y = [p1(2) p2(2) p3(2) p4(2)];
            p(i,k) = patch(y,x,'k');
            set(p(i,k),'Facecolor',cmap(k,:))
            set(p(i,k),'FaceAlpha',0.35)  
%             t = text(p1(2)+0.5*(p3(2)-pyold(k)),p1(1)+0.5*(p3(1)-pxold(i)),...
%                 strcat(num2str(A(k,i),'%10.0f')),...
%                 'HorizontalAlignment','center');
             t = text(p1(2)+0.75*(p3(2)-pyold(k)),p1(1)+0.5*(p3(1)-pxold(i)),...
                strcat(num2str(A(k,i),'%10.0f')),...
                'HorizontalAlignment','center'); %FOR PDF REPORT
%             t.FontSize = round(10+40*A(k,i)/tot); t.FontName = 'Helvetica';
            t.FontSize = 27; t.FontName = 'Helvetica'; 
            % FOR PDF REPORT
            if k == 1 
%                 t2 = text(p1(2)+0.2*(p3(2)-pyold(k)),p1(1)+0.65*(p3(1)-pxold(i)),...
%                     sprintf('%s \n %s',class(i,1)),...
%                     'HorizontalAlignment','center', 'FontWeight', 'bold');
                t2 = text(p1(2)+0.35*(p3(2)-pyold(k)),p1(1)+0.65*(p3(1)-pxold(i)),...
                    sprintf('%s \n %s',class(i,1)),...
                    'HorizontalAlignment','center', 'FontWeight', 'bold'); 
%                 FOR PDF REPORT
%                 t2.FontSize = round(10+40*A(k,i)/tot); t.FontName = 'Helvetica';    
                  t2.FontSize = 25; t.FontName = 'Helvetica';    
            end
        end
    end
    t1 = text(-0.01,p1(1)+0.4*(p3(1)-pxold(i)),...
        sprintf('%s',groups{i}),...
        'HorizontalAlignment','right', 'FontWeight', 'bold');
    
%     t1.FontSize = 10; t1.FontName = 'Helvetica'; 
      t1.FontSize = 25; t1.FontName = 'Helvetica'; %PDF

end
ylim([0 1]); x1 = xlabel('Número de niño(a)s (%)', ...
    'fontweight','bold','fontsize',16); 
xlim([0 1]); 
xticks([round(pxold*1e2)/1e2]);
set(gcf,'PaperPositionMode','auto','paperorientation','landscape');
set(gcf,'PaperPosition',[0 0 30 12]); set(gcf,'PaperSize',[30 12]);
set(gcf,'Color','white');
set(gca,'YDir','reverse');
end