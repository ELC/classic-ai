:-dynamic(paciente/3).
:-dynamic(profesional/4).
:-dynamic(turno/6).

inicio:-retractall(paciente(_,_,_)),retractall(profesional(_,_,_,_)),retractall(turno(_,_,_,_,_,_)),abrir_base,menu.

abrir_base:-consult('bdpacientes.txt').

menu:- writeln('ingresar opcion deseada'),
        writeln('OPCION 1: Listar para un paciente y un año las especialidades atendidas'),
        writeln('OPCION 2: Mostrar el nombre y la cantidad de turnos de profesionales donde el monto fue mayor a 10000'),
        writeln('OPCION 3: Salir'),
        read(Op),
        Op < 3,
        opcion(Op),
        menu.

menu:- writeln('Gracias por usar el sistema experto!').

opcion(1):- writeln('Ingrese nombre del paciente'),
            read(NomP),
            paciente(DniP,NomP,_),
            writeln('Ingrese el anio'),
            read(Anio),
            writeln('Las especialidades atendidas fueron:'),
            buscar_especialidades(DniP,Anio,[],ListaEspecialidades),
            listar_especialidades(ListaEspecialidades).

opcion(2):- listar_profesionales.

opcion(_).


buscar_especialidades(Dni,Anio,ListaSinRepetir,[Espe|T]):- turno(Dni,_,Espe,Fecha,_,_),
                                                    retract(turno(Dni,_,Espe,Fecha,_,_)),
                                                    sub_atom(Fecha,_,4,0,Anio),
                                                    not(pertenece(ListaSinRepetir,Espe)),
                                                    buscar_especialidades(Dni,Anio,[Espe|ListaSinRepetir], T).
buscar_especialidades(_,_,_,[]).

pertenece([E|_],E).
pertenece([_|T],E):-pertenece(T,E).

listar_especialidades(L):- writeln(L).
listar_especialidades([]):- writeln('No se encontraron especialidades').

listar_profesionales:- profesional(DniPro,Nom,_,_),
                        retract(profesional(DniPro,Nom,_,_)),
                        contar_pacientes(DniPro,Contador),
                        Contador>0,
                        writeln('Profesional: '),write(Nom),write(' cantidad pacientes:'),write(Contador),writeln(' '),
                        listar_profesionales.
listar_profesionales.

contar_pacientes(Dni,Cont):- turno(_,Dni,_,_,_,Monto),
                                        retract(turno(_,Dni,_,_,_,Monto)),
                                        Monto>15000,
                                        contar_pacientes(Dni,CNuevo),
                                        Cont is CNuevo + 1.

contar_pacientes(_,0).

