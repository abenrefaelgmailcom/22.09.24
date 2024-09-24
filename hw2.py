height: float = None
big_height: float = None
short_height: float = None
sum_players: int = None
above_players: int = None
higher_then_2 : int = None

heights = []
while True:
    height = float(input("Enter player's height : "))

    if height == -999:
        break

    if height < 1.60 or height > 3.0:
        continue
    heights.append(height)
    sum_players += 1

    print('numbers of players listed', len(heights))
    if big_height == None or height > big_height:
        print()
    if short_height == None or height > short_height:
        print()

    else:
    print(f"players count: {height}")
    print(f"highest player: {big_height}")
    print(f"shortest player: {short_height}")
    print(f"players above 2.0 meters count: {higher_then_2}")
    print(f"players above avarege count: {above_players}")












#
# for _ in range(MAX_COUNT):
#     result: float = float(input('whats the height? '))
#     if result < 5.80:
#         continue
#     count_good_results += 1
#     sum_good_results += result
#     # if max_score is None
#     # if not max_score
#     if max_score is None or result > max_score:
#         max_score = result
#     if result > WORLD_RECORD:
#         # TODO: what if second world record was lower than the first
#         new_world_record = result
#         print('NEW WORLD RECORD !!!!!!!!!!')
#         new_world_record_name = input('whats the name of the jumper? ')
# else:
#     avg_good_score: float = None
#     print(f"number of good jumps: {count_good_results}")
#     if count_good_results:
#         avg_good_score: float = sum_good_results / count_good_results
#     print(f"good jumps avg = {avg_good_score}")
#     print(f"highest score: {max_score}")
#     if new_world_record:
#         print(f"new world record height: {new_world_record}")
#         print(f"new world record jumper name: {new_world_record_name}")
#     else:
#         print("no new world record achieved. None")