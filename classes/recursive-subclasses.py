#!/usr/bin/python3

classes_seen = {}

node_nr = 1
dot = open('subclasses.dot', 'w')
dot.write('digraph class_hierarchy {\n')
dot.write('node [shape=plaintext]\n')

def S(c):
    global node_nr
    for sc in c.__subclasses__():
#       (repr(c) + ' --> ' + repr(sc))

        if sc in classes_seen:
           continue

        classes_seen[sc] = node_nr

        dot.write('nd_' + str(node_nr) + ' [ label="' + repr(sc) + '"];\n')
        dot.write('nd_' + str(classes_seen[c]) + ' -> ' + 'nd_' + str(node_nr) + ';\n');

        node_nr += 1

        if sc != type and sc != c:
           S(sc)




classes_seen[object] = 0
dot.write('nd_' + str(0) + ' [ label="' + repr(object) + '"]\n')

S(object)

dot.write('}\n')
