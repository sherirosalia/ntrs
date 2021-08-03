#dependencies
from ntrs import ntrs
import csv
from pprint import pprint

ntrs = ntrs()

# agentKeywordsSTR = 'extreme heat,self priming,ceramic coating,high celcius,extreme heat,high celcius, thermal barrier coating, abrasion resistance coating, 1700 Celcius ceramic coating, high temperature self priming ceramic coating, high-temperature coating composistion'
agentKeywordsSTR = 'jpeg quality estimate,image quality calculation,image quality percentage,photo analysis invention,lossy algorithm,jpeg compression,jpeg quality,image lossy algorithm,lossy format estimate,computed photo method,computed image estimate,computed jpeg quality,jpeg algorithm,jpeg estimate,image quality detection'

agentKeywordsList = agentKeywordsSTR.split(",")
# agentKeywordsList=agentKeywordsList.strip('')
print(agentKeywordsList)

trimmed_words=[]
for x in agentKeywordsList:
# for x in [agentKeywordsSTR]:
    x=x.strip()
    trimmed_words.append(x)
print(f'list of trimmed words for {x}: {trimmed_words}')


results_count=0
result_terms_list=[]
results_information = []
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
    phrase_results = r["results"]
    # pprint(phrase_results)
    
    for phrase_result in phrase_results:
        if phrase_result is not None:
            results_meta_score = phrase_result["_meta"]["score"]
            if results_meta_score is not None:
                print(results_meta_score)
            else:
                print('no score')
            
            if "subjectCategories" in phrase_result:
                results_categories = phrase_result["subjectCategories"]
                print(results_categories)
            else:
                print('no results categories')

            if "title" in phrase_result:
                results_title = phrase_result["title"]
                print(results_title)
            else:
                print('no results title') 

            if "abstract" in phrase_result:
                results_abstract = phrase_result["abstract"]
                print(results_abstract)
            else:
                print('no results abstracts')       

            results_dictionary = {
                'title' : results_title,
                'score' : results_meta_score,
                'search term': phrase,
                'categories' : results_categories,
                'abstract' : results_abstract,
            }
        results_information.append(results_dictionary)
print(f'results count: {results_count}')
print('-----------------------------------------------------------------')

from pprint import pprint
pprint(results_information)
keys=results_information[0].keys()
print(keys)
with open('data_compression_6_23.csv', 'w', encoding='utf8', newline='') as output_file:
    csv_rows= csv.DictWriter(
        output_file, fieldnames=results_information[0].keys(),
    )
    csv_rows.writeheader()
    csv_rows.writerows(results_information)

