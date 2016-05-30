# antibodyDesignLegacy
This folder hosts all the scripts that may be used for Antibody design.
The details of each script are provided below :

helix_sort.py : You need the file pdb_list (a list of pdbs you are sorting). This script will output only those pdbs that contain a helix with more than 7 residues.

sort_ddg.py : Sort all the decoys by their computational binding energy

sort_by_energy.py : Sort all the decoys by their energy score (stability index)

create_backrub_command.py : Creates a set of backrub commands that generates clusters on distributed computing

epitope_align.py : Align the epitope against the antibody
