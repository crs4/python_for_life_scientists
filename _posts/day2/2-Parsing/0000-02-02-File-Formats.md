# File formats in bioinformatics

--

## There are four types of computer readable formats in bioinformatics

- FASTA-like
- GenBank-like
- Tables (TSV, CSV)
- XML-like
- JSON
- YAML

--

![f1]({{site.url}}/img/ff1.png)

--

![f2]({{site.url}}/img/ff2.png)

--

![f3]({{site.url}}/img/ff3.png)

--

![f4]({{site.url}}/img/ff4.png)

--

![f5]({{site.url}}/img/ff5.png)

--

## CSV
### comma separated value

```yamlex
"Lane","Sample_ID","Sample_Name","Sample_Plate","Sample_Well","I7_Index_ID","index","I5_Index_ID","index2","Sample_Project","Description"
1,"SAMPLE-IN-POOL18-0194-R0001","244-18 ",,,"N701","TAAGGCGA","E501","GCGATCTA","Project","Project"
1,"SAMPLE-IN-POOL18-0195-R0001","246-18P ",,,"N702","CGTACTAG","E501","GCGATCTA","Project","Project"
1,"SAMPLE-IN-POOL18-0196-R0001","246-18M ",,,"N703","AGGCAGAA","E501","GCGATCTA","Project","Project"
1,"SAMPLE-IN-POOL18-0197-R0001","248-18R1 ",,,"N704","TCCTGAGC","E501","GCGATCTA","Project","Project"
1,"SAMPLE-IN-POOL18-0198-R0001","260-18 ",,,"N712","GTAGAGGA","E501","GCGATCTA","Project","Project"
1,"SAMPLE-IN-POOL18-0199-R0001","465-15 ",,,"N706","TAGGCATG","E501","GCGATCTA","Project","Project"
1,"SAMPLE-IN-POOL18-0200-R0001","341-16 ",,,"N707","CTCTCTAC","E501","GCGATCTA","Project","Project"
1,"SAMPLE-IN-POOL18-0201-R0001","276-18 ",,,"N708","CAGAGAGG","E501","GCGATCTA","Project","Project"
1,"SAMPLE-IN-POOL18-0202-R0001","276-18P ",,,"N709","GCTACGCT","E501","GCGATCTA","Project","Project"
1,"SAMPLE-IN-POOL18-0203-R0001","355-16 ",,,"N710","CGAGGCTG","E501","GCGATCTA","Project","Project"
1,"SAMPLE-IN-POOL18-0204-R0001","285-18 ",,,"N711","AAGAGGCA","E501","GCGATCTA","Project","Project"
1,"SAMPLE-IN-POOL18-0205-R0001","465-15P ",,,"N701","TAAGGCGA","E502","ATAGAGAG","Project","Project"
1,"SAMPLE-IN-POOL18-0206-R0001","288-18M ",,,"N702","CGTACTAG","E502","ATAGAGAG","Project","Project"
1,"SAMPLE-IN-POOL18-0207-R0001","302-18P ",,,"N703","AGGCAGAA","E502","ATAGAGAG","Project","Project"
1,"SAMPLE-IN-POOL18-0208-R0001","140-18 ",,,"N704","TCCTGAGC","E502","ATAGAGAG","Project","Project"
1,"SAMPLE-IN-POOL18-0209-R0001","286-18 ",,,"N712","GTAGAGGA","E502","ATAGAGAG","Project","Project"
1,"SAMPLE-IN-POOL18-0210-R0001","288-18P",,,"N706","TAGGCATG","E502","ATAGAGAG","Project","Project"
1,"SAMPLE-IN-POOL18-0211-R0001","301-18 ",,,"N707","CTCTCTAC","E502","ATAGAGAG","Project","Project"
1,"DNA18-0079-R0001",60086,,,"H714","GCTCATGA","H505","CTCCTTAC","Project","Project"
2,"SAMPLE-IN-POOL18-0194-R0001","244-18 ",,,"N701","TAAGGCGA","E501","GCGATCTA","Project","Project"
2,"SAMPLE-IN-POOL18-0195-R0001","246-18P ",,,"N702","CGTACTAG","E501","GCGATCTA","Project","Project"
2,"SAMPLE-IN-POOL18-0196-R0001","246-18M ",,,"N703","AGGCAGAA","E501","GCGATCTA","Project","Project"
2,"SAMPLE-IN-POOL18-0197-R0001","248-18R1 ",,,"N704","TCCTGAGC","E501","GCGATCTA","Project","Project"
2,"SAMPLE-IN-POOL18-0198-R0001","260-18 ",,,"N712","GTAGAGGA","E501","GCGATCTA","Project","Project"
2,"SAMPLE-IN-POOL18-0199-R0001","465-15 ",,,"N706","TAGGCATG","E501","GCGATCTA","Project","Project"
2,"SAMPLE-IN-POOL18-0200-R0001","341-16 ",,,"N707","CTCTCTAC","E501","GCGATCTA","Project","Project"
2,"SAMPLE-IN-POOL18-0201-R0001","276-18 ",,,"N708","CAGAGAGG","E501","GCGATCTA","Project","Project"
2,"SAMPLE-IN-POOL18-0202-R0001","276-18P ",,,"N709","GCTACGCT","E501","GCGATCTA","Project","Project"
2,"SAMPLE-IN-POOL18-0203-R0001","355-16 ",,,"N710","CGAGGCTG","E501","GCGATCTA","Project","Project"
2,"SAMPLE-IN-POOL18-0204-R0001","285-18 ",,,"N711","AAGAGGCA","E501","GCGATCTA","Project","Project"
2,"SAMPLE-IN-POOL18-0205-R0001","465-15P ",,,"N701","TAAGGCGA","E502","ATAGAGAG","Project","Project"
2,"SAMPLE-IN-POOL18-0206-R0001","288-18M ",,,"N702","CGTACTAG","E502","ATAGAGAG","Project","Project"
2,"SAMPLE-IN-POOL18-0207-R0001","302-18P ",,,"N703","AGGCAGAA","E502","ATAGAGAG","Project","Project"
2,"SAMPLE-IN-POOL18-0208-R0001","140-18 ",,,"N704","TCCTGAGC","E502","ATAGAGAG","Project","Project"
2,"SAMPLE-IN-POOL18-0209-R0001","286-18 ",,,"N712","GTAGAGGA","E502","ATAGAGAG","Project","Project"
2,"SAMPLE-IN-POOL18-0210-R0001","288-18P",,,"N706","TAGGCATG","E502","ATAGAGAG","Project","Project"
2,"SAMPLE-IN-POOL18-0211-R0001","301-18 ",,,"N707","CTCTCTAC","E502","ATAGAGAG","Project","Project"
2,"DNA18-0079-R0001",60086,,,"H714","GCTCATGA","H505","CTCCTTAC","Project","Project"
3,"SAMPLE-IN-POOL18-0212-R0001","302-18 ",,,"N701","TAAGGCGA","E501","GCGATCTA","Project","Project"
3,"SAMPLE-IN-POOL18-0213-R0001","289-18",,,"N703","AGGCAGAA","E501","GCGATCTA","Project","Project"
3,"SAMPLE-IN-POOL18-0214-R0001","299-18",,,"N704","TCCTGAGC","E501","GCGATCTA","Project","Project"
3,"SAMPLE-IN-POOL18-0215-R0001","300-18",,,"N712","GTAGAGGA","E501","GCGATCTA","Project","Project"
3,"SAMPLE-IN-POOL18-0216-R0001","303-18",,,"N706","TAGGCATG","E501","GCGATCTA","Project","Project"
3,"SAMPLE-IN-POOL18-0217-R0001","303-18P ",,,"N707","CTCTCTAC","E501","GCGATCTA","Project","Project"
3,"SAMPLE-IN-POOL18-0218-R0001","303-18M ",,,"N708","CAGAGAGG","E501","GCGATCTA","Project","Project"
3,"SAMPLE-IN-POOL18-0219-R0001","304-18 ",,,"N709","GCTACGCT","E501","GCGATCTA","Project","Project"
3,"SAMPLE-IN-POOL18-0220-R0001","320-18 ",,,"N710","CGAGGCTG","E501","GCGATCTA","Project","Project"
3,"SAMPLE-IN-POOL18-0221-R0001","322-18",,,"N711","AAGAGGCA","E501","GCGATCTA","Project","Project"
3,"SAMPLE-IN-POOL18-0222-R0001","325-18",,,"N701","TAAGGCGA","E502","ATAGAGAG","Project","Project"
3,"SAMPLE-IN-POOL18-0223-R0001","352-16",,,"N702","CGTACTAG","E502","ATAGAGAG","Project","Project"
3,"SAMPLE-IN-POOL18-0224-R0001","342-18",,,"N703","AGGCAGAA","E502","ATAGAGAG","Project","Project"
3,"SAMPLE-IN-POOL18-0225-R0001","342-18S1",,,"N704","TCCTGAGC","E502","ATAGAGAG","Project","Project"
3,"SAMPLE-IN-POOL18-0226-R0001","343-18",,,"N712","GTAGAGGA","E502","ATAGAGAG","Project","Project"
3,"SAMPLE-IN-POOL18-0227-R0001","345-18",,,"N706","TAGGCATG","E502","ATAGAGAG","Project","Project"
3,"SAMPLE-IN-POOL18-0228-R0001","346-18",,,"N707","CTCTCTAC","E502","ATAGAGAG","Project","Project"
3,"SAMPLE-IN-POOL18-0229-R0001","171-18",,,"N708","CAGAGAGG","E502","ATAGAGAG","Project","Project"
3,"DNA18-0079-R0001",60086,,,"H714","GCTCATGA","H505","CTCCTTAC","Project","Project"
4,"SAMPLE-IN-POOL18-0212-R0001","302-18 ",,,"N701","TAAGGCGA","E501","GCGATCTA","Project","Project"
4,"SAMPLE-IN-POOL18-0213-R0001","289-18",,,"N703","AGGCAGAA","E501","GCGATCTA","Project","Project"
4,"SAMPLE-IN-POOL18-0214-R0001","299-18",,,"N704","TCCTGAGC","E501","GCGATCTA","Project","Project"
4,"SAMPLE-IN-POOL18-0215-R0001","300-18",,,"N712","GTAGAGGA","E501","GCGATCTA","Project","Project"
4,"SAMPLE-IN-POOL18-0216-R0001","303-18",,,"N706","TAGGCATG","E501","GCGATCTA","Project","Project"
4,"SAMPLE-IN-POOL18-0217-R0001","303-18P ",,,"N707","CTCTCTAC","E501","GCGATCTA","Project","Project"
4,"SAMPLE-IN-POOL18-0218-R0001","303-18M ",,,"N708","CAGAGAGG","E501","GCGATCTA","Project","Project"
4,"SAMPLE-IN-POOL18-0219-R0001","304-18 ",,,"N709","GCTACGCT","E501","GCGATCTA","Project","Project"
4,"SAMPLE-IN-POOL18-0220-R0001","320-18 ",,,"N710","CGAGGCTG","E501","GCGATCTA","Project","Project"
4,"SAMPLE-IN-POOL18-0221-R0001","322-18",,,"N711","AAGAGGCA","E501","GCGATCTA","Project","Project"
4,"SAMPLE-IN-POOL18-0222-R0001","325-18",,,"N701","TAAGGCGA","E502","ATAGAGAG","Project","Project"
4,"SAMPLE-IN-POOL18-0223-R0001","352-16",,,"N702","CGTACTAG","E502","ATAGAGAG","Project","Project"
4,"SAMPLE-IN-POOL18-0224-R0001","342-18",,,"N703","AGGCAGAA","E502","ATAGAGAG","Project","Project"
4,"SAMPLE-IN-POOL18-0225-R0001","342-18S1",,,"N704","TCCTGAGC","E502","ATAGAGAG","Project","Project"
4,"SAMPLE-IN-POOL18-0226-R0001","343-18",,,"N712","GTAGAGGA","E502","ATAGAGAG","Project","Project"
4,"SAMPLE-IN-POOL18-0227-R0001","345-18",,,"N706","TAGGCATG","E502","ATAGAGAG","Project","Project"
4,"SAMPLE-IN-POOL18-0228-R0001","346-18",,,"N707","CTCTCTAC","E502","ATAGAGAG","Project","Project"
4,"SAMPLE-IN-POOL18-0229-R0001","171-18",,,"N708","CAGAGAGG","E502","ATAGAGAG","Project","Project"
4,"DNA18-0079-R0001",60086,,,"H714","GCTCATGA","H505","CTCCTTAC","Project","Project"
5,"SAMPLE-IN-POOL18-0230-R0001","276-18M",,,"N701","TAAGGCGA","E501","GCGATCTA","Project","Project"
5,"SAMPLE-IN-POOL18-0231-R0001","240-18",,,"N702","CGTACTAG","E501","GCGATCTA","Project","Project"
5,"SAMPLE-IN-POOL18-0232-R0001","178-18",,,"N703","AGGCAGAA","E501","GCGATCTA","Project","Project"
5,"SAMPLE-IN-POOL18-0233-R0001","250-18",,,"N704","TCCTGAGC","E501","GCGATCTA","Project","Project"
5,"SAMPLE-IN-POOL18-0234-R0001","70-16",,,"N712","GTAGAGGA","E501","GCGATCTA","Project","Project"
5,"SAMPLE-IN-POOL18-0235-R0001","282-18",,,"N706","TAGGCATG","E501","GCGATCTA","Project","Project"
5,"SAMPLE-IN-POOL18-0236-R0001","288-18",,,"N707","CTCTCTAC","E501","GCGATCTA","Project","Project"
5,"SAMPLE-IN-POOL18-0237-R0001","302-18M",,,"N708","CAGAGAGG","E501","GCGATCTA","Project","Project"
5,"SAMPLE-IN-POOL18-0238-R0001","321-18",,,"N709","GCTACGCT","E501","GCGATCTA","Project","Project"
5,"SAMPLE-IN-POOL18-0239-R0001","91-15R1",,,"N710","CGAGGCTG","E501","GCGATCTA","Project","Project"
5,"SAMPLE-IN-POOL18-0240-R0001","348-18",,,"N711","AAGAGGCA","E501","GCGATCTA","Project","Project"
5,"SAMPLE-IN-POOL18-0241-R0001","349-18",,,"N701","TAAGGCGA","E502","ATAGAGAG","Project","Project"
5,"SAMPLE-IN-POOL18-0242-R0001","349-18P",,,"N702","CGTACTAG","E502","ATAGAGAG","Project","Project"
5,"SAMPLE-IN-POOL18-0243-R0001","349-18M",,,"N703","AGGCAGAA","E502","ATAGAGAG","Project","Project"
5,"SAMPLE-IN-POOL18-0244-R0001","350-18",,,"N704","TCCTGAGC","E502","ATAGAGAG","Project","Project"
5,"SAMPLE-IN-POOL18-0245-R0001","350-18M",,,"N712","GTAGAGGA","E502","ATAGAGAG","Project","Project"
5,"SAMPLE-IN-POOL18-0246-R0001","352-18",,,"N706","TAGGCATG","E502","ATAGAGAG","Project","Project"
5,"SAMPLE-IN-POOL18-0247-R0001","246-18",,,"N707","CTCTCTAC","E502","ATAGAGAG","Project","Project"
5,"DNA18-0080-R0001",60090,,,"H705","GGACTCCT","H506","TATGCAGT","Project","Project"
6,"SAMPLE-IN-POOL18-0230-R0001","276-18M",,,"N701","TAAGGCGA","E501","GCGATCTA","Project","Project"
6,"SAMPLE-IN-POOL18-0231-R0001","240-18",,,"N702","CGTACTAG","E501","GCGATCTA","Project","Project"
6,"SAMPLE-IN-POOL18-0232-R0001","178-18",,,"N703","AGGCAGAA","E501","GCGATCTA","Project","Project"
6,"SAMPLE-IN-POOL18-0233-R0001","250-18",,,"N704","TCCTGAGC","E501","GCGATCTA","Project","Project"
6,"SAMPLE-IN-POOL18-0234-R0001","70-16",,,"N712","GTAGAGGA","E501","GCGATCTA","Project","Project"
6,"SAMPLE-IN-POOL18-0235-R0001","282-18",,,"N706","TAGGCATG","E501","GCGATCTA","Project","Project"
6,"SAMPLE-IN-POOL18-0236-R0001","288-18",,,"N707","CTCTCTAC","E501","GCGATCTA","Project","Project"
6,"SAMPLE-IN-POOL18-0237-R0001","302-18M",,,"N708","CAGAGAGG","E501","GCGATCTA","Project","Project"
6,"SAMPLE-IN-POOL18-0238-R0001","321-18",,,"N709","GCTACGCT","E501","GCGATCTA","Project","Project"
6,"SAMPLE-IN-POOL18-0239-R0001","91-15R1",,,"N710","CGAGGCTG","E501","GCGATCTA","Project","Project"
6,"SAMPLE-IN-POOL18-0240-R0001","348-18",,,"N711","AAGAGGCA","E501","GCGATCTA","Project","Project"
6,"SAMPLE-IN-POOL18-0241-R0001","349-18",,,"N701","TAAGGCGA","E502","ATAGAGAG","Project","Project"
6,"SAMPLE-IN-POOL18-0242-R0001","349-18P",,,"N702","CGTACTAG","E502","ATAGAGAG","Project","Project"
6,"SAMPLE-IN-POOL18-0243-R0001","349-18M",,,"N703","AGGCAGAA","E502","ATAGAGAG","Project","Project"
6,"SAMPLE-IN-POOL18-0244-R0001","350-18",,,"N704","TCCTGAGC","E502","ATAGAGAG","Project","Project"
6,"SAMPLE-IN-POOL18-0245-R0001","350-18M",,,"N712","GTAGAGGA","E502","ATAGAGAG","Project","Project"
6,"SAMPLE-IN-POOL18-0246-R0001","352-18",,,"N706","TAGGCATG","E502","ATAGAGAG","Project","Project"
6,"SAMPLE-IN-POOL18-0247-R0001","246-18",,,"N707","CTCTCTAC","E502","ATAGAGAG","Project","Project"
6,"DNA18-0080-R0001",60090,,,"H705","GGACTCCT","H506","TATGCAGT","Project","Project"
7,"SAMPLE-IN-POOL18-0248-R0001","355-18",,,"N701","TAAGGCGA","E503","AGAGGATA","Project","Project"
7,"SAMPLE-IN-POOL18-0249-R0001","368-18",,,"N702","CGTACTAG","E503","AGAGGATA","Project","Project"
7,"SAMPLE-IN-POOL18-0250-R0001","138-18",,,"N703","AGGCAGAA","E503","AGAGGATA","Project","Project"
7,"SAMPLE-IN-POOL18-0251-R0001","279-17",,,"N704","TCCTGAGC","E503","AGAGGATA","Project","Project"
7,"SAMPLE-IN-POOL18-0252-R0001","419-18",,,"N712","GTAGAGGA","E503","AGAGGATA","Project","Project"
7,"SAMPLE-IN-POOL18-0253-R0001","368-18P",,,"N706","TAGGCATG","E503","AGAGGATA","Project","Project"
7,"SAMPLE-IN-POOL18-0254-R0001","368-18M",,,"N707","CTCTCTAC","E503","AGAGGATA","Project","Project"
7,"SAMPLE-IN-POOL18-0255-R0001","370-18",,,"N708","CAGAGAGG","E503","AGAGGATA","Project","Project"
7,"SAMPLE-IN-POOL18-0256-R0001","391-18",,,"N709","GCTACGCT","E503","AGAGGATA","Project","Project"
7,"SAMPLE-IN-POOL18-0257-R0001","393-18",,,"N710","CGAGGCTG","E503","AGAGGATA","Project","Project"
7,"SAMPLE-IN-POOL18-0258-R0001","398-18",,,"N711","AAGAGGCA","E503","AGAGGATA","Project","Project"
7,"SAMPLE-IN-POOL18-0259-R0001","400-18",,,"N701","TAAGGCGA","E504","TCTACTCT","Project","Project"
7,"SAMPLE-IN-POOL18-0260-R0001","302-18S1",,,"N702","CGTACTAG","E504","TCTACTCT","Project","Project"
7,"SAMPLE-IN-POOL18-0261-R0001","406-18",,,"N703","AGGCAGAA","E504","TCTACTCT","Project","Project"
7,"SAMPLE-IN-POOL18-0262-R0001","416-18",,,"N704","TCCTGAGC","E504","TCTACTCT","Project","Project"
7,"SAMPLE-IN-POOL18-0263-R0001","417-18",,,"N712","GTAGAGGA","E504","TCTACTCT","Project","Project"
7,"SAMPLE-IN-POOL18-0264-R0001","418-18",,,"N706","TAGGCATG","E504","TCTACTCT","Project","Project"
7,"SAMPLE-IN-POOL18-0265-R0001","332-18",,,"N702","CGTACTAG","E502","ATAGAGAG","Project","Project"
7,"DNA18-0080-R0001",60090,,,"H705","GGACTCCT","H506","TATGCAGT","Project","Project"
8,"SAMPLE-IN-POOL18-0248-R0001","355-18",,,"N701","TAAGGCGA","E503","AGAGGATA","Project","Project"
8,"SAMPLE-IN-POOL18-0249-R0001","368-18",,,"N702","CGTACTAG","E503","AGAGGATA","Project","Project"
8,"SAMPLE-IN-POOL18-0250-R0001","138-18",,,"N703","AGGCAGAA","E503","AGAGGATA","Project","Project"
8,"SAMPLE-IN-POOL18-0251-R0001","279-17",,,"N704","TCCTGAGC","E503","AGAGGATA","Project","Project"
8,"SAMPLE-IN-POOL18-0252-R0001","419-18",,,"N712","GTAGAGGA","E503","AGAGGATA","Project","Project"
8,"SAMPLE-IN-POOL18-0253-R0001","368-18P",,,"N706","TAGGCATG","E503","AGAGGATA","Project","Project"
8,"SAMPLE-IN-POOL18-0254-R0001","368-18M",,,"N707","CTCTCTAC","E503","AGAGGATA","Project","Project"
8,"SAMPLE-IN-POOL18-0255-R0001","370-18",,,"N708","CAGAGAGG","E503","AGAGGATA","Project","Project"
8,"SAMPLE-IN-POOL18-0256-R0001","391-18",,,"N709","GCTACGCT","E503","AGAGGATA","Project","Project"
8,"SAMPLE-IN-POOL18-0257-R0001","393-18",,,"N710","CGAGGCTG","E503","AGAGGATA","Project","Project"
8,"SAMPLE-IN-POOL18-0258-R0001","398-18",,,"N711","AAGAGGCA","E503","AGAGGATA","Project","Project"
8,"SAMPLE-IN-POOL18-0259-R0001","400-18",,,"N701","TAAGGCGA","E504","TCTACTCT","Project","Project"
8,"SAMPLE-IN-POOL18-0260-R0001","302-18S1",,,"N702","CGTACTAG","E504","TCTACTCT","Project","Project"
8,"SAMPLE-IN-POOL18-0261-R0001","406-18",,,"N703","AGGCAGAA","E504","TCTACTCT","Project","Project"
8,"SAMPLE-IN-POOL18-0262-R0001","416-18",,,"N704","TCCTGAGC","E504","TCTACTCT","Project","Project"
8,"SAMPLE-IN-POOL18-0263-R0001","417-18",,,"N712","GTAGAGGA","E504","TCTACTCT","Project","Project"
8,"SAMPLE-IN-POOL18-0264-R0001","418-18",,,"N706","TAGGCATG","E504","TCTACTCT","Project","Project"
8,"SAMPLE-IN-POOL18-0265-R0001","332-18",,,"N702","CGTACTAG","E502","ATAGAGAG","Project","Project"
8,"DNA18-0080-R0001",60090,,,"H705","GGACTCCT","H506","TATGCAGT","Project","Project"

```

