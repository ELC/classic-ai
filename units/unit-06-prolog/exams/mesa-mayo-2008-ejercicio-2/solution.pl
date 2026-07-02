inicio:-write('Ingrese lista de numeros: '), leer( L ) , listaDif( L, LR ),
write('lista Diferencias:'), write(LR).

listaDif( [],[]).
listaDif( [H1|L],LR ):- dif(H1, L, LR), ascii('a').

dif(_,[],[]).
dif( H1, [H2|L], [H|LR] ):- H is H2-H1, dif(H2, L, LR).

leer([H|T]):-read(H), H \= [], leer(T).
leer([]).
