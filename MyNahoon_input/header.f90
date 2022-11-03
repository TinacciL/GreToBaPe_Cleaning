!       NS = NUMBER OF SPECIES
!       NRTOT = NUMBER OF REACTIONS IN THE NETWORK (THE REAL ONE!!!)
!       NX = NUMBER OF SPATIAL POINTS
!       NTIME = NUMBER OF OUTPUT TIMES
!       NELEM = NUMBER OF ELEMENTS + 1 (FOR CHARGES)
!       XCO_0 and XH2_0 are the abundances of CO and H2 at the edge of 
!       the cloud to compute shelf sheilding of CO and H2. ONE NEEDS TO PAY
!       ATTENTION TO THESE PARAMETERS SINCE THEY CAN STRONGLY AFFECT THE 
!       CHEMISTRY

       integer NS, NRTOT, NX, NTIME, NELEM 
       double precision XCO_0,XH2_0
       !new_gretobape.dat (7422) with grain reactions (14) and 489 species + 4 grain species (GRAIN-,GRAIN0,XH,e-)
       parameter (NS=493, NRTOT=7436, NTIME=124,NX=1,NELEM=14)
       parameter (XCO_0=1.D-4, XH2_0=5.D-1)
