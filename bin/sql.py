import pandas as pd
import sqlite3

connection = sqlite3.connect('NFixDB.db')
cursor = connection.cursor()

#------------------------------------------------------EVALUE TAXONOMY------------------------------------------------------
#i1
cursor.execute('CREATE TABLE IF NOT EXISTS evalue_taxonomy_i1 (GenomeID varchar, GeneName varchar, SeqID varchar, EValue float, BitScore float, Location varchar, AlnLength number, SeqLength number, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
connection.commit()
evalue_df = pd.DataFrame(pd.read_table('TSVs/evalue_taxonomy_i1.tsv'))
evalue_df.to_sql('evalue_taxonomy', connection, if_exists = 'replace')
#i2
cursor.execute('CREATE TABLE IF NOT EXISTS evalue_taxonomy_i2 (GenomeID varchar, GeneName varchar, SeqID varchar, EValue float, BitScore float, Location varchar, AlnLength number, SeqLength number, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
connection.commit()
evalue2_df = pd.DataFrame(pd.read_table('TSVs/evalue_taxonomy_i2.tsv')).drop(columns='Unnamed: 0')
evalue2_df.to_sql('evalue_taxonomy_i2', connection, if_exists = 'replace')
#i3 
cursor.execute('CREATE TABLE IF NOT EXISTS evalue_taxonomy_i3 (GenomeID varchar, GeneName varchar, SeqID varchar, EValue float, BitScore float, Location varchar, AlnLength number, SeqLength number, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
connection.commit()
evalue3_df = pd.DataFrame(pd.read_table('TSVs/evalue_taxonomy_i3.tsv')).drop(columns='Unnamed: 0')
evalue3_df.to_sql('evalue_taxonomy_i3', connection, if_exists = 'replace')

#------------------------------------------------------TOP HITS TAXONOMY------------------------------------------------------ 
#i1
cursor.execute('CREATE TABLE IF NOT EXISTS tophits_i1 (GenomeID varchar, nifH varchar, EV_nifH float, bitscore_nifH float, location_nifH varchar, alnLen_nifH number, seqLen_nifH number, nifD varchar, EV_nifD float, bitscore_nifD float, location_nifD varchar, alnLen_nifD number, seqLen_nifD number, nifK varchar, EV_nifK float, bitscore_nifK float, location_nifK varchar, alnLen_nifK number, seqLen_nifK number, anfH varchar, EV_anfH float, bitscore_anfH float, location_anfH varchar, alnLen_anfH number, seqLen_anfH number, anfD varchar, EV_anfD float, bitscore_anfD float, location_anfD varchar, alnLen_anfD number, seqLen_anfD number, anfK varchar, EV_anfK float, bitscore_anfK float, location_anfK varchar, alnLen_anfK number, seqLen_anfK number, vnfH varchar, EV_vnfH float, bitscore_vnfH float, location_vnfH varchar, alnLen_vnfH number, seqLen_vnfH number, vnfD varchar, EV_vnfD float, bitscore_vnfD float, location_vnfD varchar, alnLen_vnfD number, seqLen_vnfD number, vnfK varchar, EV_vnfK float, bitscore_vnfK float, location_vnfK varchar, alnLen_vnfK number, seqLen_vnfK number, nflD varchar, EV_nflD float, bitscore_nflD float, location_nflH varchar, alnLen_nflH number, seqLen_nflH number, nflH varchar, EV_nflH float, bitscore_nflH float, location_nflD varchar, alnLen_nflD number, seqLen_nflD number, ChlB varchar, EV_ChlB float, bitscore_ChlB float, location_ChlB varchar, alnLen_ChlB number, seqLen_ChlB number, ChIl varchar, EV_ChIl float, bitscore_ChIl float, location_ChIl varchar, alnLen_ChIl number, seqLen_ChIl number, ChlN varchar, EV_ChlN float, bitscore_ChlN float, location_ChlN varchar, alnLen_ChlN number, seqLen_ChlN number, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
connection.commit()
tophits_df = pd.DataFrame(pd.read_table('TSVs/tophits_i1.tsv'))
tophits_df.to_sql('tophits', connection, if_exists = 'replace')
#i2
cursor.execute('CREATE TABLE IF NOT EXISTS tophits_i2 (GenomeID varchar, nifH varchar, EV_nifH float, bitscore_nifH float, location_nifH varchar, alnLen_nifH number, seqLen_nifH number, nifD varchar, EV_nifD float, bitscore_nifD float, location_nifD varchar, alnLen_nifD number, seqLen_nifD number, nifK varchar, EV_nifK float, bitscore_nifK float, location_nifK varchar, alnLen_nifK number, seqLen_nifK number, anfH varchar, EV_anfH float, bitscore_anfH float, location_anfH varchar, alnLen_anfH number, seqLen_anfH number, anfD varchar, EV_anfD float, bitscore_anfD float, location_anfD varchar, alnLen_anfD number, seqLen_anfD number, anfK varchar, EV_anfK float, bitscore_anfK float, location_anfK varchar, alnLen_anfK number, seqLen_anfK number, vnfH varchar, EV_vnfH float, bitscore_vnfH float, location_vnfH varchar, alnLen_vnfH number, seqLen_vnfH number, vnfD varchar, EV_vnfD float, bitscore_vnfD float, location_vnfD varchar, alnLen_vnfD number, seqLen_vnfD number, vnfK varchar, EV_vnfK float, bitscore_vnfK float, location_vnfK varchar, alnLen_vnfK number, seqLen_vnfK number, nflD varchar, EV_nflD float, bitscore_nflD float, location_nflH varchar, alnLen_nflH number, seqLen_nflH number, nflH varchar, EV_nflH float, bitscore_nflH float, location_nflD varchar, alnLen_nflD number, seqLen_nflD number, ChlB varchar, EV_ChlB float, bitscore_ChlB float, location_ChlB varchar, alnLen_ChlB number, seqLen_ChlB number, ChIl varchar, EV_ChIl float, bitscore_ChIl float, location_ChIl varchar, alnLen_ChIl number, seqLen_ChIl number, ChlN varchar, EV_ChlN float, bitscore_ChlN float, location_ChlN varchar, alnLen_ChlN number, seqLen_ChlN number, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
connection.commit()
tophits2_df = pd.DataFrame(pd.read_table('TSVs/tophits_i2.tsv'))
tophits2_df.to_sql('tophits_i2', connection, if_exists = 'replace')
#i3
cursor.execute('CREATE TABLE IF NOT EXISTS tophits_i3 (GenomeID varchar, nifH varchar, EV_nifH float, bitscore_nifH float, location_nifH varchar, alnLen_nifH number, seqLen_nifH number, nifD varchar, EV_nifD float, bitscore_nifD float, location_nifD varchar, alnLen_nifD number, seqLen_nifD number, nifK varchar, EV_nifK float, bitscore_nifK float, location_nifK varchar, alnLen_nifK number, seqLen_nifK number, anfH varchar, EV_anfH float, bitscore_anfH float, location_anfH varchar, alnLen_anfH number, seqLen_anfH number, anfD varchar, EV_anfD float, bitscore_anfD float, location_anfD varchar, alnLen_anfD number, seqLen_anfD number, anfK varchar, EV_anfK float, bitscore_anfK float, location_anfK varchar, alnLen_anfK number, seqLen_anfK number, vnfH varchar, EV_vnfH float, bitscore_vnfH float, location_vnfH varchar, alnLen_vnfH number, seqLen_vnfH number, vnfD varchar, EV_vnfD float, bitscore_vnfD float, location_vnfD varchar, alnLen_vnfD number, seqLen_vnfD number, vnfK varchar, EV_vnfK float, bitscore_vnfK float, location_vnfK varchar, alnLen_vnfK number, seqLen_vnfK number, nflD varchar, EV_nflD float, bitscore_nflD float, location_nflH varchar, alnLen_nflH number, seqLen_nflH number, nflH varchar, EV_nflH float, bitscore_nflH float, location_nflD varchar, alnLen_nflD number, seqLen_nflD number, ChlB varchar, EV_ChlB float, bitscore_ChlB float, location_ChlB varchar, alnLen_ChlB number, seqLen_ChlB number, ChIl varchar, EV_ChIl float, bitscore_ChIl float, location_ChIl varchar, alnLen_ChIl number, seqLen_ChIl number, ChlN varchar, EV_ChlN float, bitscore_ChlN float, location_ChlN varchar, alnLen_ChlN number, seqLen_ChlN number, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar)')
connection.commit()
tophits3_df = pd.DataFrame(pd.read_table('TSVs/tophits_i3.tsv'))
tophits3_df.to_sql('tophits_i3', connection, if_exists = 'replace')

#----------------------------------------------------FILTERED HITS TAXONOMY----------------------------------------------------
#i1
cursor.execute('CREATE TABLE IF NOT EXISTS filteredhits_i1 (GenomeID varchar, GTDB_Tax varchar, NCBI_Tax varchar, nifH varchar, EV_nifH float, bitscore_nifH float, location_nifH varchar, alnLen_nifH number, seqLen_nifH number, nifD varchar, EV_nifD float, bitscore_nifD float, location_nifD varchar, alnLen_nifD number, seqLen_nifD number, nifK varchar, EV_nifK float, bitscore_nifK float, location_nifK varchar, alnLen_nifK number, seqLen_nifK number, vnfH varchar, EV_vnfH float, bitscore_vnfH float, location_vnfH varchar, alnLen_vnfH number, seqLen_vnfH number, vnfD varchar, EV_vnfD float, bitscore_vnfD float, location_vnfD varchar, alnLen_vnfD number, seqLen_vnfD number, vnfK varchar, EV_vnfK float, bitscore_vnfK float, location_vnfK varchar, alnLen_vnfK number, seqLen_vnfK number, anfH varchar, EV_anfH float, bitscore_anfH float, location_anfH varchar, alnLen_anfH number, seqLen_anfH number, anfD varchar, EV_anfD float, bitscore_anfD float, location_anfD varchar, alnLen_anfD number, seqLen_anfD number, anfK varchar, EV_anfK float, bitscore_anfK float, location_anfK varchar, alnLen_anfK number, seqLen_anfK number, nflD varchar, EV_nflD float, bitscore_nflD float, nflH varchar, EV_nflH float, bitscore_nflH float, ChlN varchar, EV_ChlN float, bitscore_ChlN float, ChIl varchar, EV_ChIl float, bitscore_ChIl float, ChlB varchar, EV_ChlB float, bitscore_ChlB float)')
connection.commit()
filteredhits_df = pd.DataFrame(pd.read_table('TSVs/filteredhits_i1.tsv'))
filteredhits_df.to_sql('filteredhits', connection, if_exists = 'replace')
#i2
cursor.execute('CREATE TABLE IF NOT EXISTS filteredhits_i2 (GenomeID varchar, GTDB_Tax varchar, NCBI_Tax varchar, nifH varchar, EV_nifH float, bitscore_nifH float, location_nifH varchar, alnLen_nifH number, seqLen_nifH number, nifD varchar, EV_nifD float, bitscore_nifD float, location_nifD varchar, alnLen_nifD number, seqLen_nifD number, nifK varchar, EV_nifK float, bitscore_nifK float, location_nifK varchar, alnLen_nifK number, seqLen_nifK number, vnfH varchar, EV_vnfH float, bitscore_vnfH float, location_vnfH varchar, alnLen_vnfH number, seqLen_vnfH number, vnfD varchar, EV_vnfD float, bitscore_vnfD float, location_vnfD varchar, alnLen_vnfD number, seqLen_vnfD number, vnfK varchar, EV_vnfK float, bitscore_vnfK float, location_vnfK varchar, alnLen_vnfK number, seqLen_vnfK number, anfH varchar, EV_anfH float, bitscore_anfH float, location_anfH varchar, alnLen_anfH number, seqLen_anfH number, anfD varchar, EV_anfD float, bitscore_anfD float, location_anfD varchar, alnLen_anfD number, seqLen_anfD number, anfK varchar, EV_anfK float, bitscore_anfK float, location_anfK varchar, alnLen_anfK number, seqLen_anfK number, nflD varchar, EV_nflD float, bitscore_nflD float, nflH varchar, EV_nflH float, bitscore_nflH float, ChlN varchar, EV_ChlN float, bitscore_ChlN float, ChIl varchar, EV_ChIl float, bitscore_ChIl float, ChlB varchar, EV_ChlB float, bitscore_ChlB float)')
connection.commit()
filteredhits2_df = pd.DataFrame(pd.read_table('TSVs/filteredhits_i2.tsv'))
filteredhits2_df.to_sql('filteredhits_i2', connection, if_exists = 'replace')
#i3
cursor.execute('CREATE TABLE IF NOT EXISTS filteredhits_i3 (GenomeID varchar, GTDB_Tax varchar, NCBI_Tax varchar, nifH varchar, EV_nifH float, bitscore_nifH float, location_nifH varchar, alnLen_nifH number, seqLen_nifH number, nifD varchar, EV_nifD float, bitscore_nifD float, location_nifD varchar, alnLen_nifD number, seqLen_nifD number, nifK varchar, EV_nifK float, bitscore_nifK float, location_nifK varchar, alnLen_nifK number, seqLen_nifK number, vnfH varchar, EV_vnfH float, bitscore_vnfH float, location_vnfH varchar, alnLen_vnfH number, seqLen_vnfH number, vnfD varchar, EV_vnfD float, bitscore_vnfD float, location_vnfD varchar, alnLen_vnfD number, seqLen_vnfD number, vnfK varchar, EV_vnfK float, bitscore_vnfK float, location_vnfK varchar, alnLen_vnfK number, seqLen_vnfK number, anfH varchar, EV_anfH float, bitscore_anfH float, location_anfH varchar, alnLen_anfH number, seqLen_anfH number, anfD varchar, EV_anfD float, bitscore_anfD float, location_anfD varchar, alnLen_anfD number, seqLen_anfD number, anfK varchar, EV_anfK float, bitscore_anfK float, location_anfK varchar, alnLen_anfK number, seqLen_anfK number, nflD varchar, EV_nflD float, bitscore_nflD float, nflH varchar, EV_nflH float, bitscore_nflH float, ChlN varchar, EV_ChlN float, bitscore_ChlN float, ChIl varchar, EV_ChIl float, bitscore_ChIl float, ChlB varchar, EV_ChlB float, bitscore_ChlB float)')
connection.commit()
filteredhits3_df = pd.DataFrame(pd.read_table('TSVs/filteredhits_i3.tsv'))
filteredhits3_df.to_sql('filteredhits_i3', connection, if_exists = 'replace')

#------------------------------------------------------TOP FASTA TAXONOMY------------------------------------------------------ 
#i1
cursor.execute('CREATE TABLE IF NOT EXISTS topfasta_i1 (GenomeID varchar, nifH varchar, EV_nifH float, bitscore_nifH float, location_nifH varchar, alnLen_nifH number, seqLen_nifH number, nifD varchar, EV_nifD float, bitscore_nifD float, location_nifD varchar, alnLen_nifD number, seqLen_nifD number, nifK varchar, EV_nifK float, bitscore_nifK float, location_nifK varchar, alnLen_nifK number, seqLen_nifK number, anfH varchar, EV_anfH float, bitscore_anfH float, location_anfH varchar, alnLen_anfH number, seqLen_anfH number, anfD varchar, EV_anfD float, bitscore_anfD float, location_anfD varchar, alnLen_anfD number, seqLen_anfD number, anfK varchar, EV_anfK float, bitscore_anfK float, location_anfK varchar, alnLen_anfK number, seqLen_anfK number, vnfH varchar, EV_vnfH float, bitscore_vnfH float, location_vnfH varchar, alnLen_vnfH number, seqLen_vnfH number, vnfD varchar, EV_vnfD float, bitscore_vnfD float, location_vnfD varchar, alnLen_vnfD number, seqLen_vnfD number, vnfK varchar, EV_vnfK float, bitscore_vnfK float, location_vnfK varchar, alnLen_vnfK number, seqLen_vnfK number, nflD varchar, EV_nflD float, bitscore_nflD float, location_nflH varchar, alnLen_nflH number, seqLen_nflH number, nflH varchar, EV_nflH float, bitscore_nflH float, location_nflD varchar, alnLen_nflD number, seqLen_nflD number, ChlB varchar, EV_ChlB float, bitscore_ChlB float, location_ChlB varchar, alnLen_ChlB number, seqLen_ChlB number, ChIl varchar, EV_ChIl float, bitscore_ChIl float, location_ChIl varchar, alnLen_ChIl number, seqLen_ChIl number, ChlN varchar, EV_ChlN float, bitscore_ChlN float, location_ChlN varchar, alnLen_ChlN number, seqLen_ChlN number)')
connection.commit()
topfasta_df = pd.DataFrame(pd.read_table('TSVs/topfasta_i1.tsv'))
topfasta_df.to_sql('topfasta', connection, if_exists = 'replace')
#i2
cursor.execute('CREATE TABLE IF NOT EXISTS topfasta_i2 (GenomeID varchar, nifH varchar, EV_nifH float, bitscore_nifH float, location_nifH varchar, alnLen_nifH number, seqLen_nifH number, nifD varchar, EV_nifD float, bitscore_nifD float, location_nifD varchar, alnLen_nifD number, seqLen_nifD number, nifK varchar, EV_nifK float, bitscore_nifK float, location_nifK varchar, alnLen_nifK number, seqLen_nifK number, anfH varchar, EV_anfH float, bitscore_anfH float, location_anfH varchar, alnLen_anfH number, seqLen_anfH number, anfD varchar, EV_anfD float, bitscore_anfD float, location_anfD varchar, alnLen_anfD number, seqLen_anfD number, anfK varchar, EV_anfK float, bitscore_anfK float, location_anfK varchar, alnLen_anfK number, seqLen_anfK number, vnfH varchar, EV_vnfH float, bitscore_vnfH float, location_vnfH varchar, alnLen_vnfH number, seqLen_vnfH number, vnfD varchar, EV_vnfD float, bitscore_vnfD float, location_vnfD varchar, alnLen_vnfD number, seqLen_vnfD number, vnfK varchar, EV_vnfK float, bitscore_vnfK float, location_vnfK varchar, alnLen_vnfK number, seqLen_vnfK number, nflD varchar, EV_nflD float, bitscore_nflD float, location_nflH varchar, alnLen_nflH number, seqLen_nflH number, nflH varchar, EV_nflH float, bitscore_nflH float, location_nflD varchar, alnLen_nflD number, seqLen_nflD number, ChlB varchar, EV_ChlB float, bitscore_ChlB float, location_ChlB varchar, alnLen_ChlB number, seqLen_ChlB number, ChIl varchar, EV_ChIl float, bitscore_ChIl float, location_ChIl varchar, alnLen_ChIl number, seqLen_ChIl number, ChlN varchar, EV_ChlN float, bitscore_ChlN float, location_ChlN varchar, alnLen_ChlN number, seqLen_ChlN number)')
connection.commit()
topfasta2_df = pd.DataFrame(pd.read_table('TSVs/topfasta_i2.tsv'))
topfasta2_df.to_sql('topfasta_i2', connection, if_exists = 'replace')
#i3
cursor.execute('CREATE TABLE IF NOT EXISTS topfasta_i3 (GenomeID varchar, nifH varchar, EV_nifH float, bitscore_nifH float, location_nifH varchar, alnLen_nifH number, seqLen_nifH number, nifD varchar, EV_nifD float, bitscore_nifD float, location_nifD varchar, alnLen_nifD number, seqLen_nifD number, nifK varchar, EV_nifK float, bitscore_nifK float, location_nifK varchar, alnLen_nifK number, seqLen_nifK number, anfH varchar, EV_anfH float, bitscore_anfH float, location_anfH varchar, alnLen_anfH number, seqLen_anfH number, anfD varchar, EV_anfD float, bitscore_anfD float, location_anfD varchar, alnLen_anfD number, seqLen_anfD number, anfK varchar, EV_anfK float, bitscore_anfK float, location_anfK varchar, alnLen_anfK number, seqLen_anfK number, vnfH varchar, EV_vnfH float, bitscore_vnfH float, location_vnfH varchar, alnLen_vnfH number, seqLen_vnfH number, vnfD varchar, EV_vnfD float, bitscore_vnfD float, location_vnfD varchar, alnLen_vnfD number, seqLen_vnfD number, vnfK varchar, EV_vnfK float, bitscore_vnfK float, location_vnfK varchar, alnLen_vnfK number, seqLen_vnfK number, nflD varchar, EV_nflD float, bitscore_nflD float, location_nflH varchar, alnLen_nflH number, seqLen_nflH number, nflH varchar, EV_nflH float, bitscore_nflH float, location_nflD varchar, alnLen_nflD number, seqLen_nflD number, ChlB varchar, EV_ChlB float, bitscore_ChlB float, location_ChlB varchar, alnLen_ChlB number, seqLen_ChlB number, ChIl varchar, EV_ChIl float, bitscore_ChIl float, location_ChIl varchar, alnLen_ChIl number, seqLen_ChIl number, ChlN varchar, EV_ChlN float, bitscore_ChlN float, location_ChlN varchar, alnLen_ChlN number, seqLen_ChlN number)')
connection.commit()
topfasta3_df = pd.DataFrame(pd.read_table('TSVs/topfasta_i3.tsv'))
topfasta3_df.to_sql('topfasta_i3', connection, if_exists = 'replace')

#------------------------------------------------------FILTERED FASTA TAXONOMY------------------------------------------------------
#i1
cursor.execute('CREATE TABLE IF NOT EXISTS filteredfasta_i1 (GenomeID varchar, nifH varchar, nifD varchar, nifK varchar, vnfH varchar, vnfD varchar, vnfK varchar, anfH varchar, anfD varchar, anfK varchar, nflD varchar, nflH varchar, ChlN varchar, ChIl varchar, ChlB varchar)')
connection.commit()
mergefasta_df = pd.DataFrame(pd.read_table('TSVs/filteredfasta_i1.tsv'))
mergefasta_df.to_sql('mergefasta', connection, if_exists = 'replace')
#i2
cursor.execute('CREATE TABLE IF NOT EXISTS filteredfasta_i2 (GenomeID varchar, nifH varchar, nifD varchar, nifK varchar, vnfH varchar, vnfD varchar, vnfK varchar, anfH varchar, anfD varchar, anfK varchar, nflD varchar, nflH varchar, ChlN varchar, ChIl varchar, ChlB varchar)')
connection.commit()
mergefasta2_df = pd.DataFrame(pd.read_table('TSVs/filteredfasta_i2.tsv'))
mergefasta2_df.to_sql('mergefasta_i2', connection, if_exists = 'replace')
#i3
cursor.execute('CREATE TABLE IF NOT EXISTS filteredfasta_i3 (GenomeID varchar, nifH varchar, nifD varchar, nifK varchar, vnfH varchar, vnfD varchar, vnfK varchar, anfH varchar, anfD varchar, anfK varchar, nflD varchar, nflH varchar, ChlN varchar, ChIl varchar, ChlB varchar)')
connection.commit()
mergefasta3_df = pd.DataFrame(pd.read_table('TSVs/filteredfasta_i3.tsv'))
mergefasta3_df.to_sql('mergefasta_i3', connection, if_exists = 'replace')

#------------------------------------------------------NFIXDB------------------------------------------------------
cursor.execute('CREATE TABLE IF NOT EXISTS NFixDB (GenomeID varchar, nifH varchar, EV_nifH float, bitscore_nifH float, location_nifH varchar, alnLen_nifH number, seqLen_nifH number, nifD varchar, EV_nifD float, bitscore_nifD float, location_nifD varchar, alnLen_nifD number, seqLen_nifD number, nifK varchar, EV_nifK float, bitscore_nifK float, location_nifK varchar, alnLen_nifK number, seqLen_nifK number, anfH varchar, EV_anfH float, bitscore_anfH float, location_anfH varchar, alnLen_anfH number, seqLen_anfH number, anfD varchar, EV_anfD float, bitscore_anfD float, location_anfD varchar, alnLen_anfD number, seqLen_anfD number, anfK varchar, EV_anfK float, bitscore_anfK float, location_anfK varchar, alnLen_anfK number, seqLen_anfK number, vnfH varchar, EV_vnfH float, bitscore_vnfH float, location_vnfH varchar, alnLen_vnfH number, seqLen_vnfH number, vnfD varchar, EV_vnfD float, bitscore_vnfD float, location_vnfD varchar, alnLen_vnfD number, seqLen_vnfD number, vnfK varchar, EV_vnfK float, bitscore_vnfK float, location_vnfK varchar, alnLen_vnfK number, seqLen_vnfK number, nflD varchar, EV_nflD float, bitscore_nflD float, location_nflH varchar, alnLen_nflH number, seqLen_nflH number, nflH varchar, EV_nflH float, bitscore_nflH float, location_nflD varchar, alnLen_nflD number, seqLen_nflD number, ChlB varchar, EV_ChlB float, bitscore_ChlB float, location_ChlB varchar, alnLen_ChlB number, seqLen_ChlB number, ChIl varchar, EV_ChIl float, bitscore_ChIl float, location_ChIl varchar, alnLen_ChIl number, seqLen_ChIl number, ChlN varchar, EV_ChlN float, bitscore_ChlN float, location_ChlN varchar, alnLen_ChlN number, seqLen_ChlN number, GTDB_Tax varchar, NCBI_TaxID number, NCBI_Tax varchar, [5S] varchar, [5.8S] varchar, [16S] varchar, [23S] varchar)')
connection.commit()
evalue_df = pd.DataFrame(pd.read_table('TSVs/NFixDB.tsv'))
evalue_df.to_sql('NFixDB', connection, if_exists = 'replace')
