    create table accion (
        id bigint not null,
        descripcion varchar(255) not null,
        fechaFin date not null,
        fechaInicio date not null,
        idAccion integer not null,
        nombre varchar(255) not null,
        programa_id bigint not null,
        primary key (id)
    );

    create table autorizacion (
        id bigint not null,
        descripcion varchar(255) not null,
        idAutorizacion integer not null,
        accion_id bigint,
        primary key (id)
    );

    create table contacto (
        id bigint not null,
        email varchar(255) not null,
        fax varchar(255) not null,
        idContacto integer not null,
        interno varchar(255) not null,
        red varchar(255) not null,
        telefono varchar(255) not null,
        primary key (id)
    );

    create table dependencia (
        id bigint not null,
        descripcion varchar(255) not null,
        idDependencia integer not null,
        nombre varchar(255) not null,
        autorizacion_id bigint,
        programa_id bigint,
        primary key (id)
    );

    create table destinatario (
        id bigint not null,
        descripcion varchar(255) not null,
        idDestinatario integer not null,
        accion_id bigint,
        primary key (id)
    );

    create table equipoTrabajo (
        id bigint not null,
        descripcion varchar(255) not null,
        fechaCreacion date not null,
        idEquipoTrabajo integer not null,
        primary key (id)
    );

    create table escuela (
        id bigint not null,
        ambito varchar(255) not null,
        anexo integer not null,
        codJurisdiccional varchar(255) not null,
        cue integer not null,
        dependencia varchar(255) not null,
        direccion varchar(255) not null,
        idEscuela integer not null,
        nombre varchar(255) not null,
        sector varchar(255) not null,
        primary key (id)
    );

    create table fondos (
        id bigint not null,
        idFondo integer not null,
        monto double not null,
        tipoFinanc varchar(255) not null,
        primary key (id)
    );

    create table instrumentoLegal (
        id bigint not null,
        descripcion varchar(255) not null,
        fecha date not null,
        idInstrumentoLegal integer not null,
        tipoDocLeg varchar(255) not null,
        primary key (id)
    );

    create table localidad (
        id bigint not null,
        codigoPostal integer not null,
        departamento varchar(255) not null,
        idLocalidad integer not null,
        nombre varchar(255) not null,
        region varchar(255) not null,
        accion_id bigint,
        escuela_id bigint,
        primary key (id)
    );

    create table nivel (
        id bigint not null,
        codigoNivel char(1) not null,
        descripcion varchar(255) not null,
        idNivel integer not null,
        escuela_id bigint,
        primary key (id)
    );

    create table persona (
        id bigint not null,
        apellido varchar(255) not null,
        direccion varchar(255) not null,
        dni integer not null,
        edad integer not null,
        idPersona integer not null,
        nacionalidad varchar(255) not null,
        nombre varchar(255) not null,
        contacto_id bigint,
        localidad_id bigint,
        primary key (id)
    );

    create table programa (
        id bigint not null,
        descripcion varchar(255) not null,
        direccion varchar(255) not null,
        fechaCreacion date not null,
        idPrograma integer not null,
        mision varchar(255) not null,
        nombre varchar(255) not null,
        contacto_id bigint,
        equipoTrabajo_id bigint,
        fondos_id bigint,
        instrumentoLegal_id bigint,
        primary key (id)
    );

    create table programa_accion (
        programa_id bigint not null,
        accion_id bigint not null,
        primary key (programa_id, accion_id),
        unique (accion_id)
    );

    create table rol (
        DTYPE varchar(31) not null,
        id bigint not null,
        idRol integer not null,
        idResponsable integer not null,
        idAgente integer not null,
        persona_id bigint,
        programa_id bigint,
        primary key (id)
    );

    create table situacionLaboral (
        id bigint not null,
        codigoCargo integer not null,
        descripcion varchar(255) not null,
        fechaIngreso date not null,
        idSituacionLaboral integer not null,
        tipoCargo char(1) not null,
        persona_id bigint,
        primary key (id)
    );

    create table tarea (
        id bigint not null,
        descripcion varchar(255) not null,
        fechaFin date not null,
        fechaInicio date not null,
        idTarea integer not null,
        nombre varchar(255) not null,
        prioridad integer not null,
        accion_id bigint,
        rol_id bigint,
        primary key (id)
    );

    alter table accion 
        add constraint FK748CB0075D4E7E9C 
        foreign key (programa_id) 
        references programa;

    alter table autorizacion 
        add constraint FKC5FD1832E35532DC 
        foreign key (accion_id) 
        references accion;

    alter table dependencia 
        add constraint FK32D53C66B4E4557C 
        foreign key (autorizacion_id) 
        references autorizacion 
        on delete cascade;

    alter table dependencia 
        add constraint FK32D53C665D4E7E9C 
        foreign key (programa_id) 
        references programa 
        on delete cascade;

    alter table destinatario 
        add constraint FKB7C9F9F1E35532DC 
        foreign key (accion_id) 
        references accion;

    alter table localidad 
        add constraint FK2FA59049E35532DC 
        foreign key (accion_id) 
        references accion;

    alter table localidad 
        add constraint FK2FA59049F5488938 
        foreign key (escuela_id) 
        references escuela;

    alter table nivel 
        add constraint FK47CABE2F5488938 
        foreign key (escuela_id) 
        references escuela;

    alter table persona 
        add constraint FK3AC8678C3D61615C 
        foreign key (contacto_id) 
        references contacto 
        on delete cascade;

    alter table persona 
        add constraint FK3AC8678C9C83E758 
        foreign key (localidad_id) 
        references localidad 
        on delete cascade;

    alter table programa 
        add constraint FKC82F167D3D61615C 
        foreign key (contacto_id) 
        references contacto 
        on delete cascade;

    alter table programa 
        add constraint FKC82F167D60FDF7FC 
        foreign key (instrumentoLegal_id) 
        references instrumentoLegal 
        on delete cascade;

    alter table programa 
        add constraint FKC82F167DEDCE515C 
        foreign key (fondos_id) 
        references fondos 
        on delete cascade;

    alter table programa 
        add constraint FKC82F167D83DA1FD8 
        foreign key (equipoTrabajo_id) 
        references equipoTrabajo 
        on delete cascade;

    alter table programa_accion 
        add constraint FK9DBBC009E35532DC 
        foreign key (accion_id) 
        references Accion;

    alter table programa_accion 
        add constraint FK9DBBC0095D4E7E9C 
        foreign key (programa_id) 
        references programa 
        on delete cascade;

    alter table rol 
        add constraint FK141AF451773F8 
        foreign key (persona_id) 
        references persona;

    alter table rol 
        add constraint FK141AF5D4E7E9C 
        foreign key (programa_id) 
        references programa;

    alter table situacionLaboral 
        add constraint FK547149CC451773F8 
        foreign key (persona_id) 
        references persona;

    alter table tarea 
        add constraint FK4CD86E1ADD1AC18 
        foreign key (rol_id) 
        references rol 
        on delete cascade;

    alter table tarea 
        add constraint FK4CD86E1E35532DC 
        foreign key (accion_id) 
        references accion;
