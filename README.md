# cmoflow_facets_cwl
CWL to mimic the logic in cmoflow_facets

# Usage

1. Clone this repo and all its submodules to your working directory.

```
git clone --recursive https://github.com/mskcc/cmoflow_facets_cwl
```

2. Edit the `inputs.yaml` file by providing the necessary information for inputs:

```
facets_vcf: {
  class: File,
  path: /insert/your/path/here (.vcf),
  secondaryFiles: [
      {
        /insert/your/secondaryFile/path/here (.vcf.gz)
    }
    ]
  }

bam_normal: { class: File, path: /bam/here }
bam_tumor: { class: File, path: /bam/here }
```
You can also edit specific parameters for `snp-pileup` and `doFacets` in the YAML.

3. Once complete, submit to the executer using `cwltool` or `cwltoil`.

If you need a CWL executer, go to https://github.com/mskcc/cwl_run_scripts_juno - and follow the installation and run steps.
