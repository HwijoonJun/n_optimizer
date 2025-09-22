

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
);

create table food (
	fdc_id integer primary key,
	data_type varchar(50),
	description varchar(255),
	food_category_id integer,
	publication_date date
);

create table nutrient (
	id integer primary key,
	name varchar(255),
	unit_name varchar(10),
	nutrient_nbr decimal,
	rank integer
);
