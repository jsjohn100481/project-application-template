
from typing import List
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from data_loader import DataLoader
from model import Issue,Event
import config

class Analyzer_Class:
    
    #-----------JONATHAN'S CODE----------------------
    # CODE TO GET LISTS OF BOTH ISSUE CREATORS AND LABELS AND REMOVE DUPLICATES
    # PRINTS LIST OF LABELS AND THE # OF CONTRIBUTORS ASSOCIATED W/ THOSE LABELS
    issuesCreatorList = []
    labelsAnalyzerList = []  
    
    def issue_Analyzer(self, issues):
        issuesLabelsSet = set()
        issuesCreatorSet = set()
        for i in range(len(issues)):
            creatorName = issues[i].creator
            issuesCreatorSet.add(creatorName)  
            
        self.issuesCreatorList = sorted(issuesCreatorSet) 
        issuesCreatorListLength = len(self.issuesCreatorList)
        
        x = 0        
        while x < issuesCreatorListLength:
            for r in range(len(issues)):
                if(self.issuesCreatorList[x] == issues[r].creator ):  
                    for h in issues[r].labels:
                        issuesLabelsSet.add(h)
            x += 1
               
        issuesLabelsList = sorted(issuesLabelsSet) 
               
        m = 0
        event_count = 0
        while m < len(issuesLabelsList):
            for x in range(len(issues)): 
                for r in range(len(issues[x].labels)): 
                    if(issuesLabelsList[m] == issues[x].labels[r]):
                        event_count = event_count + len(issues[x].events)
                        
            self.labelsAnalyzerList.append(Label_Analyzer(issuesLabelsList[m], event_count))               
            event_count = 0;
            m +=1;  
            
        #-----------------------new code-------------------------------------- 
    def issue_Contributors_Listing(self, issues):    
        self.issue_Analyzer(issues)
        #-----------------------new code--------------------------------------                         
        
        numberList:List[int] = []
        
        for i in range(len(self.labelsAnalyzerList)):
            numberList.append(self.labelsAnalyzerList[i].issueLabelContributorAmount)
            
          
        numberList.sort()
        numberSet = set(numberList)
        numberList = sorted(numberSet)
              
        for i in range(len(numberList)):
            for a in range(len(self.labelsAnalyzerList)):
                if(numberList[i] == self.labelsAnalyzerList[a].issueLabelContributorAmount):
                    print("Label - " + self.labelsAnalyzerList[a].issueLabelName) 
                    print("----# of Contributors - " + str(self.labelsAnalyzerList[a].issueLabelContributorAmount))  
        
                        
                
class Label_Analyzer:
    
    issueLabelName:str = None
    issueLabelContributorAmount:int = 0
    
    def __init__(self, name, amount):
        
        self.issueLabelName = name
        self.issueLabelContributorAmount = amount
    
    
    
    
               
        #---------END JONATHAN'S CODE--------------