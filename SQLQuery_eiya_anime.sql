create table animes(
id_anime int not null primary key,
nome_anime varchar(120) not null,
data_lancamento_anime date not null,
criador varchar(255) not null,
logo_anime varchar(255) not null,
dublagem varchar(20) not null,
descricao varchar(255) not null
)
alter table animes alter column descricao varchar(max) not null


create table trailers(
id_anime int not null foreign key references animes,
trailer varchar(255) not null
)


create table temporadas(
id_anime int not null foreign key references animes,
num_temporada int not null,
data_lancamento_temporada date not null,
img_temporada varchar(255) not null
)
alter table temporadas add id_temporada int not null primary key


create table capitulos(
id_anime int not null foreign key references animes,
num_temporada int not null foreign key references temporadas,
id_capitulos int not null,
data_lancamento_capitulo date not null,
thumbnail varchar(255) not null,
video varchar(255) not null
)
alter table capitulos add primary key(id_anime,num_temporada,id_capitulos) 
alter table capitulos drop column thumbnail


create table ligacao_generos(
id_anime int not null foreign key references animes,
id_genero int not null foreign key references generos
)


create table generos(
id_genero int not null primary key,
nome_genero varchar(20) not null,
)






select * from animes
insert into animes values(1,'Vanitas no Carte','22/12/2015','Jun Mochizuki',
'C:\Users\Aluno\Desktop\eiya_animes-main\static\img\logo_animes\1.jpg',
'pt-br','Era uma vez um vampiro conhecido como Vanitas, odiado por sua própria espécie por ter nascido sob uma lua cheia azul, já que a maioria surge na noite de uma lua vermelha. Com medo e sozinho, ele criou o "Livro de Vanitas", um grimório amaldiçoado que um dia se vingaria de todos os vampiros; é assim que a história vai, pelo menos. Vanitas no Carte segue Noé, um jovem viajando a bordo de uma aeronave na Paris do século 19 com um objetivo em mente: encontrar o Livro de Vanitas. Um ataque repentino de vampiro o leva a conhecer a enigmática Vanitas, uma médica que se especializou em vampiros e, para a surpresa de Noé, um humano completamente comum. O misterioso médico herdou o nome e o texto infame dos Vanitas da lenda, usando o grimório para curar seus pacientes. Mas por trás de sua atitude gentil está algo um pouco mais sinistro ...')

insert into animes values(2,'One Piece','22/12/2015','Jun Mochizuki',
'C:\Users\Aluno\Desktop\eiya_animes-main\static\img\logo_animes\1.jpg',
'pt-br','Era uma vez um vampiro conhecido como Vanitas, odiado por sua própria espécie por ter nascido sob uma lua cheia azul, já que a maioria surge na noite de uma lua vermelha. Com medo e sozinho, ele criou o "Livro de Vanitas", um grimório amaldiçoado que um dia se vingaria de todos os vampiros; é assim que a história vai, pelo menos. Vanitas no Carte segue Noé, um jovem viajando a bordo de uma aeronave na Paris do século 19 com um objetivo em mente: encontrar o Livro de Vanitas. Um ataque repentino de vampiro o leva a conhecer a enigmática Vanitas, uma médica que se especializou em vampiros e, para a surpresa de Noé, um humano completamente comum. O misterioso médico herdou o nome e o texto infame dos Vanitas da lenda, usando o grimório para curar seus pacientes. Mas por trás de sua atitude gentil está algo um pouco mais sinistro ...')

insert into animes values(3,'Over Lord','22/12/2015','Jun Mochizuki',
'C:\Users\Aluno\Desktop\eiya_animes-main\static\img\logo_animes\1.jpg',
'pt-br','Era uma vez um vampiro conhecido como Vanitas, odiado por sua própria espécie por ter nascido sob uma lua cheia azul, já que a maioria surge na noite de uma lua vermelha. Com medo e sozinho, ele criou o "Livro de Vanitas", um grimório amaldiçoado que um dia se vingaria de todos os vampiros; é assim que a história vai, pelo menos. Vanitas no Carte segue Noé, um jovem viajando a bordo de uma aeronave na Paris do século 19 com um objetivo em mente: encontrar o Livro de Vanitas. Um ataque repentino de vampiro o leva a conhecer a enigmática Vanitas, uma médica que se especializou em vampiros e, para a surpresa de Noé, um humano completamente comum. O misterioso médico herdou o nome e o texto infame dos Vanitas da lenda, usando o grimório para curar seus pacientes. Mas por trás de sua atitude gentil está algo um pouco mais sinistro ...')


