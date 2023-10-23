parent(john, mary).
parent(john, lisa).
parent(mary, ann).
parent(lisa, peter).
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).
goal :-
    grandparent(john, peter).
prove(true) :- !.
prove((Goal1, Goal2)) :-
    prove(Goal1),
    prove(Goal2).
prove(Goal) :-
    clause(Goal, Body),
    prove(Body).

query :-
    goal,
    write('Yes, John is a grandparent of Peter.').

:- query.
