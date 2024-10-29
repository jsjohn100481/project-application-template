
from typing import List
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from data_loader import DataLoader
from model import Issue,Event
import config

class Analyzer_Class:
    
    #-----------JONATHAN'S CODE----------------------
    def issueAnalyzer(self, issues):
        issuesCreatorSet = set()
        for i in range(len(issues)):
            count = 0
            creatorName = issues[i].creator
            issuesCreatorSet.add(creatorName)  #---gets rid of duplicate creators
            
        issuesCreatorList = sorted(issuesCreatorSet) #----alphabetizes creators list
        x = 0 # to iterate over issuesCreatorList
        count = 0
        count1 = 0
        issuesCreatorListLength = len(issuesCreatorList)
        creatorIssueLabels = 0 #number of issue labels for creator
        
        while x < issuesCreatorListLength:
            issueLabels = [] #------list of all labels associated w/ Creators Issues
            for r in range(len(issues)):
                if(issuesCreatorList[x] == issues[r].creator ):  #  finds all instances of creator
                    creatorIssueLabels = creatorIssueLabels + len(issues[r].labels) #------NEED TO ADD ALL # OF LABELS
                    for h in issues[r].labels:
                        issueLabels.append(h) #------
                        
                    count = count+1
            #---CODE 1 STARTS HERE       
            #if(count >37):
                
                #print("Issue Creator---" + issuesCreatorList[x] + " ---# of Issues: " + str(count))  # TEST - prints creator and amount of issues submitted 
                #print("---# of Labels ---" + str(creatorIssueLabels))  # TEST prints number of labels associated w/ each issues submitted by creator
                #for g in issueLabels:
                    #count1 =count1 +1
                    #print("---LABEL #"  + str(count1) +  "--" + g)  #TEST prints labels associated w/ all creator issues and numbers them
            #---CODE 1 ENDS HERE
            
            #---CODE2 STARTS HERE          
            #print("Issue Creator---" + issuesCreatorList[x] + " ---# of Issues: " + str(count))  # prints creator and amount of issues submitted 
            #print("---# of Labels ---" + str(creatorIssueLabels))  # prints number of labels associated w/ each issues submitted by creator
            #for g in issueLabels:
                #print("---LABEL --" + g)
            #---CODE2 ENDS HERE
            creatorIssueLabels = 0
            count = 0; 
            count1 = 0;      
            x += 1
           
        #---------END JONATHAN'S CODE--------------