def change_to_int(str):
    return int(str)

def days_to_candle(days: int):
    candles_per_day = 1
    total = 0
    for i in range(days):
        total += candles_per_day 
        candles_per_day += 1 
    return total + days   

data_set_num = int(input())
data_sets = list()
for data_set in range(data_set_num):
    d_set = input().split(" ")
    d_set = map(change_to_int, d_set)
    data_sets.append(list(d_set))
for data_set in data_sets:
    nb_of_candles = days_to_candle(data_set[1])
    data_set[1] = nb_of_candles
    print(f"{data_set[0]} {data_set[1]}")