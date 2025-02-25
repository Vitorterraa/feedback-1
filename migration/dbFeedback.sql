create database db_feedback;

use db_feedback;

create table tb_comentarios(
nome varchar(50) not null,
data_hora datetime not null,
comentario text not null,
cod_comentario int primary key auto_increment
);

