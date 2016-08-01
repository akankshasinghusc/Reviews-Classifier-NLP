import os,sys, re, json
return_list = []
second=[]
my_dict = {}
vocabdirectory=set()

completelinelist=[]
vocabList_of_a_class={}

#mainpath ="E:\\NLP\\Assignment 2\\op_spam_train\\op_spam_train"

mainpath=sys.argv[1]


negativedeceptivedict={}
negativetruthfuldict={}
positivedeceptivedict={}
positivetruthfuldict={}

dictlist=[negativetruthfuldict,negativedeceptivedict,positivetruthfuldict,positivedeceptivedict]


def Vocab_func(vocabList_of_a_class,line):
    count=0
    vocabdirectory
    for word in line.split():
        count=count+1
        word = re.sub(r'[^\w\s]','',word)

        vocabdirectory.add(word)
        if word in vocabList_of_a_class:
            wordfrequency=vocabList_of_a_class.get(word)+1;
            vocabList_of_a_class[word]=wordfrequency
        else:
            vocabList_of_a_class[word]=1

    return count







def foldercall():

        global return_list
        global second
        global my_dict
        global vocabdirectory

        global completelinelist
        global vocabList_of_a_class

        global dictlist

        first=os.listdir(mainpath)
        #print(first)
        count=0
        classcount=0
        DiffClass={}
        VocabClass={}
        lines_count_class={}


        for firstlist in first:
            if os.path.isdir(mainpath + "/" + firstlist):
                second=os.listdir(mainpath + "/" + firstlist)


                for secondlist in second:
                    if os.path.isdir(mainpath+ "/" + firstlist + "/" + secondlist):

                        #    Incrementing class counter
                        className=dictlist[classcount]


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
                                        #print(line)
                                        completelinelist.append(line)
                                        count+=Vocab_func(className,line)
                                        currentfile.close();
                                        #print(newlinelist)



                        className["TOTAL"]=count
                        className["TOTAL_LINES"]=len(completelinelist)
                        VocabClass[classcount]=className

                        classcount=classcount+1

        #VocabClass["Total"]=vocabdirectory
        #dictlist=[""]
        VocabClass["total vocab"]=len(vocabdirectory)
        #print(VocabClass)
        jsonData=json.dumps(VocabClass)
        output_text=open("nbmodel.txt", 'w')
        output_text.write(jsonData)
        output_text.close()


foldercall()
