
male(john).
male(mike).
male(bob).
female(lisa).
female(sarah).
female(emily).
parent(john, mike).
parent(john, lisa).
parent(mike, sarah).
parent(lisa, emily).
parent(bob, john).

father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
