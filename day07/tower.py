import click
import sys
from anytree import Node, RenderTree
@click.command()
@click.option('--file', help='File to read the lines')
def get_tower_root(file):
    if file:
        with open(file) as myfile:
            valid_lines=build_tree(myfile)

def parse_name(token):
    tokens = token.split(" ")
    name = tokens[0]
    weight = ((tokens[1].split("("))[1].split(")"))[0]
    return (name,int(weight))

def parse_links(token):
    tokens = token.split(",")
    links = [tkn.strip() for tkn in tokens]
    return links

def parse_line(line):
    line_dict = {}
    if '->' in line:
        tokens = line.split('->')
        name, weight = parse_name(tokens[0])
        links = parse_links(tokens[1])
        print "%s (%d)" % (name, weight)
        print links
        line_dict[name] = {}
        line_dict[name]["weight"] = weight
        line_dict[name]['links'] = links

    else:
        name,weight = parse_name(line)
        print "%s (%d)" % (name,weight)
        line_dict[name] = {}
        line_dict[name]["weight"] = weight
    print line_dict
    return (name,weight,line_dict)


def build_tree(file):

    links_dict = {}
    node_dict = {}
    weight_dict ={}
    for line in file:
        (name,weight,line_dict) = parse_line(line.replace("\n",""))
        if 'links' in line_dict[name]:
            links_dict[name] = line_dict[name]

        new_node = Node(name)
        node_dict[name] = new_node
        weight_dict[name] = weight

    print "\n"
    for name in links_dict:
        print 'Checking node', name
        links = links_dict[name]['links']
        print links
        parent_node = node_dict[name]
        for node in links:
            cur_node = node_dict[node]
            cur_node.parent = parent_node
        print(RenderTree(parent_node))
        latest_name = name
    print '\nFINAL tree'
    root = node_dict[latest_name].root
    print RenderTree(node_dict[root.name])
    print 'ROOT is',root

    print root.children
    #recursively find weights and unbalanced node
    get_subtree_weight(weight_dict,root,1)

def get_subtree_weight(weight_dict,child,levels):
    weight = weight_dict[child.name]
    if not child.is_leaf:
        children_weights = []
        for grandchild in child.children:
            if levels == 1:
                print "==== CHECKING subtree for ", grandchild
            child_weight = get_subtree_weight(weight_dict,grandchild,levels+1)
            children_weights.append(child_weight)
            weight+=child_weight

        if len(set(children_weights)) != 1:
            print '================ UNBALANCED TREE'
            print children_weights
            print child.children
            for idx,nd in enumerate(child.children):
                print nd.name + ": " + str(weight_dict[nd.name]) + ", children weight:"+str(children_weights[idx])
            sys.exit()

    print '\t' * levels + '%s is %d* ' % (child.name, weight)
    return weight



if __name__ == '__main__':
    valid_lines = get_tower_root()
