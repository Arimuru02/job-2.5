#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Написать программу, которая считывает текст из файла и выводит на экран только
#предложения, не содержащие запятых.

if __name__ == "__main__":

    with open('text1.txt',encoding='utf-8')as f:
        for line in f.read().split('.'):
            if ',' not in line:
                print(line.strip())


