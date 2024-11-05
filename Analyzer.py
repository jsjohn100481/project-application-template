
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
    issues:List[Issue] = DataLoader().get_issues()
    
    def issue_Analyzer(self):
        issuesLabelsSet = set()
        issuesCreatorSet = set()
        for i in range(len(self.issues)):
            creatorName = self.issues[i].creator
            issuesCreatorSet.add(creatorName)  
            
        self.issuesCreatorList = sorted(issuesCreatorSet) 
        issuesCreatorListLength = len(self.issuesCreatorList)
        
        x = 0        
        while x < issuesCreatorListLength:
            for r in range(len(self.issues)):
                if(self.issuesCreatorList[x] == self.issues[r].creator ):  
                    for h in self.issues[r].labels:
                        issuesLabelsSet.add(h)
            x += 1
               
        issuesLabelsList = sorted(issuesLabelsSet) 
               
        m = 0
        event_count = 0
        while m < len(issuesLabelsList):
            for x in range(len(self.issues)): 
                for r in range(len(self.issues[x].labels)): 
                    if(issuesLabelsList[m] == self.issues[x].labels[r]):
                        event_count = event_count + len(self.issues[x].events)
                        
            self.labelsAnalyzerList.append(Label_Analyzer(issuesLabelsList[m], event_count))               
            event_count = 0;
            m +=1;  
            
    #feature 1 analysis    
    def issue_Contributors_Listing(self):    
        
        self.issue_Analyzer()
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
    
    def creator_Issues_Analysis(self):    
        self.issue_Analyzer()                 
        creator = input("Enter 'Creator' Name:  ") 
        for i in range(len(self.issues)):  #scan issues
            if(creator == self.issues[i].creator): #see if creator is in issues
                for j in range(len(self.issues[i].labels)):  #scan every issue label for creator
                    print(creator + " created issue '" + self.issues[i].labels[j] + "' on " + str(self.issues[i].created_date))
                    for x in range(len(self.issues)):
                        for r in range(len(self.issues[x].labels)):
                            if(self.issues[i].labels[j] == self.issues[x].labels[r]):
                                for s in range(len(self.issues[x].events)):
                                    if(creator ==self.issues[x].events[s].author):
                                        print("----Contributed to label '" + self.issues[x].labels[r] + "' created by " + self.issues[x].creator + " on " + str(self.issues[x].events[s].event_date))
                                        
         
                
class Label_Analyzer:
    
    issueLabelName:str = None
    issueLabelContributorAmount:int = 0
    
    def __init__(self, name, amount):
        
        self.issueLabelName = name
        self.issueLabelContributorAmount = amount
    
    
    
    
               
        #---------END JONATHAN'S CODE--------------