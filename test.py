import sys

try:
    import tests.abstractions
    tests.abstractions.runTest()
except Exception as e:
    print("abstractions failed")
    print(e)

#try:
#    import tests.network
#    tests.network.runTest()
#except Exception as e:
#    print("network failed")
#    print(e)
