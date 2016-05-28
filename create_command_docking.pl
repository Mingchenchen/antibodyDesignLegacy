#!/usr/bin/perl

for($i = 1; $i < 161; $i++ ) {

open(file, ">command_dock$i.sh") ;

print file "#PBS -l nodes=ocean
#PBS -j oe 
#PBS -o /nas1/home/ssbhatta/Docking/$i/run.log 

cd /nas1/home/ssbhatta/Docking/$i

cmd=\" /nas1/apps/rosetta/current/source/bin/docking_protocol.linuxgccrelease -s ../cpep_3eff.pdb -database /nas1/apps/rosetta/current/database -partners AB_C -dock_pert 0.1 2.0 -nstruct 500 \" \n

echo \$cmd
\$cmd
sleep 0.3s

" ;

close file ; 
}
