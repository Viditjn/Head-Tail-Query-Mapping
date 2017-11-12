import numpy as np
import pydexter

def Entity_linkage(headQuery,tailQuery,dxtr):

	
	head_result=dxtr.nice_annotate(headQuery, min_conf=0.8)
	# print head_entities
	head_entities=set()
	for item in head_result:
		if type(item)==tuple:
			head_entities.add(item[1])

	# print head_entities		

	# getting entites in the tail query
	tail_result=dxtr.nice_annotate(tailQuery, min_conf=0.8)	

	tail_entities=set()
	for item in tail_result:
		if type(item)==tuple:
			tail_entities.add(item[1])

	if len(head_entities)==0 or len(tail_entities)==0:
		return 0		

	avg_score=0.0

	for head_entity in head_entities:
		for tail_entity in tail_entities:
			avg_score=avg_score+dxtr.relatedness(head_entity,tail_entity)["relatedness"]

	avg_score=avg_score/(len(head_entities)*len(tail_entities))
	
	# avg_score=np.tanh(avg_score)
	
	if avg_score>=0.5:
		return 1

	else:
		return 0

if __name__ == '__main__':
	
	dxtr=pydexter.DexterClient("http://dexterdemo.isti.cnr.it:8080/dexter-webapp/api/")
	count=0
	query_pairs=0
	with open("newMedium.txt") as infile:
		for line in infile:
			headQuery,tailQuery,relevance=line.split("||")
			headQuery=headQuery.strip()
			tailQuery=tailQuery.strip()
			relevance=int(relevance.strip())
			# print headQuery
			# print tailQuery
			# print relevance
			# break
			pred=Entity_linkage(headQuery,tailQuery,dxtr)
			print headQuery,tailQuery,pred

			if pred==relevance:
				count+=1

			query_pairs+==1	

	print "accuracy is: ",count/query_pairs		
	print "Done"		 
