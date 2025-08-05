import sys
import pandas as pd
import seaborn as sns
from itertools import cycle
from matplotlib.colors import to_hex

# I/O from argv
infile, outfile = sys.argv[1], sys.argv[2]

# load & split Pfams
df = pd.read_csv(infile, sep='\t')
df['Pfams'] = df['Pfam_IDs'].str.split('|')

# collect all unique Pfams
all_pfams = sorted({p for lst in df['Pfams'] for p in lst})
n = len(all_pfams)

# build palette
pal = sns.color_palette('tab20', n_colors=min(n,20))
if n > 20:
    pal += sns.color_palette('tab20b', n_colors=n-20)

# assign each Pfam a hex color
hex_cycle = cycle(to_hex(c) for c in pal)
pfam2color = {pf: next(hex_cycle) for pf in all_pfams}

# build mapping rows
rows = []
for _, r in df.iterrows():
    starts = r['Env_Starts'].split('|')
    ends   = r['Env_Ends'].split('|')
    heights = {pf: abs(int(s) - int(e)) for pf, s, e in zip(r['Pfams'], starts, ends)}
    row = {
        'name': r['Query_ID'],
        'new_name': r['Pfam_IDs']
    }
    for i, pf in enumerate(all_pfams, 1):
        h = heights.get(pf, 0)
        row[f'bar{i}_height'] = h
        row[f'bar{i}_color']  = pfam2color[pf] if h else '#FFFFFF'
    rows.append(row)

# write output
pd.DataFrame(rows).to_csv(outfile, sep='\t', index=False)
