#!/usr/bin/python 
#####################################################################
# This is my pyTool. Its here to give me access to some of the more #                      
# advanced features of python in the bash shell. Im making it pretty#
# just in case anyone other than me is ever reading this. *aMigod666#
#####################################################################
# VERSION 1.55 ######################################################
#####################################################################
# Version 1.55 - fixed bugs in memory allocation		    
#								    
# Version 1.50 - Major revsion - almost 2.0 but no extra features   
#	    But we did combine -c and -s. you can give 	            
#           -cs or -sc for caps and spaces!!			    
#								    
#								    
#           - also defined all actions into functions for           
#             a more extensible interface.		            
#							            
# Version 1.00 - Inital Release. -s removes spaces from file name   
#		 -c removes uppercase letters from                  
#           filename					    
#####################################################################
# FEATURES: -c removes capital letters from filenames		    
#	    -s removes *spaces from file names	                    
#	    -sc or -cs removes *spaces and capitol letters	    
#	         	*spaces are replaced with '_'		    
#####################################################################
# TODO:
#         * add -y argument option to always accept newFilename
#           (mainly for script usage)
#         * add -i argument option to enter "interactive" mode
#           (while in interactive mode prog will ask files to change)
#         * implement code for check_if_caps and check_if_spaced
#           functions, to ask user if they want to keep a file
#           that still has spaces or uppercased letters in it
#####################################################################
# Written By: aMigod666(KyleJRoux) - i need a job!!!!## #############
#####################################################################
#####################################################################
#FUNCTIONS###########################################################
#####################################################################
# usage_message() - print a usage message			    
#		                                                    
# lower_case() - change caps to lower case in supplied filename	    
#								    
# remove_spaces() - replace spaces ' ' in a filename to '_' 	    
#                                                                   
# check_filename() - check if user is ok with new filename          
#                                                                   
# report_success() - give user a message, for better or worse  TODO     
# 
# check_if_caps() - check if filename still has caps in it TODO
#
# check_if_spaces() - check for spaces in newFilename TODO
#####################################################################
#####################################################################
# FUNCTION DEFS #####################################################
#####################################################################
# check_filename() ##################################################
#####################################################################
def check_filename(string):
    done = False
    global newString
    while (done == False):
        print "\tFilename will change from (", string, ") to (", newString, ")"
        print "\n\tIs this ok?\n\t(last chance before i change the filename)"
        print "\n\tPlease tell me(y or n):",
        choice = raw_input()
        if (choice == 'n'):
            print "(", string, ") not changed."
            done = True
            sys.exit(1)
        elif (choice == 'y'):
            # now replace filename
            rename(argv[2], newString)
            done = True
        else:
            print("Please enter lower case y or n.")
            done = False
#####################################################################
# usage_message() ###################################################
#####################################################################
def usage_message():						    
    # give the unknowing user a good message		    
    print("USAGE: pyTool [-c -s -cs -sc] <bad-filename>")	    
    print("\n")							    
    print("\n\tUse pyTool -c to replace caps with lowercase")	    
    print("\tletters in <filename>.")				    
    print("\n\tUse pyTool -s to replace spaces with '_' in ")	    
    print("\t<filename>. ")					    
    print("\n\n\t NOTE: can take any combo of -cs or -sc for both.")
    print("\n")                                                    
    print("\t\t\tBy:aMigod666(KyleJRoux)\n")			    
    exit(1)							    
#####################################################################
# lower_case() ######################################################
#####################################################################
def lower_case(stringToLower):                                      #
    newString = stringToLower.lower()                               #
    return newString                                                #
#####################################################################
# remove_spaces() ###################################################
#####################################################################
def remove_spaces(stringWithSpaces):                                #
    newString = stringWithSpaces.replace(' ', '_')                  #
    return newString                                                #
#####################################################################
# IMPORTS  ##########################################################
#####################################################################
import os, sys, macpath    ##########################################
from os import rename	   ##########################################
from sys import argv	   ##########################################
from macpath import isfile ##########################################
#####################################################################
# GLOBALS ###########################################################
#####################################################################
global newString                                                    #
global oldString                                                    #
global tempString                                                   #
newString = ''                                                      #
oldString = ''                                                      #
tempString = ''                                                     #
#####################################################################
# START #############################################################
#####################################################################

# check for correct command line structure 

if (len(argv) == 1) or (len(argv) == 2) or (isfile(argv[2]) == False):
    usage_message()
    sys.exit(1)
else:
    if (len(argv) == 3):
        # assign filename to oldString
        oldString = argv[2]
        
        # check if '-c' was given on the command line
        if (argv[1] == '-c'):
            newString = lower_case(oldString)

        # check if '-s' was given
        elif (argv[1] == '-s'):
            newString = remove_spaces(oldString)

        # check if '-cs or -sc' was given
        elif (argv[1] == '-cs' or '-sc'):
            tempString = remove_spaces(oldString)
            newString = lower_case(tempString)

        # if none of the above then incorrect argument
        # so print usage
        else:
            usage_message()
            sys.exit(1)

# end argument check

check_filename(newString)

# see if user likes new name
#done = False
#while (done == False):
#    print "\tFilename will change from (", oldString, ") to (", newString, ")" 
#    print "\n\tIs this ok?\n\t(last chance before i change the filename)"
#    print "\n\tPlease tell me(y or n):",
#    choice = raw_input()
#    if (choice == 'n'):
#        print "**", oldString, "** not changed."
#        done = True
#        sys.exit(1)
#    elif (choice == 'y'):
        # now replace filename
#        rename(argv[2], newString)
#        done = True
#    else:
#        print("Please enter lower case y or n.")
#        done = False

# check and report success 
if (isfile(newString)):
    print "Successfully changed", oldString, "to", newString
    sys.exit(0)
else:
    print "Uhoh. Looks like somthing went. you might wanna check."
    sys.exit(1)
