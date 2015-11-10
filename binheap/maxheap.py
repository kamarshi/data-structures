#!/usr/bin/python

import os

import sys

import show_tree


# Implements a maxheap class natively
# maxheap is a binary heap with "largest" item at top
# Data item should have the __cmp__ method implemented
# A list is used to store data. Element at list index
# N has its children at 2**N+1 and 2**N+2


class maxheap(object):

    def __init__(self):
        '''
        Possibly nothing
        '''
        pass


    def exchange(self, objlist, elmA, elmB):
        tmp = objlist[elmA]

        objlist[elmA] = objlist[elmB]

        objlist[elmB] = tmp


    def find_child(self, objlist, loc):
        '''
        Find the child node to check or return False
        if no child avaliable
        '''
        found_chld = False

        try:
            l_chld = loc*2 + 1

            l_val = objlist[l_chld]

            found_chld = True

        except:
            l_val = 0

        try:
            r_chld = l_chld + 1

            r_val = objlist[r_chld]

            found_chld = True

        except:
            r_val = 0

        if r_val > l_val:
            chld = r_chld

        else:
            chld = l_chld

        return (found_chld, chld)


    def percolate_end(self, objlist):
        '''
        Apply maxheap rule to element at end of list
        '''
        loc = len(objlist) - 1

        parent = int((loc-1) / 2)

        while objlist[loc] > objlist[parent] and parent >= 0:
            self.exchange(objlist, loc, parent)

            loc = parent

            parent = int((loc-1) / 2)


    def percolate_start(self, objlist):
        '''
        Apply maxheap rule to element at start of list
        '''
        loc = 0

        found_chld, chld = self.find_child(objlist, loc)

        while found_chld and objlist[loc] < objlist[chld]:
            self.exchange(objlist, loc, chld)

            loc = chld

            found_chld, chld = self.find_child(objlist, loc)


    def heappush(self, objlist, obj):
        '''
        Make sure new obj type is same as first obj type
        Append new item to end of list, then percolate
        '''
        if len(objlist) != 0 and type(objlist[0]) != type(obj):
            raise TypeError

        objlist.append(obj)

        self.percolate_end(objlist)


    def heappop(self, objlist):
        '''
        Pops the largest heap item (first), puts end item in its
        place and applies healp rules unitl done
        '''
        size = len(objlist)

        if size == 0:
            return None

        retVal = objlist[0]

        lastVal = objlist.pop()

        objlist[0] = lastVal

        self.percolate_start(objlist)

        return retVal


    def heapify(self, objlist):
        '''
        objlist items should all be of same type
        Simply sort list in descending order
        '''
        objlist.sort(reverse=True)


def main():
    heap = [34, 14, 125, 25, 4, 66, 3, 7, 33, 87, 41]

    maxhp = maxheap()

    maxhp.heapify(heap)

    show_tree.show_tree(heap, total_width=64)

    maxhp.heappush(heap, 39)

    maxhp.heappush(heap, 5)

    show_tree.show_tree(heap, total_width=64)

    maxhp.heappop(heap)

    show_tree.show_tree(heap, total_width=64)

    maxhp.heappop(heap)

    show_tree.show_tree(heap, total_width=64)

    bl = ['The', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'brown', 'dog']

    maxhp.heapify(bl)

    show_tree.show_tree(bl, total_width=64)

    heap = []

    maxhp.heapify(heap)

    maxhp.heappush(heap, 5)

    maxhp.heappush(heap, 39)

    maxhp.heappush(heap, 2)

    maxhp.heappush(heap, 50)

    show_tree.show_tree(heap, total_width=64)


if __name__ == '__main__':
    main()
