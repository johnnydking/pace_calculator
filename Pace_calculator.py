
distance = float(input('How many miles do you plan to run?: '))
time = float(input('And in how many minutes would you like to complete the run?: '))
pace = time / distance * 60
mins = pace // 60
seconds = pace % 60
mins_int = int(mins)
seconds_int = round(seconds)

if seconds_int < 10:
    pace_sec = print('You would need an average pace of {}:0{} per mile.'.format(mins_int, seconds_int))
else:
    print('You would need an average pace of {}:{} per mile.'.format(mins_int, seconds_int))
