#! /usr/bin/python
# Python 2.7.5, requires Biopython.

# Version 1. Adam Taranto, March 2014.

import argparse; #for command line flags and input.
import sys; #for stdin, stdout input-output handling.
from Bio import SeqIO; #For .fasta output !
from Bio import Entrez; #For .fasta output !
import re; #used for extracting gi numbers from complex strings
from Bio.Blast import NCBIXML; #for generic xml handling

def main(file_dir, file_dir_output, database="protein", email=None):
	
	if email != None:
		Entrez.email=email

	gi_list = set(open(file_dir, 'rU'));
	gi_list = list(gi_list);

	#gi_str = ",".join(gi_list);
	
	print(gi_list);
	print(Entrez.email);

	output_file = open(file_dir_output, 'w')
	output_file.write("GI, Accession, Species, Strain, Host, Seq_Name, Description \n")
	
	for gi_record in gi_list:
		
		Entrez_handle = Entrez.efetch(db=database, id=gi_record.rstrip('\n'), rettype="gb", retmode="xml"); 
		record = Entrez.read(Entrez_handle);
		
		try:
			isStrain = record[0]['GBSeq_feature-table'][0]['GBFeature_quals'][1]['GBQualifier_name']
		except IndexError:
			isStrain = 'NA'

		if isStrain == "strain":
			strain = record[0]['GBSeq_feature-table'][0]['GBFeature_quals'][1]['GBQualifier_value']
		else:
			strain = "NA"
		
		try:
			isHost = record[0]['GBSeq_feature-table'][0]['GBFeature_quals'][2]['GBQualifier_name']
		except IndexError:
			isHost = 'NA'
		
		if isHost == "host":
			host = record[0]['GBSeq_feature-table'][0]['GBFeature_quals'][2]['GBQualifier_value']
		else:
			host = 'NA'

		try:
			isName = record[0]['GBSeq_feature-table'][1]['GBFeature_quals'][1]['GBQualifier_name']
		except IndexError:
			isName = 'NA'
		
		if isName == "name":
			name = record[0]['GBSeq_feature-table'][1]['GBFeature_quals'][1]['GBQualifier_value']
			name = re.sub('[\$,]', '', name)
		else: 
			name = "NA"

		species = record[0]['GBSeq_source']
		acc = record[0]['GBSeq_accession-version']
		description = record[0]['GBSeq_definition']
		description = re.sub('[\$,]', '', description)

		output_file.write("%s, %s, %s, %s , %s, %s, %s, %s" % (gi_record.rstrip('\n'), acc, species, strain, host, name, description, '\n'))
		
	output_file.close()
	Entrez_handle.close()

if __name__=='__main__':
	### Argument handling
	arg_parser = argparse.ArgumentParser(description='Takes list of GI numbers and returns record descriptions. Give command as $ python gi2descript.py myGIlist.txt database yourEmail@address.com -o outputFile.txt');
	arg_parser.add_argument("file_dir_input", help="Path to file with list of GIs. To use stdin (for piped input) enter '-'");
	arg_parser.add_argument("database", help="Which database to direct entrez query to.", choices=['protein','nucleotide']);
	arg_parser.add_argument("email", help="Email for entrez record retrieval, tells NCBI who you are.");
	arg_parser.add_argument("-o", "--file_dir_output", default=None, help="Directory/name of output file. ");
	args = arg_parser.parse_args();

	### Variable definitions/declarations
	file_dir = args.file_dir_input; #directory of text file to be parsed.
	file_dir_output = args.file_dir_output;
	email = args.email; #Required for request 
	database = args.database;

	main(file_dir, file_dir_output, database, email);