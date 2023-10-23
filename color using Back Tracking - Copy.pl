
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(strawberry, red).
fruit_color(blueberry, blue).
fruit_color(watermelon, green).
fruit_color(lemon, yellow).
color_of_fruit(Fruit, Color) :-
    fruit_color(Fruit, Color).
fruit_of_color(Color, Fruit) :-
    fruit_color(Fruit, Color).
fruits_of_color(Color, Fruits) :-
    findall(Fruit, fruit_color(Fruit, Color), Fruits).
colors_of_fruit(Fruit, Colors) :-
    findall(Color, fruit_color(Fruit, Color), Colors).
