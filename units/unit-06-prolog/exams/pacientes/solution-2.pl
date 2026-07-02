:-dynamic(paciente/3).
:-dynamic(profesional/4).
:-dynamic(turno/6).

inicio:-retractall(paciente(_,_,_)),retractall(profesional(_,_,_,_)),retractall(turno(_,_,_,_,_,_)),menu.

menu:- writeln('Ingrese opcion:'),
        writeln('OPCION 0: Salir'),
        writeln('OPCION 1: Para un paciente y un año, determinar las especialidades atendidas'),
        writeln('OPCION 2: Mostrar profesionales con turnos con montos mayores de 1500'),
        read(Op),
        Op\=0,
        Op<3,
        opcion(Op),
        menu.

menu:- writeln('Gracias por usar el sistema experto!').

opcion(1):- abrir_base,
            writeln('Ingrese nombre paciente'),
            read(Nom),
            paciente(Dni,Nom,_),
            writeln('Ingrese anio'),
            read(Anio),
            writeln('Las especialidades encontradas son:'),
            buscar_especialidades(Dni,Anio,[]).

opcion(2):- abrir_base,
            buscar_profesionales.

opcion(_).

abrir_base:-consult('bdpacientes-2.txt').

buscar_especialidades(Dni,Anio,ListaSinRep):- turno(Dni,_,Esp,Fecha,_,_),
                                    retract(turno(Dni,_,Esp,Fecha,_,_)),
                                    sub_atom(Fecha,_,4,0,Anio),
                                    not(pertenece(Esp,ListaSinRep)),
                                    writeln(Esp),
                                    buscar_especialidades(Dni,Anio,[Esp|ListaSinRep]).
buscar_especialidades(_,_,_).

pertenece(H,[H|_]).
pertenece(H,[_|T]):-pertenece(H,T).

buscar_profesionales:- retract(profesional(Dni,Nom,_,_)),
                        contar(Dni,Cont),
                        Cont>0,
                        write('Profesional: '),write(Nom),write(' con '),write(Cont),writeln(' turnos de montos mayores a 1500'),
                        buscar_profesionales.
buscar_profesionales.

contar(Dni,C):- retract(turno(_,Dni,_,_,_,Monto)),
                Monto>1500,
                contar(Dni,CNuevo),
                C is CNuevo + 1.
contar(_,0).

