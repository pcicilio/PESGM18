# File:"C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Codes\raw_fullrun_bus_fault.py", generated on TUE, OCT 31 2017  15:27, PSS(R)E release 34.03.01
psspy.cong(0)
psspy.conl(0,1,1,[0,0],[0.0, 100.0, 1.0, 1.0])
psspy.conl(0,1,2,[0,0],[0.0, 100.0, 1.0, 1.0])
psspy.conl(0,1,3,[0,0],[0.0, 100.0, 1.0, 1.0])
psspy.ordr(0)
psspy.fact()
psspy.tysl(0)
psspy.dyre_new([1,1,1,1],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\poland_CLM_test_2000.dyr""","","","")
psspy.dyre_new([1,1,1,1],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\poland_CLM_full.dyr""","","","")
psspy.bsys(1,0,[0.0,0.0],0,[],1,[10],0,[],0,[])
psspy.chsb(1,0,[-1,-1,-1,1,13,0])
psspy.strt_2([0,0],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\CLM_verify.outx""")
psspy.run(0, 0.5,1,1,0)
psspy.delete_all_plot_channels()