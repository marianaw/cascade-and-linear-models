from independent_cascade import independent_cascade
from linear_threshold import linear_threshold
from optparse import OptionParser
from igraph import Graph


#To handle an invalid model exception:
class InvalidModel(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value
    
    
#To load seed file:
def load_seed(filename):
    seed = []
    with open(filename, 'r') as f:
        for line in f:
            seed = seed + [int(x) for x in line.split(' ')]
    return seed



#To print an awesome output:
def prettyprint(model, seed, output, args):
    print('----------------------\n')
    print('The initial seed was:\n')
    print(seed)
    print('----------------------\n')
    print('----------------------\n')
    if model == 'ICM':
        s = 'Probability'
        print ('You selected the model ', model, ' with probability ', args[0], ' and activation function ', args[1])
        print ('----------------------\n')
    if model == 'LTM':
        s = 'Weight'
        print ('You selected the model ', model, '.')
        print ('----------------------\n')
    print('Step \t\t|\t\t Node \t\t|\t' + s + ' of activation:')
    print('----------------------------------------------------------------------------------')
    step = 1
    for res in output:
        for tup in res:
            print(step, '\t\t|\t\t ', tup[0], '\t\t|\t\t ', '%.3f' % tup[1])
        step = step + 1
    
def main():
    parser = OptionParser()
    parser.add_option("-m", dest="model", help="The model to run.")
    parser.add_option("-f", dest="graph", help='The file containing the graph to load.')
    parser.add_option("-n", dest="num_steps", help="Number of steps to run on LCM. If zero then the algorithm runs until it runs out of nodes.")
    parser.add_option("-s", dest="seed", help="File containing seed.")
    parser.add_option("-v", dest="verbosity", help="1 or 2 to select activation function of ICM.")
    parser.add_option("-p", dest="prob", help="Initial node probability for ICM.")
    opt, args = parser.parse_args()
        
    try:
        graph = Graph.Read_Edgelist(open(opt.graph, 'r'))
        seed = load_seed(opt.seed)
    except Exception as e:
        print('Ups! Invalid file name: ', e)

    try:
        model = opt.model
        if model == 'ICM':
            st = int(opt.num_steps)
            p = float(opt.prob)
            if p>1 or p<0:
                raise Exception('Probability falls between 0 and 1.')
            
            verbosity = int(opt.verbosity)
            A, B = independent_cascade(graph, seed, p, st, verbosity)
            args = [p, verbosity]
        else:
            if model == 'LTM':
                A, B = linear_threshold(graph, seed)
                args = []
            else:
                raise InvalidModel('Invalid model ' + model + '.')
        prettyprint(model, seed, B, args)
    except InvalidModel as e:
        print('Ups! Seems like an invalid model name: ', e)
    
    
    
    
    
if __name__ == '__main__':
    main()
    #prettyprint('LTM', [1,2,2], {})