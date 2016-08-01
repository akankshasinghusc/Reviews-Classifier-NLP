import os,sys,re,json, math

output={}
totalVocab = 0
negativedeceptivedict={}
negativetruthfuldict={}
positivedeceptivedict={}
positivetruthfuldict={}

#mainpath ="E:/NLP/Assignment 2/op_spam_train/op_spam_train_test"

mainpath=sys.argv[1]
def readData():
    with open("nbmodel.txt") as jfile:
        output= json.load(jfile)

    global negativedeceptivedict
    global negativetruthfuldict
    global positivedeceptivedict
    global positivetruthfuldict
    global totalVocab

    totalVocab= output["total vocab"]
    negativetruthfuldict=output["0"]
    negativedeceptivedict=output["1"]
    positivetruthfuldict=output["2"]
    positivedeceptivedict=output["3"]







def probability_calculate_func(line,path):

    probability_negative_deceptive= 0.0
    probability_negative_truthful = 0.0
    probability_positive_deceptive=0.0
    probability_positive_truthful=0.0



    global maxprob

    global label_path


    global negativedeceptivedict
    global negativetruthfuldict
    global positivedeceptivedict
    global positivetruthfuldict
    global totalVocab


    for word in line.split():
        word = re.sub(r'[^\w\s]','',word)
        if word in negativedeceptivedict:
            diffwordcount1=negativedeceptivedict[word]+1
        else:
            diffwordcount1=1
        if word in negativetruthfuldict:
            diffwordcount2=negativetruthfuldict[word]+1
        else:
            diffwordcount2=1
        if word in positivedeceptivedict:
            diffwordcount3=positivedeceptivedict[word]+1
        else:
            diffwordcount3=1
        if word in positivetruthfuldict:
            diffwordcount4= positivetruthfuldict[word]+1
        else:
            diffwordcount4=1

        probability_negative_deceptive= probability_negative_deceptive+ math.log10(diffwordcount1/(negativedeceptivedict["TOTAL"]+totalVocab))
        probability_negative_truthful= probability_negative_truthful+ math.log10(diffwordcount2/(negativetruthfuldict["TOTAL"]+totalVocab))
        probability_positive_deceptive= probability_positive_deceptive+ math.log10(diffwordcount3/(positivedeceptivedict["TOTAL"]+totalVocab))
        probability_positive_truthful= probability_positive_truthful+ math.log10(diffwordcount4/(positivetruthfuldict["TOTAL"]+totalVocab))

    MAX_LIST=[]
    MAX_LIST.append(probability_negative_deceptive)
    MAX_LIST.append(probability_negative_truthful)
    MAX_LIST.append(probability_positive_deceptive)
    MAX_LIST.append(probability_positive_truthful)

    maxprob=max(MAX_LIST)
    label =""

    if (maxprob==probability_negative_deceptive):
        label = 'deceptive negative '
    if(maxprob==probability_negative_truthful):
        label = 'truthful negative '
    if(maxprob==probability_positive_deceptive):
        label='deceptive positive '
    if(maxprob==probability_positive_truthful):
        label='truthful positive '

    label += path +"\n"

    return label


def folderCall_func():
        readData()
        global return_list
        global second
        global my_dict
        global vocabdirectory

        global completelinelist
        global vocabList_of_a_class

        global dictlist
        print_output_list = []

        first=os.listdir(mainpath)
        #print(first)
        count=0
        classcount=0
        DiffClass={}
        VocabClass={}

        for firstlist in first:
            if os.path.isdir(mainpath + "/" + firstlist):
                second=os.listdir(mainpath + "/" + firstlist)
                #print(second)

                for secondlist in second:
                    if os.path.isdir(mainpath+ "/" + firstlist + "/" + secondlist):
                        #    Incrementing class counter

                        third=os.listdir(mainpath+ "/" + firstlist + "/" + secondlist)


                        count=0

                        for thirdlist in third:
                            for root, dirs,filenames in os.walk(mainpath + "/" + firstlist + "/" + secondlist + "/" + thirdlist):
                                for files in filenames:

                                    if files.endswith('.txt'):

                                        #print(files)

                                        fullpathfiles= mainpath + "/" + firstlist + "/" + secondlist + "/" + thirdlist + "/" + files

                                        currentfile = open(fullpathfiles,'r')
                                        line=currentfile.readline();
                                        decision = probability_calculate_func(line,fullpathfiles)
                                        print_output_list.append(decision)






        output_file=open('nboutput.txt', 'w')
        for line in print_output_list:
            output_file.write(line)
        output_file.close()

folderCall_func()


    