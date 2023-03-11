CREATE TABLE ТРАНСПОРТ(
	НОМЕР_ТРАНСПОРТНОГО_СРЕДСТВА VARCHAR (10) NOT NULL, 
	ГАРАЖНЫЙ_НОМЕР VARCHAR(10)PRIMARY KEY NOT NULL,
	ТИП_ТРАНСПОРТА VARCHAR(50)NOT NULL,
	ГОД_ВЫПУСКА_ТРАНСПОРТА DATE NOT NULL,
	ДАТА_ТЕХОСМОТРА DATE NOT NULL,
	КОЛИЧЕСТВО_ПОСАДОЧНЫХ_МЕСТ INT NOT NULL,
	НОМЕР_МАРШРУТА CHAR(5) NOT NULL,
	НОМЕР_ДЕПО VARCHAR(10) NOT NULL);

CREATE TABLE СОТРУДНИКИ (
    ТАБЕЛЬНЫЙ_НОМЕР VARCHAR(10)PRIMARY KEY NOT NULL,
    ИМЯ VARCHAR(50)NOT NULL,
    ОТЧЕСТВО VARCHAR(50) NOT NULL,
    ФАМИЛИЯ VARCHAR(50) NOT NULL,
    ДОЛЖНОСТЬ VARCHAR(50) NOT NULL,
	СТАЖ_РАБОТЫ INT NOT NULL,
	ДАТА_ПРИЕМА_НА_РАБОТУ DATE NOT NULL,
	ПОЛ VARCHAR(10) NOT NULL,
	ДАТА_РОЖДЕНИЯ DATE NOT NULL
);

CREATE TABLE УДОСТОВЕРЕНИЯ(
    ТАБЕЛЬНЫЙ_НОМЕР VARCHAR(10)PRIMARY KEY NOT NULL,
    ВИД_УДОСТОВЕРЕНИЯ VARCHAR(50) NOT NULL,
    НОМЕР_УДОСТОВЕРЕНИЯ VARCHAR(10) NOT NULL,
    ДАТА_ВЫДАЧИ DATE NOT NULL,
    ДАТА_ЭКСПИРАЦИИ DATE NOT NULL,
    КОММЕНТАРИЙ VARCHAR(70)
	
);

CREATE TABLE КОНТАКТНЫЕ_ДАННЫЕ_СОТРУДНИКОВ(
    ТАБЕЛЬНЫЙ_НОМЕР VARCHAR(10)PRIMARY KEY NOT NULL,
    ГОРОД VARCHAR(50) NOT NULL,
    УЛИЦА VARCHAR(70) NOT NULL,
    НОМЕР_ДОМА VARCHAR(10) NOT NULL,
    НОМЕР_КВАРТИРЫ VARCHAR(10),
    НОМЕР_ТЕЛЕФОНА VARCHAR(70) NOT NULL,
    КОММЕНТАРИЙ VARCHAR(70)

);

CREATE TABLE РАСПИСАНИЕ(
    ГАРАЖНЫЙ_НОМЕР VARCHAR(10) NOT NULL,
    НОМЕР_МАРШРУТА CHAR(5) NOT NULL,
   	ОСТАНОВКА VARCHAR(70) NOT NULL,
	ВРЕМЯ_ПРИБЫТИЯ TIME NOT NULL,
    ВРЕМЯ_ПРИБЫТИЯ1 TIME NOT NULL,
    ВРЕМЯ_ПРИБЫТИЯ2 TIME NOT NULL,
    ВРЕМЯ_ПРИБЫТИЯ3 TIME NOT NULL
);


CREATE TABLE ГРАФИК_РАБОТЫ(
    ТАБЕЛЬНЫЙ_НОМЕР VARCHAR(10)PRIMARY KEY NOT NULL,
    ПОНЕДЕЛЬНИК CHAR,
	ВТОРНИК CHAR,
	СРЕДА CHAR,
	ЧЕТВЕРГ CHAR,
	ПЯТНИЦА CHAR,
	СУББОТА CHAR,
	ВОСКРЕСЕНЬЕ CHAR,
	НОМЕР_МАРШРУТА CHAR(5),
	ВРЕМЯ_ВЫХОДА_НА_МАРШРУТ TIME NOT NULL,
    ВРЕМЯ_ОКОНЧАНИЯ_РАБОТЫ TIME NOT NULL
);

CREATE TABLE ДЕПО(
    НОМЕР_ДЕПО VARCHAR(10)PRIMARY KEY NOT NULL,
    ГОРОД VARCHAR(50) NOT NULL,
    УЛИЦА VARCHAR(70) NOT NULL,
    НОМЕР_ЗДАНИЯ CHAR (5) NOT NULL,
    НОМЕР_ТЕЛЕФОНА VARCHAR(70) NOT NULL,
    ФАКС VARCHAR(70),
    КОММЕНТАРИЙ VARCHAR(70)

);

CREATE TABLE ЗАРАБОТНАЯ_ПЛАТА(
    ТАБЕЛЬНЫЙ_НОМЕР VARCHAR(10)PRIMARY KEY NOT NULL,
    ОКЛАД DOUBLE NOT NULL,
    КОММЕНТАРИЙ VARCHAR(70)

);
