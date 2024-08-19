drop DATABASE db_poo;
create DATABASE db_poo;
use db_poo;
CREATE TABLE usuario (
  id int(5) PRIMARY KEY auto_increment,
  nombre varchar(20),
  telefono varchar(20),
  email varchar(30)
) engine=InnoDB charset=latin1;
insert into usuario(nombre,telefono,email)
values ('Jaime','99887766','jf@abc.com');
