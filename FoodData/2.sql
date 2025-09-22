SELECT * FROM public.food_nutrient
ORDER BY id ASC 


alter table food_nutrient
DROP COLUMN data_points,
DROP COLUMN derivation_id


CREATE TABLE food_category (
	id INTEGER PRIMARY KEY,
	code INTEGER,
	description varchar(50)
);

create table food_nutrient (
	id integer primary key,
	fdc_id integer,
	nutrient_id integer,
	amount decimal,
	data_points integer,
	derivation_id integer	
)

create table food (
	fdc_id integer primary key,
	data_type varchar(50),
	description varchar(50),
	food_category_id integer,
	publication_date date
)

alter table food
alter column description type varchar(255)

create table nutrient (
	id integer primary key,
	name varchar(50),
	unit_name varchar(10),
	nutrient_nbr integer,
	rank integer
)

alter table nutrient
alter column nutrient_nbr type decimal

alter table nutrient
alter column name type varchar(255)


