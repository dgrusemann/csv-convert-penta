import pandas as pd
import numpy as np
import sys
def ReadCsvData(sourceFile,targetFile):
    # reading the csv data using pandas
    # storing the csv into a dataFrame
    sourceDataFrame = pd.read_csv(sourceFile)
    targetDataFrame = pd.read_csv(targetFile)
    
    # Modifying the headers (column names) into lower case names
    sourceDataFrame.columns = sourceDataFrame.columns.str.lower()
    targetDataFrame.columns = targetDataFrame.columns.str.lower()
    
    # returning the dataframes
    return sourceDataFrame,targetDataFrame

def Transform(sourceFilePath, targetFilePath):
    
    # calling function ReadCsvData to get the DataFrames for the input csv files
    sourceDataFrame,targetDataFrame = ReadCsvData(sourceFilePath, targetFilePath)
    
    # Replacing NaN Null values with NULL string
    sourceDataFrame.replace(np.NaN, 'NULL', inplace=True)


    # getting no of rows from the sourceDataFrame
    noOfRowsSourceDF = len(sourceDataFrame.axes[0])
    
    #  getting name of columns from targetDataFrame 
    nameOfColsTargetDF = targetDataFrame.axes[1]
    
    # setting the mandtory fields that should be persent in the Target.csv
    mandotryFields = ['value date','amount']
    
    # Appending the sourceDataFrame to targetDataFrame
    for i in range(0,noOfRowsSourceDF):
        # getting the details of sourceDataFrame row by row
        
        #creating the empty list for each row 
        rowToBeAppended = []
        
        # creating the empty dictionary for adding the columns values which are to be transformed
        colsValues={}
        
        # this variable is used as flag intially set to 0
        setNotToAdd=0
        
        # this loop is to get details of the column being needed for target.csv
        
        for j in range(0,len(nameOfColsTargetDF)):
            
        # current column name
            colsName = nameOfColsTargetDF[j]

            # we added the values for mandotry columns
            if colsName in mandotryFields:

                # if the sourceDataFrame has NaN value for mandotry filed we just set the flag and break
                print("this is ",bool(sourceDataFrame[colsName][i]),sourceDataFrame[colsName][i]) 
                if sourceDataFrame[colsName][i]=="NULL":
                    setNotToAdd=1
                    break
                else:
                    colsValues.update({colsName:sourceDataFrame[colsName][i]})
            else:

                if colsName in sourceDataFrame.columns:
                    colsValues.update({colsName:sourceDataFrame[colsName][i]})
                else:
                    colsValues.update({colsName:'NaN'})


        # ethier we append the dict to list or not depending upon flag
        if(setNotToAdd==1):
            rowToBeAppended[:]=[]
        else:
            rowToBeAppended.append(colsValues)
            
        # either we append the list to targetDataFrame
        if len(rowToBeAppended)>0:
            targetDataFrame = targetDataFrame.append(rowToBeAppended,ignore_index=True)
    
    # writing the targetDataFrame to target.csv file
    targetDataFrame.to_csv('test/target.csv', encoding='utf-8', index=False)
    return targetDataFrame


# To prompt the user to input the file path

# sourceFile = raw_input('Enter the path to source.csv file \n')
# targetFile = raw_input('Enter the path to source.csv file \n')

# command line argument

sourceFile = sys.argv[1]
targetFile = sys.argv[2]

targetDataFrame = Transform(sourceFile,targetFile)
print(targetDataFrame)