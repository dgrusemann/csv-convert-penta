## CSV Convert Penta
    Converts the given source.csv file to target.csv. Source file may contian data which must be brought in the form of target csv file.

### Contents
>    1) Installation
>    2) Information
>    3) How to run it
 
### Installation
> - The project is based on python2.7
> - The folder contians the file requirements.txt which contains the libaries which needed to be installed
>>  run the following command   
>>> sudo pip install -r requirements.txt

### Information
> - The project is meant for transforming one csv file to another keeping the structure of target csv file
> - Target CSV file may contain some of the mandatory fields, while the other may be optional.
> - Similary in Transform.py file there is Transform function which has mandatory fields list, you can modify these list according to your needs.

### How to run it
> - Transform.py contains a **Transfor function** which needs two parameters as the path to **source file and target file** 
>>  Transform(sourceFilePath,targetFilePath)
> - Currently I have main function which takes the input the path from the user itself
> - But you can have Transform.py file as a module which you can import into your function or main file. This module will require only the source-file-path and target-file-path

>> You can the following command to use it
>>> python Transform.py




