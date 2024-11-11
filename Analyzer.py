
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
    # PRINTS LIST OF LABELS AND THE # OF CONTRIBUTIONS ASSOCIATED W/ THOSE LABELS ALONG W/ GRAPHS CONTRIBUTIONS VS LABELS
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
    #TAKES A CREATOR AS AN ARGUMENT AND PRINTS THEIR ISSUE LABELS AND THE CREATORS CONTRIBUTIONS TO ALL ISSUES WITH THAT LABEL
    def creator_Issues_Analysis(self):    
        self.issue_Analyzer()                 
        creator = input("Enter 'Creator' Name:  ")
        creatorName = None 
        for i in range(len(self.issues)):  #scan issues
            if(creator == self.issues[i].creator): #see if creator is in issues
                creatorName = creator
                for j in range(len(self.issues[i].labels)):  #scan every issue label for creator
                    print(creator + " created issue '" + self.issues[i].labels[j] + "' on " + str(self.issues[i].created_date))
                    for x in range(len(self.issues)):
                        for r in range(len(self.issues[x].labels)):
                            if(self.issues[i].labels[j] == self.issues[x].labels[r]):
                                for s in range(len(self.issues[x].events)):
                                    if(creator == self.issues[x].events[s].author):
                                        print("----Contributed to label '" + self.issues[x].labels[r] + "' created by " + self.issues[x].creator + " on " + str(self.issues[x].events[s].event_date))
            elif(creator.upper() == "EXIT"):
                sys.exit()
        if(creatorName == None):
           print("Creator does not exist.  Please re-enter Creator or type 'EXIT' to exit feature.")
           self.creator_Issues_Analysis()
           
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
            print ("----Number of comments for label " + str(i))       
            n = n + 1
        

class Label_Analyzer:
    
    issueLabelName:str = None
    issueLabelContributorAmount:int = 0
    
    def __init__(self, name, amount):
        
        self.issueLabelName = name
        self.issueLabelContributorAmount = amount
    
    
    
    
               
       