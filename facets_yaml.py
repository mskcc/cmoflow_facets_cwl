#%%
import argparse
import os
import sys
import subprocess
import yaml

#%%
# Create the parser
facets_cwl_parser = argparse.ArgumentParser(description='Wrapper for editing cmoflow_facets_cwl YAML file on JUNO')

# Add the arguments
facets_cwl_parser.add_argument('-tb',dest = 'bam_tumor',type=str,help='File path of tumor bam')
facets_cwl_parser.add_argument('-nb',dest = 'bam_normal',type=str,help='File path of normal bam')
facets_cwl_parser.add_argument('-s',dest = 'snp_pileup_fname',type=str,help='SNP pileup file name')
facets_cwl_parser.add_argument('-cval',dest = 'cval',type=str,help='Cval for FACETS')
facets_cwl_parser.add_argument('-pcval',dest = 'pcval',type=str,help='Purity cval for FACETS')
facets_cwl_parser.add_argument('-op',dest = 'facets_output_prefix',type=str,help='FACETS output files prefix')
facets_cwl_parser.add_argument('-tid',dest = 'tumor_id',type=str,help='Tumor sample ID')
facets_cwl_parser.add_argument('-yfp',dest = 'yaml_path',type=str,help='Template yaml file path')
facets_cwl_parser.add_argument('-o',dest = 'output_path',type=str,help='Output yaml file path (file name would be tumor sample ID)')

# Execute the parse_args() method
args = facets_cwl_parser.parse_args()

#%%
# with open('/juno/work/bergerm1/bergerlab/zhengy1/cmoflow_facets_cwl/inputs.yaml') as f:
with open(args.yaml_path) as f:
    # use safe_load instead load
    facets_yaml = yaml.safe_load(f)

facets_yaml
facets_yaml['bam_tumor']['path'] = args.bam_tumor
facets_yaml['bam_normal']['path'] = args.bam_normal
facets_yaml['snp_pileup_output_file_name'] = args.snp_pileup_fname
facets_yaml['cval'] = int(args.cval)
facets_yaml['purity_cval'] = int(args.pcval)
facets_yaml['facets_output_prefix'] = args.facets_output_prefix
facets_yaml['tumor_id'] = args.tumor_id


#%%
with open(args.output_path+'/'+args.tumor_id+'.yaml', "w") as f:
    yaml.dump(facets_yaml, f, default_flow_style=False)
