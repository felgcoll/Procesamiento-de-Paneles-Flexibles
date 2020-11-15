%Directorio a recorrer
path='C:\Users\usuario\Desktop\IPP\Procesamiento-de-Paneles-Flexibles\Dataset 10 - Blob Analysis\';
files = dir (strcat(path,'*.jpg'));
L = length (files);

%Directorio a guardar los resultados
folder = 'C:\Users\usuario\Desktop\IPP\Procesamiento-de-Paneles-Flexibles\Dataset 11 - Skeleton\'; 
 
%Iteración sobre el diccionario que contiene los archivos a procesar  
for i=1:L
    
    %Se abre el fichero y el nuevo a guardar
    img = strcat(path,'',files(i).name);
    img_new = strcat(folder,'',files(i).name);
    bn = imread(img);

    %Transforma de 3D a 2D el archivo
    BN = im2bw(bn);

    %Implementación de la operación: 'Esqueletonización'
    BW3 = bwmorph(BN,'skel', Inf);
    
    %Implementación de la operación : 'Eliminación de los 'spurs''      
    %con sus respectivas iteraciones
    bw3 = bwmorph(BW3, 'spur', 200);

    %Guardar los resultados
    imwrite(bw3,img_new);

end