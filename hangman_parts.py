def parts(x):
    # if user will get 0 wrong letters will appear this picture
    if x == 0:
        print('   ',   '------')
        print('   ',   '|    |')
        print('   ',   '|     ')
        print('   ',   '|     ')
        print('   ',   '|     ')
        print('   ',   '|     ')
        print('------------')
    # if user will get one wrong letter will apper this picture
    if x == 1:
        print('   ',   '------')
        print('   ',   '|    |')
        print('   ',   '|    o')
        print('   ',   '|     ')
        print('   ',   '|     ')
        print('   ',   '|     ')
        print('------------')
    # if user will get two wrong letters will appear this picture
    if x == 2:
        print('   ',   '------')
        print('   ',   '|    |')
        print('   ',   '|    o')
        print('   ',   '|   -|-')
        print('   ',   '|     ')
        print('   ',   '|     ')
        print('------------')
    # if user will get three wrong letters will appear this picture
    if x == 3:
        print('   ',   '------')
        print('   ',   '|    |')
        print('   ',   '|    o')
        print('   ',   '|   -|-')
        print('   ',   '|    | ')
        print('   ',   '|     ')
        print('------------')
    # if user will get four wrong letters will apear this picture
    if x == 4:
        print('   ',   '------')
        print('   ',   '|    |')
        print('   ',   '|    o')
        print('   ',   '|   -|-')
        print('   ',   '|    | ')
        print('   ',   '|   / \\')
        print('------------')
