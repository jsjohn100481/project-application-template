
from typing import List
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from data_loader import DataLoader
from model import Issue,Event
import config
import sys

class Analyzer_Class:
    
   
    
    # PRINTS LIST OF LABELS AND THE # OF CONTRIBUTORS ASSOCIATED W/ THOSE LABELS
    issuesCreatorList = []
    labelsAnalyzerList = []  
    issues:List[Issue] = DataLoader().get_issues()
    
    # GET LISTS OF BOTH ISSUE CREATORS AND LABELS AND REMOVE DUPLICATES
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
    # PRINTS LIST OF LABELS AND THE # OF CONTRIBUTIONS/EVENTS ASSOCIATED W/ THOSE LABELS ALONG W/ GRAPHS CONTRIBUTIONS VS LABELS
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
                    print("----# of events - " + str(self.labelsAnalyzerList[a].issueLabelContributorAmount)) 
                    
        labelName = []
        labelContributorAmount = []
        
        for a in range(len(self.labelsAnalyzerList)):
            labelName.append(self.labelsAnalyzerList[a].issueLabelName)
            labelContributorAmount.append(self.labelsAnalyzerList[a].issueLabelContributorAmount)
        
        
        plt.bar(labelName, labelContributorAmount)
        plt.xticks(rotation=90)
        plt.ylabel('Contributions/Events')
        plt.title('List of Issue Labels')
        plt.show()
    
    #feature 2 analysis 
    #TAKES AN INPUT VALUE AND PRINTS ALL ISSUES THAT ARE REPEATED GREATER THAN THAT VALUE        
    #TAKES A CREATOR AS AN ARGUMENT AND PRINTS THEIR ISSUE(S) AND THE # OF THEIR CONTRIBUTIONS TO THEIR OWN ISSUES
    def creator_Issues_Analysis(self):
        #INPUT VALUE ANALYSIS OF IDENTICAL ISSUES
        issuesSetList = []  
        for x in range(len(self.issues)):
            issuesSetList.append(self.issues[x].labels)
            #print(self.issues[x].labels)
        
        issuesSet = []
        [issuesSet.append(x) for x in issuesSetList if x not in issuesSet]
        h = 0
        instancesOf = input("Enter a number to find instances of issue greater than: ")
        while h < len(issuesSet):
            r = 0
            for x in range(len(self.issues)):
                if (issuesSet[h] == self.issues[x].labels):
                    r = r + 1
            try:        
                if(r > int(instancesOf)):
                    print("Issue---" + str(issuesSet[h]))       
                    print("----# of instances of issue:  " + str(r))
                else:
                    pass
            except:
                print("Invalid entry please re-enter feature 2")
                sys.exit()
            h = h+1
            
        self.creator_Contribution_Analysis()    
        
        #INPUT ANALYSIS OF CREATORS CONTRIBUTION TO CREATORS OWN ISSUES
    def creator_Contribution_Analysis(self):  
        self.issue_Analyzer()  
        try:                   
            creator = input("Enter 'Creator' Name to view their issues and contributions to that issue:  ")
            creatorName = None 
            for i in range(len(self.issues)): 
                if(creator == self.issues[i].creator): 
                    creatorName = creator
                    print(creator + " created issue(s): " + str(self.issues[i].labels))
                    for j in range(len(self.issues[i].events)): 
                        if(creator == self.issues[i].events[j].author):
                            print("-----Contributed to " + str(self.issues[i].labels) + " on " + str(self.issues[i].events[j].event_date))
        except:
           print("Invalid entry please re-enter feature 2")
           
           
    #feature 3 analysis    
    #PRINTS OUT EACH ISSUE LABEL AND THE TOTAL NUMBER OF COMMENTS ASSOCIATED W/ ALL ISSUES WITH THAT LABEL                                   
    def label_Comments(self):
        self.issue_Analyzer()
        n = 0
        
        while n < len(self.labelsAnalyzerList):
            i = 0
            print(self.labelsAnalyzerList[n].issueLabelName)
            for r in range(len(self.issues)): #scan all issues
                for k in range(len(self.issues[r].labels)): #scan issue labels
                    if(self.labelsAnalyzerList[n].issueLabelName == self.issues[r].labels[k]):
                        for j in range(len(self.issues[r].events)):
                            if(self.issues[r].events[j].event_type == "commented"):
                                i = i + 1
            print ("----Number of comments associated with label " + str(i))       
            n = n + 1
        

class Label_Analyzer:
    
    issueLabelName:str = None
    issueLabelContributorAmount:int = 0
    
    def __init__(self, name, amount):
        
        self.issueLabelName = name
        self.issueLabelContributorAmount = amount
    
    
    
    
               
       