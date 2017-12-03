import functions as fn

def assert_msg(i,res,expected):
    return "\nTEST: "+str(i+1)+"\nOutput\t\t==> "+str(res)+"\nExpected\t==> "+str(expected)

files = [
    (0, 'tests/01.txt'),
    (1, 'tests/02.txt'),
    (2, 'tests/03.txt'),
    (3, 'tests/04.txt'),
    ]

expected = [
    '\nvader ALIVE 1508405807242 vader HELLO \n',
    '\nluke ALIVE 1508405807468 luke LOST leia\nleia DEAD 1508405807468 luke LOST leia\nr2d2 ALIVE 1508405807467 luke FOUND r2d2\nvader ALIVE 1508405807560 vader HELLO \n',
    '\nluke ALIVE 1508405807468 luke LOST leia\nleia DEAD 1508405807468 luke LOST leia\nr2d2 ALIVE 1508405807467 luke FOUND r2d2\nvader UNKNOWN 1508405807512 vader LOST luke\nvader UNKNOWN 1508405807378 luke LOST vader\n\n',
    '\nluke ALIVE 1508405807468 luke LOST leia\nleia DEAD 1508405807468 luke LOST leia\nr2d2 ALIVE 1508405807467 luke FOUND r2d2\nvader ALIVE 1508405807513 vader LOST leia\n',
]

for (key, f) in files:
    nodes = fn.read_file(f)
    res = '\n'
    for name in nodes:
        res = res + nodes[name].get_status() + "\n"
    print(res)
    assert (res == expected[key]), assert_msg(key, res, expected[key])
