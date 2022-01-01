# What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?

for x in range(50, 90, 10):  # range(start_value, stop_value + step_value, step_value) --> to produce 50, 60, 70, 80
    # start_value = 50, stop_value = 80 + step_value = 10 => 90, step_value = 10
    print(x)
