# Assessing Gene Dependency of Apoptotic Genes in KRAS Mutant Cancers
By: Owen, Izzy, Izadjoo, Salman, Hussain, Imran, Gierlack, Steven, Bauman, Bradly

In the pursuit of personalized medicine, large-scale studies are being performed that generate a plethora of data. In the study of cancer, this is particularly true. These studies generate large, publicly-accessible databases in which they store all of the data their study generates. This is an incredibly useful tool to allow reproducibility, as well as to move the science forward. One downside, however, is that these large deposits of data can be cumbersome and impossible to navigate.

One such project is called Project Achilles, a project of The Broad Institute of MIT and Harvard (https://portals.broadinstitute.org/achilles). From their website:
> Project Achilles is a systematic effort aimed at identifying and cataloging gene essentiality across hundreds of genomically characterized cancer cell lines. The project uses genome-scale RNAi and CRISPR-Cas9 genetic perturbation reagents to silence or knockout individual genes and identify those genes that affect cell survival. By linking these genetic dependencies to the genetic or molecular features of the tumors, this project is providing the foundation for a "Cancer Dependency Map" (https://depmap.org).

As such, we sought to generate a code that would allow one to sort through cancer lines by mutation type, and then examine the dependency of these lines for the expression of specific genes. As a demonstration, we examined KRAS mutant cancer lines for their dependency on apoptotic genes.

**File List:**
Files 1 and 2 were obtained from the Project Achilles data portal. 
File 3 was obtained from the ApoCanD database (ApoCanD: Database of Human Apoptotic Proteins in the context of cancer). Link: (crdd.osdd.net/raghava/apocand/index.php)

1. Achilles_v2.4_SampleInfo_small.csv
   
   This file lists cancer cell lines, their type and subtype, and the mutation status of a few common oncogenes (KRAS, PIK3CA, BRAF, NRAS, PTEN, APC, CTNNB1, and EGFR).  It also includes data on the cell culture conditions and how mutation statuses were confirmed.
   
2. gene_dependency.csv

   This file lists the cancer cell lines examined utilizing CRISPR-Cas9 to knockout >16,000 genes. The data output is the 
   probability that knocking out a given gene has a real depletion effect. 
   The file is a Numerical Matrix.
   Columns: genes in the format "HUGO (Entrez)"
   Rows: cell lines in the format "ID_PRIMARYSITE"
   
3. mutation_ccle_cosmic.csv

   This file is a space-separated file that lists apoptosis genes mutated in certain cancers.
   

   
   
