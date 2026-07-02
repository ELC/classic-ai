inicio :- write('ingrese una palabra:'),read(A),tipo(A).

tipo(A) :- atom_length(A,N), N>0, sub_atom(A,0,1,N1,C),
sub_atom(A,1,N1,_,A1), digtongo(C,A1).
tipo(A) :- atom_length(A,N), N>0, sub_atom(A,0,1,N1,C),
sub_atom(A,1,N1,_,A1), hiato(C,A1).
tipo(_) :- write('No es Digtongo/Hiato').

digtongo(C,A) :- atom_length(A,N), N>0, sub_atom(A,0,1,_,C1),
esAbierta(C), esCerrada(C1), write('Es Digtongo').
digtongo(C,A) :- atom_length(A,N), N>0, sub_atom(A,0,1,_,C1),
esCerrada(C), esCerrada(C1), C \= C1, write('Es Digtongo').
digtongo(C,A) :- atom_length(A,N), N>0, sub_atom(A,0,1,_,C1),
esCerrada(C), esAbierta(C1), write('Es Digtongo').
digtongo(_,A) :- atom_length(A,N), N>0, sub_atom(A,0,1,N1,C1),
sub_atom(A,1,N1,_,A1), digtongo(C1,A1).

hiato(C,A) :- atom_length(A,N), N>0, sub_atom(A,0,1,_,C1),
esAbierta(C), esAbierta(C1), write( 'Es Hiato' ).
hiato(_,A) :- atom_length(A,N), N>0, sub_atom(A,0,1,N1,C1),
sub_atom(A,1,N1,_,A1), hiato(C1,A1).

esAbierta('a').
esAbierta('e').
esAbierta('o').
esCerrada('i').
esCerrada('u').