select * from generos
insert into generos values(1,'Ação')
insert into generos values(2,'Artes Marciais')
insert into generos values(3,'Aventura')
insert into generos values(4,'Comédia')
insert into generos values(5,'Drama')
insert into generos values(6,'Escolar')
insert into generos values(7,'Esporte')
insert into generos values(8,'Ecchi')
insert into generos values(9,'Harém')
insert into generos values(10,'Hentai')
insert into generos values(11,'Isekai')
insert into generos values(12,'Iyashikei')
insert into generos values(13,'Josei')
insert into generos values(14,'Magia')
insert into generos values(15,'Mecha')
insert into generos values(16,'Mistério')
insert into generos values(17,'Música')
insert into generos values(18,'Psicológico')
insert into generos values(19,'Romance')
insert into generos values(20,'Sci-Fi')
insert into generos values(21,'Seinen')
insert into generos values(22,'Shoujo')
insert into generos values(23,'Shounen')
insert into generos values(24,'Slice of Life')
insert into generos values(25,'Sobrenatural')
insert into generos values(26,'SuperPoderes')
insert into generos values(27,'Terror')
insert into generos values(28,'Yaoi')
insert into generos values(29,'Yuri')
insert into generos values(30,'Fantasia')
insert into generos values(31,'Vampiros')


select * from ligacao_generos
insert into ligacao_generos values(1,25)
insert into ligacao_generos values(1,31)
insert into ligacao_generos values(1,30)
insert into ligacao_generos values(1,23)


select * from trailers
insert into trailers values(1,'C:\Users\Aluno\Desktop\eiya_animes-main\static\video\trailers\1\1.mp4')


select * from temporadas
insert into temporadas values(1,1,'22/12/2015','C:\Users\Aluno\Desktop\eiya_animes-main\static\img\temporadas\1\1.jpg',1)


select * from capitulos
insert into capitulos values(1,1,1,'06/08/2021','C:\Users\Aluno\Desktop\eiya_animes-main\static\video\capitulos\1\1\1.mp4')
insert into capitulos values(2,1,1,'06/08/2021','C:\Users\Aluno\Desktop\eiya_animes-main\static\video\capitulos\1\1\2.mp4')
insert into capitulos values(3,1,1,'06/08/2021','C:\Users\Aluno\Desktop\eiya_animes-main\static\video\capitulos\1\1\3.mp4')
insert into capitulos values(4,1,1,'06/08/2021','C:\Users\Aluno\Desktop\eiya_animes-main\static\video\capitulos\1\1\4.mp4')
insert into capitulos values(5,1,1,'06/08/2021','C:\Users\Aluno\Desktop\eiya_animes-main\static\video\capitulos\1\1\5.mp4')
insert into capitulos values(6,1,1,'06/08/2021','C:\Users\Aluno\Desktop\eiya_animes-main\static\video\capitulos\1\1\6.mp4')
insert into capitulos values(7,1,1,'06/08/2021','C:\Users\Aluno\Desktop\eiya_animes-main\static\video\capitulos\1\1\7.mp4')
insert into capitulos values(8,1,1,'06/08/2021','C:\Users\Aluno\Desktop\eiya_animes-main\static\video\capitulos\1\1\8.mp4')
insert into capitulos values(9,1,1,'06/08/2021','C:\Users\Aluno\Desktop\eiya_animes-main\static\video\capitulos\1\1\9.mp4')
insert into capitulos values(10,1,1,'06/08/2021','C:\Users\Aluno\Desktop\eiya_animes-main\static\video\capitulos\1\1\10.mp4')
insert into capitulos values(11,1,1,'06/08/2021','C:\Users\Aluno\Desktop\eiya_animes-main\static\video\capitulos\1\1\11.mp4')
insert into capitulos values(12,1,1,'06/08/2021','C:\Users\Aluno\Desktop\eiya_animes-main\static\video\capitulos\1\1\12.mp4')

select * from animes

select count(*) from animes