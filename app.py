#dependencies
from ntrs import ntrs


ntrs = ntrs()

# agentKeywordsSTR = 'Treating diabetes with herbs, phytoconstituent purchase, active ingredient manufacturers, biochemical diabetic treatment, chemical compound manufacture, phytonutrient medication, prophenylphenols diabetes, phytoconstituent production, phytoconstituent producer, phytoconstituent process, phytoconstituent fabrication, herbal diabetic, homeopathic manufacture, herbal remedies factory'
# agentKeywordsSTR = 'diabetes herbs,phytoconstituent purchase,active ingredient manufacturers,biochemical diabetic treatment,chemical compound manufacture,phytonutrient medication,prophenylphenols diabetes,phytoconstituent production,phytoconstituent producer,phytoconstituent process,phytoconstituent fabrication,herbal diabetic,homeopathic manufacture,herbal remedies factory'
agentKeywordsSTR = 'medical diagnostics,animal laboratory,animal diagnostic approaches,human diagnostics'

# agentKeywordsSTR = 'folia mechanism,folia device,foliar equipment,folia apparatus,foliar spray,carbon spray,leaf carbon application,leaf fertilizer method,folia fertilize method,chemical folia technique,inorganic phosphate application,farming spray equipment,horticulture spray device,horticulture device manufacture,horticulture dressing apparatus,foliar enrichment application,foliage device,enrich'
# agentKeywordsSTR = 'furfural from Levulinic Acid,Direct conversion of furfural,synthesis furfural,Direct conversion of furfural,synthesis levulinic,synthesis,yield levulinate'
agentKeywordsList = agentKeywordsSTR.split(",")
# agentKeywordsList=agentKeywordsList.strip('')


trimmed_words=[]
for x in agentKeywordsList:
# for x in [agentKeywordsSTR]:
    x=x.strip()
    trimmed_words.append(x)
print(f'list of trimmed words for {x}: {trimmed_words}')


results_count=0
result_terms_list=[]
for phrase in trimmed_words:

    print(phrase)
    r = ntrs.search(phrase,0)
    phrase_num_records = r["stats"]["total"]
    print(phrase_num_records)
    result_terms=r['results']
    print(len(result_terms))
    result_terms_list.append(result_terms)
    print(f'phrase records: {phrase_num_records}')
    results_count=phrase_num_records + results_count
print(f'results count: {results_count}')




# print(f'result terms list first item: {result_terms_list[0][1]}')
# for results in result_terms_list:
    ## if len(results) > 0:
#     score=results[0]['_meta']['score']   
#     center=results[0]['center']['name']
#     # full_response=results[1]
#     print(f'_______________________')
#     # print(full_response)
#     print(f'score: {score}')
#     print(f'center: {center}')
# # r = ntrs.search(agentKeywordsList,0)
# # totalRecords = r["stats"]["total"]
# # resultterms=r['results']
# # print(resultterms)
# # print(totalRecords)
