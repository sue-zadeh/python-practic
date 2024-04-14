colPlanes = {"RegMark":str,"Manufacturer":str,"Model":str,"Seating":int,"MinRunwayLength":int}

dbPlanes = [('ZK-PLB','Pilatus','PC12',9,758),
('ZK-PLS','Pilatus','PC12',9,758),
('ZK-PDM','Cessna','208 Caravan',12,762),
('ZK-SAA','Cessna','208 Caravan',12,762),
('ZK-SAY','Cessna','208 Caravan',12,762),
('ZK-NEE','Bombardier','Q300 Dash 8',50,1178),
('ZK-NEF','Bombardier','Q300 Dash 8',50,1178),
('ZK-NEH','Bombardier','Q300 Dash 8',50,1178),
('ZK-NEJ','Bombardier','Q300 Dash 8',50,1178),
('ZK-NEK','Bombardier','Q300 Dash 8',50,1178)]


## Write a program that displays the name of each manufacturer (once) and then a list of all planes from the manufacturer showing their RegMark and Model
## 
## Hint: Use a flag variable to detect the change in manfacturer
##
## e.g.
## Bombardier
##              ZK-NEE Q300 Dash 8
##              ZK-NEF Q300 Dash 8
