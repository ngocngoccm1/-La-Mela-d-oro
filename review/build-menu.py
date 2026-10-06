import json,pathlib,re,unicodedata
root=pathlib.Path(__file__).resolve().parent.parent
inv=json.loads((root/'review/assets-inventory.json').read_text())
categories={}
veg={'101','115','151','161','215','221','149'}
scharf={'124','125','143','144','155','156','708','207'}
for line in (root/'review/transcription.txt').read_text().splitlines():
 if not line: continue
 if line.startswith('@'):
  source,name,label,*notes=line[1:].split('|'); source=int(source)
  catid=re.sub(r'[^a-z0-9]+','-',unicodedata.normalize('NFKD',name).encode('ascii','ignore').decode().lower()).strip('-')
  category=categories.setdefault(catid,{'id':catid,'category':name,'label':label,'note':notes[0] if notes else '', 'items':[]})
  continue
 number,name,description,prices,codes=line.split('|')
 variants=[]
 if prices!='?':
  for p in prices.split(';'):
   label,price=p.rsplit(':',1) if ':' in p else ('Portion',p)
   variants.append({'label':label,'priceCents':round(float(price)*100)})
 if number=='extra': variants=[{'label':s,'priceCents':450} for s in ['Kroketten','Pommes Frites','Bratkartoffeln']]
 # Source repeats number 950 for Ginger Ale and beer. IDs are category-qualified.
 item={'id':catid+'-'+number,'number':number if number!='extra' else '', 'name':name,'description':description,'variants':variants,'allergenCodes':[c for c in codes.split(',') if c], 'tags':(['vegetarisch'] if number in veg else [])+(['scharf'] if number in scharf else []),'source':inv[source-1]['file'],'sourcePage':source,'needsReview':prices=='?'}
 if prices=='?': item['reviewReason']='Preis am rechten Bildrand abgeschnitten; nicht ergänzt.'
 category['items'].append(item)
food=['pizze','antipasti','zuppe','insalate','pizzapane-pizzabrot','spaghetti','penne','rigatoni','tagliatelle','tortellini','canelloni','lasagne','primi-piatti-di-riso','carni-di-maiale','carni-di-manzo-e-vitello','pesce-di-mare','pesce-dacqua-dolce','spezialita-per-bambini','beilagen','dolce','gelati']
sushi=['sushi','sashimi','nigiri','inside-out-roll','special-roll','crunchy-roll','sushi-menu','japanische-kuche']
for cat in categories.values(): cat['group']='sushi' if cat['id'] in sushi else 'food' if cat['id'] in food else 'drinks'
order=food+sushi+['bevande-analcolici','succhi','bevande-calde','birra-alla-spina','birra-speziale','vini-rossi','vini-bianchi','cocktails','alcolici']
# use actual generated IDs for punctuation normalization
print('Category IDs:',list(categories))
menu={'currency':'EUR','language':'de','source':'25 provided menu photographs; manually transcribed','notes':['Allergen- und Zusatzstoffcodes sind aus der Originalkarte übernommen. Die zugehörige Legende wurde nicht mitgeliefert. Bitte fragen Sie bei Allergien im Restaurant nach.'],'categories':sorted(categories.values(),key=lambda c:order.index(c['id']) if c['id'] in order else 99)}
(root/'website/dist/data/menu.json').write_text(json.dumps(menu,ensure_ascii=False,indent=2))
for record in inv:
 record.update({'type':'menu','reviewed':True,'items':sum(i['sourcePage']==record['index'] for c in categories.values() for i in c['items'])})
(root/'review/assets-inventory.json').write_text(json.dumps(inv,ensure_ascii=False,indent=2))
print('Total:',sum(len(c['items']) for c in categories.values()),'Review:',sum(i['needsReview'] for c in categories.values() for i in c['items']))
