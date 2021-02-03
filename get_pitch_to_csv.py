import os
import re
import linecache
import numpy as np
import pandas as pd
import codecs


def get_value(file):
    ans = []
    f = codecs.open(file, 'r', 'utf_16_be')
    lines = f.readlines(1000)
    lineA = lines[2]
    pitchA = re.split(',', lineA)
    lineB = lines[4]
    pitchB = re.split(',', lineB)
    pitch = pitchA[7:-1]+pitchB[7:-1]
    return pitch


def main():
    files = os.listdir('data')
    ans = []
    fileNames = []
    for file in files:
        file_name = file.split('.')[0]
        fileNames.append(str(file_name))
        ans.append(get_value('data/' + file))
    # print(ans[0:3])
    # print(fileNames[0:3])
    ans = pd.DataFrame(index=fileNames, data=ans)
    # print(ans)
    ans.to_csv('result.csv')


if __name__ == '__main__':
    main()
