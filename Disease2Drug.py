import urllib2
import ast

# get user input, output proper dieasetype
user_input = "hypertension"
url = "https://rxnav.nlm.nih.gov/REST/rxclass/spellingsuggestions.json?term="+user_input+"&type=CLASS"
response = urllib2.urlopen(url).read()
newdict = ast.literal_eval(response)
print newdict['suggestionList']['suggestion'][0]
dieseasetype = newdict['suggestionList']['suggestion'][0]

# get diseaseid
url2 = "https://rxnav.nlm.nih.gov/REST/rxclass/class/byName.json?className="+dieseasetype
response2 = urllib2.urlopen(url2).read()
newdict2 = ast.literal_eval(response2)
print newdict2['rxclassMinConceptList']['rxclassMinConcept'][0]['classId']
diesaseid = newdict2['rxclassMinConceptList']['rxclassMinConcept'][0]['classId']

#get list of drugs
url3 = 'https://rxnav.nlm.nih.gov/REST/rxclass/classMembers.json?classId='+ diesaseid + '&relaSource=NDFRT&rela=may_treat&trans=0'
response3 = urllib2.urlopen(url3).read()
newdict3 = ast.literal_eval(response3)
resultingdrugs = []
for value in newdict3['drugMemberGroup']['drugMember']:
    resultingdrugs.append(value['minConcept']['rxcui'])
print resultingdrugs