--

![f6]({{site.url}}/img/ff6.png)

--

![f7]({{site.url}}/img/ff7.png)

--

![f8]({{site.url}}/img/ff8.png)

--

## YAML

```yaml
samples: /ELS/els9/users/biosciences/projects/agris/samples.tsv
units: /ELS/els9/users/biosciences/projects/agris/units.tsv

references:
    basepath: "/ELS/els9/users/biosciences/references"
    provider: "ncbi"
    genome_release: "Ovis_aries_4.0"

genome_fasta: "oar_ref_Oar_v4.0_fixChr.fa"

known_variants:
    dbsnp: "known_variants/dbSNP151_sorted_Ovis_aries.vcf"
    agris_snp: "known_variants/all.filt.SNP.vcf.gz"
    agris_indel: "known_variants/all.filt.INDEL.vcf.gz"

paths:
  to_tmp: "/scratch/users/biox"

rules:
    bwa-mem:
        arguments: "-M"
        platform: "illumina"
    multiqc:
        arguments: ""
    trim_galore_pe:
        arguments: "--paired -q 20"
    picard_MarkDuplicates:
        arguments: "REMOVE_DUPLICATES=false ASSUME_SORTED=true CREATE_INDEX=true"
    picard_WGSMetrics:
        arguments: "MINIMUM_MAPPING_QUALITY=-1 MINIMUM_BASE_QUALITY=-1 READ_LENGTH=150 COUNT_UNPAIRED=true"
    gatk_SplitIntervals:
        scatter-count: 100
        mode: BALANCING_WITHOUT_INTERVAL_SUBDIVISION
        intervals: "/ELS/els9/users/biosciences/references/ncbi/Ovis_aries_4.0/calling_regions/ovis_aries_4.0_calling_regions.intervals"
    gatk_BQSR:
        known_sites:
            - dbsnp
```

