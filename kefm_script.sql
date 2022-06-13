CREATE DATABASE IF NOT EXISTS kefm_python;
USE kefm_python;

CREATE TABLE doctores(
    id              int(25) auto_increment not null,   
    nombre          varchar(255) not null,
    apellidos       varchar(255),
    especialidad    MEDIUMTEXT,
    no_consultorio  int(25),
    dni             int(25) not null,
    email           varchar(255) not null,
    password        varchar(255) not null,
    fecha           date not null,
    CONSTRAINT pk_doctores PRIMARY KEY(id)
)ENGINE=InnoDb;

CREATE TABLE citas(
    id                  int(25) auto_increment not null,
    doctores_id         int(25) not null,
    nombre_paciente     varchar(255) not null,
    descripcion         MEDIUMTEXT,
    fecha_cita          date not null,
    fecha_create        date not null,
    CONSTRAINT pk_citas PRIMARY KEY(id),
    CONSTRAINT fk_cita_doctor FOREIGN KEY(doctores_id) REFERENCES doctores(id)
)ENGINE=InnoDb;