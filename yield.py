def test():
    print("generator start")
    n = 1
    while True:
        yield_expression_value = yield n
        print("yield_expression_value = %d" % yield_expression_value)
        n += 1


# ① create generator obj
generator = test()
print(type(generator))

print("\n---------------\n")

# ② call generator
next_result = generator.__next__()
print("next_result = %d" % next_result)

print("\n---------------\n")

# ③ send value to yield expression
send_result = generator.send(666)
print("send_result = %d" % send_result)


