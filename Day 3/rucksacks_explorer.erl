-module(rucksacks_explorer).
-export([solve/0]).

divide_in_half([], First_half, Second_half) ->
    {First_half, lists:reverse(Second_half)};

divide_in_half([HD|TL], First_half, Second_half) ->
    Last_element = lists:last(TL),
    divide_in_half(lists:droplast(TL), [HD | First_half], [Last_element | Second_half]).

divide_in_half(Rucksack) ->
    divide_in_half(Rucksack, [], []).

get_common_item(First_half, Second_half) ->
    Common_items = [X || X <- First_half, Y <- Second_half, X == Y],
    lists:last(Common_items).

get_common_items(First_half, Second_half) ->
    [X || X <- First_half, Y <- Second_half, X == Y].

get_priority(Item) when Item >= 97 ->
    Item - 96;

get_priority(Item) when Item >= 65 ->
    Item - 38.

get_priority_points([], Priority_points) ->
    Priority_points;

get_priority_points([HD|TL], Priority_points) ->
    {First_half, Second_half} = divide_in_half(binary_to_list(HD)),
    get_priority_points(TL, Priority_points + get_priority(get_common_item(First_half, Second_half))).

get_group(Rucksacks, 0, Group) ->
    {Rucksacks, Group};

get_group([HD | TL], N, Group) ->
    get_group(TL, N - 1, [binary_to_list(HD) | Group]).

get_priority_group([], Priority_points) -> 
    Priority_points;

get_priority_group(Rucksacks, Priority_points) ->
    {Remaining_rucksacks, Group} = get_group(Rucksacks, 3, []),
    First_common_items = get_common_items(lists:nth(1, Group), lists:nth(2, Group)),
    get_priority_group(Remaining_rucksacks, Priority_points + get_priority(get_common_item(First_common_items, lists:nth(3, Group)))).

solve() ->
    {_, Rucksacks_file} = file:read_file("../inputs/rucksacks_items.txt"),
    Priority_points = get_priority_points(binary:split(Rucksacks_file, <<"\n">>, [global]), 0),
    io:format("The priority of the item is: ~p ~n", [Priority_points]),
    Group_priority = get_priority_group(binary:split(Rucksacks_file, <<"\n">>, [global]), 0),
    io:format("The priority of the item shared ny the group is: ~p ~n", [Group_priority]).
