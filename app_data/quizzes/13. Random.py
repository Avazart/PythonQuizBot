# # 1==========================================================================


# ? Which method should I use to get 4 elements from the following list
# / randomly


sample_list = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]


# - random.choice(sample_list, 4)
# + random.sample(sample_list, 4)


# # 2==========================================================================


# ? To generate a random secure Universally unique ID which method should I
# / use


# + uuid.uuid4()
# - uuid.uuid1()
# - uuid.uuid3()
# - random.uuid()


# # 3==========================================================================


# ? To Generate a random secure integer number, select all the correct
# / options.


# + random.SystemRandom().randint()
# - random.System.randint()
# + secrets.randbelow()


# # 4==========================================================================


# ? Choose the correct function to get 3 elements from the list randomly in
# / such a way that each element of the list has a different probability of
# / being selected.


number_list = [100, 200, 300, 400, 500]


# + random.choices(number_list, weights=(10, 5, 15, 20, 50), k=3)
# - random.choice(number_list, weights=(10, 5, 15, 20, 50), k=3)
# - random.sample(number_list, weights=(10, 5, 15, 20, 50), k=3)


# # 5==========================================================================


# ? str = “PYnative”. Choose the correct function to pick a single character
# / from a given string randomly.


# - random.sample(str)
# + random.choice(str)
# - random.get(str, 1)


# # 6==========================================================================


# ? Which method should i use to capture and change the current state of the
# / random generator


# + random.getstate() random.setstate(state)
# - random.getstate()
# - random.setstate(state)
# - random.currentstate() random.setcurrentstate(state)
# - random.currentstate()
# - random.setcurrentstate(state)


# # 7==========================================================================


# ? I want to generate a random secure hex token of 32 bytes to reset the
# / password, which method should I use


# - secrets.hexToken(32)
# - secrets.hex_token(32)
# - secrets.tokenHex(32)
# + secrets.token_hex(32)


# # 8==========================================================================


# ? The random.seed() method is used to initialize the pseudorandom number
# / generator. The random module uses the seed value as a base to generate a
# / random number. If seed value is not present, it takes the system’s current
# / time.


# + True
# - False


# # 9==========================================================================


# ? To generate a random float number between 20.5 to 50.5, which function of
# / a random module I need to use


# - random.random(20.5, 50.5)
# + random.uniform(20.5, 50.5)
# - random.randrange(20.5, 50.5)
# - random.randfloat(20.5, 50.5)


# # 10=========================================================================


# ? Choose the correct function from the following list to get the random
# / integer between 99 to 200, which is divisible by 3.


# + random.randrange(99, 200, 3)
# - random.randint(99, 200, 3)
# - random.random(99, 200, 3)

