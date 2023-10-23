can_fly(bird).

is_fish(X) :- can_swim(X).

is_bird(X) :- can_fly(X).


is_bird(X) :- has_feathers(X).
lives_in_water(X) :- is_fish(X).

is_wet(X) :- lives_in_water(X).

forward_chain :-

    (
        (can_fly(X), \+ is_bird(X)) -> assert(is_bird(X))
    ;   (can_swim(X), \+ is_fish(X)) -> assert(is_fish(X))
    ;   (has_feathers(X), \+ is_bird(X)) -> assert(is_bird(X))
    ;   (is_fish(X), \+ lives_in_water(X)) -> assert(lives_in_water(X))
    ;   (lives_in_water(X), \+ is_wet(X)) -> assert(is_wet(X))
    ),
    forward_chain.




?- forward_chain, is_bird(X).
% Output: X = bird.

?- forward_chain, is_wet(penguin).
% Output: true.

?- forward_chain, can_fly(dog).
% Output: false.
