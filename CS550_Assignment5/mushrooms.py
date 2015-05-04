'''
Created on May 3, 2015

@author: cxj8923
'''
import example_reader
import copy
import learners.learning
import math
from learners.utils import log2

def main():
    data = example_reader.csv_data('mushrooms/attributes.csv', 'mushrooms/agaricus-lepiota.csv', 'mushrooms/attribute-value-abbr.csv')
    exampleCount = len(data['examples'])
    examples = data['examples']
    for i in xrange(6):
        partitionSize = exampleCount/6
        startSlice = i*partitionSize
        endSlice = startSlice + partitionSize
        testExamples = examples[startSlice:endSlice]
        trainingExamples = copy.deepcopy(examples)
        del trainingExamples[startSlice:endSlice]
        dataSet = learners.learning.DataSet(examples=trainingExamples,attrnames=data['attributes'])
        tree = learners.learning.DecisionTreeLearner(dataSet)
        correct = 0
        incorrect = 0
        misclassified = []
        for example in testExamples:
            prediction = tree(example)
            if prediction != example[-1]:
                misclassified.append(example)
        print 'Test ' + str(i+1)
        print 'Training examples: ' + str(len(trainingExamples))
        testCount = int(len(testExamples))
        print 'Test Examples: ' + str(testCount)
        misCount = int(len(misclassified))
        print "Misclassified: " + str(misCount)
        misRate = float(float(misCount)/float(testCount))
        print "Misclassified Rate: " + str(misRate)
        for misclass in misclassified:
            print misclass
    calcInfoGain(data)

def calcInfoGain(data):
    #Information gain for each variable
    #Things to find out
    # 1. For a given attribute, how many classifications
    # 2. For a class of attribute, how many positive
    # 3. For a class of attribute how many negative
    #q = p/p+n
    #B(q) = -qlog2q-(1-q)log2(1-q)
    attributeNames = data['attributes']
    examples = data['examples']
    abbreviations = data['abbrev']
    i = 0
    for attribute in attributeNames:
        print "\nAttribute " + str(attribute) 
        for abbreviation in abbreviations[attribute]:
            count = 0
            posCount = 0
            negCount = 0
            for example in examples:
                if example[i] == abbreviation:
                    count += 1
                    if example[-1] == 'e':
                        posCount += 1
                    else:
                        negCount +=1       
            #print str(abbreviation) + ': ' + str(count) + ' pos: ' + str(posCount) + ' neg: ' + str(negCount)
            q = 0.0
            if (posCount + negCount) > 0:
                q = float(posCount)/(float(posCount)+float(negCount))
            if ((q - 0.0) < 0.0000001) or (posCount == count):
                Bq = 0
            else:
                Bq = (-1*q*log2(q)*q)-((1-q)*log2(1-q))
            print str(abbreviation) + ': ' + str(count) + ' pos: ' + str(posCount) + ' neg: ' + str(negCount) + ' q: ' + str(q) + ' Bq: ' + str(Bq)
        i = i+1
        #print abbreviations[attribute]
        #print len(abbreviations[attribute])
        #print abbreviations.keys()
    
        

if __name__ == '__main__':
    main()