from functions import parse, show

test_in = [
    [
        [1508405807242, 1508405807141, 'vader', 'HELLO']
    ],
    [
        [1508405807242, 1508405807141, 'vader', 'HELLO'],
        [1508405807340, 1508405807350, 'luke', 'HELLO'],
        [1508405807378, 1508405807387, 'luke', 'LOST', 'vader'],
        [1508405807512, 1508405807400, 'vader', 'LOST', 'luke'],
        [1508405807467, 1508405807479, 'luke', 'FOUND', 'r2d2'],
        [1508405807468, 1508405807480, 'luke', 'LOST', 'leia'],
        [1508405807560, 1508405807504, 'vader', 'HELLO']
    ]
]

test_out = [
    [
        ['vader', 'ALIVE', 1508405807242, 'vader', 'HELLO']
    ],
    [
        ['vader', 'ALIVE', 1508405807560, 'vader', 'HELLO'],
        ['leia', 'DEAD', 1508405807468, 'luke', 'LOST', 'leia'],
        ['luke', 'ALIVE', 1508405807468, 'luke', 'LOST', 'leia'],
        ['r2d2', 'ALIVE', 1508405807467, 'luke', 'FOUND', 'r2d2'],
    ]
]

i=0
for test in test_in:
    res = parse(test)
    assert (res == test_out[i]), "\nTEST: "+str(i+1)+"\nOutput\t\t==> "+show(res)+"\nExpected\t==> "+show(test_out[i])
    i=i+1