--

## JSON

```json
{
    "references": {
        "basepath": "/ELS/els9/users/biosciences/references",
        "provider": "ucsc",
        "genome_release": "hg19"
    },
    "genome_fasta": "ucsc.hg19.fasta",
    "known_variants": {
        "dbsnp": "known_variants/dbSNP146_chr.vcf",
        "hapmap": "known_variants/hapmap_3.3.hg19.sites.vcf",
        "g1k": "known_variants/1000G_phase1.snps.high_confidence.hg19.sites.vcf",
        "omni": "known_variants/1000G_omni2.5.hg19.sites.vcf",
        "mills": "known_variants/Mills_and_1000G_gold_standard.indels.hg19.sites.vcf",
        "ph1_indels": "known_variants/1000G_phase1.indels.hg19.sites.vcf"
    },
    "intervals": {
        "NexteraRapidCaptureExpandedExome": {
            "bedTarget": "intervals/NexteraRapidCaptureExpandedExome_Target.bed",
            "probes": "intervals/NexteraRapidCaptureExpandedExome_Probes.HybridSelection",
            "hsTarget": "intervals/NexteraRapidCaptureExpandedExome_Target.HybridSelection"
        },
        "NimblegenSeqCapExomeUTR": {
            "bedTarget": "intervals/NimblegenSeqCapExomeUTR_Targets.bed",
            "probes": "intervals/NimblegenSeqCapExomeUTR_Probes.HybridSelection",
            "hsTarget": "intervals/NimblegenSeqCapExomeUTR_Targets.HybridSelection"
        },
        "NexteraRapidCaptureExomev1.2": {
            "bedTarget": "intervals/NexteraRapidCaptureExomev1.2_Target.bed",
            "probes": "intervals/NexteraRapidCaptureExomev1.2_Probes.HybridSelection",
            "hsTarget": "intervals/NexteraRapidCaptureExomev1.2_Target.HybridSelection"
        },
        "AgilentSureSelectHumanAllExonV6UTR": {
            "bedTarget": "intervals/AgilentSureSelectHumanAllExonV6UTR_Target.bed",
            "probes": "intervals/AgilentSureSelectHumanAllExonV6UTR_Probes.HybridSelection",
            "hsTarget": "intervals/AgilentSureSelectHumanAllExonV6UTR_Target.HybridSelection"
        },
        "AgilentSureSelectHumanAllExonV5UTR": {
            "bedTarget": "intervals/AgilentSureSelectHumanAllExonV5UTR_Target.bed",
            "probes": "intervals/AgilentSureSelectHumanAllExonV5UTR_Probes.HybridSelection",
            "hsTarget": "intervals/AgilentSureSelectHumanAllExonV5UTR_Target.HybridSelection"
        }
    },
    "intervals_default": "NexteraRapidCaptureExomev1.2",
    "platform": "ILLUMINA",
    "params_bwa_mem": "-M",
    "odpd": {
        "DNA16-0389-R0001": 100
    },
    "tmp_dir": "/scratch/users/biox",
    "samples_intervals": {
        "DNA16-0389-R0001": "NexteraRapidCaptureExomev1.2"
    },
    "samples": {
        "VASCPR002": [
            "VASCPR002_S10_L001",
            "VASCPR002_S10_L004",
            "VASCPR002_S10_L002",
            "VASCPR002_S10_L003"
        ],
        "RTXPR071": [
            "RTXPR071_S2_L002",
            "RTXPR071_S2_L001",
            "RTXPR071_S2_L004",
            "RTXPR071_S2_L003"
        ],
    }
}
```

--

# ...