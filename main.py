import os
import time
from argparse import ArgumentParser

def bulid_Parser():
    '''
    Parse the command line argument
    '''
    parser = ArgumentParser()
    parser.add_argument('-file','--file',required=True,type=str,help='Enter the file name to be deleted, case sensitive')
    parser.add_argument('-folder','--folder',required=False,type=str,default='.',help='Enter the root folder directory of where you would like to start deleting the file from, case sensitive. Default value is set to your current root directory')

    return parser

def walk(args):
    count = 0
    for (dirPaths, dirNames, fileNames) in os.walk(args.folder):
        for file in fileNames:
            if file == args.file:
                file_Path = (os.path.join(dirPaths,file))
                os.remove(file_Path)
                count += 1          
    print('Total of {} {} file(s) deleted \n'.format(count, args.file))        
            

def main():
    args = bulid_Parser().parse_args()
    
    start  = time.time()
    walk(args)
    end = time.time()

    print('Time taken is {} seconds'.format(end-start))


if __name__ == "__main__":
    main() 