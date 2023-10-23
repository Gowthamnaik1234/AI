
heuristic(Node, H) :-

    H is abs(Node - 10).


goal_state(Goal) :-

    Goal = 10.


best_first_search(Start, Solution) :-

    heuristic(Start, H),
    Node = node(Start, H, []),
    best_first_search_helper([Node], [], Solution).


best_first_search_helper([node(State, _, Path) | _], _, Path) :-
    goal_state(State).
 Recursive case: Expand the best node based on the heuristic.
best_first_search_helper(OpenList, ClosedList, Solution) :-
    select_best_node(OpenList, BestNode),                                         remove(BestNode, OpenList, UpdatedOpenList),
    expand_node(BestNode, ClosedList, UpdatedOpenList, NewNodes),
    append(ClosedList, [BestNode], UpdatedClosedList),
    best_first_search_helper(NewNodes, UpdatedClosedList, Solution).


select_best_node([Node | Rest], BestNode) :-
    select_best_node(Rest, Node, BestNode).

select_best_node([], BestNode, BestNode).
select_best_node([Node | Rest], BestSoFar, BestNode) :-
    node_heuristic(Node, H1),
    node_heuristic(BestSoFar, H2),
    (H1 < H2 -> select_best_node(Rest, Node, BestNode); select_best_node(Rest, BestSoFar, BestNode)).

% Calculate the heuristic value of a node.
node_heuristic(node(_, Heuristic, _), Heuristic).

% Remove an element from a list.
remove(X, [X | Tail], Tail).
remove(X, [Y | Tail], [Y | NewTail]) :- remove(X, Tail, NewTail).

% Expand a node by generating its successors.
expand_node(node(State, _, Path), ClosedList, OpenList, NewNodes) :-
    findall(node(ChildState, ChildHeuristic, [State | Path]),
        (generate_successor(State, ChildState), \+ member(node(ChildState, _, _), ClosedList)),
        Children),
    append(Children, OpenList, NewNodes).


generate_successor(State, ChildState) :-
    State < 10,
    ChildState is State + 1.


?- best_first_search(5, Solution).
