
dob(john, '1990-03-15').
dob(anna, '1985-07-22').
dob(mike, '1995-11-30').
dob(lisa, '2000-01-10').
dob(emma, '1998-05-03').



find_dob(Name, DOB) :- dob(Name, DOB).


born_after_year(Year, Name) :- dob(Name, DOB), DOB @> Year.


born_in_month(Month, Name) :- dob(Name, DOB), DOB =.. [_, Y, M, _], M =:= Month.
