diet_recommendation(diabetes, [
    'Limit your intake of carbohydrates and sugar.',
    'Eat more whole grains, vegetables, and lean proteins.',
    'Avoid sugary drinks and snacks.',
    'Monitor your blood sugar levels regularly.'
]).

diet_recommendation(hypertension, [
    'Reduce your sodium (salt) intake.',
    'Eat a diet rich in fruits, vegetables, and whole grains.',
    'Limit processed and high-fat foods.',
    'Monitor your blood pressure regularly.'
]).

diet_recommendation(obesity, [
    'Consume fewer calories than you burn.',
    'Increase your physical activity.',
    'Eat a balanced diet with portion control.',
    'Avoid excessive sugar and high-fat foods.'
]).
suggest_diet(Disease) :-
    diet_recommendation(Disease, Recommendations),
    write('Diet Recommendations for '), write(Disease), write(':'), nl,
    print_recommendations(Recommendations).
print_recommendations([]).
print_recommendations([Recommendation | Rest]) :-
    write('- '), write(Recommendation), nl,
    print_recommendations(Rest).
