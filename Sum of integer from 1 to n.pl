sum_integers(0, 0).
sum_integers(N, Sum) :-
    N > 0,
    N1 is N - 1,
    sum_integers(N1, SubSum),
    Sum is SubSum + N.

%output.
%?- sum_integers(5, Sum).
%sum = 15.
