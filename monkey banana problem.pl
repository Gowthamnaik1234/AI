
at(door, s0).
at(bananas, s0, ceiling).
at(monkey, s0, door).
has(monkey, s0, no).


% Action: walk
can(walk, S) :-
    at(monkey, S, X),
    at(X, S).

% Action: climb
can(climb, S) :-
    at(monkey, S, chair).

% Action: push
can(push, S) :-
    at(monkey, S, chair),
    at(chair, S, X),
    at(X, S).

% Action: grab
can(grab, S) :-
    at(monkey, S, X),
    at(bananas, S, X),
    has(monkey, S, no).


% After climbing, the monkey is on the chair.
result(climb, S, S1) :-
    at(monkey, S, chair),
    at(chair, S, X),
    at(monkey, S1, X).

% After walking, the monkey is at the other location.
result(walk, S, S1) :-
    at(monkey, S, X),
    at(X, S, Y),
    at(monkey, S1, Y).

% After pushing, the chair is at the other location.
result(push, S, S1) :-
    at(monkey, S, chair),
    at(chair, S, X),
    at(X, S, Y),
    at(chair, S1, Y).

% After grabbing, the monkey has the bananas.
result(grab, S, S1) :-
    at(monkey, S, X),
    at(bananas, S, X),
    has(monkey, S1, yes).

% Define a goal state where the monkey has the bananas.
goal_state(S) :-
    has(monkey, S, yes).

% Plan to reach the goal state using a depth-first search.
plan(S, Plan) :-
    depth_first(S, Plan, [S], 10).

% Base case for the depth-first search (no actions to take).
depth_first(S, [], _, _) :-
    goal_state(S).

% Depth-first search with a limit on the number of actions.
depth_first(S, [Action | Rest], Visited, Limit) :-
    Limit > 0,
    can(Action, S),
    result(Action, S, S1),
    not(member(S1, Visited)),
    depth_first(S1, Rest, [S1 | Visited], Limit - 1).


execute_plan([Action | Rest], S, S1) :-
    can(Action, S),
    result(Action, S, S1),
    write('Action: '), write(Action), nl,
    execute_plan(Rest, S1, _).
execute_plan([], S, S).


% Example: To solve the problem, call:
% ?- plan(s0, Plan), execute_plan(Plan, s0, _).
