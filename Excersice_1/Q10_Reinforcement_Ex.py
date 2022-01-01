# What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

for x in range(8, -10, -2):  # range(start_value, stop_value + step_value, step_value) --> to produce 8,6,...,-6,-8
    # start_value = 8, stop_value = -8 + step_value = -2 => -10, step_value = -2
    print(x)
