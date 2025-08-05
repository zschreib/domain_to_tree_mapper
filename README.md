# 

A simple script to transform [PHIDRA](https://github.com/zschreib/phidra) pfam_validated_report.tsv domain annotations into a color-coded mapping file for tree visualization.

## Features

- Reads a TSV of Pfam hits per query  
- Calculates bar heights = |Env_Starts - Env_Ends| for each Pfam  
- Assigns each unique Pfam a hex color.
- Outputs a TSV with one row per query used as a mapping file upload in [Iroki](https://www.iroki.net/)

## Requirements

- Python 3.6+  
- pandas  
- seaborn  
- matplotlib  

## Usage

```
python phidra_domain_to_tree_map.py <input.tsv> <output.tsv>
```

![Mapping tree example](https://raw.githubusercontent.com/zschreib/domain_to_tree_mapper/main/test_output/ENA_polA_example.png)

## Authors

Contributors names and contact info.

zschreib@udel.edu

## Acknowledgments

Tree visuals provided by [Iroki](https://www.iroki.net/)
