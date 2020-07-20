#! /usr/bin/env python

with open("read_sample.txt", 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        print(line.strip())
#with open쓰면 close 안써도된대
#strip() 안쓰면 enter가 들어가서 써야지 딱 붙어서 나와 유노
#if startswith부터 쓰면 header가 지워져서 나온다.
