#!/usr/bin/python

import os

import sys

import random

from collections import defaultdict


# Define a Node object, that carries graph information for a node in
# the form of a list of (nodeID, distance) tuples


class Node(object):
    def __init__(self):
        # list of (nodeID, distance) tuples
        self.connlist = []



class GraphStore(object):
    def __init__(self):
        self.nodestor = defaultdict(Node)


    def addConnection(self, id1, id2, dist):
        '''
        Add nodes id1 and id2 (if they don't already exist)
        and add their distance (or cost), to nodestor
        '''
        ndval1 = self.nodestor.get(id1)

        ndval2 = self.nodestor.get(id2)

        # Update connlist fields
        if ndval1 == None and ndval2 == None:
            ndval1 = Node()

            self.nodestor[id1] = ndval1

            ndval2 = Node()

            self.nodestor[id2] = ndval2

        elif ndval1 == None and ndval2 != None:
            ndval1 = Node()

            self.nodestor[id1] = ndval1

        elif ndval1 != None and ndval2 == None:
            ndval2 = Node()

            self.nodestor[id2] = ndval2

        else:
            pass

        ndval1.connlist.append((id2, dist))

        ndval2.connlist.append((id1, dist))


    def delConnection(self, id1, id2):
        '''
        Delete connection between id1 and id2
        '''
        ndval1 = self.nodestor.get(id1)

        ndval2 = self.nodestor.get(id2)

        if ndval1 == None or ndval2 == None:
            print 'Attempt to delete non existent connection: %d:%d' % (id1, id2)

        else:
            thetup = (None,None)

            for idc, dist in ndval1.connlist:
                if idc == id2:
                    thetup = (idc, dist)

            try:
                ndval1.connlist.remove(thetup)

            except:
                print 'Connection info not found - nodestor compromised [%d:%d]' % (thetup[0], thetup[1])

            thetup = (id1, thetup[1])

            try:
                ndval2.connlist.remove(thetup)

            except:
                print 'Connection info not found - nodestor compromised [%d:%d]' % (thetup[0], thetup[1])


    def dumpNodestor(self):
        keys = self.nodestor.keys()

        for key in keys:
            print key, ':', self.nodestor[key].connlist

        print '----------------'


class dijkstraObj(object):
    def __init__(self, max_dist):
        self.srcNode = None

        self.destNode = None

        # Dictionary stores a tuple (min tentative dist to src,
        #                            id of neighbor for that dist)
        self.unvisited = {}

        # Dictionary stores a tuple (min dist to src,
        #                            id of neighbor for that dist)
        self.min_dist = {}

        self.max_dist = max_dist


    def addNode(self, node_id):
        '''
        Check if node is already in unvisited.  If so
        ignore, else, if node is not srcNode, add
        (MAX_INT, None) as tuple in unvisited dict
        at this node_id key
        '''
        if self.unvisited.get(node_id) == None:
            # First time seeing this node ID
            if node_id == self.srcNode:
                self.unvisited[node_id] = (0, None)

            else:
                self.unvisited[node_id] = (self.max_dist, None)


    def getSmallestID(self):
        '''
        Cycle through unvisited ids and get the one with
        min tentative dist to srcNode
        '''
        keys = self.unvisited.keys( )

        min_d = self.max_dist

        min_d_key = 0

        for key in keys:
            dist, _ = self.unvisited[key]

            if dist < min_d:
                min_d = dist

                min_d_key = key

        if min_d == self.max_dist:
            return (None, True)

        else:
            return (min_d_key, False)


    def processNode(self, node_id, connlist):
        '''
        1. Get curr node's tentative dist
        2. Walk through curr node's neighbors from connlist
        3. For each neighbor, update tentative min dist in
           unvisited set
        4. Pop curr node from unvisited set and add it to
           min_dist dictionary 
        '''
        curr_t_d, curr_nb = self.unvisited[node_id]

        for n_id, n_dist in connlist:
            if self.unvisited.has_key(n_id) == True:
                n_t_d, n_nb = self.unvisited.get(n_id)

                if (curr_t_d + n_dist) < n_t_d:
                    self.unvisited[n_id] = ((curr_t_d + n_dist), node_id)

            else:
                print 'neighbor node id not found in unvisited: %d' % n_id

        # All current node's neighbors are accounted for, so retire
        self.min_dist[node_id] = (curr_t_d, curr_nb)

        self.unvisited.pop(node_id)

        if node_id == self.destNode:
            return True

        else:
            return False


def gstest_main( ):
    gs = GraphStore()

    random.seed(1)

    dump_count = 4

    tuple_stor = []

    curr_count = 0

    for indx in range(30):
        id1 = random.randint(1, 30)

        while True:
            id2 = random.randint(1, 30)

            if id2 != id1:
                break

        try:
            location = tuple_stor.index((id1,id2))

            print 'Skipping duplicate connection', id1, ':', id2

        except:

            try:
                location = tuple_stor.index((id2, id1))

                print 'Skipping duplicate connection', id2, ':', id1

            except:
                print 'New connection: ', '(', id1, ',', id2, ')'

                dist = random.randint(1, 10)

                gs.addConnection(id1,id2,dist)

                tuple_stor.append((id1, id2))

                curr_count +=1

        if curr_count == dump_count:
            gs.dumpNodestor()

            curr_count = 0

    print 'Final graph:'

    gs.dumpNodestor()

    print tuple_stor

    id1 = tuple_stor[3][0]

    id2 = tuple_stor[3][1]

    print 'Deleting connection: ', '(', id1, ',', id2, ')'

    gs.delConnection(id1, id2)

    print 'Graph after delete'

    gs.dumpNodestor()

    print tuple_stor


def dijkstra_main( ):
    '''
    Create a GraphStore for storing connection and distance
    information, as connections get created.
    Designate a random node as the source node. and a different
    node as destination node, for shortest distance.
    Build a dijkstra object, then run analysis
    '''
    gs = GraphStore()

    # Create a Dijkstra object with an arbitrarily
    # chosen max distance [TODO]
    do = dijkstraObj(500)

    random.seed(3)

    tuple_stor = []

    # Randomly chosen src node id
    do.srcNode = 2

    # Randomly chosen dest node id
    do.destNode = 20

    for indx in range(20):
        id1 = random.randint(1, 20)

        while True:
            id2 = random.randint(1, 30)

            if id2 != id1:
                break

        try:
            location = tuple_stor.index((id1,id2))

            print 'Skipping duplicate connection', id1, ':', id2

        except:

            try:
                location = tuple_stor.index((id2,id1))

                print 'Skipping duplicate connection', id2, ':', id1

            except:
                print 'New connection: ', '(', id1, ',', id2, ')'

                dist = random.randint(1, 10)

                gs.addConnection(id1,id2,dist)

                do.addNode(id1)

                do.addNode(id2)

                tuple_stor.append((id1, id2))

    print 'Final graph:'

    gs.dumpNodestor()

    print tuple_stor

    all_done = False

    while not all_done:
        # Get the node ID that has smallest tentative dist
        close_id, all_done = do.getSmallestID( )

        if not all_done:
            connlist = gs.nodestor[close_id].connlist

            all_done = do.processNode(close_id, connlist)

    # Dump out min distance path
    keys = do.min_dist.keys()

    print 'min dist dump'

    for key in keys:
        print key, ':', do.min_dist[key][0], ':', do.min_dist[key][1]


if __name__ == '__main__':
    dijkstra_main()
