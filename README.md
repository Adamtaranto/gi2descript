gi2descript
================================

What: Fetches summary data for genbank records, including: Seq name, species, isolate number, and host species  

How: Takes a list of gi numbers and queries NCBI via the Entrez API


Example
-------------------------

    python gi2descript.py myGIlist.txt protein yourEmail@address.com -o output.csv


Options
-------------------------

usage: gi2descript.py file_dir_input {protein,nucleotide} email [-h] [-o FILE_DIR_OUTPUT] 


<table>

  <tr>
	<th>Arg</th><th>Name</th><th>Description</th>
  </tr>
  
  <tr>
	<td>[1]</td><td>file_dir</td><td>Path to gi list</td>
  </tr>
  
  <tr>
	<td>[2]</td><td>{protein,nucleotide}</td><td>Which database to direct entrez query to.</td>
  </tr>

  <tr>
	<td>[3]</td><td>email</td><td>Email for entrez record retrieval, tells NCBI who you are.</td>
  </tr>

  <tr>
    <td>-o</td><td>FILE_DIR_OUTPUT</td><td>Set name of output file</td>
  </tr>
  
  <tr>
    <td>-h</td><td>help</td><td>Print help message and exit</td>
  </tr>

</table>
