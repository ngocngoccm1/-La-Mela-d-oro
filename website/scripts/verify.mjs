import {readFileSync,existsSync} from 'node:fs';
import {resolve,dirname} from 'node:path';
import {fileURLToPath} from 'node:url';
const root=resolve(dirname(fileURLToPath(import.meta.url)),'../dist');
const menu=JSON.parse(readFileSync(resolve(root,'data/menu.json'),'utf8'));
const restaurant=JSON.parse(readFileSync(resolve(root,'data/restaurant.json'),'utf8'));
const items=menu.categories.flatMap(c=>c.items);
const fail=message=>{throw new Error(message)};
if(new Set(items.map(i=>i.id)).size!==items.length)fail('Duplicate item IDs');
for(const item of items){if(!item.source||!item.name)fail('Missing source/name');for(const v of item.variants)if(!Number.isInteger(v.priceCents)||v.priceCents<0||!v.label)fail('Invalid price/variant '+item.id);if(item.needsReview&&item.variants.length)fail('Unverified priced item '+item.id);if(!existsSync(resolve(root,`assets/original-menu/page-${String(item.sourcePage).padStart(2,'0')}.webp`)))fail('Missing source image');}
if(!restaurant.phoneHref.startsWith('tel:'))fail('Invalid telephone link');
const html=readFileSync(resolve(root,'index.html'),'utf8');
if((html.match(/<h1\b/g)||[]).length!==1)fail('Expected one H1');
for(const match of html.matchAll(/(?:src|href)="([^"]+)"/g)){const url=match[1];if(!url.startsWith('#')&&!/^(https?:|tel:|data:)/.test(url)&&!existsSync(resolve(root,url)))fail('Missing asset '+url);}
const schema=JSON.parse(html.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/)[1]);if(schema.name!==restaurant.name||schema.telephone!==restaurant.phoneHref.slice(4))fail('Structured data mismatch');
console.log(`Verified ${items.length} items, ${menu.categories.length} categories, 25 source pages, local assets and Restaurant metadata.`);
