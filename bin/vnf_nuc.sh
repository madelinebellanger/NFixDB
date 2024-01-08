#!/bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name=vnf-nuc
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --mem=128GB
#SBATCH --time=1-0
#SBATCH -o slurm-%x-%j.out
#SBATCH --mail-type=END,FAIL,REQUEUE

echo "====================================================="
echo "Start Time  : $(date)"
echo "Submit Dir  : $SLURM_SUBMIT_DIR"
echo "Job ID/Name : $SLURM_JOBID / $SLURM_JOB_NAME"
echo "Node List   : $SLURM_JOB_NODELIST"
echo "Num Tasks   : $SLURM_NTASKS total [$SLURM_NNODES nodes @ $SLURM_CPUS_ON_NODE CPUs/node]"
echo "======================================================"
echo ""

mafft --localpair --maxiterate 100 ../fastas/R2/final_nuc/vnfD_01032024.fna > ../alignments/R2/final_nuc/vnfD-local_aln_final_01032024.fna
mafft --localpair --maxiterate 100 ../fastas/R2/final_nuc/vnfH_01032024.fna > ../alignments/R2/final_nuc/vnfH-local_aln_final_01032024.fna
mafft --localpair --maxiterate 100 ../fastas/R2/final_nuc/vnfK_01032024.fna > ../alignments/R2/final_nuc/vnfK-local_aln_final_01032024.fna

echo ""
echo "======================================================"
echo "End Time   : $(date)"
echo "======================================================"
echo ""
