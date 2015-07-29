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
    
    

def main():
    parser = OptionParser()
    parser.add_option("-m", dest="model", help="The model to run.")
    parser.add_option("-f", dest="graph", help='The file containing the graph to load.')
    parser.add_option("-n", dest="num_steps", help="Number of steps to run on LCM. If zero then the algorithm runs until it runs out of nodes.")
    opt, args = parser.parse_args()
        
    try:
        g = Graph.Read_Edgelist(open(opt.graph, 'r'))
    except Exception as e:
        print('Ups! Invalid file name: ', e)

    try:
        model = opt.model
        if model == 'ICM':
            #Call independent cascade model.
            print ('Good!')  
        else:
            if model == 'LTM':
                #Call linear threshold model.
                print ('Wow')
            else:
                raise InvalidModel('Invalid model ' + model + '.')
    except InvalidModel as e:
        print('Ups! Seems like an invalid model name: ', e)
    
    #print ('Good!')
    
if __name__ == '__main__':
    main()