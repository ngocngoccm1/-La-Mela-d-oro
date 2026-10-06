import sys
sys.path.insert(0, r'C:\nhtn\landingPage\La Mela d_oro\review\font-tools')
from fontTools import subset
from pathlib import Path
root=Path(r'C:\nhtn\landingPage\La Mela d_oro\website\dist\assets')
for name in ['display','body']:
 options=subset.Options();options.flavor='woff2';options.layout_features=['*']
 font=subset.load_font(str(root/(name+'.ttf')),options)
 sub=subset.Subsetter(options=options);sub.populate(unicodes=set(range(0x0000,0x0250))|set(range(0x2000,0x2070))|{0x20ac,0x2212});sub.subset(font)
 subset.save_font(font,str(root/(name+'.woff2')),options)
 print(name,(root/(name+'.woff2')).stat().st_size)
