has_scales(fish).
has_feathers(bird).
can_fly(bird).
lays_eggs(bird).
has_fur(mammal).
gives_milk(mammal).
has_horns(mammal).
is_cold_blooded(X) :- has_scales(X).
is_warm_blooded(X) :- has_feathers(X).
is_mammal(X) :- has_fur(X), gives_milk(X).
forward_chaining :-
    repeat,
    (   new_fact(Fact),
        assert(Fact),
        write('New fact: '), write(Fact), nl,
        fail
    ;   true
    ).
query_cold_blooded(X) :-
    is_cold_blooded(X),
    write(X), write(' is cold-blooded.').

query_warm_blooded(X) :-
    is_warm_blooded(X),
    write(X), write(' is warm-blooded.').

query_mammal(X) :-
    is_mammal(X),
    write(X), write(' is a mammal.').

%?- forward_chaining.
%?- query_cold_blooded(fish).
%?- query_warm_blooded(bird).
%?- query_mammal(mammal).

