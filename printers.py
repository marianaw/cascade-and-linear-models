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



def which_step_prob(n, B):
    i = 1
    for step in B:
        if len(step) != 0:
            for t in step:
                if t[0] == n:
                    return i, t[1]
        i = i+1
        
            
    
def prettyprint_2(g, model, seed, A, B, args):
    print('----------------------\n')
    print('The initial seed was:\n')
    print(seed)
    print('----------------------\n')
    print ('You selected the model ', model, '.')
    if model == 'ICM':
        print ('Probability: ', args[0])
        print ('Verbosity: ', args[1])
    print('----------------------\n')
    print('Node\t\t Active/Inactive \t\t Activation value \t\t Step of activation (if any)')
    print('-------------------------------------------------------------------------------------------\n')
    nodes = set([i for (i, _) in g.get_edgelist()] + [i for (_, i) in g.get_edgelist()])
    if len(B) == 0:
        raise Exception('Nothing to print!')
    activated_nodes = set(A).difference(set(seed))
    for n in nodes:
        if n in activated_nodes:
            active = 1
            step, prob = which_step_prob(n, B)
        else:
            active = 0
            prob = '--'
            step = '\t\t--'
        print (n, '\t\t\t', active, '\t\t\t', prob, '\t\t\t', step)
    print('********')
    
    
    
def prettyoutput(g, A, B, seed, args, filename):
    f = open(filename, 'w')
    f.write('----------------------\n')
    model = args[0]
    f.write('You selected the model ' + model + '.\n')
    if model == 'ICM':
        f.write('Probability: ' + str(args[1]) + '\n\n')
    f.write('----------------------\n')
    f.write('Node\t\t Active/Inactive \t\t Activation value \t\t Step of activation (if any)\n')
    f.write('-------------------------------------------------------------------------------------------\n')
    nodes = set([i for (i, _) in g.get_edgelist()] + [i for (_, i) in g.get_edgelist()])
    if len(B) == 0:
        raise Exception('Nothing to print!\n')
    activated_nodes = set(A).difference(set(seed))
    for n in nodes:
        if n in activated_nodes:
            active = 1
            step, prob = which_step_prob(n, B)
        else:
            active = 0
            prob = '--'
            step = '\t\t--'
        f.write('\n' + str(n) + '\t\t\t' + str(active) + '\t\t\t' + str(prob) + '\t\t\t' + str(step) + '\n')
    f.write('\n********')
    f.close()
    return 
    