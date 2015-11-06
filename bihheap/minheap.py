#!/usr/bin/python

import os

import sys

import heapq

import show_tree

# Implements a minheap class, using the heapq module

class minheap(object):

    def __init__(self):
        '''
        Possibly nothing
        '''
        pass


    def heappush(self, objlist, obj):
        '''
        Make sure new obj type is same as first obj type
        Call heapq's heappush method
        '''
        if len(objlist) != 0 and type(objlist[0]) != type(obj):
            raise TypeError

        heapq.heappush(objlist, obj)


    def heappop(self, objlist):
        '''
        Pops the smallest help item, puts largest in its
        place and applies healp rules unitl done
        This method just calls heapq's heappop method
        '''
        heapq.heappop(objlist)


    def heapify(self, objlist):
        '''
        objlist items should all be of same type
        Call heapq's heapify method
        [TODO] heapq.heapify does not check for uniform type
        in list elements
        '''
        heapq.heapify(objlist)


def main():
    heap = [34, 14, 125, 25, 4, 66, 3, 7, 33, 87, 41]

    minhp = minheap()

    minhp.heapify(heap)

    show_tree.show_tree(heap, total_width=64)

    minhp.heappush(heap, 39)

    minhp.heappush(heap, 5)

    show_tree.show_tree(heap, total_width=64)

    minhp.heappop(heap)

    show_tree.show_tree(heap, total_width=64)

    minhp.heappop(heap)

    show_tree.show_tree(heap, total_width=64)

    bl = ['The', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'brown', 'dog']

    minhp.heapify(bl)

    show_tree.show_tree(bl, total_width=64)


if __name__ == '__main__':
    main()

