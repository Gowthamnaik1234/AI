
planet(mercury, terrestrial, 0.39, 0.38, 88, 1407).
planet(venus, terrestrial, 0.72, 0.95, 225, 5832).
planet(earth, terrestrial, 1.0, 1.0, 365, 24).
planet(mars, terrestrial, 1.52, 0.38, 687, 25).
planet(jupiter, gas_giant, 5.20, 318, 4332, 10).
planet(saturn, gas_giant, 9.58, 95, 10759, 11).
planet(uranus, ice_giant, 19.22, 14.5, 30687, 17).
planet(neptune, ice_giant, 30.05, 17.1, 60190, 16).

planet_info(Name, Type, Distance, Mass, Days, Hours) :- planet(Name, Type, Distance, Mass, Days, Hours).

terrestrial_planet(Name) :- planet(Name, terrestrial, _, _, _, _).

gas_giant_planet(Name) :- planet(Name, gas_giant, _, _, _, _).

ice_giant_planet(Name) :- planet(Name, ice_giant, _, _, _, _).
